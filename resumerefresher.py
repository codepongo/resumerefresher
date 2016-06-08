#coding: utf-8
import urllib2
import cookielib
import hashlib
import urllib
import json
from cfg import *

__doc__ = """resumerefresher - it freshes the resume in finding job website
zhaopin() function provides to refresh the resume in www.zhaopin.com
fiftyonejob() function provides to refresh the resume in www.51job.com
liepin() function provides to refresh the resume in www.liepin.com
usage:
    make a cfg.py file to config the account for website then run the python script
e.g.
user = {}
password = {}
resume = {}
user['liepin'] = 'user name'
password['liepin'] = 'password'
resume['liepin'] = 'resume id that can be found in the html source code'
"""
user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17'

def liepin(user, password):
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    query = 'user_login=' + urllib.quote(user) + '&'
    query += 'user_pwd=' + str(hashlib.md5(password).hexdigest())
    try:
        req = urllib2.Request('http://www.liepin.com/user/ajaxlogin/?isMd5=1',query, headers={"User-Agent":user_agent})
    except urllib2.HTTPError, e:
        print 'login request is failed [errorno = %s]' % e.code
        return False
    rep = json.loads(opener.open(req).read())
    if rep['flag'] != '1':
        print rep
        return False
    req = urllib2.Request('http://m.liepin.com/resume/refreshresume/?res_id_encode=%s' % resume['liepin'], headers={"User-Agent":user_agent})
    rep = json.loads(opener.open(req).read())
    if rep['result'] != '1':
        print rep
        return False
    return True

def fiftyonejob(user, password):
    httpHandler = urllib2.HTTPHandler(debuglevel=10)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    try:
        req = urllib2.Request('http://m.51job.com/my/login.php')
    except urllib2.HTTPError, e:
        print 'login request is failed [errorno = %s]' % e.code
        return False
    req.add_header('User-agent', user_agent)
    opener.open(req).read()

    data = {}
    data['username'] = urllib.quote(user)
    data['password'] = password
    data['verifycode'] = ''
    data['autologin'] = 1
    data = urllib.urlencode(data)
    try:
        req = urllib2.Request('http://m.51job.com/ajax/my/login.ajax.php','username=offerbox%2540163.com&password=passw0rD&verifycode=&autologin=1')
    except urllib2.HTTPError, e:
        print 'login request is failed [errorno = %s]' % e.code
        return False
    req.add_header('Origin', 'http://m.51job.com')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Accept', 'application/json')
    req.add_header('Referer', 'http://m.51job.com/my/login.php')
    req.add_header('User-agent', user_agent)
    rep = opener.open(req).read()
    rep = json.loads(rep)
    if rep['status'] != '1':
        print rep['desc'].encode('utf8')
        return False
    req = urllib2.Request('http://m.51job.com/ajax/resume/refreshresume.ajax.php','rsmid=%s' % resume['51job'], headers={"User-Agent":user_agent})
    rep = json.loads(opener.open(req).read())
    if rep['status'] != 1:
        print rep['desc'].encode('utf8')
        print rep
        return False
    return True

def zhaopin(user, password):
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    query = 'userName=' + urllib.quote(user) + '&'
    query += 'pwd=' + password
    try:
        req = urllib2.Request('http://m.zhaopin.com/account/logon',query, headers={"User-Agent":user_agent})
    except urllib2.HTTPError, e:
        print 'login request is failed [errorno = %s]' % e.code
        return False
    rep = json.loads(opener.open(req).read())
    if not rep['RequestSusess']:
        print rep
        print rep['StatusDescription']
        return False

    req = urllib2.Request('http://m.zhaopin.com/resume/refreshresume', 'resumeId=%s&language=1'%resume['zhaopin'], headers={"User-Agent":user_agent})
    cookie = ''
    if req.has_header('Cookie'):
        cookie = req.get_header('Cookie')
    for c in rep['cookies']:
        cookie = c['Name']+'='+c['Value']+';'+cookie
    req.add_header('Cookie', cookie)
    rep = json.loads(opener.open(req).read())
    if not rep['RequestSusess']:
        print rep
        return False
    return True

if __name__ == '__main__':
    print 'refresh the resume in liepin.com:', liepin(user['liepin'], password['liepin'])
    print 'refresh the resume in zhaopin.com:', zhaopin(user['zhaopin'], password['zhaopin'])
    print 'refresh the resume in 51job.com:', fiftyonejob(user['51job'], password['51job'])
