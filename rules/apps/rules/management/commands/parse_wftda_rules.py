# -*- coding:utf-8 -*-
import urllib2
import re
import logging
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from rules.apps.rules.models import *


URL_RULES = 'http://wftda.com/rules/20130615'
EXCLUDE_SECTIONS = ('11',)


class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    help = 'Parse the WFTDA website'
    logger = logging.getLogger('wftda')

    def __init__(self):
        super(Command, self).__init__()

    def handle(self, *args, **options):
        self.logger.info('Parsing...')
        try:
            Page(URL_RULES).parse()
        except Exception as e:
            raise CommandError('Error during the parsing process. : %s' % e)


class Page:
    content = BeautifulSoup()

    def __init__(self, url):
        sock = urllib2.urlopen(url)
        html = sock.read()
        sock.close()

        self.content = BeautifulSoup(html)

    def parse(self, section=False):
        """
        Parses the HTML content
        """
        if self.is_page_section():
            self.parse_sections()
        else:
            self.parse_rules(section)

    def is_page_section(self):
        """
        Returns True if current page is a section page
        """
        if len(self.content.find_all('div', 'ruleSection')) > 0:
            return True
        return False

    def is_page_rule(self):
        """
        Returns True if current page is a rule page
        """
        return not self.is_page_section()

    def get_page_title(self):
        """
        Returns the page title
        """
        if not self.is_page_rule():
            return False

        infos = self.content.find('h2')
        title = infos.text
        dash_pos = title.find('-')
        numero = title[:dash_pos - 1]

        return numero

    def parse_rules(self, section=False):
        """
        Parses the rules in a rule page
        Inserts the rule in the database if it doesn't exist
        Updates the content rule if it's already in database
        """
        if not self.is_page_rule():
            return False

        i = 0

        def is_a_rule(css_class):
            return css_class is not None and css_class == "rule"

        rules = self.content.find_all('div', class_=is_a_rule)

        for element in rules:
            if i == 0:
                snb = self.get_page_title()
            else:
                if element.find('span', 'ruleNumber'):
                    snb = element.find('span', 'ruleNumber').text
                else:
                    snb = self.get_page_title()

            if element.find('p'):
                rule = element.find('p').text
                if re.search('\d', rule):
                    rule = rule[rule.find('-') + 2:]

                rule, created = Rule.objects.get_or_create(number=snb, section=section, defaults={'content': rule})
                if not created:
                    rule.content = rule
                    rule.save()

            i += 1

        return True

    def parse_sections(self):
        """
        Parses each seaction of the page
        """
        sections = self.content.find_all('div', 'ruleSection')
        for section in sections:
            href = section.find('a', href=re.compile("rules"))
            link = "http://wftda.com%s" % href['href']

            title = section.text
            dash_pos = title.find('-')
            numero = title[:dash_pos - 1]
            title = title[dash_pos + 2:]

            if not numero in EXCLUDE_SECTIONS:
                section, created = Section.objects.get_or_create(number=numero.strip(), label=title.strip())
                Page(link).parse(section)