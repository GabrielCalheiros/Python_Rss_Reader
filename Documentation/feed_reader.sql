-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 25/10/2024 às 20:02
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `feed_reader`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `category`
--

CREATE TABLE `category` (
  `id_category` int(20) NOT NULL,
  `category_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `entries`
--

CREATE TABLE `entries` (
  `id_entry` int(20) NOT NULL,
  `id_subcategory` int(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `subtitle` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `published` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `tags` varchar(255) NOT NULL,
  `summary` varchar(255) NOT NULL,
  `content` varchar(255) NOT NULL,
  `comments` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `rating` varchar(255) NOT NULL,
  `statistics` varchar(255) NOT NULL,
  `duration` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `publisher` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `feeds`
--

CREATE TABLE `feeds` (
  `id_feed` int(20) NOT NULL,
  `id_category` int(20) NOT NULL,
  `id_subcategory` int(20) NOT NULL,
  `feed_name` varchar(255) NOT NULL,
  `html_url` varchar(255) NOT NULL,
  `xml_url` varchar(255) NOT NULL,
  `feed_icon` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `subcategory`
--

CREATE TABLE `subcategory` (
  `id_subcategory` int(20) NOT NULL,
  `name_subcategory` varchar(255) NOT NULL,
  `id_view` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `view`
--

CREATE TABLE `view` (
  `id_view` int(20) NOT NULL,
  `view_name` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id_category`);

--
-- Índices de tabela `entries`
--
ALTER TABLE `entries`
  ADD PRIMARY KEY (`id_entry`);

--
-- Índices de tabela `feeds`
--
ALTER TABLE `feeds`
  ADD PRIMARY KEY (`id_feed`);

--
-- Índices de tabela `subcategory`
--
ALTER TABLE `subcategory`
  ADD PRIMARY KEY (`id_subcategory`);

--
-- Índices de tabela `view`
--
ALTER TABLE `view`
  ADD PRIMARY KEY (`id_view`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `category`
--
ALTER TABLE `category`
  MODIFY `id_category` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `entries`
--
ALTER TABLE `entries`
  MODIFY `id_entry` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `feeds`
--
ALTER TABLE `feeds`
  MODIFY `id_feed` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `subcategory`
--
ALTER TABLE `subcategory`
  MODIFY `id_subcategory` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `view`
--
ALTER TABLE `view`
  MODIFY `id_view` int(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
