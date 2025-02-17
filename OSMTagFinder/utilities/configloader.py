# -*- coding: utf-8 -*-
'''
Created on 10.10.2014

@author: Simon Gwerder
'''

import codecs
from ConfigParser import SafeConfigParser

from utilities import utils


class ConfigLoader:

    configFileLoc = None

    websiteSection = 'Website'
    thesaurusSection = 'Thesaurus'
    tagInfoSection = 'TagInfoAPI'
    openThesaurusSection = 'OpenThesaurusAPI'
    altervistaSection = 'AltervistaAPI'
    gemetSection = 'GemetAPI'
    wordnikSection = 'WordnikAPI'

    __parser = SafeConfigParser()

    def __init__(self):
        self.configFileLoc = utils.dataDir() + 'config.ini'
        with codecs.open(self.configFileLoc, 'r', encoding='utf-8') as configFile:  # open the file with the correct encoding
            self.__parser.readfp(configFile)

    def getThesaurusString(self, option):
        return self.__parser.get(self.thesaurusSection, option)

    def getThesaurusInt(self, option):
        return self.__parser.getint(self.thesaurusSection, option)

    def getTagInfoAPIString(self, option):
        return self.__parser.get(self.tagInfoSection, option)

    def getWebsiteString(self, option):
        return self.__parser.get(self.websiteSection, option)

    def getWebsiteBoolean(self, option):
        return self.__parser.getboolean(self.websiteSection, option)

    def getWebsiteInt(self, option):
        return self.__parser.getint(self.websiteSection, option)

    def setWebsiteString(self, option, strValue):
        self.__parser.set(self.websiteSection, option, strValue)

    def getOpenThesaurusAPIString(self, option):
        return self.__parser.get(self.openThesaurusSection, option)

    def getAltervistaAPIString(self, option):
        return self.__parser.get(self.altervistaSection, option)

    def getGemetAPIString(self, option):
        return self.__parser.get(self.gemetSection, option)

    def getWordnikAPIString(self, option):
        return self.__parser.get(self.wordnikSection, option)

    def write(self):
        self.configFileLoc = utils.dataDir() + 'config.ini'
        with codecs.open(self.configFileLoc, 'wb', encoding='utf-8') as configFile:  # open the file with the correct encoding
            self.__parser.write(configFile)



