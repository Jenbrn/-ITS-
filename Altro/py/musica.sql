
USE its2026;

drop table if exist jenic;

create table jenic (
    canzone_id int primary key auto_increment,
    titolo varchar(200),
    artista varchar(120),
    album varchar(100),
    genere varchar(80),
    certificazione varchar(50),
    anno int,
    durata_secondi int
);

INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Bohemian Rhapsody', 'Queen', 'A Night at the Opera', 'Rock', 'Platino', '1975', '354);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Billie Jean', 'Michael Jackson', 'Thriller', 'Pop', 'Platino', '1982', '294);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Smells Like Teen Spirit', 'Nirvana', 'Nevermind', 'Grunge', 'Oro', '1991', '301);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Hotel California', 'Eagles', 'Hotel California', 'Rock', 'Platino', '1977', '391);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Rolling in the Deep', 'Adele', '21', 'Soul', 'Platino', '2010', '228);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Lose Yourself', 'Eminem', '8 Mile Soundtrack', 'Hip-Hop', 'Platino', '2002', '326);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Shape of You', 'Ed Sheeran', 'Divide', 'Pop', 'Platino', '2017', '234);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Stairway to Heaven', 'Led Zeppelin', 'Led Zeppelin IV', 'Rock', 'Oro', '1971', '482);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Someone Like You', 'Adele', '21', 'Soul', 'Platino', '2011', '285);
INSERT INTO jenic (titolo, artista, album, genere, certificazione, anno, durata_secondi) VALUES ('Blinding Lights', 'The Weeknd', 'After Hours', 'Synth-pop', 'Platino', '2019', '200);
