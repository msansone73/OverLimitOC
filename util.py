import owncloud
import lerConfig
import logging
import os
import sys
import time
import logUtil

def geraOC(usuario):
    oc = owncloud.Client(lerConfig.get_server())
    oc.login(lerConfig.get_user(usuario), lerConfig.get_password(usuario))
    return oc

def planoTeste00(oc):
    logging.info('inicio planoTeste00')
    oc.mkdir('testdir00')
    oc.put_file('testdir00/remotefile.txt', 'D:/NB24146/Documents/Projects/projeto_owncloud/untitled1/teste.py')
    oc.put_file('testdir00/remotefile2.txt', 'D:/teste.txt')
    oc.put_file('testdir00/remotefile3.txt', "D:/teste.txt")
    oc.put_file_contents('testdir00/remotenewfile.txt', 'conteudo do arquivo manual')
    link_info = oc.share_file_with_link('testdir00/remotefile.txt')
    print "link =" + link_info.get_link()
    logging.info('fim planoTeste00')

def recriaDiretorioBase(oc):
    dirBase=lerConfig.get_diretorioBase()
    recriaDiretorio(oc, dirBase)

def existeDiretorio(oc,path):
    try:
        dir = oc.file_info(path)
        return True
    except:
        return False

def recriaDiretorio(oc,path):
    print "recriando diretorio "+ path
    resultado=False
    while (not(resultado)):
        try:
            if (existeDiretorio(oc,path)):
                oc.delete(path)
                time.sleep(5)
            oc.mkdir(path)
            dir = oc.file_info(path)
            resultado = True
        except:
            print "falha ao recriar diretorio "+ path
            resultado=False


def apagaLog():
    arquivo_log=lerConfig.get_fileLogPath()+'/'+lerConfig.get_fileLogName()
    try:
        if os.path.exists(arquivo_log):
            os.remove(arquivo_log)
    except:
        pass

def dbLog(filename, size, time, qtdthread):
    logUtil.insert_log_transfer(filename, size, time, qtdthread)
    #dbAccess.insert_db_transfer(filename, size, time, qtdthread)


def enviaDiretorioRecursivo(oc, dir, remDir):
    recriaDiretorio(oc,remDir)
    qtdThead=lerConfig.get_parametro('uploadDirPeriodo','qtdThread')
    for file in os.listdir(dir):
        if (os.path.isdir(dir+'//'+file)):
            enviaDiretorioRecursivo(oc,dir+'//'+ file, remDir+'//'+ file)
        else:
            msg= dir+'//'+file+'  -->  '+ remDir
            print msg
            try:
                t1 = time.time()
                origem=dir+'//'+file
                destino=remDir+'//'+file
                oc.put_file(destino, origem)
                t2 = time.time()
                dbLog(destino,os.stat(origem).st_size,t2-t1,qtdThead)
            except:  # catch *all* exceptions
                e = sys.exc_info()[0]


# identifica quantidade de thread com melhor performance
def cicloPeriodo(oc, remDir, minutos,qtdThead):
    segundo=minutos*60
    t_inicio = time.time()
    remDir = lerConfig.get_diretorioBase() + '/' + remDir
    oc.mkdir(remDir)
    cont=0
    while (time.time()<(t_inicio+segundo)):
        destino = remDir + '/arq' + str(cont) + '.txt'
        t1 = time.time()
        try:
            oc.put_file_contents(destino, '0123456789')
        except:  # catch *all* exceptions
            e = sys.exc_info()[0]
            break
        t2 = time.time()
        dbLog(destino, 10, t2 - t1, qtdThead)
        cont=cont+1



apagaLog()
logging.basicConfig(format='%(asctime)s %(message)s', filename=lerConfig.get_fileLogPath()+lerConfig.get_fileLogName(),level=logging.INFO)
logging.info('INICIO-------------------------------------------------------------')
logging.info('inicia login')