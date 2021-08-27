
Exemplo Banco de dados

create table pessoas(
    id_pessoas int(4) NOT NULL PRIMARY KEY auto_increment,
    nome varchar(30)not null,
    nascimento (DATE) 
) 

insert into pessoas (nome, nascimento) values ('Cláudio','1978-05-24')
insert into pessoas (nome, nascimento) values ('Amanda' ,'1982-05-08')
insert into pessoas (nome, nascimento) values ('Laura' , '2012-05-08')



