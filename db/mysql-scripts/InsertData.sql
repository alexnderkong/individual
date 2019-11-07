
--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Alex','Kong','alex@gmail.com','');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'Bulbasaur','Grass',6,'2019-10-22','/static/bulbasaur.png',1),(2,'Charizard','Fire',90,'2019-10-22','/static/charizard.jpg',1),(3,'Squirtle','Water',10,'2019-10-22','/static/squirtle.png',1),(5,'Onix','Grass',37,'2019-10-22','/static/onix.jpg',1),(6,'Gyarados','Water',72,'2019-10-22','/static/gyarados.png',1),(7,'Pikachu','Fire',6,'2019-10-23','/static/Pikachu.png',1);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
