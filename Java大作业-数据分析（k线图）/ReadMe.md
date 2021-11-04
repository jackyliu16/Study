### 使用操作说明
*注意：为了防止乱码，因此，我文本中所做的所有注释都是以英语形式写的，但是由于我扣脚的英语水平，只是达到勉强*
*能看的水平，因此大幅度的采用了翻译的操作(因此有可能有点理解问题，敬请理解)*

本作业包含多个模块的内容：

其中可以**完美完成所有需求的为Main.java文件** 
> 在使用java文件的时候需要注意，在同目录下方必须存在子目录data，于其中存放需要进行绘图操作的csv格式的数据

### 作业需求
Task: Draw Yearly Candlestick Charts from Daily Prices
> Draw yearly candlestick charts from daily prices in the two .csv files (HSI.csv and IXIC.csv) in the attached data.zip.
> Note the data in the .csv files are daily open, high, low and close prices and should be converted to yearly open, high, low and close prices before plotting.
> Yearly prices are calculated from daily prices in the following way.
> The open price of a period (e.g. a year) is the first open in the period.
> The high price of a period is the highest high in the period.
> The low price of a period is the lowest low in the period.
> The close price of a period is the last close in the period.
> Note the recent year starts today till one year earlier. For example, the recent one year is from 2020-10-16 to 2021-10-15 if today is 2021-10-15.
> Note there may be invalid values (null) in the .csv files. Manually editing the .csv files are not allowed.
> Below is a screenshot of null values in HSI.csv

### 附件说明
Apple.java
>	主要对于**数据切片功能以及数据分析功能**进行**测试**
> 	起到的主要作用是通过切片以及分析功能，得到在各个年份的top, bottom, high, low
> 	四组数据所组成的Double[][]数组

Banana.java
> 	是在Apple.java文件创建过程中对于compare的这个模块进行**测试**而产生的临时文件

Cat.java
> 	对于Draw模块进行测试（测试边框以及x的取值范围等）

Dog.java
> 	类似与Apple.java
> 	但是我已经忘记我为啥要搞这个东西了
> 	好吧，是修正[sp,sp+1) 为(sp,sp+1] 专用的副本文件

candle.java
> 	上课的时候抄的一部分有关于K线图实现的代码(虽然基本没有用到)

IOTest.java
> 	在整合各个模块之前的Main.java文件

HSI.csv:
>	There should be 35 candlesticks representing the yearly open, high, low, close prices of 35 years from 1986-12-31 to 2021-10-15.
>	For example, if today is 2021-10-15, the recent one year is from 2020-10-16 to 2021-10-15, and is represented by the last (rightmost) candlestick in the following chart for HSI.csv.
> 	The first year in HSI.csv is from 1986-12-31 to 1987-10-15, and is represented by the first (leftmost) candlestick in the following chart for HSI.csv.

IXIC.csv:
> 	There should be 51 candlesticks representing the yearly open, high, low, close prices of 51 years from 1971-02-05 to 2021-10-15.
>	For example, if today is 2021-10-15, the recent one year is from 2020-10-16 to 2021-10-15, and is represented by the last (rightmost) candlestick in the following chart for IXIC.csv.
>	The first year in IXIC.csv is from 1971-02-05 to 1971-10-15, and is represented by the first (leftmost) candlestick in the following chart for IXIC.csv.