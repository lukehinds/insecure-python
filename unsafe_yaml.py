import yaml

conf_str = '''
!!python/object:__main__.AttackerObj
key: 'value'
'''
conf = yaml.load(conf_str)
