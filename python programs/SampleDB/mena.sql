Drop database if exists menagerie;
CREATE DATABASE menagerie;
USE menagerie;
SOURCE D:/SampleDB/cr_pet_tbl.sql
LOAD DATA LOCAL INFILE 'D:/SampleDB/pet.txt' INTO TABLE pet;
SOURCE D:/SampleDB/ins_puff_rec.sql
SOURCE D:/SampleDB/cr_event_tbl.sql
LOAD DATA LOCAL INFILE 'D:/SampleDB/event.txt' INTO TABLE event;















