-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-01-2023 a las 23:11:31
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.2.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `informacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `documento` varchar(20) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `nombre`, `apellido`, `documento`, `correo`, `telefono`) VALUES
(1, 'martin', 'mora', '1010202020', 'mmora@gmail.com', '3001234567'),
(2, 'ana', 'contreras', '1010202021', 'acontreras@gmail.com', '3002345678'),
(3, 'patricia', 'castaño', '1010202022', 'acastano@gmail.com', '3003456789'),
(4, 'jose', 'robledo', '1010202023', 'jrobledo@gmail.com', '3004567890'),
(5, 'rosaura', 'mora', '1010202024', 'rmora@gmail.com', '3011234567'),
(6, 'hernando', 'contreras', '1010202025', 'hcontreras@gmail.com', '3012345678'),
(7, 'patricia', 'hernandez', '1010202026', 'phernandez@gmail.com', '3013456789');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(11) NOT NULL,
  `codigo` varchar(20) DEFAULT NULL,
  `nombre` varchar(50) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `subcategoria` varchar(50) NOT NULL,
  `precio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `codigo`, `nombre`, `categoria`, `subcategoria`, `precio`) VALUES
(1, '804301', 'jabon de avena', 'aseo personal', 'aseo', 3000),
(2, '804302', 'jabon de clasico', 'aseo personal', 'aseo', 3000),
(3, '671901', 'fresas x 500gr', 'frutas', 'fruver', 7000),
(4, '671902', 'uchuvas x 500gr', 'frutas', 'fruver', 5000),
(5, '804311', 'detergente as x 1000 gr', 'aseo hogar', 'aseo', 8000),
(6, '804312', 'blancox x 2l', 'aseo hogar', 'aseo', 10000),
(7, '804313', 'fabuloso lavanda x 1l', 'aseo hogar', 'aseo', 5000),
(8, '671911', 'acelga x 500gr', 'verdura', 'fruver', 12000),
(9, '671912', 'espinaca x 500gr', 'verdura', 'fruver', 13000),
(10, '402011', 'arroz x 500gr', 'granos', 'granos y cereales', 2000),
(11, '402012', 'avena x 500gr', 'cereales', 'granos y cereales', 4000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id` int(11) NOT NULL,
  `idcliente` int(11) NOT NULL,
  `idproducto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`id`, `idcliente`, `idproducto`, `cantidad`, `total`, `fecha`) VALUES
(1, 1, 1, 2, 14000, '2022-01-01'),
(2, 2, 1, 3, 21000, '2022-01-01'),
(3, 5, 5, 4, 20000, '2022-01-02'),
(4, 6, 5, 6, 30000, '2022-01-02'),
(6, 7, 3, 1, 8000, '2022-02-01'),
(7, 3, 3, 4, 32000, '2022-02-01'),
(8, 7, 2, 1, 5000, '2022-03-01'),
(10, 2, 2, 5, 25000, '2022-03-01'),
(11, 6, 2, 6, 12000, '2022-04-15'),
(12, 7, 2, 10, 120000, '2022-04-15'),
(13, 4, 4, 1, 10000, '2022-05-15'),
(14, 7, 4, 2, 20000, '2022-05-15'),
(15, 2, 4, 3, 30000, '2022-05-15'),
(16, 1, 8, 1, 2000, '2022-06-15'),
(17, 2, 8, 1, 2000, '2022-06-15'),
(18, 3, 8, 1, 2000, '2022-06-15'),
(19, 4, 8, 1, 2000, '2022-06-15'),
(20, 5, 8, 1, 2000, '2022-06-15'),
(21, 6, 8, 1, 2000, '2022-06-15');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `documento` (`documento`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idcliente` (`idcliente`),
  ADD KEY `idproducto` (`idproducto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`idcliente`) REFERENCES `cliente` (`id`),
  ADD CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
