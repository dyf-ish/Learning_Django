# 初識Django

需要准備的：
- Python：函數、面向對象
- 前端三件套
- MySQL數據庫操作

Python的Web框架：
- Flask：體量較小，適合輕量化的小項目
- Django：内部集成了很多組件，更全能

## 1 安裝Django

```shell
pip install django
```
注意：
```
在Python的路徑下：
	- python.exe
	- Scripts
		- pip.exe
		- django-admin.exe // 工具，幫助創建django項目的
	- Lib
		- 内置模塊
		- site-packages
			- openpyxl
			- python-docx
			- flask
			- django // 框架的源碼
```

## 2 創建項目

>Django中項目會帶有默認的一些文件與文件夾
### 2.1 在終端

- 打開終端
- 進入要創建項目的目錄
- 執行命令創建項目

```shell
"django-admin的目錄" startproject 項目名稱
# 如果Python的Scripts文件夾已加入系統環境變量
django-admin startproject 項目名稱
```

### 2.2 PyCharm

>別放到解釋器目錄去咯
- 最標准的是用命令行
- PyCharm會在基礎文件上增添内容
	創建了templates文件夾，會在settings.py裏將TEMPLATES的'DIRS'設置爲該文件夾，這是使得程序以後尋找模板時將在template文件夾中尋找。
- 整體文件佈局：
	```
	djangoProject
		- manage.py   // 後續項目啓動和管理、數據管理等都需要用到，不需要修改
		- djangoProject
			- __init__.py
			- urls.py   // 負責記錄每個url和函數的對應關係
			- settings.py   // 項目配置文件
			- wsgi.py   // 同步接收網絡請求，不需要修改
			- asgi.py   // 異步接收網絡請求，不需要修改，不太成熟
	```
	其中常用文件有manage.py、urls.py和settings.py，而後兩者常常涉及到修改，但是manage.py則往往只是使用

## 3 App

- 用於區分一個項目的不同功能模塊，每個可以有自己的表結構、函數、HTML和CSS，我的水平在學習階段應該只會有一個App。
- 不是手機應用程序那個App
- 使用指令可以新建App
	```shell 
	python manage.py startapp django_app_1
	```
	- 我是在PyCharm的終端内這樣創建的
	- 創建後獲得如下文件
		```
		- django_app_1
			- __init__.py
			- admin.py   // [固定] django默認提供了admin後臺管理
			- apps.py   // [固定] app啓動類
			- migrations   // [固定] 數據庫變更記錄
				- __init__.py
			- models.py   // [**重要**] 數據庫操作（類似於自帶的pymysql）
			- tests.py   // [固定] 單元測試
			- views.py   // [**重要**] 函數
		```

## 4 快速上手

### 4.1 寫一個頁面

- App先要在settings.py注冊
	- 在apps.py中有以下代碼：
		```python
		class App01Config(AppConfig):  
		    default_auto_field = 'django.db.models.BigAutoField'  
		    name = 'app01'   # 我的App名字叫app01
		```
		這些便是與注冊App相關的類，具體操作如下：
		- 打開settings.py
		- 在其中找到INSTALLED_APPS這一個列表
		- 在最後加上`'app01.apps.App01Config'`

- 編寫URL與視圖函數的對應關係
	- 打開urls.py，原先有以下内容：
		```python
		urlpatterns = [  
		    path('admin/', admin.site.urls),  # 默認的關聯，我們需要更改
		]
		```
	- 對其進行更改：
		```python
		from app01 import views  
		urlpatterns = [  
		    # 儅用戶訪問 你的域名/index/時會自動運行views裏的函數index  
		    path('index/', views.index),  
		]
		```
	- 編寫對應的函數：（于views.py中添加）
		```python
		from django.shortcuts import render, HttpResponse  
		  
		# Create your views here.  
		  
		def index(request):  
		    return HttpResponse("Hello World") 
		```

