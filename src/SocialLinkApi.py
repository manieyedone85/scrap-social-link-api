import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request

social_link_api = Blueprint('social_link_api', __name__)


@social_link_api.route("", methods=['POST'])
def remove_bg():
    print(request.json["url"])  # request.json["kk"]
    url = request.json["url"]
    social_media_dict = {}
    smc = get_social_media_handles(get_html_content(url))
    if smc:
        social_media_dict["status"] = "Success"
    else:
        social_media_dict["status"] = "Failure"
    social_media_dict["links"] = smc
    print(social_media_dict)
    return social_media_dict


def get_html_content(url):
    soup = None
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    except:
        return soup
    return soup


def get_social_media_handles(html_code):
    social_media_urls = {}
    if html_code != None:
        links = html_code.find_all('a', href=True)
        if len(links) > 0:
            urls = []
            for link in links:
                urls.append(link['href'])
            urls = list(set(urls))
            for url in urls:
                so, category = is_social_media(url.lower())
                if so:
                    social_media_urls[category] = url
    return social_media_urls


def is_social_media(url):
    keywords = ['facebook', 'twitter', 'instagram', 'youtube', 'spotify', 'pinterest', 'tiktok', 'linkedin']
    for key in keywords:
        if key in url:
            return True, key
    return False, None
