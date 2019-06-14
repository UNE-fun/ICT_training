CREATE TABLE users(
  id INT NOT NULL AUTO_INCREMENT,
  userid VARCHAR(32) NOT NULL,
  password VARCHAR(128) NOT NULL,
  access_token VARCHAR(128) NOT NULL,
  PRIMARY KEY (id)
);

INSERT into users (id, userid, password, access_token) VALUES (0, "hoge", "hoge", "hoge");