- 啓動django項目
	- 命令行啓動 `python manage.py runserver`
	- PyCharm啓動
		![[startDjango_fromPycharm.png]]

### 4.2 頁面 templates目錄

- urls.py中的操作與之前相似，主要的區別在於函數内部
- views.py
```python
def user_list(request):
	# 會去app01目錄下的templates目錄尋找user_list.html
	# 實際上根據App的注冊順序逐一去他們的templates文件夾中尋找
	# settings.py中如果由PyCharm創建，也就是有'DIRS': [BASE_DIR / 'templates']
	# 那將默認優先從項目根目錄的templates文件夾中尋找，找不到再是根據注冊順序
    return render(request, "user_list.html")
```

### 4.3 靜態文件 static目錄

- 在app01目錄下新建一個static文件夾放置靜態文件，一般以下資源被認爲是靜態文件：
	- CSS文件
	- 圖片、視頻、音頻等
	- Js文件
	- 字體文件
- 在django中HTML文件調取靜態文件有特殊的語法
	```html
	{% load static %}  
	  
	<!DOCTYPE html>  
	<html lang="en">  
	<head>  
	    <meta charset="UTF-8">  
	    <title>注冊</title>  
	    <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1-dist/css/bootstrap.css' %}">  
	    <link rel="stylesheet" href="{% static 'plugins/fontawesome-free-6.6.0-web/css/all.css' %}">
	...
	```
	這些便屬於django中提供的框架，絕大多數都很類似，爲了便於學習，想要仔細瞭解需要查看[官方文檔](https://docs.djangoproject.com/en/5.1/ref/templates/language/)中的相應資料，我的這個學習筆記只會涵蓋部分模板語法。

## 5 模板語法

> 本質上就是在HTML上構建一些特殊的佔位符，而後期將會由框架傳輸數據到這些佔位符上，很多知识django限定的咯，别的框架可能会爆掉！

- view.py
	```python
	def tpl(request):  
	  
	    name = "Thomas"  
	    skills = ["Python", "Django", "C/C++", "JavaScript"]  
	    info = {  
	        "id": 12345,  
	        "name": name,  
	        "married": False,  
	        "role": "皇帝"  
	    }  
	  
	    return render(request, "tpl.html", {"username": name, "skills": skills, "info": info})
	```
- HTML
	- 普通调用一个数据
		```html
		<div>{{ username }}</div>
		```
	- 调用一个列表中的某个数据
		```html
		<div>The first skill: {{ skills.0 }}</div>
		```
	- 使用`for`循环遍历一个列表
		```html
		{% for item in skills %}  
		    <span style="color: darkred">{{ item }}</span>  
		{% endfor %}
		```
	- 使用`for`循环遍历一个字典的索引
		```html
		{% for item in info.keys %}  
		    <th>{{ item }}</th>  
		{% endfor %}
		```
	- 使用`for`循环遍历一个字典的值
		```html
		{% for item in info.values %}  
		    <th>{{ item }}</th>  
		{% endfor %}
		```
	- 使用`for`循环遍历一个字典的索引和值
		```html
		{% for key, item in info.items %}  
		    <li>{{ key }}: {{item}}</li>  
		{% endfor %}
		```
	- 使用判斷語句
		```html
		{% if username == "Thomas" %}  
		    <h1>恭迎陛下！陛下萬歲萬歲萬萬歲！</h1>  
		{% elif username == "Alex" %}  
		    <h1>不是你誰啊？</h1>  
		{% else %}  
		    沒有人：  
		{% endif %}
		```

> 模板語法的整個流程：
> ![[模板語法流程]]
> 視圖函數的render内部：
> 1. 讀取含有模板語法的HTML文件
> 2. 内部進行渲染，即執行模板語法並將其替換爲數據，最終得到只包含HTML標簽的字符串
> 3. 將渲染和替換完成的字符串返還給瀛湖瀏覽器
> 也就是説整個模板語法的轉譯過程是在服務器端就執行完畢的而非瀏覽器内