import sqlite3
from sqlite3 import Error
#https://www.youtube.com/watch?v=-_VopVDLhms&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=48

#########Criar Conexao
def ConexaoBanco():
    caminho = "C:\\Users\\leozi\\Desktop\\Repositorios Python\\Youtube\\BancoDados\\dbSqlite.db"
    con = None

    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)

    return con

def InsertBanco(parametros, sql ):
    try:
        conexao =ConexaoBanco() 
        cursor = conexao.cursor()
        cursor.execute(sql, parametros, )
        conexao.commit()
        print("Adicionado com sucesso")
    except Error as ex:
        print ("Erro:   "+ str(ex))

##########Criar Tabela
def CriarTabela():
    conexao = ConexaoBanco()
    try:
        vsql = """CREATE TABLE tb_pessoa(
            id_pessoa    INTEGER      PRIMARY KEY,
            nome_pessoa  VARCHAR (30) UNIQUE,
            vida_pessoa          INT (3)
        );"""
        cursor = conexao.cursor()
        cursor.execute(vsql)
        print("Tabela Criada Com Sucesso")
    except Error as ex:
        print("Erro: " + str(ex))

    conexao.close()

################################################################################################################
nome = "veronicas"
vida = 100
parametros = [nome,   vida,]
query = "INSERT INTO tb_pessoa (nome_pessoa, vida_pessoa) VALUES ($s, $s)" 

outraQuery = """select * from tb_pessoa""" 

#InsertBanco(query, ConexaoBanco(), parametros)
InsertBanco(parametros, query)