use ITS2026;

drop table products;

#---------------------------------------------------------

create table products(
	code char(8) primary key,
    name varchar(30) not null,
    price decimal(6,2) not null,
    quantity int check(quantity <100)
);

alter table products
add column description varchar(120) after name;

show create table products;
alter table products drop check products_chk_1;
alter table products add constraint limite_peso check(quantity <= 100);

#-------------------------------------------------------------------------

create table orders(
	id int primary key,
    order_data date,
    total decimal(10,2),
    shipping enum('delivered', 'shipped', 'to ship'),
    shipping_address varchar(100),
    customer_id int
);

alter table orders modify id int auto_increment;

#------------------------------------------------------------------------------

create table clienti(
	id int primary key,
    first_name varchar(30),
    last_name varchar(30),
    email varchar(100),
    address varchar(100),
    city varchar(50),
    province char(2),
    region varchar(30),
    registration_date date
);

alter table clienti modify last_name varchar(50);

alter table clienti
add column phone varchar(20) after last_name;

alter table clienti
add column postal_code char(5) after region;

alter table clienti
	drop column phone,
    drop column postal_code;
    
alter table clienti
	add column phone varchar(20) after last_name,
    add column postal_code char(5) after region;
    
rename table clienti to customers;

alter table customers modify id int auto_increment;
describe customers;

#-----------------------------------------------------------------
    
create table america(
	id int primary key,
    state varchar(50) not null,
    capital_id int check (capital_id < 256),
    population int check (population < 1428627664)
);

CREATE TABLE asia LIKE america;
INSERT INTO asia SELECT * FROM america;

create table africa like asia;
insert into africa select * from asia;

alter table america modify population int unsigned;
alter table asia modify population int unsigned;
alter table africa modify population int unsigned;

alter table america modify id int auto_increment;
alter table asia modify id int auto_increment;	
alter table africa modify id int auto_increment;

#-----------------------------------------------------------------------

create table books(
	iban char(13) primary key,
	title varchar(100),
    price decimal(6,2),
    price_vat decimal(6,2),
    pages int,
    editor_id int
);

alter table books rename column iban to isbn;

#----------------------------------------------------------