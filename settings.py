from os.path import isfile

if isfile('.env'):
    env.read_envfile('.env')