# encoding: utf-8
import os
import re
import xmlrpc.client

from .models import Picture

ID_SERVER = xmlrpc.client.ServerProxy("http://64.161.32.153:31128/RPC")
PICTURES_DIR = "C:/Dev/picmatch/pictures"

# print(ID_SERVER)

# print(ID_SERVER.getDbImgCount(1))
# print(ID_SERVER.addImg(1, 999999, os.path.join(PICTURES_DIR,"1.jpg")))
# print(ID_SERVER.addKeywordImg(1,1,3))
# print(ID_SERVER.getKeywordsImg(1,1))
# print(ID_SERVER.queryImgID(1,6, 3))

def picmatcher(pic_name):
    """pic_name -- Limit a text to 20 chars length, if necessary strips the
    middle of the text and substitute it for an ellipsis.

    Compares an image with a list of images using the SSIM metric.

    """
    match_res = list()
    match_name ='pictures/'+pic_name
    p = Picture.objects.filter(file=match_name)
    print('Saved image:', pic_name)
    #print(Picture.objects.all()[70].slug,Picture.objects.all()[70].file)
    print(p)
    if p:
        add_success = ID_SERVER.addImg(1, p[0].id, os.path.join(PICTURES_DIR, p[0].slug))
        query_res = ID_SERVER.queryImgID(1, p[0].id, 20)
        for img in query_res[1:]:
            tmp_dict=dict()
            tmp_dict['name'] = Picture.objects.filter(id=img[0])[0].slug
            tmp_dict['svalue']  = "%.2f" % img[1]+"%"
            match_res.append(tmp_dict)
    return match_res
