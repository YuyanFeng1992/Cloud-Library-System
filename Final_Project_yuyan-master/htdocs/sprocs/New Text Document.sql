CREATE database school;
use school;

delimiter //
create procedure get_userPwd(IN login varchar(50))
begin

select  pwd
from users u
where u.login = login;

end //
delimiter ;

-- CALL get_userPwd('fengyuya');


delimiter //
create procedure delete_inventory( In in_BookId int)
begin

delete from Inventory where BookId = in_BookId;
delete from BookInfo where BookId = in_BookId;

end //
delimiter ;
----------------------------------------------------------------------
--CALL delete_inventory('20');
--CALL delete_bookinfo('2');
--delete from BookInfo where BookId = v_BookId;
--delete_Inventory

delimiter //
create procedure get_category()
begin

select BookCName 
from Category 
order by  BookCName;

end //
delimiter ;
--CALL get_category();

delimiter //
create procedure get_book_record()
begin
select B.BookId, B.BookName ,C.BookCName, B.Author , B.Publisher, B.Pubdate, B.Price, B.Sellingprice
from Inventory I
JOIN BookInfo B ON B.BookId = I.BookId
JOIN Category C ON C.Cid = I.Cid
order by  I.CUDDate;
end //
delimiter ;
--CALL get_book_record();
--CALL add_ebook('qwe', 'qwe', 'qwe', '0607', '123', '123', 'Computer Science');
--CALL add_ebook('qs', 'asd', 'jkl', '1212', '233', '1223', 'Nursing');
delimiter //
create procedure add_ebook(In in_BookName varchar(40),IN in_Author varchar(40),IN in_Publisher varchar(40),IN  in_Pubdate varchar(40),IN in_price varchar(40),IN in_Sellingprice  varchar(40),In in_BookCName varchar(100))
begin

declare v_BookId int;
declare v_CId int;
declare v_BookName varchar(40);
declare v_Athor varchar(40) ;
declare v_Publisher varchar(40);
declare v_Pubdate varchar(40);
declare v_Price varchar(40);
declare v_Sellingprice varchar(40);
declare v_BookCName varchar(100);

select BookId 
into v_BookId 
from BookInfo B 
where B.BookName = in_BookName and B.Author = in_Author and B.Publisher = in_Publisher and B.Pubdate = in_Pubdate and B.Price = in_Price and B.Sellingprice = in_Sellingprice 
limit 1;

if (v_BookId is null) then
  insert into BookInfo ( BookName, Author, Publisher, Pubdate, Price, Sellingprice, CUDAction) 
    values (in_BookName, in_Author, in_Publisher, in_Pubdate, in_Price, in_Sellingprice, 1);
  set v_BookId = LAST_INSERT_ID();
end if ;

select CId 
into v_CId 
from Category C 
where C.BookCName = in_BookCName;

INSERT INTO Inventory (BookId, CId, CUDAction) 
SELECT v_BookId, v_CId,  1 
FROM (SELECT v_BookId, v_CId) AS tmp
WHERE NOT EXISTS (
    SELECT I.BookId, I.CId 
    FROM Inventory I
    WHERE I.BookId = v_BookId and I.CId = v_CId
) LIMIT 1;
 
end //

delimiter ;


CREATE TABLE BookInfo (
  BookId int NOT NULL AUTO_INCREMENT,
  BookName varchar(40) DEFAULT NULL,
  BookCName varchar(100) DEFAULT NULL,
  Author varchar(40) DEFAULT NULL,
  Publisher varchar(40) DEFAULT NULL,
  Pubdate varchar(40) DEFAULT NULL,
  Price int DEFAULT NULL,
  Sellingprice varchar(40) DEFAULT NULL,
  CUDDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CUDAction int,
  PRIMARY KEY (BookId)
);


CREATE TABLE Category (
  CId int NOT NULL AUTO_INCREMENT,
  BookCName varchar(100) DEFAULT NULL,
  CUDDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CUDAction int,
  PRIMARY KEY (CId)
);


CREATE TABLE Inventory(
  BookId int,
  CId int,
  CUDDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CUDAction int,
  KEY BookId (BookId),
  KEY CId (CId),
  CONSTRAINT Inventory_ibfk_1 FOREIGN KEY (BookId) REFERENCES BookInfo (BookId),
  CONSTRAINT Inventory_ibfk_2 FOREIGN KEY (CId) REFERENCES Category (CId)
);

CREATE TABLE users (
  userId int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  pwd varchar(300),
  login varchar(50),
  CUDDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CUDAction int,
  CONSTRAINT users_unique UNIQUE (login)
);


insert into Category (BookCName, CUDAction) values ('Computer Science',  1);
insert into Category (BookCName, CUDAction) values ('Electrical Engineering',  1);
insert into Category (BookCName, CUDAction) values ('Biological Science',  1);
insert into Category (BookCName, CUDAction) values ('Nursing',  1);
insert into Category (BookCName, CUDAction) values ('Civil Engineering',  1);

insert into users (login, pwd, CUDAction) values ('fengyuya', 'e828d9946fdbff263b003cf683e8a9ab47f816abaabb19f28f51af5cf9d50850ff03f53010f80725f46311b6381af4763c804f5958eeada3072c748ae5c52ddb', 1);
  --username: fengyuya
  --password: fyygrubby123