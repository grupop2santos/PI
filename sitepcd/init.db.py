import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO candidato (nome) VALUES (?)",
            (['Eder'])
            )

cur.execute("INSERT INTO empresa (nome, cnpj) VALUES (?, ?)",
            ('Empresa1', '12345678912345')
            )

cur.execute("INSERT INTO vaga (titulo, descricao, empresa_id) VALUES (?, ?, ?)",
            ('Desenvolvedor Full Stack', 'Fazer tudo', 1)
            )

cur.execute("INSERT INTO aplicacoes (vaga_id, candidato_id) VALUES (?, ?)",
            (1, 1)
            )

connection.commit()
connection.close()



