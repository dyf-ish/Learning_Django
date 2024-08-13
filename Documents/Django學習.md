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
	# 此處輸入的request實質上只是一個變量
	# 與第三方模塊requests無關
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

- 案例：新聞頁面
	- 做新聞頁面之前你肯定要有新聞資料，通常做相關業務如果不是主營新聞方面的咨詢服務是不會自己去親自寫整個新聞内容的，因此往往需要引入第三方服務。
	- urls.py的内容這裏就不附帶了，和之前一樣寫個path就好了。
	- view.py:
		```python
		def news(request): 
			import requests   # 訪問外部的網絡信息所必須的
			import datetime   # 爲了將一些外部的數字時間轉化爲人類可讀的時間信息
			import time   # 爲了防止過頻繁的訪問而設置的一些延遲所需要的
		
		### 第一種：新浪的API，這邊用的好像是過時的，給的信息都是2023年的 ###
		
			url = "https://feed.mix.sina.com.cn/api/roll/get"  
			params = {  
				"pageid": "153",  
				"lid": "2514",  # 使用財經頻道的lid
				"num": "20",    # 獲取20條新聞 
				"versionNumber": "1.2.8",  
				"page": "1"  
			}  
			res = requests.get(url, params=params)  
			data = res.json()  
			print(data)  
			  
			news_items = data['result']['data']  
			extracted_data = []  
			  
			for item in news_items:  
				news_entry = {  
					'title': item.get('title', '無標題'),  
					# 這裏是時間格式的轉換
					'time': datetime.datetime.fromtimestamp(int(item.get('ctime', '無時間'))).strftime('%Y-%m-%d %H:%M:%S'),  
					'summary': item.get('summary', '無概要'),  
					'images': item.get('images', [])  
				}  
				image_urls = [img.get('u') for img in news_entry['images']]  
				news_entry['images'] = image_urls  
			  
				extracted_data.append(news_entry)  
			  
			print(extracted_data)
		
		### 第二種：Hacker News的API ###
		
			url = "https://hacker-news.firebaseio.com/v0/newstories.json"  
			data = {}  
			  
			try:  
			    # 獲取新故事的ID列表
			    response = requests.get(url, timeout=10)  
			    response.raise_for_status()  # 確保請求成功  
			    story_ids = response.json()  
			  
			    # 遍歷每個故事ID以獲得詳細信息  
			    for story_id in story_ids[:30]:  # 僅獲取前30個故事以免請求過多  
			        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"  
			        try:  
			            story_response = requests.get(story_url, timeout=10)  
			            story_response.raise_for_status()  # 確保請求成功 
			            story_details = story_response.json()  
			            data[story_id] = story_details  
			            time.sleep(0.05)  # 等待0.05秒以免請求過於頻繁  
			        except requests.RequestException as e:  
			            print(f"請求故事{story_id}發生錯誤:{e}")  
			  
			except requests.RequestException as e:  
			    print(f"獲取編號ID的故事列表時發生錯誤:{e}")  
			  
			print(data)  
			  
			data_list = []  
			  
			for item in data.values():  
			    info = dict()  
			    info["author"] = item["by"]  
			    info["title"] = item["title"]  
			    info["time"] = datetime.datetime.fromtimestamp(item["time"]).strftime('%Y-%m-%d %H:%M:%S')  
			    data_list.append(info)
			    
		### 第三種：NewsAPI，這個個人感覺更好一點，有圖片、免費、還比較實時 ###
			url = "https://newsapi.org/v2/top-headlines"  
			params = {  
			    "apiKey": "My'API",  # MyAPI替換爲你的API密鑰  
			    "q": "news"  # 使用了通用的查詢詞  
			}  
			  
			# 發送GET請求  
			response = requests.get(url, params=params)  
			  
			# 解析Json響應  
			data = response.json()  
			  
			# print(data.encode('utf-8'))  
			  
			data_list = []  
			# 檢查響應狀態  
			if data["status"] == "ok":  
			    # 提取新聞數據  
			    articles = data["articles"]  
			  
			    # 遍歷新聞内容  
			    for article in articles:  
			        info = dict()  
			        info["images"] = article.get("urlToImage", "No Image URL")  
			        info["title"] = article.get("title", "No Title")  
			        info["author"] = article.get("author", "No Author Name")  
			        info["time"] = article.get("publishedAt", "No Publish Date")  
			        info["summary"] = article.get("description", "No Description")  
			        info["content"] = article.get("content", "No Content")  
			        info["url"] = article.get("url", "No URL")  
			        data_list.append(info)  
			else:  
			    print("Failed to retrieve news data.")
			
			
			# 返回數據給框架，然後框架對html文件進行填充
			# 注意上述方法是三選一
			return render(request, 'news.html', {'data_list': data_list})
		```
	- news.html：
		```html
		{% load static %}
		{# 要記得讀取static #}
		
		<!DOCTYPE html>  
		<html lang="en">  
		<head>  
		    <meta charset="UTF-8">  
		    <title>新聞</title>  
		    {#  用了美美的字體  #}  
		    <style>  
		        @font-face {  
		            font-family: "優雅";  
		            src: url({% static 'fonts/qiji-combo-large.ttf' %}) format('truetype');  
		            font-weight: normal;  
		            font-style: normal;  
		            font-size: 20px;  
		        }  
		        body {  
		            font-family: 優雅;  
		            padding: 30px;  
		        }  
		    </style>  
		</head>  
		<body>  
		    <table border="1">  
		        <thead>
		        <tr>
				        {# 先把第一個新聞字典的每個索引遍歷了當作列的標題 #}  
		                {% for key in data_list.0.keys %}  
		                    <th>{{ key }}</th>  
		                {% endfor %}  
		            </tr>  
		        </thead>
		        <tbody>
					{# 每個新聞 #}  
		            {% for dict in data_list %}  
		                <tr>  
		                    {# 每個新聞的元素 #}  
		                    {% for key, item in dict.items %}  
		                        <td>  
			                        {# 檢查是否是圖片 #}
		                            {% if key == "images" %}
		                                <img src="{{ item }}" style="max-width: 100px" alt="No Image">
		                            {% else %}  
		                                {{ item }}  
		                            {% endif %}
		                        </td>  
		                    {% endfor %}  
		                </tr>  
		            {% endfor %}  
		        </tbody>  
		    </table>
		</body>  
		</html>
		```

