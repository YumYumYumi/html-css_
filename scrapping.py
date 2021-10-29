from flask import Flask, render_template, request, redirect, send_file
import requests
from bs4 import BeautifulSoup


headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }

db = {}


def extract_link(html):
    link = html.find_all("img")[0]["src"]
    if link is not None: 
      link = link
    return {
        "link": link
    }



def extract_links(word):
    links = []
    result = requests.get(f"https://unsplash.com/s/photos/{word}?orientation=portrait", headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "VQW0y Jl9NH"})
    for result in results:
        link = extract_link(result)
        links.append(link)
    return links



def get_jobs_remoteok(word):   
    links = extract_links(word)
    print(links)
    return links



get_jobs_remoteok("national-park")



