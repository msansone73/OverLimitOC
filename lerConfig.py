import ConfigParser
config = ConfigParser.ConfigParser()
config.read('testeoc.conf')

def get_parametro(module, parametro):
    return config.get(module, parametro)

def get_testes(teste):
    return config.get('testes',teste)

def get_server():
    return config.get('conexao','server')

def get_user(usuario):
    return config.get(usuario,'user')

def get_password(usuario):
    return config.get(usuario,'password')

def get_fileLogPath():
    return config.get('util','fileLogPath')

def get_fileLogName():
    return config.get('util','fileLogName')

def get_diretorioBase():
    return config.get('util','diretorioBase')

def get_MySqlUser():
    return config.get('mysql','user')

def get_MySqlPassword():
    return config.get('mysql','password')

def get_MySqlHost():
    return config.get('mysql','host')

def get_MySqlDatabase():
    return config.get('mysql','database')
