import pymysql


def conection_bd():
    conection = pymysql.connect(
      host="localhost",
      user="root",
      password="2323",
      database="bancojl"
)
    return conection
    
    
def register_table(nome, descricao, valor, disponivel):
    conection = conection_bd()
    cursor = conection.cursor()
    sql = "INSERT INTO produtos (nome, descricao, valor, disponivel) VALUES (%s,%s,%s,%s)"
    valores = (nome, descricao, valor, disponivel)
    cursor.execute(sql, valores)
    conection.commit()
    
def show_list_product():
   conection = conection_bd()
   cursor = conection.cursor()
   consulta = "SELECT nome, valor FROM produtos ORDER BY valor ASC"
   cursor.execute(consulta)
   resultados = cursor.fetchall()
   cursor.close()
   conection.close()      
   return resultados