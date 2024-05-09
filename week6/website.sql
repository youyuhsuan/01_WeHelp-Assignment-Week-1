import mysql.connector

con = mysql.connector.connect(
    user="root", password="23322907", host="localhost", database="website"
)
productName = "紅茶"

print("連線成功")
cursor = con.cursor()
cursor.execute(f"INSERT INTO product(name) VALUES('{productName}')")
# cursor.execute("UPDATE product SET name='咖啡' WHERE id=1")
# cursor.execute("SELECT * FROM product WHERE id=2")
# data = cursor.fetchone()
# print(f"id:{data[0]}\nname:{data[1]}")
cursor.execute("SELECT * FROM product")
datas = cursor.fetchall()
for data in datas:
    print(f"id:{data[0]}\nname:{data[1]}")

con.commit()
con.close()

CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
)