CREATE DATABASE dbproject;

create table customer(
	ID int,
    FirstName varchar(255) ,
    LastName varchar(255),
    address varchar(255),
    email varchar(255),
    password varchar(255),
    PRIMARY KEY (ID)
);
create table restaurant(
	ID int,
    RestaurantName varchar(255),
    RestaurantAdress varchar(255),
    primary key (ID)
);
create table item(
	ID int,
    resID int,
    foodName varchar(255),
    foodPrice int,
    primary key (ID),
    foreign key (resID) references restaurant(ID)
);
create table manager(
	ID int, 
    resID int,
    email varchar(255),
    customerID int,
    primary key (email),
    foreign key (resID) references restaurant(ID),
    foreign key (customerID) references customer(ID)
);
create table orders(
    orderID int,
    date datetime,
    customerID int,
    primary key (orderID),
    foreign key (customerID) references customer(ID)
);
CREATE TABLE orderItems (
    orderItemID int,
    orderID int,
    itemID int,
    quantity int,
    primary key (orderItemID),
    foreign key (orderID) references orders(orderID),
    foreign key (itemID) references item(ID)
);