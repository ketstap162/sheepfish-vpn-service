import re

import requests
from django.contrib.auth import get_user_model

from VPN.models import Site


def get_original_site_url(user: get_user_model(), alias: str, path: str) -> str:
    site = Site.objects.get(alias=alias, user=user)
    return site.url + "/" + path


def get_site_data(url: str) -> dict:
    response = requests.get(url)
    data = {
        "headers": dict(response.headers),
        "content": response.text,
    }
    return data


def post_site_data(url: str, data: dict):
    response = requests.post(url, data)
    data = {
        "headers": dict(response.headers),
        "content": response.text,
    }
    return data


def replace_urls(url: str, alias: str, text: str) -> str:
    pattern = re.compile(r"<a(.*?)>")

    def replace_match(match):
        return match.group(0).replace(url, "vpn/" + alias)

    return pattern.sub(replace_match, text)
