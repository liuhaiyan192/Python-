import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

# base_url = 'https://www.toutiao.com/search_content/?' + urlencode(params)

headers = {
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

# 获取页面
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    # url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print(e.args)


# 解析页面返回的Json
def get_images(json):
    if json.get('data') and not json.get('data'):
        for items in json.get('data'):
            author = items.get('media_name')
            urls = items.get('image_list')
            if urls is None:
                pass
            else:
                # print(type(urls))
                for url in urls:
                    # print('http:' + url.get('url'))
                    yield {
                    # 获取完整链接
                    'url': 'http:' + url.get('url'),
                    'author': author
                    }

# 将图片保存到本地
def save_image(item):
    if not os.path.exists(item.get('author')):
        os.mkdir(item.get('author'))
    try:
        if item.get('url'):
            print(item.get('url'))
            response = requests.get(item.get('url'))
            if response.status_code == 200:
                # 将获取到的图片保存到本地的时候，修改格式为jpg格式
                file_path = '{0}/{1}.{2}'.format(item.get('author'), md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Download', file_path)
    except requests.ConnectionError as e:
        print('Falied', e.args)

Group_Start = 1
Group_End = 20

# 主方法
def main(offset):
    json = get_page(offset)
    for items in get_images(json):
        # print(items)
        save_image(items)

if __name__ == '__main__':
    pool = Pool()
    print(range(Group_Start, Group_End+1))
    groups = ([x * 20 for x in range(Group_Start, Group_End+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
