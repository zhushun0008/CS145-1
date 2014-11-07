drop table if exists auctionusers;
drop table if exists bids;
drop table if exists items;
drop table if exists categories;
drop table if exists CurrentTime;

create table auctionusers (
user_id int not null PRIMARY KEY,
rating int not null,
location text,
country text);

create table bids (
item_id int not null,
user_id int not null,
time text not null,
bid_amount real not null,
unique (item_id,time),
unique (item_id,user_id,bid_amount),
foreign key(user_id) references auctionusers(user_id),
foreign key(item_id) references items(item_id)
);

create table items (
item_id int not null PRIMARY KEY,
name text not null,
currently real not null,
first_bid real not null,
number_of_bids int not null,
started text not null,
ends text not null,
seller_id text not null,
description text not null,
buy_price real,
foreign key(seller_id) references auctionusers(user_id),
CHECK(ends>started)
);

create table categories (
item_id int not null,
category text not null,
PRIMARY KEY(item_id,category)
);

create table CurrentTime (
time text not null
);

insert into CurrentTime values ('2001-12-20 00:00:01');

select * from CurrentTime;