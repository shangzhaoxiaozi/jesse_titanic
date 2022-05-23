from typing import Optional
from pydantic import BaseModel
from fastapi.responses import FileResponse,StreamingResponse,Response
from pydantic import BaseModel
from fastapi import FastAPI, Form
import uvicorn
import os, random, sys, requests,json,io
from requests_toolbelt.multipart.encoder import MultipartEncoder 
import asyncio
import datetime,time
#具体脚本
import YqHours
import WscDaily
import DyDaily
import DyRetui
import DyXd


# 接口部分
app = FastAPI()

class Item(BaseModel):
    target : str


async def asy_task(target):
    if target == 'YqHours':
        YqHours.ini_all('舆情自动化测试群')
        # YqHours.ini_all('autotest')
    if target == 'WscDaily':
        WscDaily.ini_all('微商城日报测试群')
#         WscDaily.ini_all('autotest')
    if target == 'DyDaily':
        DyDaily.ini_all('抖音监控每天')
        # DyDaily.ini_all('autotest')
    if target == 'DyRetui':
        DyRetui.ini_all('抖音热推临时替代群')
#         DyRetui.ini_all('抖音数据日化分享群')
#         DyRetui.ini_all('autotest')
    if target == 'DyXd':
        DyXd.ini_all('抖音XBI')
#         DyXd.ini_all('autotest')
        
    if target == 'autotest':   # 测试用
        DyDaily.ini_all('autotest')


@app.get("/")
async def read_root():
    return {'data' : 'get ok'}


@app.post("/fs_autoFile")
async def yqhours_send(item: Item):
    print('收到请求，将使用：',item.dict()['target'],' 发送文件：')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    
    if item.dict()['target'] == 'YqHours':
        asyncio.create_task(asy_task(item.dict()['target']))   # 创建一个新的可以调度的协程,后台执行发送任务
        # asyncio.create_task(asy_task('autotest'))   # test
        return {"status" : 'ok'}

    if item.dict()['target'] == 'WscDaily':
        asyncio.create_task(asy_task(item.dict()['target']))
        # asyncio.create_task(asy_task('autotest'))   # test
        return {"status" : 'ok'}

    if item.dict()['target'] == 'DyDaily':
        asyncio.create_task(asy_task(item.dict()['target']))
        # asyncio.create_task(asy_task('autotest'))   # test
        return {"status" : 'ok'}
    
    if item.dict()['target'] == 'DyRetui':
        asyncio.create_task(asy_task(item.dict()['target']))
        # asyncio.create_task(asy_task('autotest'))   # test
        return {"status" : 'ok'}
    
    if item.dict()['target'] == 'DyXd':
        asyncio.create_task(asy_task(item.dict()['target']))
        # asyncio.create_task(asy_task('autotest'))   # test
        return {"status" : 'ok'}

    if item.dict()['target'] == 'autotest':
        asyncio.create_task(asy_task(item.dict()['target']))   # 
        return {"status" : 'ok'}


    
    return {"status" : 'error'}



if __name__ == '__main__':   
     uvicorn.run(app='FsAutoFileServer:app', host="0.0.0.0", port=80, reload=True, debug=True)
     # uvicorn.run(app='FsAutoFileServer:app', host="127.0.0.1", port=80, reload=True, debug=True)

