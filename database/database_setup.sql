-- MySQL dump 10.13  Distrib 8.0.42, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: ALU_SMS
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `receiver`
--

DROP TABLE IF EXISTS `receiver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receiver` (
  `receiver_id` int NOT NULL AUTO_INCREMENT,
  `account_owner` varchar(191) DEFAULT NULL,
  `phone_number` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`receiver_id`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sender`
--

DROP TABLE IF EXISTS `sender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sender` (
  `sender_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(191) DEFAULT NULL,
  `phone_number` varchar(32) NOT NULL,
  PRIMARY KEY (`sender_id`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sms`
--

DROP TABLE IF EXISTS `sms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sms` (
  `sms_id` int NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `body` text NOT NULL,
  `address` varchar(191) DEFAULT NULL,
  `readable_date` datetime DEFAULT NULL,
  `service_center` varchar(191) DEFAULT NULL,
  `status` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`sms_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `system_logs`
--

DROP TABLE IF EXISTS `system_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `log_date` datetime NOT NULL,
  `log_level` varchar(32) NOT NULL,
  `message` text NOT NULL,
  `transaction_id` int DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `transaction_id` (`transaction_id`),
  CONSTRAINT `system_logs_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transaction` (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `amount` decimal(19,4) NOT NULL,
  `transaction_date` datetime NOT NULL,
  `balance` decimal(19,4) DEFAULT NULL,
  `sender_message` text,
  `sms_id` int DEFAULT NULL,
  `sender_id` int DEFAULT NULL,
  `receiver_id` int DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  UNIQUE KEY `sms_id` (`sms_id`),
  KEY `sender_id` (`sender_id`),
  KEY `receiver_id` (`receiver_id`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`sms_id`) REFERENCES `sms` (`sms_id`),
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`sender_id`) REFERENCES `sender` (`sender_id`),
  CONSTRAINT `transaction_ibfk_3` FOREIGN KEY (`receiver_id`) REFERENCES `receiver` (`receiver_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `transaction_category`
--

DROP TABLE IF EXISTS `transaction_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(128) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  UNIQUE KEY `category_name` (`category_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `transaction_category_map`
--

DROP TABLE IF EXISTS `transaction_category_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_category_map` (
  `transaction_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`transaction_id`,`category_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `transaction_category_map_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `transaction` (`transaction_id`),
  CONSTRAINT `transaction_category_map_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `transaction_category` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'ALU_SMS'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-16 20:46:18