>附上一些好玩的錯誤：![[錯誤使用字典.png]]
>要注意先是`key`再是`item`，這個和定義時`"key": item`是一樣的順序，如圖就錯誤的將索引給到了`item`變量，將内容給到了`key`變量。同時，在下方的判斷語句中沒有給`images`加引號，這時該變量的值為空，而`key`變量實際上是某個新聞的内容，另一方面獲得的新聞信息只有圖片地址可能為空，所以當且僅當沒有圖片時，字典内容為空，賦值到變量`key`裏后與一直為空的變量`images`作比較，則正好依然能過濾出所有沒有圖片的項目並跳轉顯示`"#"`，引用我高中數學老師的話，這就是錯了又錯了結果對了。![[錯誤使用字典后.png]]

## 6 請求和響應

### 6.1 簡單介紹下常見請求和響應

```python
def something(request):  
	# request是一個對象，封裝了用戶發送過來的請求和相關數據  
  
	# 1. 獲取請求方式：GET或POST  
	print(request.method)  
  
	# 2. 在URL上傳遞值 /something/?q1=question1&q2=blablabla    print(request.GET)  
  
	# 3. 在請求中提交數據  
	print(request.POST)  
  
	# 4. HttpResponse("返回内容字符串給請求者")  
	return HttpResponse("Hello World")  
  
	# 5. render(request, 'something.html', {"text": "這個部分之前一直在用就不講了"})  
	# 基本就是讀取HTML的内容再渲染后返回字符串也就是html給用戶瀏覽器  
  
	# 6. 重定向  
	# return redirect('index'或者別的url)  
	# 關於重定向：  
	# 在Django的框架下，整個流程是瀏覽器訪問我們的服務器，服務器會返回瀏覽器一個信息，讓用戶瀏覽器自己去訪問重定向的地址  
	# 也就是後續的重定向網址的訪問與我們就無關了，只是一個介紹人的職責，而不是中間人
```

### 6.2 案例：登錄界面

