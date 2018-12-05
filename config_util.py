'''
config_util.py

Utility methods for working with configuration files

Created:
	6/3/18 by Chris Boyke

'''
import configparser, sys, os, json, re, glob

VERBOSE=False

'''
Config filename is usually the first parameter after the script name.
If none provided, then use the script's base name, replacing .py with .ini
'''
def get_config_filename():
	if len(sys.argv) < 2:
		config_filename=sys.argv[0].replace('.py','.ini')
		if os.path.isfile(config_filename):
			return config_filename
		else:
			files=glob.glob('*.ini')
			if files:
				i=0
				print("\nAvailable .ini files:\n")
				sorted_files = sorted(files)
				for f in sorted_files:
					i+=1
					print('{:2d}.'.format(i) ,f)
				c=input("\nYour Choice: ")
				if c.isdigit():
					file=sorted_files[int(c)-1]
					return file
				else:
					print('invalid response -- exiting')
					sys.exit(1)
	else:
		return sys.argv[1]

def read_config():
	cfgfile = get_config_filename()
	config = read_config_with_include(cfgfile)
	return config

'''
Read a configuration file with possible includes.
The include is specified by:

[config]
include=<comma-separated list of filenames>

If found, the include file will be loaded, and then the 'outer' config will be read again,
overriding any values in the included file

'''
def read_config_with_include(file):
	if VERBOSE:
		print('Reading',file)
	file=expand_path(file)
	if not os.path.isfile(file):
		print('Configuration file ' + file + ' not found -- exiting')
		sys.exit(1)

	config=configparser.ConfigParser()
	config.optionxform=str
	config.read(file)

	if config.has_section('config'):
		includes=config.get('config','include').split(',')
		if includes:
			for include in includes:
				include=expand_path(include)
				if VERBOSE:
					print('Reading included file',include)
				if not os.path.isfile(include):
					print('Warning',include,'not found -- continuing...')
				config.read(include)
			
			# Now read original file again
			config.read(file)	

	return config


'''
	Expand a filename, looking for environment variables.  Throw an error if no match
'''
def expand_path(s):
	for m in re.finditer(r'\$(\w+)',s):
		var=m.group(1)
		if not var in os.environ:
			print('Environment Variable',var,'not set -- exiting')
			sys.exit(1)

	s = os.path.expandvars(s)
	if '~' in s:
		s = os.path.expanduser(s)
	return s

