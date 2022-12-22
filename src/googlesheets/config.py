import os
from configparser import ConfigParser

HOME_PATH = os.path.dirname(os.path.relpath(__file__))

def to_list(text: str, dtype: type = str) -> list:
    if dtype == int:
        try:
            return [int(a) for a in text.split(',')]
        except Exception as e:
            print(e)
    elif dtype == float:
        try:
            return [float(a) for a in text.split(',')]
        except Exception as e:
            print(e)
    else:
        try:
            return text.split(',')
        except Exception as e:
            print(e)

def get_config(ARQUIVO_PATH: str = HOME_PATH) -> dict:
    config = ConfigParser()
    config.read(ARQUIVO_PATH)
    configuration = {
        'api':{
            'scopes': to_list(config['api']['scopes'])
        },
        'sheets':{
            'sheet_id': config['sheets']['sheet_id'],
            'range':config['sheets']['range']
        },
        'paths':{
            'token':config['paths']['token'],
            'credentials':config['paths']['credentials']
        }
    }
    return configuration