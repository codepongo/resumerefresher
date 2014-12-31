resumerefresher
===============

it freshes the resume in finding job website

* zhaopin() function provides to refresh the resume in www.zhaopin.com
* fiftyonejob() function provides to refresh the resume in www.51job.com
* liepin() function provides to refresh the resume in www.liepin.com
## usage ##
make a cfg.py file to config the account for website then run the python script
e.g.
<pre>
user = {}
password = {}
resume = {}
user['liepin'] = 'user name'
password['liepin'] = 'password'
resume['liepin'] = 'resume id that can be found in the html source code'
</pre>

刷新招聘网站上的建立
* zhaopin() 刷新[智联招聘](www.zhaopin.com)的简历
* fiftyonejob() 刷新[51job](www.51job.com)的简历
* liepin() 刷新[猎聘网](www.liepin.com)的简历

## 用法 ##
建立一个cfg.py文件用于保存网站账户信息
例如：
<pre>
user = {}
password = {}
resume = {}
user['liepin'] = 'user name'
password['liepin'] = 'password'
resume['liepin'] = 'resume id that can be found in the html source code'
</pre>
*由于resumeid都是固定的，为提高（开发和运行）效率不必通过html分析去获取，直接查看html源文件找到后复制至cfg.py即可*

** cfg.py 中明文保存用户信息，注意其安全性 **
