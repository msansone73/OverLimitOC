import mysql.connector
import lerConfig

def geraConexao():
    return  mysql.connector.connect(  user=lerConfig.get_MySqlUser(),
                                    password=lerConfig.get_MySqlPassword(),
                                    host=lerConfig.get_MySqlHost(),
                                    database=lerConfig.get_MySqlDatabase())


def lista_nomes():
    cnx = geraConexao()
    query = "select nome, email, senha from usuarios;"
    cursor= cnx.cursor()
    cursor.execute(query)
    for (nome, email, senha) in cursor:
        print "nome = {}, email = {}" .format(nome, email)
    cnx.close()

def insert_db_transfer(filename, size, time, qtdthread):
    cnx = geraConexao()
    query = "insert into tb_transferencia (filename, size, time, qtdthread)  values ('{0}', {1}, {2}, {3})".format(filename, size, time, qtdthread)
    print query
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cnx.close()

def limpaLog():
    cnx = geraConexao()
    query = "delete from tb_transferencia;"
    print query
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cnx.close()

#limpaLog()
