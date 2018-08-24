'''
config_util.py

Utility methods for working with configuration files

Created:
	6/3/18 by chris.boyke@bloomreach.com

'''
import configparser, sys, os, json, re

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
			print("Usage: ",os.path.basename(sys.argv[0]),"<ini_file>")
			sys.exit(1)
	return sys.argv[1]

def read_config():
	cfgfile = get_config_filename()
	return read_config_with_include(cfgfile)

'''
Read a configuration file with possible includes.
The include is specified by:

[config]
include=filename

If found, the include file will be loaded, and then the 'outer' config will be read again,
overriding any values in the included file

'''
def read_config_with_include(file):
	file=expand_path(file)
	if not os.path.isfile(file):
		print('Configuration file ' + file + ' not found -- exiting')
		sys.exit(1)

	config=configparser.ConfigParser()
	config.optionxform=str
	config.read(file)

	if config.has_section('config'):
		include=config.get('config','include')
		if include:
			config=read_config_with_include(include)
			config.read(file)

	# For jenkins jobs which specify an "include" parameter:
	env_override(config,'instances','include')
	return config


'''
	Expand a filename, looking for environment variables.  Throw an error if no match
'''
def expand_path(file):
	for m in re.finditer(r'\$(\w+)',file):
		var=m.group(1)
		if not var in os.environ:
			print('Environment Variable',var,'not set -- exiting')
			sys.exit(1)
	return os.path.expandvars(file)



# Override a value in the config file with an environment variable of the same name
def env_override(config,section,key):
	if key in os.environ:
		val=os.environ[key]
		if val:
			config[section][key]=val
