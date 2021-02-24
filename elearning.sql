create database elearning;

create table vcategory(
    vcategory_id serial primary key,
    vcategory_name varchar(50) not null
);

create table video(
    video_id serial primary key,
    video_name varchar(50) not null,
    video_link varchar(200) not null,
    vcategory_id int references vcategory(vcategory_id)
);