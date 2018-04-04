import lerConfig

lista = lerConfig.get_parametro('uploadDirRecursivo','usuarios')
print lista.replace(' ','').split(',')