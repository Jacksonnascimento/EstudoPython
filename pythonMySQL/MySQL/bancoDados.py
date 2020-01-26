#import MySQLdb
import pymysql

host = "localhost"
user = "aplicacao"
password = "@jn87519023"
bd = "escola_curso"
port = 3306 


con = pymysql.connect(host, user, password, bd, port)
#con = MySQLdb.connect(host, user, password, bd, port)

c = con.cursor(pymysql.cursors.DictCursor) 
#pymysql.cursors.DictCursor faz o resultado voltar com dicionário

def select(fields, tables, where = None):
    
    global c
    
    query = "Select " + fields + " From " + tables
    if(where):
        query = query + " Where " + where
        
    c.execute(query)
    return c.fetchall()

def insert (values, table, fields = None):
     global c, con
     
     query = "Insert into " + table 
     if(fields):
         query = query + " (" + fields + ") "
     query = query + " values " + ",".join(["(" + v + ")"for v in values]) #separar por vírgula
     
     c.execute(query)
     con.commit()
     
def update(sets, table, where = None):
    
    global c, con
    
    query = "Update " + table
    query = query + " Set " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if(where):
        query = query + " Where " + where
        
    c.execute(query)
    con.commit()
    
def delete(table, where):
    
    global c, con
    
    query = "Delete from " + table + " Where " + where
    
    c.execute(query)
    con.commit()

#delete    
'''print(select("*", "aluno", "id_aluno = 4"))
delete("aluno", "id_aluno = 4")
print(select("*", "aluno", "id_aluno = 4")) '''
    
    
#update
'''update({"nome": "Belinha", "endereco": "Curitiba"}, "aluno", "id_aluno = 2")
print(select("*", "aluno", "id_aluno = 1"))'''




#insert
'''values = [
        "DEFAULT, '1997-03-26',  'Marcelo', 'Teceira travessa de R1', '1444848448'",
        "DEFAULT, '1997-03-26',  'Jonas', 'Rua b', '324343'",
        "DEFAULT, '1997-03-26',  'Amanda', 'Rua h', '465676'"]  


#insert(values, "aluno")        
#print(select("*", "aluno")) '''
 

#select 
print(select("nome, cpf", "aluno", "id_aluno = 1"))

result = select("nome, cpf", "aluno")

print(result[0]["nome"]) #primeiro regristro com o campo nome


cpf = result[0]["cpf"]

print(cpf)  