- 首先還是弄個`Path`
- 然後去views裏編寫對應的函數`login`
	```python
		def login(request):  
	    if request.method == "GET":  
	        return render(request, "login.html")  
	  
	    # 小技巧：由於if語句執行後可以提前退出，即執行return，所以後續的内容不需要放在else裏  
	    # 快捷鍵：我縂忘記，shift+tab是往前縮進，也就是撤銷tab  
	  
	    # POST下我們需要獲得用戶傳輸的數據  
	    # print(request.POST)  
	    username = request.POST.get("name")  
	    pwd = request.POST.get("pwd")  
	    # print(username, pwd)  
	    if username == "Thomas" and pwd == "123":  
	        return redirect("/news/")   # 注意這個功能要import  
	  
	    # return HttpResponse("登陸失敗")  
	    # 我們希望重新返回登錄頁面並通過error_msg返回錯誤信息  
	    return render(request, "login.html", {"error_msg": "用戶名或密碼錯誤，也有可能是驗證碼錯誤，你自己看看"})
	```
- 後續的HTML沒什麽好説的，詳見對應的文件内容。在此只額外提以下幾點：
	- `{% load static %}`不要忘記添加，不然無法讀取設定好的靜態文件
	- `<form style="padding: 20px" action="/login/" method="POST">`這個`action`和`method`不要忘記
	- Django比Flask多一個csrf_token安全驗證的過程需要在要提交的表單内加入對應的指令`{% csrf_token %}`，否則會報錯。![[Forbidden_403.png]]注意一定要加載表單裏！
	- 表單提交後的檢索是依據`<input>`的`name`屬性
	- 添加`<span style="color: red">*{{ error_msg }}</span>`可以在錯誤時返回錯誤數據，如圖![[登錄錯誤效果.png]]

## 7 數據庫操作

- MySQL + pymysql![[Python與MySQL]]
- Django開發時操作數據庫會更簡單，它内部提供了ORM框架![[ORM]]另一方面，Django最新版本直接使用pymysql存在一些bug大概據説。

### 7.1 安裝第三方模塊

```shell
pip install mysqlclient
```

### 7.2 ORM

ORM可以幫助我們做的兩件事
- 創建、修改、刪除數據庫中的表（不用SQL語句），但是無法創建數據庫。
- 操作表中的數據（不用SQL語句）

>![[初始化數據庫]]

- 我創建的數據庫命名爲testDjango_1

#### 7.2.1 配置數據庫

- 打開settings.py可以看到原先就有一個叫數據庫的字典，我們需要對它進行更改
	```python
	DATABASES = {  
	    'default': {  
	        'ENGINE': 'django.db.backends.mysql',  
	        'NAME': 'testDjango_1',   # 數據庫名字  
	        'USER': 'root',  
	        'PASSWORD': '<PASSWORD>',  
	        'HOST': '127.0.0.1',   # 數據庫所在的電腦IP  
	        'PORT': '3306',  
	    }
	```

#### 7.2.2 Django對表操作

- 創建表
	- 在models.py添加新的繼承后的新類
		```python
		class UserInfo(models.Model):  
		    id = models.IntegerField(primary_key=True)  
		    name = models.CharField(max_length=100)  
		    password = models.CharField(max_length=100)  
		    age = models.IntegerField(default=18)  
		  
		    # 等價於執行了  
		    """  
		    create table app01_userInfo(
			    id bigint auto_increment primary key,
			    name varchar(100),
			    password varchar(100),
			    age bigint
			    )
			"""
		```
	- 在命令欄進行執行，主要兩點
		- 使用的python解釋器需要安裝了mysqlclient庫
		- 執行命令的位置需要在manage.py的目錄下，或者直接引導到manage.py的路徑
		- App01需要提前注冊
			```shell
			python manage.py makemigrations
			python manage.py migrate
			```
			有點崩潰我在這弄了半天，最後用的那個`python manage.py makemigrations --empty app01`清除然後重建了才可以的。
		- 注意後面想要改寫你的内容也可以繼續用這兩個指令並在models.py内做更改，但是要注意的是修改同一個表的結構時，注釋或刪掉原有的列后在執行上面的兩個指令可以重新部署表而不影響其他列的數據
		- 但是當我們要給已有的表增加一列時，計算機事先不知道應當填充什麽樣的數據到新增列内，這時需要我們初始化
			1. 手動輸入一個值
			2. 設置默認值
				```python
				age = models.IntegerField(default = 18)
				```
			3. 允許爲空
				```python
				data = models.IntegerField(null=True, blank=True)
				```
