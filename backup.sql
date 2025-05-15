-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: library_system
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator` (
  `admin_account` varchar(20) NOT NULL,
  `admin_password` varchar(20) NOT NULL,
  `admin_name` varchar(20) NOT NULL,
  `admin_email` varchar(30) DEFAULT NULL,
  `admin_phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`admin_account`),
  UNIQUE KEY `admin_email` (`admin_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` VALUES ('administrator','123456','管理员',NULL,NULL);
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `book_title` varchar(50) NOT NULL,
  `book_author` varchar(20) NOT NULL,
  `book_publisher` varchar(20) DEFAULT NULL,
  `book_year` int DEFAULT NULL,
  `isbn` varchar(13) DEFAULT NULL,
  `book_state` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  UNIQUE KEY `isbn` (`isbn`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'红楼梦','曹雪芹','人民文学出版社',2005,'9787020002200','未借出'),(2,'西游记','吴承恩','人民文学出版社',2005,'9787020002201','未借出'),(3,'水浒传','施耐庵','人民文学出版社',2005,'9787020002202','未借出'),(4,'三国演义','罗贯中','人民文学出版社',2005,'9787020002203','未借出'),(5,'论语','孔子','中华书局',2006,'9787501302821','未借出'),(6,'道德经','老子','中华书局',2006,'9787501302822','未借出'),(7,'孙子兵法','孙武','商务印书馆',2007,'9787107116503','未借出'),(8,'资治通鉴','司马光','中华书局',2007,'9787501302823','未借出'),(9,'史记','司马迁','中华书局',2007,'9787501302824','未借出'),(10,'庄子','庄周','中华书局',2006,'9787501302825','未借出'),(11,'孟子','孟子','中华书局',2006,'9787501302826','未借出'),(12,'诗经','多位作者','中华书局',2006,'9787501302827','未借出'),(13,'楚辞','屈原等','中华书局',2006,'9787501302828','未借出'),(14,'儒林外史','吴敬梓','上海古籍出版社',2008,'9787532670414','未借出'),(15,'金瓶梅','兰陵笑笑生','上海古籍出版社',2008,'9787532670415','未借出'),(16,'红高粱家族','莫言','作家出版社',2009,'9787506360431','未借出'),(17,'活着','余华','作家出版社',2009,'9787506360432','未借出'),(18,'围城','钱钟书','人民文学出版社',2010,'9787020002204','未借出'),(19,'平凡的世界','路遥','人民文学出版社',2010,'9787020002205','未借出'),(20,'百年孤独','加西亚·马尔克斯','外语教学与研究出版社',2011,'9787561517324','未借出'),(21,'悲惨世界','雨果','人民文学出版社',2011,'9787020002206','未借出'),(22,'茶花女','小仲马','人民文学出版社',2011,'9787020002207','未借出'),(23,'简爱','夏洛蒂·勃朗特','外语教学与研究出版社',2012,'9787561517325','未借出'),(24,'骆驼祥子','老舍','人民文学出版社',2012,'9787020002208','未借出'),(25,'安娜·卡列尼娜','列夫·托尔斯泰','人民文学出版社',2013,'9787020002209','未借出'),(26,'曾国藩家书','曾国藩','湖南人民出版社',2013,'9787503003022','未借出'),(27,'傅雷家书','傅雷','上海译文出版社',2014,'9787532759325','未借出'),(28,'瓦尔登湖','亨利·戴维·梭罗','商务印书馆',2014,'9787107116525','未借出'),(29,'白鹿原','陈忠实','作家出版社',2015,'9787506360434','未借出'),(30,'白夜行','东野圭吾','上海译文出版社',2016,'9787532765531','未借出'),(31,'嫌疑人X的献身','东野圭吾','上海译文出版社',2016,'9787532765532','未借出'),(32,'海边的卡夫卡','村上春树','上海译文出版社',2017,'9787532765533','未借出'),(33,'挪威的森林','村上春树','上海译文出版社',2017,'9787532765534','未借出'),(34,'小王子','安东尼·德·圣埃克苏佩里','接力出版社',2018,'9787506398393','未借出'),(35,'麦田里的守望者','J.D.塞林格','外语教学与研究出版社',2018,'9787561517326','未借出'),(36,'1984','乔治·奥威尔','人民文学出版社',2019,'9787020002210','未借出'),(37,'动物农场','乔治·奥威尔','人民文学出版社',2019,'9787020002211','未借出'),(38,'霍乱时期的爱情','加西亚·马尔克斯','外语教学与研究出版社',2019,'9787561517327','未借出'),(39,'爱在瘟疫蔓延时','加西亚·马尔克斯','外语教学与研究出版社',2020,'9787561517328','未借出'),(40,'堂吉诃德','塞万提斯','商务印书馆',2020,'9787107116526','未借出'),(41,'老人与海','欧内斯特·海明威','外语教学与研究出版社',2021,'9787561517330','未借出'),(42,'源氏物语','紫式部','上海译文出版社',2022,'9787532765536','未借出'),(43,'尼罗河上的惨案','阿加莎·克里斯蒂','外语教学与研究出版社',2022,'9787561517331','未借出'),(44,'傲慢与偏见','简·奥斯汀','外语教学与研究出版社',2023,'9787561517332','未借出'),(45,'双城记','查尔斯·狄更斯','人民文学出版社',2023,'9787020002213','未借出'),(46,'简·爱','夏洛蒂·勃朗特','外语教学与研究出版社',2023,'9787561517333','未借出'),(47,'朝花夕拾','鲁迅','人民文学出版社',2024,'9787020002214','未借出'),(48,'长恨歌','王安忆','人民文学出版社',2024,'9787020002215','未借出'),(49,'狼图腾','姜戎','作家出版社',2024,'9787506360436','未借出'),(50,'霍乱时期的爱情','加西亚·马尔克斯','外语教学与研究出版社',2024,'9787561517335','未借出');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan` (
  `loan_id` int NOT NULL AUTO_INCREMENT,
  `book_id` int DEFAULT NULL,
  `student_account` varchar(20) DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  PRIMARY KEY (`loan_id`),
  KEY `book_id` (`book_id`),
  KEY `student_account` (`student_account`),
  CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`student_account`) REFERENCES `student` (`student_account`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES (1,38,'2022300878','2024-07-01','2024-07-31','2024-06-20'),(2,22,'2022300881','2024-12-01','2024-12-31','2024-12-20');
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_account` varchar(20) NOT NULL,
  `student_password` varchar(20) NOT NULL,
  `student_name` varchar(20) NOT NULL,
  `student_email` varchar(30) DEFAULT NULL,
  `student_phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`student_account`),
  UNIQUE KEY `student_email` (`student_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('2022300878','123456','夏宇轩',NULL,NULL),('2022300881','123456','魏智敏',NULL,NULL);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-22  0:14:39
