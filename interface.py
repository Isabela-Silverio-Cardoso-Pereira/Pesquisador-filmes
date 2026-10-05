import tkinter as tk
from tkinter import ttk
import sqlite3

#criando janela principal e guardando em uma variável
janela = tk.Tk()

#titulo da janela
janela.title("Pesquisador de filmes")

#tamanho da janela 
janela.geometry("1000x650")

#tamanho minimo da janela
janela.minsize(800, 550)

#cor do fundo principal
FUNDO = "#171A21"

# Fundo dos cards
CARD = "#222631"

# Cor de destaque
ROXO = "#8B5CF6"

# Roxo mais claro
ROXO_CLARO = "#A78BFA"

# Texto principal
BRANCO = "#F5F5F5"

# Texto secundário
CINZA = "#A7A9B4"


# Cor da caixa de pesquisa
INPUT = "#2B303B"
janela.configure(bg=FUNDO)

titulo = tk.Label(
    janela, 
    text = "Pesquisador de filmes",
    font = ("Arial", 26, "bold"),
    fg = BRANCO,
    bg = FUNDO
)
# pack() coloca o elemento dentro da janela
titulo.pack(pady=(40, 5))

subtitulo = tk.Label(
    janela, 
    text = "encontre informações sobre filmes",
    font = ("arial",16),
    fg = CINZA,
    bg = FUNDO

)
subtitulo.pack(pady=(0, 30))


#parte da pesquisa (frame pode colocar outros elementos dentro dele)
area_pesquisa = tk.Frame(
    janela,
    bg = FUNDO
)

area_pesquisa.pack()


campo_pesquisa = tk.Entry(
    area_pesquisa,

    # Tamanho aproximado do campo
    width=45,

    # Fonte do texto digitado
    font=("Arial", 13),

    # Cor do texto
    fg=BRANCO,

    # Cor de fundo
    bg=INPUT,

    # Remove a borda padrão
    bd=0
)

# pady/padx criam espaço ao redor do elemento
campo_pesquisa.pack(
    side="left",
    ipady=10,
    padx=(0, 10)
)

def pesquisar():
    filme = campo_pesquisa.get()

    conexao = sqlite3.connect("filmes.db")
    cursor = conexao.cursor()

    pesquisa_filme = "SELECT title FROM filmes WHERE title LIKE ?"
    cursor.execute(pesquisa_filme, (f"%{filme}%",))

    resultado = cursor.fetchall()
    print(resultado)

    conexao.close()



botao_pesquisar = tk.Button(
    area_pesquisa,
    text="PESQUISAR",
    font=("Arial", 11, "bold"),
    bg=ROXO,
    fg=BRANCO,
    bd=0,
    padx=20,
    pady=10,
    command=pesquisar
)

botao_pesquisar.pack(side="left")


filtros = tk.Frame(
    janela,
    bg=FUNDO
)

filtros.pack(pady=30)



label_genero = tk.Label(
    filtros,
    text="Gênero",
    font=("Arial", 10, "bold"),
    fg=CINZA,
    bg=FUNDO
)

label_genero.grid(
    row=0,
    column=0,
    padx=10
)


generos = ttk.Combobox(
    filtros,

    # Opções que aparecerão no menu
    values=[
        "Todos",
        "Ação",
        "Aventura",
        "Comédia",
        "Drama",
        "Terror",
        "Ficção Científica"
    ],

    state="readonly",
    width=18
)

generos.current(0)

generos.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)



label_ano = tk.Label(
    filtros,
    text="Ano",
    font=("Arial", 10, "bold"),
    fg=CINZA,
    bg=FUNDO
)

label_ano.grid(
    row=0,
    column=1,
    padx=10
)


campo_ano = tk.Entry(
    filtros,
    width=15,
    font=("Arial", 11),
    bg=INPUT,
    fg=BRANCO,
    bd=0
)

campo_ano.grid(
    row=1,
    column=1,
    padx=10,
    ipady=7
)



resultados_titulo = tk.Label(
    janela,
    text="RESULTADOS",
    font=("Arial", 15, "bold"),
    fg=ROXO_CLARO,
    bg=FUNDO
)

resultados_titulo.pack(
    anchor="w",
    padx=70,
    pady=(10, 10)
)




card = tk.Frame(
    janela,
    bg=CARD,
    width=860,
    height=130
)

card.pack(
    padx=70,
    fill="x"
)

# Impede que o Frame diminua para o tamanho dos elementos internos
card.pack_propagate(False)


nome_filme = tk.Label(
    card,
    text="Batman",
    font=("Arial", 18, "bold"),
    fg=BRANCO,
    bg=CARD
)

nome_filme.pack(
    anchor="w",
    padx=20,
    pady=(15, 5)
)


# Informações do filme

informacoes = tk.Label(
    card,
    text="2008  •  Ação  •  Crime  •  Drama",
    font=("Arial", 10),
    fg=ROXO_CLARO,
    bg=CARD
)

informacoes.pack(
    anchor="w",
    padx=20
)


# Descrição


descricao = tk.Label(
    card,
    text="Resultado de exemplo. Depois essas informações virão do SQLite.",
    font=("Arial", 10),
    fg=CINZA,
    bg=CARD
)

descricao.pack(
    anchor="w",
    padx=20,
    pady=8
)

janela.mainloop()