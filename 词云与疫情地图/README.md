# 文件的定义

## 词云功能的实现
### getData.py
> 从网上爬取对应数据并且进行基础处理
> 最终将网页上的数据整理并且分类放置到xlsx中
1. 通过requests.get爬取网页源代码
2. 通过lxml中的xpath对于html文件进行解析
   1. 在数据的粗处理中通过json将string数据转化成为dict数据
3. 通过openpyxl [Excel模块] 导出数据
    其中牵涉到在2中所产生的字典文件[*在网站源代码中*]
### word_cloud.py
> 对于getData.py中所生成的文件进行分析
> 同时生成词云

1. 在导入的时候跳过所有有省份的词条，将余下的信息放入frequency
2. 国际方面
   1. 在对于中国数据进行加总之后放入世界frequency中
   2. 对于工作簿进行遍历，在此基础上遍历其中的所有国家信息

## 中国疫情地图的实现

### data_more.py
> 主要工程文件，其中import了MapDraw.py and dataGet.py
>
> 主要操作在于爬取数据，并且对于结果进行处理，然后再进行画图
> 
> 在一开始，导入dataGet.py 中的GetData文件，将数据进行分类之后导入MapDraw.py模块进行画图

### MapDraw.py
> 通过网站https://gallery.pyecharts.org/#/Map/map_visualmap_piecewise
> 中提供的方法，实现数据的可视化呈现


### dataGet.py
> 重新从网上爬取数据，但是不同的是为了在另外一个py文件中进行引用
> 因而被封装到类中
1. getData()

   得到网站源文件，并且写入text文件

2. getTime()
    
    通过正则表达式对于整个网页文件中所出现的特征词汇进行搜索，进而得到对应的下载时间
3. parseData()

    对于数据进行初步预处理，在其中配合使用dump等方法，将数据进行初步处理之后重新写回data.json文件中

## 美国疫情地图的实现

### getProvinceName.py
> 通过打开一个csv文件，读取其中的所有省份并且放入Province_State列表

### Jan.py 等一系列文件
> 逐步打开对应文件夹中的所有文件，并且生成符合pyechart框架所需求的数据结构格式，
> 也就是一个列表包含多个字典，每个字典中包含有一个province：州名，和一个value：confirmed人数的键值对
> 然后保存在json文件中