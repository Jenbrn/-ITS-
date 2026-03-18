# SQL lezione del 23/01/2026

## termninale windows

```bash
mysql> create database ITS2026;
Query OK, 1 row affected (0.01 sec)

mysql> create user ITS2026@localhost identified by 'ITS2026';
Query OK, 0 rows affected (0.01 sec)

mysql> grant all on ITS2026.* to ITS2026@localhost;
Query OK, 0 rows affected (0.01 sec)

```




```bash
PS C:\Users\m.bogliaccino\Desktop\ITS2026_ACA> mysql -u ITS2026 -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 19
Server version: 8.4.8 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show tables;
ERROR 1046 (3D000): No database selected
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |

mysql> show tables;
ERROR 1046 (3D000): No database selected
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
ERROR 1046 (3D000): No database selected
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| Database           |
+--------------------+
| information_schema |
| information_schema |
| its2026            |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)

mysql> use its2026;
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> create table canzoni(id int, titolo varchar(40) , cantante varchar(60));
Query OK, 0 rows affected (0.04 sec)

mysql> show tables;
+-------------------+
| Tables_in_its2026 |
+-------------------+
| canzoni           |
+-------------------+
1 row in set (0.00 sec)

mysql> desc canzoni;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| id       | int         | YES  |     | NULL    |       |
| titolo   | varchar(40) | YES  |     | NULL    |       |
| cantante | varchar(60) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.03 sec)

mysql> insert into canzoni values (1, '', '');
Query OK, 1 row affected (0.02 sec)

mysql> drop table canzoni;
Query OK, 0 rows affected (0.07 sec)

mysql> show tables; 
Empty set (0.00 sec)

mysql> create table canzoni(id int, titolo varchar(40) NOT NULL , cantante varchar(60));
Query OK, 0 rows affected (0.10 sec)

mysql> insert into canzoni values (1, '', '');
Query OK, 1 row affected (0.01 sec)

mysql> drop table canzoni;
Query OK, 0 rows affected (0.10 sec)

mysql> create table canzoni(id int, titolo varchar(40) NOT NULL DEFAULT 'titolo sconosciuto' , cantante varchar(60) NOT NULL);
Query OK, 0 rows affected (0.11 sec)

mysql> insert into canzoni values (1, NULL, NULL);
ERROR 1048 (23000): Column 'titolo' cannot be null
mysql> insert into canzoni values (1, '', NULL);  
ERROR 1048 (23000): Column 'cantante' cannot be null
mysql> insert into canzoni values (1, '', '');  
Query OK, 1 row affected (0.03 sec)

mysql> slect * from canzoni;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'slect * from canzoni' at line 1
mysql> select * from canzoni;
+------+--------+----------+
| id   | titolo | cantante |
+------+--------+----------+
|    1 |        |          |
+------+--------+----------+
1 row in set (0.00 sec)

mysql> select * from canzoni;                     
+------+--------+----------+
| id   | titolo | cantante |
+------+--------+----------+
|    1 |        |          |
+------+--------+----------+
1 row in set (0.00 sec)

mysql> update canzoni set titolo = 'Sinceramente', cantante = 'Annalisa' where id = 1;
Query OK, 1 row affected (0.05 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> delete from canzoni where id = 1;
Query OK, 1 row affected (0.02 sec)

mysql> select * from canzoni;
Empty set (0.00 sec)

mysql>
```


```sql
drop table canzoni;

create table canzoni(

	id int primary key auto_increment,
    titolo varchar(40) not null,
    cantante varchar(60) not null

);

show create table canzoni;


SELECT * FROM its2026.canzoni where cantante like '%shiva%';



use its2026;

insert into canzoni (titolo, cantante) values ('Sinceramente', "Annalisa");

select distinct cantante from canzoni order by cantante;

```
