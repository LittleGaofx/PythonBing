import os
import requests

#Get CN Bing Wallpaper
api_url_cn = "https://cn.bing.com/HPImageArchive.aspx?n=1&mkt=zh-cn&idx=0&format=js"
response = requests.get(api_url_cn)
if response.status_code == 200:
    #保存图片
    data = response.json()
    urlbase = data["images"][0]["urlbase"]
    url = "https://www.bing.com" + urlbase + "_UHD.jpg"
    image_data = requests.get(url).content
    image_path = os.path.join("img", "background.jpg")
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    with open(image_path, "wb") as f:
        f.write(image_data)
        f.close()
    print(f"图片已经保存到 {image_path}")
    #获取图片信息
    enddate = data["images"][0]["enddate"]
    yy = f"{enddate[:4]}"
    mm = f"{enddate[4:6]}"
    dd = f"{enddate[6:]}"
    enddate = f"{enddate[:4]}-{enddate[4:6]}-{enddate[6:]}"
    copy = data["images"][0]["copyright"]
    title = data["images"][0]["title"]
    #写入README.md
    info_path = os.path.join("README.md")
    with open(info_path, "w", encoding='utf-8') as f:
        f.write(f"## Today's Bing Wallpaper\n")
        f.write(f"Update: {enddate}\n")
        f.write(f"![]({url}&w=1000)Download: [{copy}]({url})")
        f.write(f"\n\nAuto get programm by LtgX\n")
    print(f"信息已经保存到 {info_path}")
    #写入备份
    history_file_name = f"{dd}.md"
    history_path = os.path.join("history",yy,mm,history_file_name)
    os.makedirs(os.path.dirname(history_path), exist_ok=True)
    with open(history_path, "w", encoding='utf-8') as f:
        f.write(f"## History Bing Wallpaper\n")
        f.write(f"Wallpaper date: {enddate}\n")
        f.write(f"![]({url}&w=1000)Download: [{copy}]({url})")
        f.write(f"\n\nAuto get programm by LtgX\n")
    print(f"信息已经保存到 {history_path}")
else:
    print(f"请求失败，状态码为 {response.status_code}")


#Get Blobal Bing Wallpaper
RegionList = ["en-US", "ja-JP", "en-IN", "pt-BR", "fr-FR", "de-DE", "en-CA", "en-GB", "it-IT", "es-ES", "fr-CA"] #add your country here
#Create Readme.md for github display
info_path = os.path.join("global","README.md")
os.makedirs(os.path.dirname(info_path), exist_ok=True)
with open(info_path, "w", encoding='utf-8') as f:
    f.write(f"## Today's Bing Wallpaper\n")
    f.write(f"|      |      |      |\n")
    f.write(f"| :----: | :----: | :----: |\n")

#Main function
for region in RegionList:
    api_url_global = f"https://global.bing.com/HPImageArchive.aspx?n=1&setmkt={region}&setlang=en&idx=0&format=js"
    response = requests.get(api_url_global)
    if response.status_code == 200: #Check response
        data = response.json()
        urlbase = data["images"][0]["urlbase"]
        url = "https://www.bing.com" + urlbase + "_UHD.jpg"
        image_data = requests.get(url).content

        #Note: The following code is used for wallpaper download. If you need it, just enable it.

        #image_path = os.path.join("global",region,"img","background.jpg")
        #os.makedirs(os.path.dirname(image_path), exist_ok=True)
        #with open(image_path, "wb") as f:
            #f.write(image_data)
            #f.close()
        #print(f"Picture saved to {image_path}")

        #End

        #All codes below is to write README.md to display on github.
        enddate = data["images"][0]["enddate"]
        yy = f"{enddate[:4]}"
        mm = f"{enddate[4:6]}"
        dd = f"{enddate[6:]}"
        enddate = f"{enddate[:4]}-{enddate[4:6]}-{enddate[6:]}"

        copy = data["images"][0]["copyright"]
        title = data["images"][0]["title"]
        info_path = os.path.join("global",region,"README.md")
        os.makedirs(os.path.dirname(info_path), exist_ok=True)
        with open(info_path, "w", encoding='utf-8') as f:
            f.write(f"## Today's Bing Wallpaper\n")
            f.write(f"Update: {enddate}\n")
            f.write(f"![]({url}&w=1000)Download: [{copy}]({url})")
            f.write(f"\n\nAuto get programm by LtgX\n")
        print(f"Picture infomations saved to  {info_path}")

        history_file_name = f"{dd}_{region}.md"
        history_path = os.path.join("global",region,"history",yy,mm,history_file_name)
        os.makedirs(os.path.dirname(history_path), exist_ok=True)
        with open(history_path, "w", encoding='utf-8') as f:
            f.write(f"## History Bing Wallpaper\n")
            f.write(f"Wallpaper date: {enddate}\n")
            f.write(f"![]({url}&w=1000)Download: [{copy}]({url})")
            f.write(f"\n\nAuto get programm by LtgX\n")
        print(f"Picture infomations saved to {history_path}")

        info_path = os.path.join("global","README.md")
        with open(info_path, "a", encoding='utf-8') as f:
            f.write(f"|Region: {region}\n|")
            f.write(f"|![]({url}&pid=hp&w=1152&h=648&rs=1&c=4)|{enddate} [download]({url})|\n")
    
    else:
        print(f"Failed with statue code: {response.status_code}")

#By LtgX
info_path = os.path.join("global","README.md")
os.makedirs(os.path.dirname(info_path), exist_ok=True)
with open(info_path, "a", encoding='utf-8') as f:
    f.write(f"\nAuto get programm by LtgX\n")
