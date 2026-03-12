use ITS2026;

drop table products;

create table products(
	code char(8) primary key,
    name varchar(30) not null,
    price decimal(6,2) not null,
    quantity int check(quantity <100)
);

alter table products
add column description varchar(120) after name;

create table orders(
	id int primary key,
    order_data date,
    total decimal(10,2),
    shipping enum('delivered', 'shipped', 'to ship'),
    shipping_address varchar(100),
    customer_id int
);

describe products;
describe orders;
describe clienti;

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

describe america;
describe asia;
describe africa;

create table books(
	iban char(13) primary key,
	title varchar(100),
    price decimal(6,2),
    price_vat decimal(6,2),
    pages int,
    editor_id int
);

rename table clienti to customers;


