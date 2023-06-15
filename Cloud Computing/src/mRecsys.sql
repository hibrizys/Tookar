-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: 34.101.34.210
-- Generation Time: Jun 14, 2023 at 06:27 PM
-- Server version: 5.7.40-google-log
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Tookar`
--

-- --------------------------------------------------------

--
-- Table structure for table `mRecsys`
--

CREATE TABLE `mRecsys` (
  `Customer_ID` int(11) NOT NULL,
  `Kota` varchar(10) NOT NULL,
  `Barang` varchar(22) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `mRecsys`
--

INSERT INTO `mRecsys` (`Customer_ID`, `Kota`, `Barang`) VALUES
(1, 'Jakarta', 'Jeans'),
(2, 'Batam', 'Kabel Konektor Kamera'),
(3, 'Manado', 'Monopod Kamera'),
(4, 'Lampung', 'Stabilizer Kamera'),
(5, 'Surabaya', 'Silica Gel Kamera'),
(6, 'Malang', 'Microphone Kamera'),
(7, 'Bandung', 'Tripod Kamera'),
(8, 'Medan', 'Amplifier'),
(9, 'Banten', 'Earphone'),
(10, 'Riau', 'Headphone'),
(11, 'Yogyakarta', 'Speaker'),
(12, 'Solo', 'Voice Recorder'),
(13, 'Makassar', 'TWS'),
(14, 'Palembang', 'Sound System'),
(15, 'Pasuruan', 'Baterai Kamera'),
(16, 'Jakarta', 'Charger Kamera'),
(17, 'Batam', 'Battery Grip Kamera'),
(18, 'Manado', 'Cleaning Cloth & Wipe'),
(19, 'Lampung', 'Dry Box Kamera'),
(20, 'Surabaya', 'Cleaning Swab'),
(21, 'Malang', 'Rubber Dust Air Blower'),
(22, 'Bandung', 'Lenspen'),
(23, 'Medan', 'Aksesoris Drone'),
(24, 'Banten', 'Drone Kamera'),
(25, 'Riau', 'Album Foto'),
(26, 'Yogyakarta', 'Disposable Camera'),
(27, 'Solo', 'Kamera Lomo'),
(28, 'Makassar', 'Kamera Film'),
(29, 'Palembang', 'Kamera Instan'),
(30, 'Pasuruan', 'Action Camera'),
(31, 'Jakarta', 'Kamera Mirrorless'),
(32, 'Batam', 'Kamera Pocket'),
(33, 'Manado', 'Case Kamera'),
(34, 'Lampung', 'Buku'),
(35, 'Surabaya', 'Celemek'),
(36, 'Malang', 'Gunting'),
(37, 'Bandung', 'Talenan'),
(38, 'Medan', 'Chopper'),
(39, 'Banten', 'Kotak Makan'),
(40, 'Riau', 'Botol Makan'),
(41, 'Yogyakarta', 'Bento'),
(42, 'Solo', 'Tas Botol'),
(43, 'Makassar', 'Kardus'),
(44, 'Palembang', 'Food Paper Bag'),
(45, 'Pasuruan', 'Box'),
(46, 'Jakarta', 'Paper Rice Bowl'),
(47, 'Batam', 'Dish Dryer'),
(48, 'Manado', 'Sabut'),
(49, 'Lampung', 'Bak Cuci Piring'),
(50, 'Surabaya', 'Cobek'),
(51, 'Malang', 'Deep Fryer'),
(52, 'Bandung', 'Air Fryer'),
(53, 'Medan', 'Cetakan Es'),
(54, 'Banten', 'Steamer'),
(55, 'Riau', 'Kompor'),
(56, 'Yogyakarta', 'Wajan'),
(57, 'Solo', 'Spatulla'),
(58, 'Makassar', 'Presto'),
(59, 'Palembang', 'Griller'),
(60, 'Pasuruan', 'Sumpit'),
(61, 'Jakarta', 'Gelas'),
(62, 'Batam', 'Canking'),
(63, 'Manado', 'Piring'),
(64, 'Lampung', 'Pitcher'),
(65, 'Surabaya', 'Mangkok'),
(66, 'Malang', 'Sedotan'),
(67, 'Bandung', 'Tudung Saji'),
(68, 'Medan', 'Rak Dapur'),
(69, 'Banten', 'Pompa Galon'),
(70, 'Riau', 'Alat pembuka botol'),
(71, 'Yogyakarta', 'timbangan dapur'),
(72, 'Solo', 'Water Purifier'),
(73, 'Makassar', 'Kertas Baking'),
(74, 'Palembang', 'Loyang Kue'),
(75, 'Pasuruan', 'Alumunium Foil'),
(76, 'Jakarta', 'Plastik Klip'),
(77, 'Batam', 'AC'),
(78, 'Manado', 'Juicer'),
(79, 'Lampung', 'Air Purifier'),
(80, 'Surabaya', 'Kipas Angin'),
(81, 'Malang', 'Oven'),
(82, 'Bandung', 'Toaster'),
(83, 'Medan', 'Kulkas'),
(84, 'Banten', 'Blender'),
(85, 'Riau', 'Rice Cooker'),
(86, 'Yogyakarta', 'Mixer'),
(87, 'Solo', 'Slow Cooker'),
(88, 'Makassar', 'Setrika'),
(89, 'Palembang', 'Mesin Cuci'),
(90, 'Pasuruan', 'Vacuum Cleaner'),
(91, 'Jakarta', 'Setrika Uap'),
(92, 'Batam', 'Hand Blower'),
(93, 'Manado', 'TV'),
(94, 'Lampung', 'Remote TV'),
(95, 'Surabaya', 'Televisi'),
(96, 'Malang', 'Bracket TV'),
(97, 'Bandung', 'Printer'),
(98, 'Medan', 'Tinta Printer'),
(99, 'Banten', 'Keyboard'),
(100, 'Riau', 'Radio'),
(101, 'Yogyakarta', 'Lampu Baca'),
(102, 'Solo', 'Senter'),
(103, 'Makassar', 'Lampu Dinding'),
(104, 'Palembang', 'Bohlam'),
(105, 'Pasuruan', 'Celana Jeans'),
(106, 'Jakarta', 'Topi'),
(107, 'Batam', 'Syal'),
(108, 'Manado', 'Baju Renang'),
(109, 'Lampung', 'Jumper'),
(110, 'Surabaya', 'Jaket'),
(111, 'Malang', 'Sepatu'),
(112, 'Bandung', 'Kemeja'),
(113, 'Medan', 'Jas Tuxedo'),
(114, 'Banten', 'Hoodie'),
(115, 'Riau', 'Dompet'),
(116, 'Yogyakarta', 'Tas'),
(117, 'Solo', 'Koper'),
(118, 'Makassar', 'Ransel'),
(119, 'Palembang', 'Pashmina'),
(120, 'Pasuruan', 'Jilbab'),
(121, 'Jakarta', 'Hijab Instan'),
(122, 'Batam', 'Cardigan'),
(123, 'Manado', 'Baju Koko'),
(124, 'Lampung', 'Gamis'),
(125, 'Surabaya', 'Mukena'),
(126, 'Malang', 'Peci'),
(127, 'Bandung', 'Sajadah'),
(128, 'Medan', 'Ikat Pinggang'),
(129, 'Banten', 'Kaos Polo'),
(130, 'Riau', 'Piyama'),
(131, 'Manado', 'Laptop Acer');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mRecsys`
--
ALTER TABLE `mRecsys`
  ADD PRIMARY KEY (`Customer_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
