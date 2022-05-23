import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime,time


def job_YqHours(**kwargs):
    print('本次任务运行时间************************************')
    print('舆情2小时-数据更新任务启动：')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    req_body = {
    'target' : kwargs['chat_name']
    }
    res=requests.post(post_url,json=req_body)
    print(res.text)


def job_WscDaily(**kwargs):
    print('本次任务运行时间************************************')
    print('微商城日报-数据更新任务启动：')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    req_body = {
    'target' : kwargs['chat_name']
    }
    res=requests.post(post_url,json=req_body)
    print(res.text)


def job_DyDaily(**kwargs):
    print('本次任务运行时间************************************')
    print('抖音小店-数据更新任务启动：')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    req_body = {
    'target' : kwargs['chat_name']
    }
    res=requests.post(post_url,json=req_body)
    print(res.text)

def job_DyRetui(**kwargs):
    print('本次任务运行时间************************************')
    print('内容热推-数据更新任务启动：')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    req_body = {
    'target' : kwargs['chat_name']
    }
    res=requests.post(post_url,json=req_body)
    print(res.text)
    
def job_DyXd(**kwargs):
    print('本次任务运行时间************************************')
    print('抖音小店-数据更新任务启动：')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    req_body = {
    'target' : kwargs['chat_name']
    }
    res=requests.post(post_url,json=req_body)
    print(res.text)



# post_url = "http://127.0.0.1:80/fs_autoFile"
post_url = "http://47.102.219.231:80/fs_autoFile"
sched = BlockingScheduler()
sched.add_job(job_WscDaily, 'cron',hour=11, minute=5,kwargs = {'chat_name':'WscDaily'})
sched.add_job(job_DyDaily, 'cron',hour=12,minute=1,kwargs = {'chat_name':'DyDaily'})
sched.add_job(job_DyRetui, 'cron',hour=11,minute=30,kwargs = {'chat_name':'DyRetui'})
sched.add_job(job_DyXd, 'cron',hour=14,minute=40,kwargs = {'chat_name':'DyXd'})



# sched.add_job(job_YqHours, 'cron',hour=14,minute=10,kwargs = {'chat_name':'autotest'})
# sched.add_job(job_WscDaily, 'cron',hour=14,minute=10,kwargs = {'chat_name':'autotest'})
# sched.add_job(job_DyDaily, 'cron',hour=14,minute=10,kwargs = {'chat_name':'autotest'})

# 测试
# sched.add_job(job_YqHours, 'cron',hour=14, minute=28,kwargs = {'chat_name':'YqHours'})    # 舆情2小时的访问小北会调用，所以这边不需要我调用
# sched.add_job(job_WscDaily, 'cron',hour=14, minute=28,kwargs = {'chat_name':'WscDaily'})
# sched.add_job(job_DyDaily, 'cron',hour=14,minute=28,kwargs = {'chat_name':'DyDaily'})

sched.start()







