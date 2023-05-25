-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19-Fev-2022 às 13:22
-- Versão do servidor: 10.4.22-MariaDB
-- versão do PHP: 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `projeto_m16`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargos`
--

CREATE TABLE `cargos` (
  `Cargo` varchar(100) DEFAULT NULL,
  `Permissao` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cargos`
--

INSERT INTO `cargos` (`Cargo`, `Permissao`) VALUES
('Gerente', 0),
('Chefe de loja', 1),
('Chefe de Secção', 2),
('Funcionário', 3),
('Estagiário', 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `detalhes_encomenda`
--

CREATE TABLE `detalhes_encomenda` (
  `id_encomenda` varchar(10) NOT NULL,
  `id_produto` varchar(15) NOT NULL,
  `quantidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `detalhes_encomenda`
--

INSERT INTO `detalhes_encomenda` (`id_encomenda`, `id_produto`, `quantidade`) VALUES
('K9H9GpxP8S', '1111', 3),
('K9H9GpxP8S', '1111', 3),
('K9H9GpxP8S', '1111', 3),
('K9H9GpxP8S', '1111', 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `encomendas`
--

CREATE TABLE `encomendas` (
  `ID` varchar(20) NOT NULL,
  `Morada de Entrega` varchar(255) DEFAULT NULL,
  `Morada de Faturação` varchar(255) DEFAULT NULL,
  `Valor total` float DEFAULT NULL,
  `Estado` varchar(50) DEFAULT NULL,
  `Data de encomenda` date DEFAULT NULL,
  `Data de entrega` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `encomendas`
--

INSERT INTO `encomendas` (`ID`, `Morada de Entrega`, `Morada de Faturação`, `Valor total`, `Estado`, `Data de encomenda`, `Data de entrega`) VALUES
('K9H9GpxP8S', 'm', 'm', 100, 'Entregue', '2022-01-29', '2022-02-01');

-- --------------------------------------------------------

--
-- Estrutura da tabela `fornecedores`
--

CREATE TABLE `fornecedores` (
  `Nome` varchar(255) NOT NULL,
  `Morada` varchar(255) DEFAULT NULL,
  `IBAN` varchar(35) DEFAULT NULL,
  `NIF` varchar(30) DEFAULT NULL,
  `Nº de telefone` varchar(20) DEFAULT NULL,
  `Email` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `fornecedores`
--

INSERT INTO `fornecedores` (`Nome`, `Morada`, `IBAN`, `NIF`, `Nº de telefone`, `Email`) VALUES
('100', 'teste', 'adwa', 'aadadda', 'awdawd', 'adawd'),
('1000256', '1a', '1a', '1a', '1a', '1a'),
('1234', 'morada', '6523', '58444', '98522', 'email fixolas'),
('4555', 'awd', '123', '123', '123', 'wdd'),
('Carvalhos Rena LDa', 'Rua Santo Lucas Abreu nº203', 'PT 1839482734581734853928453', '654126582', '965482145', 'geral@carvalhosrena.pt'),
('João reis', 'morada ira', '123', '123', '123', 'email giro'),
('nome fonecer', 'morada', '123', '123', '123', 'awdad'),
('Teste', 'morada ', 'PT 658452', '56325', '658965214', 'email@fe.pt'),
('teste 3', 'morada ', 'PT 658452', '56325', '658965214', 'email@fe.pt');

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

CREATE TABLE `produtos` (
  `ID` varchar(8) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `Seccao` varchar(50) DEFAULT NULL,
  `Preco` float DEFAULT NULL,
  `Stock` int(11) DEFAULT NULL,
  `Fornecedor` varchar(255) DEFAULT NULL,
  `Descricao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`ID`, `Nome`, `Seccao`, `Preco`, `Stock`, `Fornecedor`, `Descricao`) VALUES
('111', '1111', 'Frutaria', 123, 123, '100', '123'),
('1111', '123', 'Frutaria', 123, 123, '100', '123'),
('12344', 'champoo', 'ouyo', 100, 100, '100', 'nada'),
('12345678', 'Maça', 'Frutaria', 1, 10, '1234', 'Maçã vinda de áfrica'),
('555', 'Comida', 'Frutaria', 10.5, 3, '100', 'Comida saborosa'),
('5555', 'coiso e tal', 'Frutaria', 10.94, 12, '100', 'nada a descrever');

-- --------------------------------------------------------

--
-- Estrutura da tabela `seccao`
--

CREATE TABLE `seccao` (
  `Nome da Secção` varchar(50) NOT NULL,
  `Responsável pela Secção` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `seccao`
--

INSERT INTO `seccao` (`Nome da Secção`, `Responsável pela Secção`) VALUES
('Frutaria', 5000),
('ouyo', 5000);

-- --------------------------------------------------------

--
-- Estrutura da tabela `trabalhadores`
--

CREATE TABLE `trabalhadores` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `Cargo` int(11) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Estado` varchar(10) DEFAULT NULL,
  `Salario` float DEFAULT NULL,
  `Secção` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `trabalhadores`
--

INSERT INTO `trabalhadores` (`ID`, `Nome`, `Cargo`, `Password`, `Estado`, `Salario`, `Secção`) VALUES
(5000, 'Afonso Almeida', 0, '4g==*yMUdnaMHQ5Uw+wVmsI/BEw==*8wLuSZxmCD8csKaHLzuoZw==*yoK45M2QCK/BuYcGzzAvyQ==', 'Ativo', 4500.5, 'Frutaria'),
(5004, 'Joana', 3, 'U52jEA==*yvanJp51VrJtjtcx7BuS2A==*vUR3n30s+GPp79BUjfDdcg==*4+j1WYffkBqLhpdtqL2BmA==', 'Ativo', 12344, 'Frutaria');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`Permissao`);

--
-- Índices para tabela `detalhes_encomenda`
--
ALTER TABLE `detalhes_encomenda`
  ADD KEY `id_encomenda` (`id_encomenda`),
  ADD KEY `id_produto` (`id_produto`);

--
-- Índices para tabela `encomendas`
--
ALTER TABLE `encomendas`
  ADD PRIMARY KEY (`ID`);

--
-- Índices para tabela `fornecedores`
--
ALTER TABLE `fornecedores`
  ADD PRIMARY KEY (`Nome`);

--
-- Índices para tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Seccao` (`Seccao`),
  ADD KEY `Fornecedor` (`Fornecedor`);

--
-- Índices para tabela `seccao`
--
ALTER TABLE `seccao`
  ADD PRIMARY KEY (`Nome da Secção`),
  ADD KEY `Responsável pela Secção` (`Responsável pela Secção`);

--
-- Índices para tabela `trabalhadores`
--
ALTER TABLE `trabalhadores`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Cargo` (`Cargo`),
  ADD KEY `trabalhadores` (`Secção`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `trabalhadores`
--
ALTER TABLE `trabalhadores`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5005;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `detalhes_encomenda`
--
ALTER TABLE `detalhes_encomenda`
  ADD CONSTRAINT `detalhes_encomenda_ibfk_1` FOREIGN KEY (`id_encomenda`) REFERENCES `encomendas` (`ID`),
  ADD CONSTRAINT `detalhes_encomenda_ibfk_2` FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`ID`);

--
-- Limitadores para a tabela `produtos`
--
ALTER TABLE `produtos`
  ADD CONSTRAINT `Produtos_ibfk_1` FOREIGN KEY (`Seccao`) REFERENCES `seccao` (`Nome da Secção`),
  ADD CONSTRAINT `Produtos_ibfk_2` FOREIGN KEY (`Fornecedor`) REFERENCES `fornecedores` (`Nome`);

--
-- Limitadores para a tabela `seccao`
--
ALTER TABLE `seccao`
  ADD CONSTRAINT `Seccao_ibfk_1` FOREIGN KEY (`Responsável pela Secção`) REFERENCES `trabalhadores` (`ID`);

--
-- Limitadores para a tabela `trabalhadores`
--
ALTER TABLE `trabalhadores`
  ADD CONSTRAINT `Trabalhadores_ibfk_1` FOREIGN KEY (`Cargo`) REFERENCES `cargos` (`Permissao`),
  ADD CONSTRAINT `trabalhadores` FOREIGN KEY (`Secção`) REFERENCES `seccao` (`Nome da Secção`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
