# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.5-10.1.34-MariaDB)
# Database: graphql
# Generation Time: 2019-04-03 07:52:29 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `graphql` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `graphql`;

# Dump of table articles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `articles`;

CREATE TABLE `articles` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `author_id` int(11) NOT NULL COMMENT '作者ID',
  `content` longtext NOT NULL COMMENT '文章内容',
  `title` varchar(255) NOT NULL DEFAULT '' COMMENT '文章标题',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章表';

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;

INSERT INTO `articles` (`id`, `author_id`, `content`, `title`, `created_at`, `updated_at`)
VALUES
	(1,1,'新的呢','标题1','2019-02-26 22:10:54','2019-03-26 22:37:10'),
	(2,1,'内容2','标题2','2019-02-26 22:10:56','2019-02-27 00:37:41'),
	(3,2,'内容3','标题3','2019-02-26 22:10:59','2019-02-27 00:37:45'),
	(4,2,'内容4','标题4','2019-02-26 22:11:01','2019-02-27 00:37:42'),
	(5,2,'内容5','标题5','2019-02-26 22:11:03','2019-02-27 00:37:43');

/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table authors
# ------------------------------------------------------------

DROP TABLE IF EXISTS `authors`;

CREATE TABLE `authors` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '作者ID',
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '作者姓名',
  `writer_type` varchar(15) NOT NULL DEFAULT '' COMMENT '作家的类型:专业(professional)和业余(ordinary)',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='作者表';

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;

INSERT INTO `authors` (`id`, `name`, `writer_type`, `created_at`, `updated_at`)
VALUES
	(1,'hao','ordinary','2019-01-30 11:20:16','2019-04-03 14:31:51'),
	(2,'fly','professional','2019-01-30 11:20:17','2019-04-03 14:32:05');

/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table comments
# ------------------------------------------------------------

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '评论ID',
  `article_id` int(11) NOT NULL COMMENT '文章ID',
  `content` text NOT NULL COMMENT '评论内容',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='评论表';

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;

INSERT INTO `comments` (`id`, `article_id`, `content`, `created_at`, `updated_at`)
VALUES
	(1,1,'好评1','2019-02-26 22:12:19','2019-02-27 00:38:07'),
	(2,2,'好评2🤣','2019-02-26 22:12:22','2019-02-27 00:38:09'),
	(3,3,'好评3','2019-02-26 22:12:25','2019-02-27 00:38:10'),
	(4,4,'😀😃😄😁😆','2019-02-26 22:12:27','2019-02-27 00:38:11'),
	(5,5,'😅😂🤣😊😊','2019-02-26 22:12:30','2019-02-27 00:38:13'),
	(6,1,'差评','2019-02-26 22:12:32','2019-02-27 00:38:14');

/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table ordinary_writers
# ------------------------------------------------------------

DROP TABLE IF EXISTS `ordinary_writers`;

CREATE TABLE `ordinary_writers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL COMMENT '对应的author_id',
  `job` varchar(20) NOT NULL DEFAULT '' COMMENT '职业',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='业余作家表';

LOCK TABLES `ordinary_writers` WRITE;
/*!40000 ALTER TABLE `ordinary_writers` DISABLE KEYS */;

INSERT INTO `ordinary_writers` (`id`, `author_id`, `job`)
VALUES
	(1,1,'computer');

/*!40000 ALTER TABLE `ordinary_writers` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table professional_writers
# ------------------------------------------------------------

DROP TABLE IF EXISTS `professional_writers`;

CREATE TABLE `professional_writers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL COMMENT '对应的author_id',
  `publishing_house` varchar(50) NOT NULL DEFAULT '' COMMENT '出版社',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='专业作家表';

LOCK TABLES `professional_writers` WRITE;
/*!40000 ALTER TABLE `professional_writers` DISABLE KEYS */;

INSERT INTO `professional_writers` (`id`, `author_id`, `publishing_house`)
VALUES
	(1,2,'某出版社');

/*!40000 ALTER TABLE `professional_writers` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
