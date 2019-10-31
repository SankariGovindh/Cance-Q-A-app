CREATE DATABASE  IF NOT EXISTS `inventory` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `inventory`;
-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: inventory
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `question_id` int(11) NOT NULL,
  `content` varchar(750) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  `is_anonymous` tinyint(1) NOT NULL,
  `source` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  CONSTRAINT `comment_chk_1` CHECK ((`is_anonymous` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,1,1,'Mom\'s doctor told us the chemo (not gemzar) would \"thin\" her hair. Nope. Wiped it our completely in 3 days. After the second or third treatment. I wish we had gone to the wig stylist while mom still had her hair. She did a good job from pictures but it would have been easier to do sooner. Just my 2 cents. (Mom was very concerned about the hair loss. Said \"why does that bother me more than the cancer?\" I reassured her that was ok to feel that way)','2019-08-16 00:00:00','2019-08-16 00:00:00',1,'Facebook'),(2,2,1,'My moms worried about her hair a lot too though it might seem trivial too me I get it she’s trying to keep all normalcy possible','2019-08-16 00:00:00','2019-08-16 00:00:00',1,'Facebook'),(3,3,1,'yes, probably. And it\'s a constant reminder of their illness, to themselves and others. Now my mom is so used to the little caps she isn\'t wearing the wig at all. But her friend who had cancer treatment told us how the wigs were easier...just pop one on, no worries! Hair all styled!','2019-08-16 00:00:00','2019-08-16 00:00:00',1,'Facebook'),(6,4,3,'Miralax as a softener a couple times a day. Milk of Magnesia mixed with prune juice warmed up can be effective within a few hours. An RX from her doctor for Lactulose will certainly get things moving. But its a continuous battle that she will have to stay on top of.','2019-10-07 00:00:00','2019-10-07 00:00:00',1,'Facebook'),(7,5,3,'Hot oatmeal with dried plums helps my mom. They also have her on colace twice a day.','2019-10-07 00:00:00','2019-10-07 00:00:00',1,'Facebook'),(8,6,3,'Miralax 3 x a day and 1 senecot twice a day, this is what dr told us to do. Sometimes we give 2 senecot twice a day. Senecot is vegetable base laxative and stool softener so very gentle. This has worked for us she is consistent. If diarrhea starts cut back.','2019-10-07 00:00:00','2019-10-07 00:00:00',1,'Facebook'),(9,4,4,'Hot prune juice. Make sure its 100% juice and heat it till its about the temp of coffee. Should work within minutes','2019-03-07 00:00:00','2019-03-07 00:00:00',1,'Facebook'),(10,3,5,'My mom used senokot-s. Now uses lax a day.','2018-09-16 00:00:00','2018-09-16 00:00:00',1,'Facebook'),(11,NULL,6,'Magnesium sulfate he can drink it and it will take effect fast any drug store carry’s it','2017-12-13 00:00:00','2017-12-13 00:00:00',1,'Facebook'),(12,NULL,7,'2 tablespoons of milk of magnesia in 6 ounces of prune juice. It worked very well for my husband.','2017-10-14 00:00:00','2017-10-14 00:00:00',1,'Facebook'),(13,NULL,7,'Pharmacist recommended something like Senokot...I chose the Walgreens brand. Unfortunately it takes 6-12 hours to work. But is suppose to be really good as a laxative & softer.','2017-10-14 00:00:00','2017-10-14 00:00:00',1,'Facebook'),(14,NULL,8,'Warm prune juice with a pat of butter.','2019-02-23 00:00:00','2019-02-23 00:00:00',1,'Facebook'),(15,NULL,8,'You can try Senna-S . It was recommended for David by his doctors when he went through treatment. It worked well and I know of many of my patients that are in pain management use it too.','2019-02-23 00:00:00','2019-02-23 00:00:00',1,'Facebook'),(16,NULL,9,'Call your dr. It’s on the list of symptoms to watch out for. It could mean that your immune system might be attacking your colon so they want to know','2018-03-01 00:00:00','2018-03-01 00:00:00',1,'Facebook'),(17,NULL,10,'It is likely the chemo causing it. It is hard on the digestive system. I would suggest getting her some Imodium AD. Works well for me.','2019-08-21 00:00:00','2019-08-21 00:00:00',1,'Facebook'),(18,NULL,11,' My partner was given medication to help with loose stools while he was on IV chemo. He’s taking oral chemo now and Imodium AD worked wonders! If it’s not available where you live most anti-diarrhea medications should work. Any questions, ask your doctor. Have him drink plenty of water to keep hydrated days before, during and days after treatment.','2019-08-22 00:00:00','2019-08-22 00:00:00',1,'Facebook'),(19,NULL,12,'Milk of mag. Worked for my husband, he didn\'t follow the directions and took two big swigs, plus plenty of water. Helped within hours','2018-05-03 00:00:00','2018-05-03 00:00:00',1,'Facebook'),(20,NULL,12,'My husband has had success with the magnesium citrate drink available over the counter at any pharmacy','2018-05-03 00:00:00','2018-05-03 00:00:00',1,'Facebook'),(21,NULL,13,'Suppositories work wonders for when you just cant go','2019-03-26 00:00:00','2019-03-26 00:00:00',1,'Facebook'),(22,NULL,14,'There are alots of things to give him but please find out first if he has a blockage. If he doesn\'t they recommend MiraLax or warm prune juice with butter. That\'s so painful. I hope they can find something to help him.','2019-08-03 00:00:00','2019-08-03 00:00:00',1,'Facebook'),(23,NULL,15,'Hubby had terrible diarrhoea on keytruda. Had to have large dose of steroids to stop it.','2019-04-29 00:00:00','2019-04-29 00:00:00',1,'Facebook'),(24,NULL,16,'One of the side affects of Keytruda is the diarrhea, you should go and checked out and let the Dr. know. I had my reaction onThanksgiving and couldn’t eat until I received anti-diarrhea meds.','2019-08-31 00:00:00','2019-08-31 00:00:00',1,'Facebook');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `question` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `content` varchar(500) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  `is_anonymous` tinyint(1) NOT NULL,
  `source` varchar(25) DEFAULT NULL,
  `num_comments` int(11) DEFAULT NULL,
  PRIMARY KEY (`question_id`),
  CONSTRAINT `question_chk_1` CHECK ((`is_anonymous` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,1,NULL,'My mothers curious, how many of you patients or caregivers have noticed extreme hair loss or thinning using Gemzar? Her doctors are saying it’s hopefully going to be minimal but my moms all worried about it','2019-10-29 19:55:09','2019-10-29 19:55:09',1,'SideEffects App',NULL),(2,8,NULL,'Will my hair grow back after chemotherapy stage3a?','2019-10-30 11:29:27','2019-10-30 11:29:27',0,'dummyTest',0),(3,2,NULL,'Okay gang, I know my wife can\'t be the only one to suffer constipation from her chemo. What has everyone done to help relieve this.','2019-10-31 16:26:16','2019-10-31 16:26:16',1,'Facebook',0),(4,5,NULL,'What can I buy for very fast relief of constipation please?','2019-10-31 16:26:39','2019-10-31 16:26:39',1,'Facebook',0),(5,6,NULL,'What have u seen work for constipation from chemotherapy?','2019-10-31 16:26:48','2019-10-31 16:26:48',1,'Facebook',0),(6,6,NULL,'My husband is on pain meds for nsc lung cancer. He is having lots of problems with constipation. He is taking Colace ','2019-10-31 16:26:57','2019-10-31 16:26:57',1,'Facebook',0),(7,3,NULL,'What is the Best medicine for constipation after chemo','2019-10-31 16:27:09','2019-10-31 16:27:09',1,'Facebook',0),(8,1,NULL,'I have a question been doing radiation for 14 days and chemo 3 days last week so now I am so constipated also on steroids what is good for me to buy for that thanks','2019-10-31 16:27:18','2019-10-31 16:27:18',1,'Facebook',0),(9,2,NULL,'Has anyone experienced diarrhea from Keytruda? This is my first side effect in a year and half and it’s been working so well.','2019-10-31 16:27:41','2019-10-31 16:27:41',0,'Facebook',0),(10,2,NULL,'My mom is on the 21 day schedule for chemo. She goes again the 27th of this month. She has nsclc that has metastasized into the bone. This is her 2nd go round with cancer. My question is...she is having diarrhea that looks like oil or greasy. Did anyone else have this symptom? If so what did you do and what caused it? It is making her sick.','2019-10-31 16:27:48','2019-10-31 16:27:48',0,'Facebook',0),(11,4,NULL,'Advice on how to stop stomach pain, and diarrhea after chemptherapy?','2019-10-31 16:27:59','2019-10-31 16:27:59',0,'Facebook',0),(12,4,NULL,'My mum is facing constipation issue for past 5 days, what should I do?','2019-10-31 16:28:04','2019-10-31 16:28:04',0,'Facebook',0),(13,5,NULL,'Anyone have a great constipation treatment...5 days without going. Today have taken 2 senna pills, 3 doses of miralax. Senna and miralax every day prior. Wont take magnesium citrate..causes vomiting.','2019-10-31 16:28:15','2019-10-31 16:28:15',1,'Facebook',0),(14,6,NULL,'My husband has lost so much weight that he has no fat round his bum. He is badly constipated and hasn’t been for 6 weeks. I’m sorry if this is not nice but he had hard poo and sitting laying he is in pain. His just come out of hospital and been on 3 laxative. Help any advice please.','2019-10-31 16:28:23','2019-10-31 16:28:23',1,'Facebook',0),(15,6,NULL,'Has anyone experienced sickness and diarrhea why on immunotherapy ?','2019-10-31 16:28:29','2019-10-31 16:28:29',1,'Facebook',0),(16,6,NULL,'My husband has been feeling very ill (it hit him all of a sudden) since about 11 a.m. today. His first Keytruda treatment was August 13th ','2019-10-31 16:28:37','2019-10-31 16:28:37',1,'Facebook',0);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(200) NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `gender_id` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `cancer_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Max','Doe','maxdoe','maxdoe@email.com','pbkdf2:sha256:150000$kCE61cY2$27e2ba6d87ad521f84df3bfdd8c1caf10b7442674d668a2163018f1ca7e28b29','2019-10-31 12:23:33',NULL,NULL,NULL),(2,'Sally','Mae','sallymae','sallymae@email.com','pbkdf2:sha256:150000$Q5D3Un47$0819a86d8d1fcf66f75c4baf651b757f383474f10992cdc2695e8a489dc08b72','2019-10-31 12:24:02',NULL,NULL,NULL),(3,'Justin','Ho','justinho','justinho@email.com','pbkdf2:sha256:150000$x2Ju1cvn$902058ce5a62f3bc82c75b6400550ba87007a04fe9c9d355fe4cb4972f2fdea3','2019-10-31 12:53:04',NULL,NULL,NULL),(30,'Amy','Chung','amychung','amychung@email.com','pbkdf2:sha256:150000$kBY2bUCO$f17015df8e135c0b67f788ccdda8dbb7c6f2a5b347df5b31557ac20a9274aadd','2019-10-31 16:22:23',NULL,NULL,NULL),(31,'Kevin','Tran','kevintran','kevintran@email.com','pbkdf2:sha256:150000$RphxoY1Z$78a15764f5d75d80de4ef07675c0397d1b0ebef119e5ed9a5eadb5d6f0465cad','2019-10-31 16:22:49',NULL,NULL,NULL),(32,'Sankari','Govindarajan','sankarigovindarajan','sankarigovindarajan@email.com','pbkdf2:sha256:150000$aBTUdhuF$6d4018956092ec616667d232c8a2588294a89d81348df85c818e5008563c95c4','2019-10-31 16:23:54',NULL,NULL,NULL),(33,'Sangeeth','Koratten','sangeethkoratten','sangeethkoratten@email.com','pbkdf2:sha256:150000$vQ4kKmZE$ccc134ff51ef7e772351913c462ebf96fdf0ec413103de9faccaec53f6e87088','2019-10-31 16:24:13',NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-31 16:41:44
