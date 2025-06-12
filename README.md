## 图书馆管理系统

随着近年来大语言模型的兴起，大模型在辅助人们的日常生活中发挥着重要作用。本项目在实现基本功能的同时在学生账户和管理员账户的主页提供了一个聊天窗口，供用户与大模型交互，为学生推荐所需书籍，为管理图书提供建议。为在本地运行此项目，请参考以下的说明进行相应的配置。

---

#### 环境配置

命令行进入解压后的文件夹所在目录，之后所有的操作都基于该目录。

运行以下命令，安装项目所依赖的django、mysqlclient等包。

```
pip install -r requirements.txt
```

---

首先创建library_system数据库，之后运行以下命令，导入备份数据库。

```
mysql -u root -p library_system < backup.sql
```

注意：windows操作系统下以上命令在powershell中运行会报错，需要在命令提示符下运行。

---

配置环境变量DASHSCOPE_API_KEY="YOUR_DEEPSEEK_API"。

---

#### 运行项目

打开library_system文件夹中的settings.py文件，在88行按照注释提示修改数据库配置。

---

运行以下命令，完成django框架到数据库的迁移。

```
python manage.py makemigrations
python manage.py migrate
```

---

运行以下命令，启动项目。

```
daphne -b 0.0.0.0 -p 8000 library_system.asgi:application
```


项目正确启动之后所有操作的日志会显示在该终端。

---

浏览器中输入以下链接，进入项目的登录界面。

```
http://127.0.0.1:8000/login/
```

初始数据库中提供了2022300881+123456学生账户和administrator+123456管理员账户，也可以自行注册一个学生账户。
