create database bancojl;

use bancojl;

create table produtos(
	nome VARCHAR(255) NOT NULL,
	descricao VARCHAR(255) NOT NULL,
	valor DECIMAL(10,2) NOT NULL,
	disponivel  TINYINT(1) NOT NULL
);
