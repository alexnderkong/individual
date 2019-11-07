--
-- Table structure for table `users`
--


/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE IF NOT EXISTS users
           (
                        id         INTEGER NOT NULL AUTO_INCREMENT,
                        first_name VARCHAR(50) NOT NULL,
                        last_name  VARCHAR(50) NOT NULL,
                        email      VARCHAR(150) NOT NULL,
                        PASSWORD   VARCHAR(100) NOT NULL,
                        PRIMARY KEY (id),
                        UNIQUE (email)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--

--
-- Table structure for table `posts`
--


/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE IF NOT EXISTS posts (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        title VARCHAR(200) NOT NULL, 
        content VARCHAR(100) NOT NULL, 
        level INTEGER NOT NULL, 
        date_posted DATETIME NOT NULL, 
        image_file VARCHAR(150) NOT NULL, 
        user_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(user_id) REFERENCES users (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