- 修改、刪除：
	對於ORM内的數據庫操作，當我們需要調整表及其結構時步驟如下：
	1. 更改models.py
	2. 使用命令

#### 7.2.3 Django對表内數據操作

我接下來直接用示例了
- 新建
	- views.py
		```python
		def orm(request):  
		    # 測試ORM對表中數據操作  
		    UserInfo.objects.create(name="Thomas")  
		    UserInfo.objects.create(password="123")  
		    UserInfo.objects.create(age=22)  
		    return HttpResponse("成功")
		```
	- 數據庫，有點亂糟糟但是能看懂的吧
		```sql
		+----+--------+----------+-----+
		| id | name   | password | age |
		+----+--------+----------+-----+
		|  1 | Thomas |          |  18 |
		|  2 |        | 123      |  18 |
		|  3 |        |          |  22 |
		+----+--------+----------+-----+
		```
		這時候可以明顯看出每次創建它都是一整行一整行創建的，要一次生成一整行需要這樣：
	- views.py
		```python
		def orm(request):  
		    # 測試ORM對表中數據操作  
		    # UserInfo.objects.create(name="Thomas")  
		    # UserInfo.objects.create(password="123")
		    # UserInfo.objects.create(age=22)  
		    UserInfo.objects.create(name="Alex", password="apple", age=19)  
		    UserInfo.objects.create(name="Lucy", password="123Lci", age=35)  
		    return HttpResponse("成功")
		```
	- 數據庫
		```sql
		+----+--------+----------+-----+
		| id |  name  | password | age |
		+----+--------+----------+-----+
		|  1 | Thomas |          |  18 |
		|  2 |        | 123      |  18 |
		|  3 |        |          |  22 |
		|  4 | Alex   | apple    |  19 |
		|  5 | Lucy   | 123Lci   |  35 |
		+----+--------+----------+-----+
		```
- 刪除
	- views.py
		```python
		def orm(request): 
		    ###   2. 刪除   ###
			UserInfo.objects.filter(id=3).delete()  
		    # UserInfo.objects.all().delete()
		```
	- 數據庫
		```sql
		+----+--------+----------+-----+
		| id | name   | password | age |
		+----+--------+----------+-----+
		|  1 | Thomas |          |  18 |
		|  2 |        | 123      |  18 |
		|  4 | Alex   | apple    |  19 |
		|  5 | Lucy   | 123Lci   |  35 |
		|  6 | Alex   | apple    |  19 |
		|  7 | Lucy   | 123Lci   |  35 |
		+----+--------+----------+-----+
		```
- 獲取
	- views.py
		```python
		def orm(request):  
		    ###   3. 獲取數據   ###
		    # data_list = [row,row,row]  Query Set類型  
		    data_list = UserInfo.objects.all()  
		    for obj in data_list:  
		        print(obj.id, obj.name, obj.age)  
		    return HttpResponse("成功")
		```
	- 終端
		```shell
		1 Thomas 18
		2  18
		4 Alex 19
		5 Lucy 35
		6 Alex 19
		7 Lucy 35
		```
		如果用了`.filter()`替代`.all()`則可以實現篩選，如果只想獲得某行，比如我選擇的是id為5的一行，此時可以用`rol_obj = UserInfo.objects.filter(id=5).first()`來實現直接調取成一個循環中的`obj`那樣的字典
- 更新
	- views.py
		```python
		def orm(request):  
			###   4. 更新數據   ###
			UserInfo.objects.all().update(password="<PASSWORD>")  
		    # 改成篩選出的某些數據也行，all和filter某種意義上是用法一致的  
		    return HttpResponse("成功")
		```
	- 數據庫
		```sql
		+----+--------+------------+-----+
		| id | name   | password   | age |
		+----+--------+------------+-----+
		|  1 | Thomas | <PASSWORD> |  18 |
		|  2 |        | <PASSWORD> |  18 |
		|  4 | Alex   | <PASSWORD> |  19 |
		|  5 | Lucy   | <PASSWORD> |  35 |
		|  6 | Alex   | <PASSWORD> |  19 |
		|  7 | Lucy   | <PASSWORD> |  35 |
		+----+--------+------------+-----+
		```

## 8 Django組件

