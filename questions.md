# Interview Question

## 网络

IO/多路复用:<br>
https://mp.weixin.qq.com/s?__biz=MzUxODAzNDg4NQ==&mid=2247489558&idx=1&sn=7a96604032d28b8843ca89cb8c129154&chksm=f98e5cbccef9d5aa249c02489614d81ce865eacb165846df84721636cd4717d1aaa830dbec56&scene=21#wechat_redirect


三次握手和四次挥手:<br>
https://zhuanlan.zhihu.com/p/86426969

TCP与UDP的区别:<br>
https://zhuanlan.zhihu.com/p/411843083

SSL/TLS:<br>
https://zhuanlan.zhihu.com/p/114342329
TCP三次握手结束->SSL四次握手->传输数据

SSL/TSL握手的简单原理(个人理解):<br>
https://www.notion.so/SSL-TLS-e3a39acac28141448fb35e3dfc07e4b8


## 计算机基础
进程, 线程和协程之间的关系:<br>
是否共享地址空间几乎是进程和线程的本质区别.linux内核并不区别对待它们,线程对于内核来说仅仅是一个共享特定资源的进程而已


进程间通信的五种方式:<br>
https://www.zhihu.com/question/458380614/answer/2931438114




## Python基础

python字典底层实现原理:<br>
https://blog.csdn.net/answer3lin/article/details/84523332

如何理解python万物皆对象:<br>
https://zhuanlan.zhihu.com/p/350060973

python迭代器和生成器:<br>
https://www.zhihu.com/question/20829330/answer/2320711618
https://www.zhihu.com/question/44015086/answer/119281039

python读取大文件的方法:<br>
https://zhuanlan.zhihu.com/p/611650797

python with语句及实现原理:<br>
https://www.zhihu.com/search?q=python%20with%E8%AF%AD%E5%8F%A5&search_source=Suggestion&utm_content=search_suggestion&type=content

python 异步 + 协程(如何使用):<br>


python GIL锁, 如何避免GIL锁:<br>
GIL 实际上是cpython解释器的全局解释器锁
1. 使用多进程, 不同的进程有不同的内存空间和解释器
2. 使用其他解释器
3. 使用cython





## 数据库原理
mysql索引原理:<br>

mysql统计记录数, count(*) 和 count(表名)的区别:<br>
https://zhuanlan.zhihu.com/p/105615075


数据库的常用优化:<br>


慢查询分析:<>




mysql优化

redis  面试题
https://www.zhihu.com/search?q=redis%E9%9D%A2%E8%AF%95%E7%9F%A5%E8%AF%86%E7%82%B9&search_source=Suggestion&utm_content=search_suggestion&type=content



## 数据结构与算法
二叉树的四种遍历:<br>
https://leetcode.cn/problems/binary-tree-preorder-traversal/solutions/247053/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/


## 设计模式

python装饰器:<br>

工厂模式:<br>
https://www.notion.so/afa75ebd58054c60b95bee87891428e7?pvs=4
