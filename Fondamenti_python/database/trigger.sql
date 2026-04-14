use chinook;
drop procedure AddArtist;
drop trigger LogArtisti;

DELIMITER $$

create procedure AddArtist(in id int, in nome varchar(30))
begin
	insert into artist ( Artistid, `name`) value (id, nome);
end $$

delimiter ;

call AddArtist(276, "Bruce Springsteen");
call AddArtist(277, "Ghali");

create table artist_log (
	log_id int primary key auto_increment,
    Evento varchar(50),
    DataEvento date
);

DELIMITER $$

create trigger LogArtisti
after insert -- , update, delete
on artist for each row
begin
	insert into artist_log (Evento, DataEvento)
    values ('Modifica agli ordini', curdate());
end $$

delimiter ;

