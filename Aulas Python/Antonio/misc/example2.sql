use antonio_1;
CREATE TABLE POST(
Num INT PRIMARY KEY AUTO_INCREMENT,
Author INT NOT NULL,
Creation DATETIME NOT NULL,
Content TEXT NOT NULL,
CONSTRAINT fk_post_user2 FOREIGN KEY(Author) REFERENCES user2(num)
);

/*multiline*/
-- single line

CREATE TABLE POST_LIKED(
user2 INT NOT NULL,
Post INT NOT NULL,
PRIMARY KEY(user2,Post),
CONSTRAINT fk_post_liked_user2 FOREIGN KEY(user2) REFERENCES user2(num),
CONSTRAINT fk_post_liked_post FOREIGN KEY(POST) REFERENCES POST(num)
);

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