''' 
Subclass of ConfigParser that adds some useful methods:

get_list - returns a list from a comma-separated value - stripping whitespaces around each list entry

get_filename - return a filename, substituting embedded environment variables

'''
import configparser,json,config_util


class ListConfigParser(configparser.ConfigParser):

    def get_list(self,section,key):
        value=self.get(section,key,fallback=None)
        if value is None:
            return None
        return [ x.strip() for x in value.split(',')]

    def get_filename(self,section,key):
        filename=self.get(section,key,fallback=None)
        if filename is None:
            return None
        return config_util.expand_path(filename)