- 梗概
	- 首先面對的需求是什麽？
		1. 用戶提交數據需要校驗
		2. 輸入信息不符合要求頁面上應當存在錯誤提示
		3. 頁面上每個重複字段都需要手寫
		4. 關聯數據需要手動獲取并通過循環語法顯示在頁面
	- 實際上舊有的辦法可以解決，但是會顯得很業餘且很繁瑣，因此django對於這些需求提供了兩個組件
		- Form組件：輕便但是只能實現前三種
		- ModelForm組件：成熟、完備、簡便
### 8.1 初識Form
#### 8.1.1 view.py
```python
class MyForm(Form):
	# Form這些下面的都要自己寫，雖然比直接在網頁上佈置輕鬆了已經
	uper = forms.CharField(widget=forms .Input )
	pwd = form.CharFiled(widget=forms.Input)
	email = form.CharFiled(widget=forms.Input)
	account = form.CharFiled(widget=forms.Input)
	create time = form.CharFiled(widget=forms.Input)
	depart = form.CharFiled(widget=forms.Input)
	gender = form.Charriled(widget=forms.Input)
def user_add(request):
	if request.method =="GET":
		form = MyForm()
	return render(request,'user add.html',{"form":form})
```

#### 8.1.2 user_add.html
```html
<form method="post">
	{% for field in form %}
		({ field }}
	{% endfor %}
	<!-- 等價於 -->
	<!-- <input type="text" placeholder="姓名" name="user" />-->
</form>
```

### 8.2 ModelForm（推薦）

#### 8.2.1 初識：
- 現在我們擁有一個表，其在model.py内的代碼為：
	```python
	class UserInfo(models.Model):  
	    """ 員工表 """
	    name = models.CharField(verbose_name="姓名", max_length=16)  
	    gender_choice = (  
	        (0, "男"),  
	        (1, "女"),  
	    )  
	    gender = models.SmallIntegerField(verbose_name="性別", choices=gender_choice)  
	    password = models.CharField(verbose_name="密碼", max_length=16)  
	    age = models.IntegerField(verbose_name="年齡")  
	    account = models.DecimalField(verbose_name="賬戶餘額", max_digits=10, decimal_places=2, default=0)  
	    create_time = models.DateTimeField(verbose_name="注冊日期", auto_now_add=True)  
	    introduction = models.TextField(verbose_name="簡介", null=True, blank=True)
	```
- 而在views.py中：
	```python
	class MyForm(ModelForm):
		# xx = form.CharField*("...")  也就是還能自定義字段，在數據本身外再加
		class Meta:
			model = User_Info
			fields = [
				"name",
				"gender",
				"password",
				"age",
				"account",
				"create_time",
				"introduction"
			]
	```
- 其餘部分與Form一致，也就是説他比較好的實現了數據表與輸出的聯係，能簡化view.py内的書寫。

#### 8.2.2 引例深入
- 在models裏代碼一致，而views中如下：
	```python
	########################## ModelForm示例 ##########################
	from django import forms  
	from app01 import models  
	class UserModelForm(forms.ModelForm):  
	    class Meta:  
	        model = models.UserInfo  
	        fields = "__all__"   # 代表全選
	  
	def user_add(request):  
	    """ 使用ModelForm的添加用戶 """
	    form = UserModelForm(request.POST or None)  
	    return render(request, 'user_add.html', {'form': form})
	```
- 此時在user_add.html中：
	```html
	<!DOCTYPE html>  
	<html lang="en">  
	<head>  
	    <meta charset="UTF-8">  
	    <title>Title</title>  
	</head>  
	<body>  
	    <form method="post"></form>  
	        {% csrf_token %}  
	        {% for field in form %}  
	            {# 這個可以顯示標簽，標簽就是那個verbose_name #}  
	            {{ field.label }}: 
	            
	            {# 這個顯示選框 #}  
	            {{ field }}
	        {% endfor %}
	        {# 檢索還可以直接用點 #}  
			{{ field.password.label }}
	</body>  
	</html>
	```
- 目前仍然存在的問題是，他輸出的外鍵選框内部是object什麽什麽，也就是不是我們想要的要素名稱，而在源碼中，每個選項都是一個類的實例，那麽print類的實例時不會得到名稱，所以需要在類中定義`__str__()`方法。