# visitorStatistic
本项目致力于为静态网站（例如hexo）提供访客统计&展示服务。  
本项目具有以下特点：  
1.根据cookies信息确保是否为重复访问，防止统计错误  
2.源服务器使用国内节点，确保国内用户正常访问  
3.仅需两行源码即可使用，无需任何复杂配置  
4.可同时显示网站累计访问次数以及每一位访客的访问顺序  
即刻开始展示网站流量：  

```
<p>Bingo!您是本站第<span id="visitorId">0</span>个访客</p><br />
<p>截至目前本页面已经被打开过<span id="sum">0</span>次</p>
<script src="visitor_statistic.js"></script>
```

本项目前后端完全开源，其中app.py为后端，使用flask作为框架，visitor_statistoc.js为前端。  
如对本项目有兴趣，欢迎通过pull request为本项目贡献代码。

演示地址：https://st.api.bnnet.com.cn/release/demo

数据千万条，保密第一条。机密忘记删，跑路泪两行。