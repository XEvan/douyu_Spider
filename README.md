# douyu_Spider

需求：

  1、抓取斗鱼手机客户端直播间的信息，包含 房间号、ID、热度、房间说明、标签、房间图片地址
  
  2、将抓取到的数据存入MySQL
  

实现步骤：

1、先分析需求，然后根据需求创建相应的数据库

  mysql> create database douyuInfo charset=utf8;
  
  mysql> use douyuInfo;
  
  mysql> create table douyu( id int auto_increment primary key, roomID varchar(10), nickName varchar(10), hotNumber varchar(8), roomName varchar(20), roomLabel varchar(18), roomPic varchar(100));
  
  
2、通过Fiddler抓包工具，抓取手机的通信信息，前提是手机和电脑处于同一局域网内，然后进行以下设置

  手机端添加Fiddler所在电脑的ip（比如192.168.11.11）和端口号（比如8888），然后打开手机浏览器，输入192.168.11.11：8888，下载信任证书，然后就可以通过Fiddler来抓包。

3、创建一个scrapy项目

  scrapy startproject douyu_Spider
  

遇到的问题：

1、要先判断当前的url是否是有效的url，如果当前url无有关信息，则响应中的error不为0，那么做出相应的处理，比如打印出相关信息

2、如果在爬取的时候出现 HTTP status code is not handled or not allowed 这个错误，在settings.py里面加上HTTPERROR_ALLOWED_CODES = [状态码]

3、在不会对服务器造成影响的情况下，可以取消robots规则，在settings.py里面将ROBOTSTXT_OBEY置为False

4、使用Fiddler来抓包，将headers的信息添加到settings.py中，模拟客户端浏览信息，一种简单的反反爬虫机制

5、创建数据库的时候，要加上charset=utf8，否则存中文的时候会出现问题。
