# diceware
Generate memorizable strong password for Chinese user.   
We use coin here because coins are widely used. It's everywhere, if not, use the `second hand` on a watch.   
<hr>
易于记忆的强密码生成器.   
这里生成的密码词典针对的是硬币, 毕竟硬币随处可见. 连硬币也没有? 随机看秒表的奇偶.   

# Why
Combined words in Chinese are like English word. But single word in Chinese is like a-z. For example:  

|beijing|bei / jing|
|---|---|
|shanghai|shang / hai|
|brainwashing|brain / washing|
|kungfu|kong / fu|

So single char [wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_simplified.txt) used in Bitcoin is not practical.   

# Warning 警告
Set an alarm MONTHLY to remind you RECITE your password in case you may forget it.   
<hr>
记得设置闹钟每月提醒自己默背设置好的强密码，否则一定会忘记并丢失资料的。   


# Usage 使用方法
get password:  
获取密码:
```bash
# clone repo:
git clone https://github.com/cryptogun/diceware
cd diceware
# run:
python3 password.py
```
generate wordlist:  
生成词典:
```bash
# generate:
python3 generate_wordlist.py
```

Exclude word:
排除拼音:
```bash
# 编辑 pinyin_excluded.txt
nano pinyin_excluded.txt
# generate
python3 generate_wordlist.py

```


