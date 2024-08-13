import datetime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def user_list(request):
    # 會去app01目錄下的templates目錄尋找user_list.html
    # 實際上根據App的注冊順序逐一去他們的templates文件夾中尋找
    # settings.py中如果由PyCharm創建，也就是有'DIRS': [BASE_DIR / 'templates']
    # 那將默認優先從項目根目錄的templates文件夾中尋找，找不到再是根據注冊順序
    return render(request, "user_list.html")

def register(request):
    return render(request, "register.html")

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

def news(request):
    import requests
    import datetime
    import time

    # url = "https://feed.mix.sina.com.cn/api/roll/get"
    # params = {
    #     "pageid": "153",
    #     "lid": "2514",  # 使用科技频道的lid
    #     "num": "20",    # 获取10条新闻
    #     "versionNumber": "1.2.8",
    #     "page": "1"
    # }
    # res = requests.get(url, params=params)
    # data = res.json()
    # print(data)
    #
    # news_items = data['result']['data']
    # extracted_data = []
    #
    # for item in news_items:
    #     news_entry = {
    #         'title': item.get('title', '无标题'),
    #         'time': datetime.datetime.fromtimestamp(int(item.get('ctime', '無時間'))).strftime('%Y-%m-%d %H:%M:%S'),
    #         'summary': item.get('summary', '无概要'),
    #         'images': item.get('images', [])
    #     }
    #     image_urls = [img.get('u') for img in news_entry['images']]
    #     news_entry['images'] = image_urls
    #
    #     extracted_data.append(news_entry)
    #
    # print(extracted_data)

    # url = "https://hacker-news.firebaseio.com/v0/newstories.json"
    # data = {}
    #
    # try:
    #     # 获取新故事 ID 列表
    #     response = requests.get(url, timeout=10)
    #     response.raise_for_status()  # 确保请求成功
    #     story_ids = response.json()
    #
    #     # 遍历每个故事 ID 获取详细信息
    #     for story_id in story_ids[:30]:  # 仅获取前30个故事以避免请求过多
    #         story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    #         try:
    #             story_response = requests.get(story_url, timeout=10)
    #             story_response.raise_for_status()  # 确保请求成功
    #             story_details = story_response.json()
    #             data[story_id] = story_details
    #             time.sleep(0.05)  # 等待0.05秒钟以避免对 API 的请求过于频繁
    #         except requests.RequestException as e:
    #             print(f"请求故事 {story_id} 发生错误: {e}")
    #
    # except requests.RequestException as e:
    #     print(f"获取故事 ID 列表时发生错误: {e}")
    #
    # print(data)
    #
    # data_list = []
    #
    # for item in data.values():
    #     info = dict()
    #     info["author"] = item["by"]
    #     info["title"] = item["title"]
    #     info["time"] = datetime.datetime.fromtimestamp(item["time"]).strftime('%Y-%m-%d %H:%M:%S')
    #     data_list.append(info)

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": "Your api key",  # 替換爲你的API密鑰
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

    return render(request, 'news.html', {'data_list': data_list})

def something(request):
    # request是一個對象，封裝了用戶發送過來的請求和相關數據

    # 1. 獲取請求方式：GET或POST
    print(request.method)

    # 2. 在URL上傳遞值 /something/?q1=question1&q2=blablabla
    print(request.GET)

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

from app01.models import UserInfo
def orm(request):
    # 測試ORM對表中數據操作
    ###   1. 新建 ###
    # UserInfo.objects.create(name="Thomas")
    # UserInfo.objects.create(password="123")
    # UserInfo.objects.create(age=22)
    # UserInfo.objects.create(name="Alex", password="apple", age=19)
    # UserInfo.objects.create(name="Lucy", password="123Lci", age=35)
    # 每次create都是一整行
    ###   2. 刪除   ###
    # UserInfo.objects.filter(id=3).delete()
    # UserInfo.objects.all().delete()
    ###   3. 獲取數據   ###
    # data_list = [row,row,row]  Query Set類型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.age)
    # rol_obj = UserInfo.objects.filter(id=5).first()
    ###   4. 更新數據   ###
    UserInfo.objects.all().update(password="<PASSWORD>")
    # 改成篩選出的某些數據也行，all和filter某種意義上是用法一致的
    return HttpResponse("成功")