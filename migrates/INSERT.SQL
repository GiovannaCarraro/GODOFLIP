INSERT INTO produtos
(nome, desc_produto, preco, categoria, disponibilidade)
VALUES
(
'Skate Street Black',
'Skate ideal para manobras urbanas e street.',
300.00,
'Skate Completo',
TRUE
),
(
'Skate Fire Wheels',
'Modelo com rodas de alta resistência e velocidade.',
250.00,
'Skate Completo',
TRUE
),
(
'Godoflip Classic',
'Modelo clássico da Godoflip para iniciantes e intermediários.',
220.00,
'Skate Completo',
TRUE
),
(
'Urban Skate Pro',
'Skate profissional para uso urbano e pistas.',
380.00,
'Skate Completo',
TRUE
),
(
'Flip Dark Edition',
'Edição especial com design escuro exclusivo.',
365.00,
'Skate Completo',
TRUE
);



INSERT INTO img_produtos
(produto_id, url)
VALUES
(1, 'imagens/skate1_angulo1.webp'),
(2, 'imagens/skate2_angulo1.webp'),
(3, 'imagens/skate3_angulo01.webp'),
(4, 'imagens/skate4_angulo1.webp'),
(5, 'imagens/skate5_angulo1.webp');


INSERT INTO produtos
(nome, desc_produto, preco, categoria)
VALUES
('Truck Profissional', 'Alta resistência e estabilidade para manobras.', 129.90, 'pecas'),
('Rodas Street', 'Velocidade e controle para o dia a dia.', 89.90, 'pecas'),
('Rolamentos ABEC-7', 'Desempenho suave e alta rotação.', 59.90, 'pecas'),
('Kit Parafusos', 'Fixação segura para seu setup completo.', 19.90, 'pecas'),
('Lixa Profissional', 'Aderência máxima para manobras precisas.', 29.90, 'pecas');

INSERT INTO img_produtos
(produto_id, url)
VALUES
(1, 'img_pecas/truck.webp'),
(2, 'img_pecas/rodas.webp'),
(3, 'img_pecas/rolamentos.jpg'),
(4, 'img_pecas/parafusos.webp'),
(5, 'img_pecas/lixa.webp');


INSERT INTO produtos (nome, desc_produto, preco, categoria) 
VALUES 
('Lixa Profissional', 'Alta aderência para manobras precisas.', 29.90, 'acessorios'),
('Rodas Street', 'Durabilidade e velocidade para o dia a dia.', 89.90, 'acessorios'),
('Rolamentos ABEC-7', 'Desempenho suave e rápido.', 59.90, 'acessorios');


INSERT INTO img_produtos (produto_id, url) 
VALUES 
(11, 'img_acessorios/lixa.webp'),
(12, 'img_acessorios/rodas.webp'),
(13, 'img_acessorios/rolamentos.jpg');

INSERT INTO img_produtos (produto_id, url)
VALUES
(6, 'img_pecas/truck.webp'),
(7, 'img_pecas/rodas.webp'),
(8, 'img_pecas/rolamentos.jpg'),
(9, 'img_pecas/parafusos.webp'),
(10, 'img_pecas/lixa.webp');

ALTER TABLE produtos ADD COLUMN destaque BOOLEAN DEFAULT FALSE;

-- Ativa o destaque apenas para alguns IDs específicos
UPDATE produtos SET destaque = TRUE WHERE cod_produto IN (1, 2, 3);

ALTER TABLE usuarios ADD CONSTRAINT UNIQUE (email);

-- INSERT INTO paginas_dinamicas (slug, titulo, conteudo) 
-- VALUES (
-- 'politica-de-trocas', 
-- 'Política de Trocas', 
 --    '<h2>Regras para Trocas e Devoluções</h2><p>Na GODOFLIP, você tem até 7 dias para trocar o seu skate ou peça caso não tenha curtido ou tenha vindo com defeito.</p><p>Para solicitar, envie um email para godoflip@gmail.com.</p>'
-- );




-- Desativa temporariamente as travas de chave estrangeira para limpar os testes antigos
SET FOREIGN_KEY_CHECKS = 0;

-- Limpa a tabela de usuários antigos (ou limpe também favoritos/comentarios se der erro)
TRUNCATE TABLE usuarios;

-- Reativa as chaves estrangeiras
SET FOREIGN_KEY_CHECKS = 1;