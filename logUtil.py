import lerConfig
import os
import socket

def get_log_file_name():
    logfile = lerConfig.get_parametro('util', 'logAnalitic')
    hostname=socket.gethostname()
    return logfile.replace('.', '_'+hostname+'.')

def insert_log_transfer(filename, size, time, qtdthread):
    logfile= get_log_file_name()
    file = open(logfile, 'a')
    line = filename+ '|' + str(size)+ '|' + str(time)+ '|' + str(qtdthread)+ '\n'
    file.write(line)
    file.close()

def apaga_log_transfer():
    logfile = get_log_file_name()
    os.remove(logfile)
