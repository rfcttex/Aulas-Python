
    CREATE TABLE IF NOT EXISTS Documento(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        tipo TEXT NOT NULL    
        )

    CREATE TABLE IF NOT EXISTS livro  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        tipo TEXT NOT NULL,
        paginas INTEGER NOT NULL,    
        )

    CREATE TABLE IF NOT EXISTS ebook  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        tipo TEXT NOT NULL,
        tamanho INTEGER NOT NULL,
        extensao TEXT NOT NULL    
        )

    INSERT TABLE documento  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        tipo TEXT NOT NULL    
        )
