# login_script
技术实现：selenium+phantomjs+requests


## 关于

模拟登陆基本采用的是直接登录或者使用selenium+webdriver的方式。

可以在登录过后得到的cookie维护起来，然后调用requests或者scrapy等进行数据采集，这样数据采集的速度可以得到保证。

下面是已经实现和待实现的目标

- [x] 微博
- [x] 知乎
- [x] QQ空间
- [x] 京东
- [x] 163邮箱
- [x] CSDN
- [x] 百度


其中比较典型的是微博这一类的模拟登陆，会用到RSA、Base64等加密和编码算法，关于它的分析过程，我写了[一篇文章](http://www.jianshu.com/p/816594c83c74)，写得很详细，帮助大家理解

## 常见问题

- 关于验证码：本项目所用的方法都没有处理验证码，识别复杂验证码的难度就目前来说，还是比较大的。以我的心得来说，做爬虫最好的方式就是尽量规避验证码。
- 代码失效：由于网站策略或者样式改变，导致代码失效，请给我提issue，如果你已经解决，可以提PR，谢谢！

## 其它

- 授人以鱼不如授人以渔，如果感觉自己分析模拟登陆过程还有比较大的困难的，可以仔细阅读一下我写的三篇文章，包括了两种典型的模拟登陆和三种分析思路.
 - [模拟登陆csdn](http://www.rookiefly.cn/detail/65)
 - [模拟登陆微博](http://www.jianshu.com/p/816594c83c74)
 - [模拟登陆百度网盘](http://www.jianshu.com/p/efcf030e68c5)
- 如果你有什么比较难登陆的网站，比如发现用了selenium+webdriver都还登陆不了的网站，欢迎给我提issue.
- 如果该repo对大家有帮助，给个star鼓励鼓励吧.

## 需要安装的库
- [ExecJS](https://pypi.org/project/PyExecJS/)
- [selenium](https://pypi.org/project/selenium/)
- [rsa](https://pypi.org/project/rsa/)
- [Pillow](https://pypi.org/project/Pillow/)


## Chrome 驱动
- [chromedriver](http://npm.taobao.org/mirrors/chromedriver/)