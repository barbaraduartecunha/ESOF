conn = sqlite3.connect('pets.db')
# connect_db.py
# 01_create_db.py
import sqlite3
path = 'C:\sqlite\banco'
path
'C:\\sqlite\x08anco'
conn = sqlite3.connect(path+r'\pets.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE pets (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
raca TEXT NOL NULL,
idade INTEGER,
nome TEXT,
responsavel INTEGER,
fone TEXT NOT NULL,
criado_em DATE NOT NULL
);
""")
print ("tabale criada com sucesso.')
       conn.close()

import sqlite3
conn = sqlite2.connect('dados.db')
cursor = conn.cursor()
cursor.execute("""
INSERT INTO pets (raca, idade, nome, responsavel, fone, criado_em)
VALUES ('beagle', '10','pitty', 'Barbara', '34-991458155', 2016-11-18')
""")

cursor.execute("""
INSERT INTO pets (raca, idade, nome, responsavel, fone, criado_em)
VALUES ('labrador', '5','Marley', 'Bruno', '34-992389036', 2016-11-18')
""")
       
cursor.execute("""
INSERT INTO pets (raca, idade, nome, responsavel, fone, criado_em)
VALUES ('vira-lata', '8','lilica', 'jessica', '34-992765434', 2016-11-18')
""")

cursor.execute("""
INSERT INTO pets (raca, idade, nome, responsavel, fone, criado_em)
VALUES ('dalmata', '13','bob', 'vanessa', '34-998567432', 2016-11-18')
""")

conn.commit()
print ('Dados inseridos com sucesso.')
       conn.close()
       
import sqlite3
       conn = sqlite3.connect('pets.db')
       cursor = conn.cursor()
       lista = [(
           'poodle', '12', 'bernardo', 'luis', '34-99926733', '2016-11-18',)
                ('vira-lata', '8', 'Tomy', 'Thaynara', '34-992345674', '2016-11-18',)
                ('labrador', '2', 'Aslan', 'Jovair', '34-93456788', '2016-11-18',)]

       cursor.executemany("""
INSERT INTO pets(raca, idade, nome, responsavel, fone, criado_em)
VALUES (?,?,?,?,?,?_
""", lista)

       con.commit()
       print ('Dados inseridos com sucesso.')
       conn.close()

# 05_create_data_param.py
    import sqlite3
       conn = sqlite3.connect('pets.db')
       cursor = conn.cursor()
       p_raca = input('Raça: ')
       p_idade = input('Idade: ')
       p_nome = input('Nome: ')
       p_responsavel = input('Responsavel: ')
       p_fone = input('Fone: ')
       p_criado_em = input('Criado em (yyyy-mm-dd): ')

cursor.execute(""" INSERT INTO pets (raca, idade, nome, responsavel, fone, criado_em)
VALUES (?,?,?,?,?,?,?,?) """, (p_raca, p_idade, p_nome, p_responsavel, p_fone, p_criado_em))
       
 conn.commit() 
 
print('Dados inseridos com sucesso.') 
 
conn.close()

# 06_read_data.py
    import sqlite3
       conn = sqlite3.connect('pets.db')
       cursor = conn.cursor()
       cursor.execute("""
SELECT * FROM pets;
""") 
 
for linha in cursor.fetchall():
       print(linha)
       conn.close()

# 07_update_data.py
       import sqlite3
       conn = sqlite3.connect('pets.db')
       cursor = conn.cursor() 
 
id_pets = 1
novo_fone = '11-1000-2014'
novo_criado_em = '2014-06-11' 
 
# alterando os dados da tabela
       cursor.execute("""
UPDATE pets
SET fone = ?, criado_em = ?
WHERE id = ?
""", (novo_fone, novo_criado_em, id_pets)) 
 
conn.commit() 
 
print('Dados atualizados com sucesso.') 
 
conn.close()
       
# 08_delete_data.py
       import sqlite3
       conn = sqlite3.connect('pets.db')
       cursor = conn.cursor() 
 
id_pets = 8 
 
       cursor.execute("""
DELETE FROM pets
WHERE id = ?
""", (id_pets,)) 
 
conn.commit() 
 
print('Registro excluido com sucesso.') 
 
conn.close()

# 09_alter_table.py
       
       import sqlite3
       conn = sqlite3.connect('pets.db')
       cursor = conn.cursor() 
 

       cursor.execute("""
ALTER TABLE pets
ADD COLUMN bloqueado BOOLEAN;
""") 
 
conn.commit() 
 
print('Novo campo adicionado com sucesso.') 
 
conn.close()


# 10_view_table_info.py
       import sqlite3
       conn = sqlite3.connect('pets.db')
       cursor = conn.cursor() nome_tabela = 'pets' 
 

       cursor.execute('PRAGMA table_info({})'.format(nome_tabela)) 
 
colunas = [tupla[1] for tupla in cursor.fetchall()]
print('Colunas:', colunas)


 
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""") 
 
print('Tabelas:')
for tabela in cursor.fetchall():
       print("%s" % (tabela)) 
 
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,)) 
 
print('Schema:')
       for schema in cursor.fetchall():
       print("%s" % (schema)) 
 
conn.close()

# 11_backup.py
       import sqlite3
       import io
       conn = sqlite3.connect('pets.db')
       with io.open('pets_dump.sql', 'w') as f:
       for linha in conn.iterdump():
       f.write('%s\n' % linha)
       print('Backup realizado com sucesso.')
       print('Salvo como pets_dump.sql') 
 
conn.close()


# 12_read_sql.py
       import sqlite3
       import io
       conn = sqlite3.connect('pets_recuperado.db')
       cursor = conn.cursor()
       f = io.open('pets_dump.sql', 'r')
       sql = f.read()
       cursor.executescript(sql)
       print('Banco de dados recuperado com sucesso.')
       print('Salvo como pets_recuperado.db')
       
 
conn.close()

# gen_random_values.py
       import random
       import rstr
       import datetime
       def gen_age():
       return random.randint(15, 99)
       def gen_phone():
       return '({0}) {1}-{2}'.format(
           rstr.rstr('1234567890', 2),
           rstr.rstr('1234567890', 4),
           rstr.rstr('1234567890', 4))
       def gen_timestamp():
    year = random.randint(1980, 2015)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(
        year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date
       
       # connect_db.py
       import sqlite3 
 
class Connect(object): 
 
    def __init__(self, db_name):         try:
       self.conn = sqlite3.connect(db_name)
       self.cursor = self.conn.cursor()
       print("Banco:", db_name)
       self.cursor.execute('SELECT SQLITE_VERSION()')
       self.data = self.cursor.fetchone()
       print("SQLite version: %s" % self.data)
       except sqlite3.Error:
       print("Erro ao abrir banco.")
       return False

       def close_db(self):
       if self.conn:
       self.conn.close()
       print("Conexão fechada.") 

class petsDb(object): 
 
    def __init__(self):
       self.db = Connect('pets.db') 
 
    def close_connection(self):
       self.db.close_db()
       if __name__ == '__main__':
       pets = petsDb()
       pets.close_connection()

       
       




       
       

    
