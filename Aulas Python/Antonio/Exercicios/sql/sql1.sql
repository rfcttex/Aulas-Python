/* 
1- Crirar DB countries 
2- Crirar TABLE continents com as seguintes colunas:
    - continent_id inteiro auto increment PK
    - name string de 255 caracteres not null
1- Crirar TABLE languages com as colunas:
    - region_id inteiro auto increment PK
    - continent_id inteiro
    - name string de 100 caracteres not null
    - fk enrtre as colunas continent_id desta tabela
*/

CREATE IF NOT EXISTS DATABASE countries

CREATE IF NOT EXISTS TABLE continents (
    continent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE IF NOT EXISTS TABLE languages (
    region_id INT AUTO_INCREMENT PRIMARY KEY,
    continent_id INT,
    name VARCHAR(100) NOT NULL,
    CONSTRAINT fk_languages_continent FOREIGN KEY (continent_id) REFERENCES continents(continent_id)
);