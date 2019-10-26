# tables.py
# SQL code to create tables of 'inventory' database

tables = {}
tables['users'] = (
    "CREATE TABLE `comments` ("
    "   `comment_id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `user_id` int(11) DEFAULT NULL,"
    "   `question_id` int(11) NOT NULL,"
    "   `comment_text` varchar(750) NOT NULL,"
    "   `is_anonymous` tinyint(4) DEFAULT '1',"
    "   `source` varchar(45) NOT NULL DEFAULT 'SideEffects App',"
    "   PRIMARY KEY (`comment_id`),"
    "   UNIQUE KEY `id_UNIQUE` (`comment_id`)"
    "   ) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
)

tables['questions'] = (
    "CREATE TABLE `questions` ("
    "   `question_id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `user_id` int(11) DEFAULT NULL,"
    "   `title` varchar(500) NOT NULL,"
    "   `date_created` datetime NOT NULL,"
    "   `date_updated` datetime NOT NULL,"
    "   `is_anonymous` tinyint(4) DEFAULT '1',"
    "   `source` varchar(25) NOT NULL DEFAULT 'SideEffects App',"
    "   `num_comments` int(11) NOT NULL DEFAULT '0',"
    "   PRIMARY KEY (`question_id`),"
    "   UNIQUE KEY `id_UNIQUE` (`question_id`),"
    "   UNIQUE KEY `title_UNIQUE` (`title`)"
    ") ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
)

tables['comments'] = (
    "CREATE TABLE `comments` ("
    "   `comment_id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `user_id` int(11) DEFAULT NULL,"
    "   `question_id` int(11) NOT NULL,"
    "   `comment_text` varchar(750) NOT NULL,"
    "   `is_anonymous` tinyint(4) DEFAULT '1',"
    "   `source` varchar(45) NOT NULL DEFAULT 'SideEffects App',"
    "   PRIMARY KEY (`comment_id`),"
    "   UNIQUE KEY `id_UNIQUE` (`comment_id`)"
    "   ) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
)