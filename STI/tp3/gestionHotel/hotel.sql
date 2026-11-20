-- XAMPP-Lite
-- version 8.5.5
-- https://xampplite.sf.net/
--
-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2026 at 02:35 PM
-- Server version: 11.4.10-MariaDB-log
-- PHP Version: 8.5.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `evaluation`
--

CREATE TABLE `evaluation` (
  `dateeval` date NOT NULL,
  `idhotel` int(11) NOT NULL,
  `noteaccueil` int(11) NOT NULL,
  `noterest` int(11) NOT NULL,
  `noteextra` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `evaluation`
--

INSERT INTO `evaluation` (`dateeval`, `idhotel`, `noteaccueil`, `noterest`, `noteextra`) VALUES
('2017-05-22', 10, 3, 1, 0),
('2017-06-15', 20, 3, 2, 2),
('2017-06-15', 30, 2, 1, 2),
('2018-02-20', 10, 2, 1, 1),
('2018-04-13', 30, 2, 2, 7);

-- --------------------------------------------------------

--
-- Table structure for table `hotel`
--

CREATE TABLE `hotel` (
  `idhotel` int(11) NOT NULL,
  `nomhotel` varchar(50) NOT NULL,
  `telkotel` varchar(8) NOT NULL,
  `villehotel` varchar(30) NOT NULL
) ;

--
-- Dumping data for table `hotel`
--

INSERT INTO `hotel` (`idhotel`, `nomhotel`, `telkotel`, `villehotel`) VALUES
(10, '5 Stars', '76333444', 'Tozeur'),
(20, 'Globe', '78111111', 'Tabarka'),
(30, 'The Sun', '73888888', 'Monastir');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `evaluation`
--
ALTER TABLE `evaluation`
  ADD PRIMARY KEY (`dateeval`,`idhotel`),
  ADD KEY `idhotel` (`idhotel`);

--
-- Indexes for table `hotel`
--
ALTER TABLE `hotel`
  ADD PRIMARY KEY (`idhotel`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `evaluation`
--
ALTER TABLE `evaluation`
  ADD CONSTRAINT `evaluation_ibfk_1` FOREIGN KEY (`idhotel`) REFERENCES `hotel` (`idhotel`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
