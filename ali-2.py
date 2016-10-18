# -*- coding=utf-8 -*-
import requests
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import json
import jieba

class OCR(object):
    def __init__(self):
        self.imageFile = 'test.jpg'
    
    def run(self):
        datagen, headers = multipart_encode({"imageFile": open(self.imageFile, "rb")})
        headers['Host']='aligreen.alibaba.com'
        headers['Connection']='keep-alive'
        headers['Accept']='application/json, text/javascript, */*; q=0.01'
        headers['Origin']='http://aligreen.alibaba.com'
        headers['X-Requested-With']='XMLHttpRequest'
        headers['Accept-Encoding']='gzip, deflate'
        headers['Accept-Language']='zh-CN,zh;q=0.8'
        headers['Cookie']='cna=6c9rEM7A8W0CAbeB2ukCuutX; l=AmtrPA8gwLaNmLmcW7nvXzBMe4VXhn8C; isg=Am9vM74Oa-OMeG_fwI48Af5s_oMVAuQaV5JRi4H-DV7l0I7SieBphhXGJHeU'
        headers['User-Agent']='Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'

        register_openers()

        request = urllib2.Request("http://aligreen.alibaba.com/rpc/image/upload_image.json", datagen, headers)
        upload_result = urllib2.urlopen(request).read()
        tempdict = json.loads(upload_result)

        imageurl = tempdict['imageUploadResultList'][0]['imageUrl']
        # Detection-----------------------------------------------------------
        detection_url = 'http://aligreen.alibaba.com/rpc/image/detect.json'
        payload = {'imageUrls[]': imageurl, 'scene': 'ocr'}
        headers = {'Host':'aligreen.alibaba.com','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Content-Length': '2'}
        r = requests.post(detection_url,data=payload)
        sentence = json.loads(r.text)[0]['images'][0]['ocr']['text'][0]
        temp = '/'.join(jieba.cut(sentence))
        words = temp.split("/"),type(temp.split("/"))
        print words
        return words

OCR().run()