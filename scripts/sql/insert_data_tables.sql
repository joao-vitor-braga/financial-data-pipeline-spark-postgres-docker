--dados tabela associado
INSERT INTO associado (id, nome, sobrenome, idade, email) VALUES
(1, 'Joao', 'Braga', 30, 'joaovitorbraga10@hotmail.com'),
(2, 'Mateus', 'Silva', 25, 'mateussilva@hotmail.com'),
(3, 'Alessandra', 'Farias', 20, 'alessandrafarias@hotmail.com');

--dados tabela conta
INSERT INTO conta (id, tipo, data_criacao, id_associado) VALUES
(1, 'Corrente', '2025-10-26 16:00:00', 1),
(2, 'Poupanca', '2025-10-22 15:00:00', 2),
(3, 'Poupanca', '2025-09-20 14:00:00', 3);

--dados tabela cartao
INSERT INTO cartao (id, num_cartao, nom_impresso, id_conta, id_associado) VALUES
(1, 1111111111111111, 'JOAO BRAGA', 1, 1),
(2, 2222222222222222, 'MATEUS SILVA', 2, 2),
(3, 3333333333333333, 'ALESSANDRA FARIAS', 3, 3);

--dados tabela movimento
INSERT INTO movimento (id, vlr_transacao, des_transacao, data_movimento, id_cartao) VALUES
(1, 200.00, 'Academia', '2025-10-26 16:30:00', 1),
(2, 350.00, 'Crossfit', '2025-10-24 10:00:00', 2),
(3, 550.80, 'Mercado', '2025-10-02 19:30:00', 3);