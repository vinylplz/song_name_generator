#!/usr/bin/env python
import sys

import argparse

from colorama import init, Back

from random import randrange

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--numnames', action='store', dest='numnames', type=int, default=15)
    parser.add_argument('-W', '--wordfile', action='store', dest='wordfile', default=None)
    parser.add_argument('-T', '--templatefile', action='store', dest='templatefile', default=None)
    parsed = parser.parse_args()
    main(parsed)
    return

class SongNameGenerator(object):
    """Generates song names from a list of words"""
    def __init__(self,wordlist=[],templates=[],wordfile=None,templatefile=None):
        super(SongNameGenerator, self).__init__()
        self._wordlist = wordlist
        self._templates = templates
        if wordfile:
            self.add_words_from_file(wordfile)
        if templatefile:
            self.add_templates_from_file(templatefile)

    def add_word(self, word=""):
        self._wordlist.append(word.rstrip())

    def add_words(self, words=[""]):
        for w in words:
            self._wordlist.append(w.rstrip())

    def add_words_from_file(self, wordfile):
        with open(wordfile) as wf:
            words = wf.readlines()
            self.add_words(words)
    
    def add_template(self, template):
        self._templates.append(template.rstrip())

    def add_templates(self, templates=[]):
        for t in templates:
            self._templates.append(t.rstrip())

    def add_templates_from_file(self, templatefile):
        with open(templatefile) as tf:
            templates = tf.readlines()
            self.add_templates(templates)

    def generate_name(self):
        if len(self._templates) == 0 :
            print "ERROR: No templates loaded"
            sys.exit(1)
        if len(self._wordlist) == 0 :
            print "ERROR: No words loaded"
            sys.exit(1)

        template = self._get_random_template()
        return template.format(self._get_random_word(),self._get_random_word())
        
    def _get_random_word(self):
        return self._wordlist[randrange(0,len(self._wordlist))]

    def _get_random_template(self):
        return self._templates[randrange(0,len(self._templates))]
        

def main(parsed):
    init()
    colors = [Back.GREEN, Back.YELLOW, Back.RED]
    numnames = getattr(parsed, 'numnames')
    wordfile = getattr(parsed, 'wordfile')
    templatefile = getattr(parsed, 'templatefile')
    generator = SongNameGenerator()

    if wordfile:
        generator.add_words_from_file(getattr(parsed,'wordfile'))
    else:
        try:
            generator.add_words_from_file('wordlist.txt')
        except:
            pass

    if templatefile:
        generator.add_templates_from_file(getattr(parsed, 'templatefile'))
    else:
        try:
            generator.add_templates_from_file('templates.txt')
        except:
            pass

    for i in range(0,numnames):
        name = generator.generate_name()
        print colors[i % len(colors)], name.upper() ,Back.RESET
    return

if __name__ == '__main__':
    parse_arguments()
