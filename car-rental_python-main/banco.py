import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Mobi')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Argo')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Gol')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Compass')"))
cursor.execute(("INSERT INTO carros(nome_carro) VALUES ('Hrv')"))
banco.commit()
banco.close()


