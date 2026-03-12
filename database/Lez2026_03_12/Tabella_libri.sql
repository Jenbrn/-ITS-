create database biblioteca;

grant all on biblioteca.* to ITS2026@localhost;

use biblioteca;

select * from libri;

drop table libri;

show create table libri;

CREATE TABLE `libri` (
   `id` int DEFAULT NULL,
   `Codice` text,
   `Autore` text,
   `Titolo` text,
   `Editore` text,
   `Anno` text,
   `Luogo` text,
   `Pagine` int DEFAULT NULL,
   `Classificazione` text
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci