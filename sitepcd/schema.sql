DROP TABLE if EXISTS posts;
DROP TABLE if EXISTS candidato;
DROP TABLE if EXISTS vaga;
DROP TABLE if EXISTS empresa;
DROP TABLE if EXISTS aplicacoes;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE candidato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE empresa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cnpj TEXT NOT NULL
);

CREATE TABLE vaga (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    criada TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    empresa_id INTEGER,
    FOREIGN KEY(empresa_id) REFERENCES empresa(id)
);

CREATE TABLE aplicacoes (
    vaga_id INTEGER,
    candidato_id INTEGER,
    FOREIGN KEY(vaga_id) REFERENCES vaga(id),
    FOREIGN KEY(candidato_id) REFERENCES candidato(id)
);