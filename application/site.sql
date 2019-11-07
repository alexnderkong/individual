CREATE TABLE posts 
             ( 
                          id          INTEGER NOT NULL, 
                          title       VARCHAR(200) NOT NULL, 
                          content     VARCHAR(100) NOT NULL, 
                          level       INTEGER NOT NULL, 
                          date_posted DATETIME NOT NULL, 
                          image_file  VARCHAR(50) NOT NULL, 
                          user_id     INTEGER NOT NULL, 
                          PRIMARY KEY (id), 
                          FOREIGN KEY(user_id) REFERENCES users (id)

CREATE TABLE users
             (
                          id         INTEGER NOT NULL,
                          first_name VARCHAR(50) NOT NULL,
                          last_name  VARCHAR(50) NOT NULL,
                          email      VARCHAR(150) NOT NULL,
                          PASSWORD   VARCHAR(100) NOT NULL,
                          PRIMARY KEY (id),
                          UNIQUE (email)
