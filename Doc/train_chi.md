# 使用不同的字符集 #
## 字符集
*   什么是字符集？  
字符(Character)是各种文字和符号的总称，包括各国家文字、标点符号、图形符号、数字等。字符集(Character set)是多个字符的集合，字符集种类较多，每个字符集包含的字符个数不同，常见字符集名称：ASCII字符集、GB2312字符集、BIG5字符集、 GB18030字符集、Unicode字符集等。
*   tesseract如何使用字符集来识别？  
在Linux环境下，tesseract安装在了/usr/share/tesseract/4.00目录下，里面只有一个tessdata文件夹，里面存放的就是各种不同不同的字符集以及一些相关的config文件。字符集都以.traineddata为后缀。在环境部署时的test.py里有 “-l eng”这样的config，即代表使用的是eng.traineddata这个字符集来识别图片的。想使用自己训练生成的字符集只需要修改这个config即可。
*   如何训练自己的字符集？  
    *   在window环境下安装jTessBoxEditor。  
    *   将源图片转换成tif格式，用于生成box文件。直接另存为即可。
    *   更改名字为[lang].[fontname].exp[num].tif的格式。  
        *   lang：语言
        *   fontname：字体
        *   num：代表自身的数字
    *   生成box文件：
    ```
    tesseract d.normal.exp1.tif d.normal.exp1 -l eng1 batch.nochop makebox
    ```
    *   打开jTessBoxEditor观察并矫正错误：  
    直接修改左侧列表里的值即可。
    ![](./picture/jTess.png)
    *   训练：
    ```
    tesseract  d.normal.exp1.tif d.normal.exp1  nobatch box.train

    unicharset_extractor d.normal.exp1.box  
    ```
    *   新建font_properties文件，输入normal 0 0 0 0 0表示默认普通
    *   继续输入：
    ```
    mftraining -F font_properties -U unicharset -O d.unicharset d.normal.exp1.tr

    cntraining.exe d.normal.exp1.tr 
    ```
    *   此时有很多新生成的文件，把这些文件最前面加上前缀：d，再执行以下命令：
    ```
    combine_tessdata d.
    ```
    *   即可得到训练好的字库：d.traineddata。将该字库移入Linux环境下tessdata里，修改test.py里使用的language即可使用自己训练的字库了。  

为了避免每次训练输入太多重复的代码，写了一个bat脚本：
```
    rem 执行改批处理前先要目录下创建font_properties文件  

    echo Run Tesseract for Training..  
    tesseract  d.normal.exp1.tif d.normal.exp1  nobatch box.train
    
    echo Compute the Character Set..  
    unicharset_extractor d.normal.exp1.box  
    mftraining -F font_properties -U unicharset -O d.unicharset d.normal.exp1.tr  
    
    echo Clustering..  
    cntraining.exe d.normal.exp1.tr  
    
    echo Rename Files..  
    rename normproto d.normproto  
    rename inttemp d.inttemp  
    rename pffmtable d.pffmtable  
    rename shapetable d.shapetable   
    
    echo Create Tessdata..  
    combine_tessdata d.  

    echo Delete useless file
    del unicharset,d.unicharset,d.shapetable,d.pffmtable,d.normproto,d.normal.exp0.tr,d.inttemp
```
*   使用自定义字库效果：  
Source:  
![](./picture/2s.png)                         
Output：  
![](picture/2o.png)  
很容易发现该识别并不是完美的，一方面是字符集的精度不够，另一方面是对图像的处理存在缺陷，从官方文档里可知，tesseract对在方框里面的字符识别能力较差，这一点待改进

