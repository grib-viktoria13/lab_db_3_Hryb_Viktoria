

CREATE TABLE artist (
        id int NOT NULL,
	name varchar(80) NOT NULL,
	country varchar(50),
	tcu float4,
	years int
);


CREATE TABLE genre (
	id int NOT NULL,
	artist_id int NOT NULL,
	genre_name varchar(50) NOT NULL
);


CREATE TABLE sell (
	id int NOT NULL,
	artist_id int NOT NULL,
	selling int
);

alter table artist add constraint PK_artist PRIMARY KEY (id);
alter table genre add constraint PK_genre PRIMARY KEY (id);
alter table sell add constraint PK_sell PRIMARY KEY (id);

alter table genre add constraint FK_genre_artist FOREIGN KEY (artist_id) REFERENCES artist (id); 
alter table sell add constraint FK_artist_sell FOREIGN KEY (artist_id) REFERENCES artist (id);