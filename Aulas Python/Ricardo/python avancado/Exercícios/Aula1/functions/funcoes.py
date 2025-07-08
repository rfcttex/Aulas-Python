import os
import sqlite3

# === Função de conexão ===


def get_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.normpath(os.path.join(base_dir, '..', 'data', 'db.db'))
    return sqlite3.connect(db_path)

# === Criar as tabelas ===


def databaseStarter():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                tipo TEXT NOT NULL,
                paginas INTEGER NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ebook (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                tipo TEXT NOT NULL,
                tamanho INTEGER NOT NULL,
                extensao TEXT NOT NULL
            )
        ''')

        conn.commit()
        print("Tabelas criadas com sucesso.")
    except Exception as e:
        print("Erro ao criar tabelas:", e)
    finally:
        conn.close()

# === Registrar documentos ===


def registar():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        selection = input(
            "Deseja registar um livro ou um e-book? ").strip().lower()

        if selection == "livro":
            num = int(
                input(f"Quantos registros de {selection} deseja inserir?: "))
            for i in range(num):
                print(f"\nRegistro {i+1}:")
                titulo = input("Título: ")
                autor = input("Autor: ")
                tipo = input("Tipo: ")
                paginas = int(input("Número de páginas: "))

                cursor.execute(
                    "INSERT INTO livro (titulo, autor, tipo, paginas) VALUES (?, ?, ?, ?)",
                    (titulo, autor, tipo, paginas)
                )
            print(f"\n{num} livro(s): {titulo} registrado(s) com sucesso!")

        elif selection in ["ebook", "e-book"]:
            num = int(
                input(f"Quantos registros de {selection} deseja inserir?: "))
            for i in range(num):
                print(f"\nRegistro {i+1}:")
                titulo = input("Título: ")
                autor = input("Autor: ")
                tipo = input("Tipo: ")
                tamanho = int(input("Tamanho (MB): "))
                extensao = input("Extensão (ex: pdf, epub): ")

                cursor.execute(
                    "INSERT INTO ebook (titulo, autor, tipo, tamanho, extensao) VALUES (?, ?, ?, ?, ?)",
                    (titulo, autor, tipo, tamanho, extensao)
                )

            print(f"\n{num} e-book(s): {titulo} registrado(s) com sucesso!")

        else:
            print("Tipo inválido. Use 'livro' ou 'ebook'.")

        conn.commit()

    except Exception as e:
        print("Erro ao registar:", e)
    finally:
        conn.close()

# === Pesquisar documentos ===


def pesquisar():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        selection = input(
            "Deseja pesquisar um livro ou um e-book? ").strip().lower()

        if selection not in ["livro", "ebook", "e-book"]:
            print("Tipo inválido.")
            return

        nome = input(f"Qual é o nome do {selection}? ").strip()

        table = "livro" if selection == "livro" else "ebook"

        cursor.execute(
            f"SELECT * FROM {table} WHERE LOWER(titulo) = LOWER(?)", (nome,))
        rows = cursor.fetchall()

        if not rows:
            print("Nenhum registro encontrado.")
            return

        print(f"\nRegistros encontrados em {table}:\n")
        for row in rows:
            print(" | ".join(str(col) for col in row))
            print("-" * 40)

    except Exception as e:
        print("Erro ao pesquisar:", e)
    finally:
        conn.close()


# === Funções futuras ===


def vender():
    print("Função 'vender' ainda não implementada.")


def emprestar():
    print("Função 'emprestar' ainda não implementada.")
