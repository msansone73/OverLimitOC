import util
import logging
import thread
import lerConfig
import time
import sys

def main():
#    oc00=util.geraOC('usuario00')
#    util.recriaDiretorioBase(oc00)

    if (lerConfig.get_testes('uploadDirRecursivo')=='True'):
        qtd=int(lerConfig.get_parametro('uploadDirRecursivo','qtdThread'))
        folder = lerConfig.get_parametro('uploadDirRecursivo', 'folder')
        print "Test upload recusive, runing ..."
        usuarios = lerConfig.get_parametro('uploadDirRecursivo', 'usuarios')
        lusuario= usuarios.replace(' ', '').split(',')
        for usuario in lusuario:
            oc00 = util.geraOC(usuario)
            util.recriaDiretorioBase(oc00)
            for i in range(qtd):
                thread.start_new( util.enviaDiretorioRecursivo, (oc00,folder,'Th0'+str(i)) )

    if (lerConfig.get_testes('uploadDirPeriodo')=='True'):
        nthead=int(lerConfig.get_parametro('uploadDirPeriodo', 'qtdThread'))
        tempo = int(lerConfig.get_parametro('uploadDirPeriodo', 'periodo_min'))
        usuarios = lerConfig.get_parametro('uploadDirRecursivo', 'usuarios')
        lusuario = usuarios.replace(' ', '').split(',')
        for usuario in lusuario:
            oc00 = util.geraOC(usuario)
            util.recriaDiretorioBase(oc00)
            for i in range(nthead):
                thread.start_new( util.cicloPeriodo, (oc00,'dir00T'+str(nthead)+'-'+str(i),tempo, nthead))


    while 1:
        pass

if __name__ == "__main__":
    main()


