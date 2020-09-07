## Chrome打包crx并导出安装

### 打包

#### 1.查看要打包的扩展程序

> 在`chrome`中输入`chrome://extensions`,打开[开发者模式],并复制相关`ID`
>
> ![10281](https://gitee.com/ningwenyan/My_chat_picgo/raw/master/2020-9-7/1599490755361-10281.png)

#### 2.查找扩展位置

> 在`chrome`中输入`chrome://version`,找到[个人资料位置],并找到[extensions]文件夹
>
> ![10282](https://gitee.com/ningwenyan/My_chat_picgo/raw/master/2020-9-7/1599490921389-10282.png)
>
> 我使用的文件管理工具是`thundar`,安装`ID`找到文件位置.
>
> ```bash
> $ thunar /home/kning/.config/google-chrome/Default/Extensions/  
> ```
>
> ![10283](https://gitee.com/ningwenyan/My_chat_picgo/raw/master/2020-9-7/1599491141212-10283.png)

#### 3.打包扩展

> 点击打包扩展程序,并输入要打包的扩展插件目录.
>
> ![10284](https://gitee.com/ningwenyan/My_chat_picgo/raw/master/2020-9-7/1599491291104-10284.png)

#### 4.打包完成

> 打包完成后,可以在插件`ID`目录下找到打包好的`CRX`程序
>

### 安装

#### 1.直接安装

> `CRX`程序可直接拖动到`chrome`浏览器中安装,但是有时候,有些插件不能安装,这时候就需要使用其他方法安装.

#### 2.解压缩安装

> - 右键`CRX`文件,选择更改名称,修改后缀为`rar`或者`zip`.然后选择系统的压缩工具进行解压缩.
>
> - 在`chrome`中输入`chrome://extensions`,打开[开发者模式]
>
> - 选择`加载已解压的扩展程序` ,选择解压后的文件夹位置,即可直接安装插件.