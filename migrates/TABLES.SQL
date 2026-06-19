CREATE DATABASE IF NOT EXISTS db_skate;
USE db_skate;


CREATE TABLE usuarios (
    cod_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(255)
);


CREATE TABLE produtos (
    cod_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    desc_produto TEXT,
    preco DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(50),
    disponibilidade BOOLEAN DEFAULT TRUE
);


CREATE TABLE img_produtos (
    cod_img INT PRIMARY KEY AUTO_INCREMENT,
    produto_id INT NOT NULL,
    url VARCHAR(255) NOT NULL,

    FOREIGN KEY (produto_id)
    REFERENCES produtos(cod_produto)
);


CREATE TABLE carrinhos (
    cod_carrinho INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT UNIQUE NOT NULL,

    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(cod_usuario)
);

CREATE TABLE itens_carrinhos (
    cod_item_carrinho INT PRIMARY KEY AUTO_INCREMENT,
    carrinho_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL DEFAULT 1,

    FOREIGN KEY (carrinho_id)
    REFERENCES carrinhos(cod_carrinho),

    FOREIGN KEY (produto_id)
    REFERENCES produtos(cod_produto)
);

CREATE TABLE favoritos (
    cod_favorito INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    produto_id INT NOT NULL,

    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(cod_usuario),

    FOREIGN KEY (produto_id)
    REFERENCES produtos(cod_produto)
);


CREATE TABLE comentarios (
    cod_comentario INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    produto_id INT NOT NULL,
    nota INT CHECK (nota >= 0 AND nota <= 5),
    comentario TEXT,

    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(cod_usuario),

    FOREIGN KEY (produto_id)
    REFERENCES produtos(cod_produto)
);


CREATE TABLE pedidos (
    cod_pedido INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(50),
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(cod_usuario)
);


CREATE TABLE itens_pedidos (
    cod_item_pedido INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (pedido_id)
    REFERENCES pedidos(cod_pedido),

    FOREIGN KEY (produto_id)
    REFERENCES produtos(cod_produto)
);

CREATE TABLE paginas_dinamicas (
    cod_pagina INT AUTO_INCREMENT PRIMARY KEY,
    slug VARCHAR(50) UNIQUE, 
    titulo VARCHAR(100),     
    conteudo TEXT           
);