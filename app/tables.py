# tables.py
# SQL code to create tables of 'inventory' database

tables = {}
tables['users'] = (
    "CREATE TABLE `users` ("
    "   `id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `username` varchar(45) NOT NULL,"
    "   `email` varchar(45) NOT NULL,"
    "   `password` varchar(45) NOT NULL,"
    "   `date_created` datetime NOT NULL,"
    "   `question_history` json DEFAULT NULL,"
    "   `cancer_history` json DEFAULT NULL,"
    "   PRIMARY KEY (`id`),"
    "   UNIQUE KEY `ID_UNIQUE` (`id`),"
    "   UNIQUE KEY `username_UNIQUE` (`username`),"
    "   UNIQUE KEY `email_UNIQUE` (`email`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	'"
)

tables['questions'] = (
    "CREATE TABLE `questions` ("
    "   `question_id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `user_id` int(11) NOT NULL,"
    "   `title` varchar(250) NOT NULL,"
    "   `date_created` datetime NOT NULL,"
    "   `date_updated` datetime NOT NULL,"
    "   `is_anonymous` tinyint(4) NOT NULL DEFAULT '1',"
    "   `source` varchar(25) NOT NULL DEFAULT 'SideEffects App',"
    "   PRIMARY KEY (`id`),"
    "   UNIQUE KEY `id_UNIQUE` (`id`),"
    "   UNIQUE KEY `title_UNIQUE` (`title`)"
    ") ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
)

tables['comments'] = (
    "CREATE TABLE `comments` ("
    "   `id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `user_id` int(11) NOT NULL,"
    "   `question_id` int(11) NOT NULL,"
    "   `comment_text` varchar(500) NOT NULL,"
    "   `is_anonymous` tinyint(4) NOT NULL,"
    "   `source` varchar(45) NOT NULL DEFAULT 'SideEffects App',"
    "   PRIMARY KEY (`id`),"
    "   UNIQUE KEY `id_UNIQUE` (`id`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
)