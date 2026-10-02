import sqlite3
conexao = sqlite3.connect("filmes.db")
cursor = conexao.cursor()


filme = input("digite o nome do filme")
pesquisa_filme = ("SELECT title FROM filmes WHERE title LIKE ?")
cursor.execute(pesquisa_filme, (f"%{filme}%",))
resultado = cursor.fetchall()
cursor.execute("SELECT COUNT(*) FROM filmes")
print(resultado)