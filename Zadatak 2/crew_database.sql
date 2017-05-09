-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2017 at 04:45 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crew_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `aircrafts`
--

CREATE TABLE `aircrafts` (
  `id` int(10) UNSIGNED NOT NULL,
  `model` varchar(60) NOT NULL,
  `type` enum('small','medium','large') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `aircrafts`
--

INSERT INTO `aircrafts` (`id`, `model`, `type`) VALUES
(1, 'Embraer KC-390', 'small'),
(2, 'C-130 Hercules', 'small'),
(3, 'Airbus A-400M', 'medium'),
(4, 'C-17 Globemaster-III', 'medium'),
(5, 'Antonov AN-124', 'large'),
(6, 'C-5 Galaxy', 'large'),
(7, 'Airbus A-380', 'large'),
(8, 'Boeing 747-8', 'large');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `id` int(10) UNSIGNED NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `age` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`id`, `first_name`, `last_name`, `age`) VALUES
(1, 'Mark', 'Collins', 25),
(2, 'Peter', 'Rufus', 31),
(3, 'John', 'Peters', 34),
(4, 'Collin', 'Williams', 24),
(5, 'Josh', 'Burns', 26),
(6, 'Mike', 'Patters', 30),
(7, 'Jonah', 'Hickle', 23),
(8, 'Gavin', 'Cooper', 29);

-- --------------------------------------------------------

--
-- Table structure for table `member_aircraft`
--

CREATE TABLE `member_aircraft` (
  `id` int(10) UNSIGNED NOT NULL,
  `member_id` int(10) UNSIGNED NOT NULL,
  `aircraft_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `member_aircraft`
--

INSERT INTO `member_aircraft` (`id`, `member_id`, `aircraft_id`) VALUES
(1, 1, 2),
(2, 1, 3),
(3, 1, 4),
(4, 1, 6),
(5, 3, 1),
(6, 4, 2),
(7, 4, 5),
(8, 5, 7),
(9, 6, 8),
(10, 7, 8),
(11, 8, 1),
(12, 8, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aircrafts`
--
ALTER TABLE `aircrafts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `member_aircraft`
--
ALTER TABLE `member_aircraft`
  ADD PRIMARY KEY (`id`),
  ADD KEY `member_id` (`member_id`,`aircraft_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aircrafts`
--
ALTER TABLE `aircrafts`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `member_aircraft`
--
ALTER TABLE `member_aircraft`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