# Features 特点
* Source: [Lexicon of Common Words in Contemporary Chinese](https://gist.github.com/indiejoseph/eae09c673460aa0b56db).
* Principle: Filter on disyllable only. Order by frequency rank. And limit 4<=len(word)<=8.
* Memo tips: One-to-many relationship for `pinyin - hanzi` by looping through the entire source instantly.
* Support black list for un-memorizable pinyin. Just add them to `pinyin_excluded.txt`.
* Printable txt wordlist generated. Total 139 pages.
* Word space is 8192(2^13), slightly larger than 7776(6^5) using a dice.
* Use coin instead of dice. 1 toss equals 1 bit of entropy.
* Written in Python. 1. Lightweighted; 2. Easy to audit; 3. Universal exec.
* No 3-party package dependance. Minimize attack surface.
* Use [SystemRandom](https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python) which use `urandom` for non-important password generation.
* word length distribution: {4: 594, 5: 1740, 6: 2479, 7: 2162, 8: 1217}
<hr>

- 词典来源: [现代汉语常用词表](https://gist.github.com/indiejoseph/eae09c673460aa0b56db) 课题组.
- 取词原则: 由高到低选取最常用的词汇; 只取双音节词, 利于记忆; 限制拼音长度的上下限, 兼顾安全性和便利性.
- 快速分析整个**现代汉语常用词表**, 提取同音多词, 可以提示联想.
- 支持黑名单, 手动排除难以联想和记忆的拼音. (在pinyin_excluded.txt里添加, 添加后需要重新编译新词典. 欢迎提供你的黑名单.)
- 生成txt词典, 方便打印. (有139多页.)
- 词典拼音数量为8192(2^13), 比英文原版7776(6^5)多.
- 使用常见的硬币而非骰子产生随机数. 抛一次硬币信息熵 +1bit.
- 使用Python脚本编写. 1. 轻量易用. 2. 易于审查代码(目前仅230多行代码); 3. 代码通用, 可以在各种系统运行.
- 无第三方依赖包, 攻击面窄.
- 利用Python[密码学安全级别](https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python)的随机数生成器`SystemRandom`. 他是系统`urandom`的封装接口. 足够生成普通密码.  
- 编码(拼音)长度分布: {4: 594, 5: 1740, 6: 2479, 7: 2162, 8: 1217}

# Cons 缺点
- `Pinyin`s (that are hard to associate, hard to memo, hard to match) are not fully reviewed.
- `Pseudo`-random is not `true` random. Use coins as much as possible.
<hr>

* 未排除部分难联想/难记/难匹配的拼音.
* 伪随机毕竟不是真随机, 即使用到了`urandom`. 比如我尝试了100多次, `实习` `yindu`在下面的例子中各出现了2次; `春联`出现在同一密码中. 这几率都是8x100x(1/8192)^2. 所以还是推荐用硬币.

# Contribution 共建
本项目采用MIT许可(MIT, BSD, Apache 3大自由许可之一), 无限制, 更自由. 欢迎提建议, 合并代码!

- 需要人工排除部分难联想/难记/难匹配的拼音. 你可以到[random.org](https://www.random.org/integers/?num=1&min=1&max=8192&col=1&base=10&format=plain&rnd=new)获取随机的行号, 打开[wordlist.txt](https://github.com/cryptogun/diceware/blob/master/wordlist.txt)词典文件, 审阅拼音, 审多少行都行. 遇到不好的拼音提个issue或者修改[pinyin_excluded.txt](https://github.com/cryptogun/diceware/blob/master/pinyin_excluded.txt)然后pull request都行.

一些感想:

* 查到的资料说, 抛硬币的结果跟初始朝上的面有关. 上:下=51:49. 抛之前捂手里摇几下可以增加随机变量. 接的高度可以任意随机决定. 小心显示器.
* prefix codes(来自: `chinese-diceware`)确实可以防止密码空间塌陷(2句中文句子对应同一串拼音). 可以用反证法从左到右推导. 这保证了拼音密码无法错开诠释. 缺点就是会排除一些可以导致塌陷却高频的词汇.
* 目前8位密码的强度是2^(13x8). 如果仅仅是词典翻倍, 强度是2^(14x8); 如果仅仅增加一位密码, 强度是2^(13x9). 后者更多. 但要考虑到词语常见度, 词典打印页数, 密码长度, 节律, 审阅工作量等问题.
* 之前用的是搜狗高频词库. 结果能用, 但不是太理想. 毕竟大众输入的质量跟国家审核过的没法比. 目前借鉴`chinese-diceware`, 使用**现代汉语常用词表**.
* 这几条路应该不行(基于先前的搜狗词库):
    - `pypinyin`库无法快速注音.
    - `jieba`分类词性, 结果只有动词和名词够用(都 > 8192).
    - `动名动名 动名动名`模式不好记.
    - 动词后半部分基本都是生僻的动词.

这里有词频: [现代汉语频率词典](http://www.unicode.org/reports/tr38/#kHanyuPinlu)
还可以参考这个项目: [chinese-diceware](https://github.com/cfbao/chinese-diceware)

# Name 名字
Dice includes coin, according to the Wikipedia.   
<hr>
使用通用的名字diceware而不用coinware. 根据维基百科所说, 骰子包括多面骰子, 也包括2面骰子即硬币. 

# Example 例子
|密码|联想 越具体/奇异/逼真越好|
|:-:|:-|
|juji.gengjia.jianguo.yuanxing.shufu.chongji.kuangwu.shoujuan<br>狙击.更加.坚果.圆形.叔父.充饥.狂舞.手绢|狙击远处的一颗圆形的坚果, 越狙越坚硬. 叔父为了充饥, 狂舞手绢.|
|xiantiao.lianmang.jieli.jiyu.wannian.paizi.bucuo.kaifang<br>线条.连忙.接力.急于.晚年.牌子.不错.开放|拿起线条连忙赶去接力, 太急于求成了. 小平晚年看见资本主义的牌子不错, 决定改革开放.|
|tengfei.wugu.weichi.daxiao.rongxing.jingdi.wanxiang.tuichi<br>腾飞.五谷.维持.大小.荣幸.劲敌.万象.推迟|腾飞的五谷居然能够维持大小! 很荣幸能遇到劲敌, 他居然把一万头大象都给推迟了.|
|daode.yinmu.xiama.tuzai.neihang.shixing.touchan.shoujie<br>道德.银幕.下马.屠宰.内行.施行.投产.首届|道德只有在银幕上才能见到. 他一下马就屠宰狗肉. 内行人施行并投产, 那是首届, 头一遭.|
|zhuyi.beihou.shumian.weiyue.teyao.yishan.yinyong.fangfu<br>主意.背后.书面.违约.特要.衣衫.饮用.防腐|出的什么馊主意, 居然叫我背后书面违约. 死之前还不忘特别要一件上衣衫, 还要饮用防腐剂!|
|gushi.tanlun.rongren.suoyou.huanghai.fenbu.dongdang.shenyin<br>股市.谈论.容忍.所有.黄海.分布.动荡.呻吟|想要参与股市谈论, 就得容忍所有的意见. 小鬼子查探黄海的分布情况, 动荡的年代到处都是痛苦的呻吟.|
|zijue.haoshi.chaoe.yindu.huijian.zuijiao.chaoqi.neibu<br>自决.好事.超额.引渡.回见.嘴角.潮气.内部|民族自决是好事, 你看美国都超额引渡非法移民了. 回头看看那些难民, 嘴角的潮气都从内部渗出来了.|
|qiaoran.tiaopi.pojiu.beibu.qili.ruhe.yinshui.renli<br>悄然.调皮.破旧.背部.气力.如何.引水.人力|悄悄然, 调皮的你把我的椅子换了个破旧的背部. 气力如何? 西部凿壁引水需要人力.|
|dayu.zhanshu.shengzi.zengjia.chazui.mingri.daixie.shouling<br>大雨.战书.生字.增加.插嘴.明日.代谢.守灵|战场上的大雨, 淋湿和模糊了战书, 生字增加了. 花朵插嘴, 明日就代谢了, 像黛玉那样守灵.|
|zhengzhi.guanqu.huoguang.qiangdu.zhuce.zhuanke.yuwen.fenyong<br>正值.灌渠.火光.强度.注册.专科.语文.粪泳|正值雨水灌渠的时节, 日夜赶工, 火光强度却远远不够.  一个注册专科护士却想教语文? 先到粪池里游泳一圈.|
|pendi.pixie.yuanxing.weizhu.zangzu.tianxian.shixi.renshi<br>盆地.皮鞋.圆形.为主.藏族.天仙.实习.人世|盆地就像皮鞋, 以圆形为主. 藏族都是天仙呐, 到人世间实习来了, 怪不得住那么高.|
|genzhe.shangu.benyi.shousuo.shuilv.weifan.yecai.guoqing<br>跟着.山姑.本意.售锁.税率.违反.野菜.国庆|跟着山姑本意是想售锁, 没想到违反了税率, 这个国庆只能吃野菜充饥了. 都反了啊.|
|guina.haosheng.zuihou.bochang.chahuo.junheng.zhenqing.shenyi<br>鬼拿.耗声.最后.波长.查获.均衡.真情.深意|鬼拿耗子的声音, 那是最后的波长. 今天查获的茶货比较均衡, 有真情, 有深意.|
|haian.weirao.tongche.fuxi.yishu.fangkong.bianji.dayi<br>海岸.胃要.通车.复习.医书.防空.变机.打蚁|海岸线像个胃一样, 要通车了. 有位帅哥在车上复习医书. 海上要防空啊, 所以火车就变成了飞机, 把地上的一只蚂蚁打死了.|
|fankang.xiangdai.shenzhou.shixi.mingri.menkan.tuidong.xuedi<br>反抗.想待.神州.实习.明日.门槛.推动.雪地|非法移民遇到恶人不敢反抗, 因为想待在神州大地上实习. 雪太大了, 明日要把门槛拆了才能推动雪地.|
|chouti.shouduan.guandao.pojie.liannian.danshui.songxie.yindu<br>抽屉.手断.管道.破解.连年.淡水.松懈.印度|抽屉把手指给夹断了, 骨头露了出来. 喜马拉雅山上的管道经过破解, 连年都有淡水, 一旦松懈下来, 让印度给污染了.|
|chibang.weixin.mifeng.jiaohuo.diaoke.pingyong.peiyu.liushui<br>翅膀.微信.蜜蜂.交货.雕刻.平庸.培育.流水|翅膀上都印着微信二维码的蜜蜂过来交货了, 为了卖蜂蜜真实不遗余力. 这雕刻太平庸了, 你们学校都是培育流水线的吧?|
|huangyan.shangyou.diaodong.lvzhou.daoqi.benneng.mangmu.pinqiong<br>晃眼.上游.调动.绿洲.到期.本能.盲目.贫穷|敌人的飞机晃眼, 敌人的舰艇在上游, 我军调动一大批军队就像绿洲. 兵役到期, 由于人的本能, 盲目择业, 贫穷潦倒.|
|yishen.zaoyu.yujian.keben.dedao.hanyou.shengdi.siyi<br>蚁神.早语.遇见.课本.得道.汉游.胜地.司仪|蚁神很早就会说话了, 又遇见了语文课本. 得道之后来到汉地旅游,  居然在某胜地某了个主持仪式的职位.|
|jinqi.huaduo.shanye.daomei.minzhong.dahui.dengzi.ziji<br>近期.花朵.山野.倒霉.民众.大会.凳子.自己|近期, 花朵开满山野,  却被采花贼偷走了. 倒霉的民众开大会讨论, 凳子却要自己搬.|
|ningyuan.zonglan.muke.haozhao.lishun.caifa.xinpian.ganma<br>宁愿.粽蓝.木刻.好找.理顺.采伐.芯片.干嘛|屈原宁愿纵身蓝色的江底. 有人在船沿的木头上刻下标记, 靠岸后更好找. 把木头理顺后更好采伐, 要那么现代化的芯片自动化干嘛.|
|xiaoxiao.jianmo.ezhan.touhao.wucha.qiuhe.rongzhu.kuangjia<br>小小.缄默.恶战.头号.误差.求和.熔铸.框架|小小缄默了, 恶战需要在头上绑上号码. 由于枪械有误差, 只能求和了. 愤怒之下把他们都熔铸成了框架. 杀千刀的兵工厂!|
|zhanche.fenshao.cheli.yongren.jianxun.baodao.neizang.zisheng<br>战车.焚烧.撤离.佣人.简讯.报道.内脏.滋生|坦克战车被焚烧, 车里的佣人被活活烧死了. 按照简讯的报道, 他们内脏都滋生出来了.|
|tuichi.anjian.zaibian.weixie.sengren.qingshi.xingbing.zuse<br>推迟.安检.栽便.威胁.僧人.情史.性病.阻塞|你必须推迟安检, 否则我在包里中便威胁. 僧人也是有情史的, 因为染上了性病, 这条路被阻塞了, 不方便.|
|buliao.yansu.neige.yinci.mucao.xiexie.xiaofang.shimin<br>布料.严肃.内阁.因此.牧草.谢谢.消防.市民|因为布料起火事故, 需要严肃整顿内阁. 因此, 牧草们希望谢谢消防中队里的市民.|
|quanti.xiazi.yugan.bingqi.lengzhan.diya.yinjiu.canshu<br>全体.虾子.预感.冰期.冷战.低压.饮酒.惨输|全体虾子预感到冰期的到来. 冷战之下没有低压只有高压, 饮酒误事惨输.|
|jianfei.jixing.daxiao.ezhi.bobo.diguo.dingqi.loumian<br>减肥.畸形.大小.饿脂.饽饽.帝国.定期.露面|减肥减到畸形, 上大下小, 还说是饿脂. 饽饽帝国的伯伯还定期带着饽饽露面, 口水都三千尺了.|
