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
> 
> 并且通过调用生成词云的函数generate_pic时导入相关数据的方法
> 同时在其中调用OpenCV-python库所提供的图像处理方法，
> 实现由不完全符合wordcloud中的mask所规定的np.array的空数组的图像，
> 能编程符合要求的图像
> 
> 同时生成词云

1. 在导入的时候跳过所有有省份的词条，将余下的信息放入frequency
2. 国际方面
   1. 在对于中国数据进行加总之后放入世界frequency中
   2. 对于工作簿进行遍历，在此基础上遍历其中的所有国家信息

## 中国疫情地图的实现 [ 基本照抄bilibili,仅进行学习 ]

### data_more.py
> 主要工程文件，其中import了MapDraw.py and dataGet.py
>
> 主要操作在于爬取数据，并且对于结果进行处理，然后再进行画图
> 
> 在一开始，导入dataGet.py 中的GetData文件，将数据进行分类之后导入MapDraw.py模块进行画图

### MapDraw.py [在data_more.py中被调用]
> 通过网站https://gallery.pyecharts.org/#/Map/map_visualmap_piecewise
> 中提供的方法，实现数据的可视化呈现


### dataGet.py [在data_more.py中被调用]
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

### Jan.py 等一系列文件【已经删除，曾经存在过】
> 逐步打开对应文件夹中的所有文件，并且生成符合pyechart框架所需求的数据结构格式，
> 也就是一个列表包含多个字典，每个字典中包含有一个province：州名，和一个value：confirmed人数的键值对
> 然后保存在json文件中

### GetDataFromCSVToDataStructure.py
> 读取我们人工分拣出的csv文件，并且转化成为我们所使用的可视化框架pyecharts所对应的数据结构
> 并且输出到json文件格式。

### DrawUsaMap.py
> 读取json文件中所包含的数据，并且通过调用pyecharts来实现对应的画图功能
> 其中另外一个部分实现了将输入数据进行简单的改造以将左侧的bar更变成为有一定顺序的。
> 
> 

## 其他文件说明
1. add.zip
   
   包含我们在GetDataFromCSVToDataStructure.py中所需求的，人工分拣出的csv格式文件
2. 881259.png
   opencv 的导入文件
3. 5237843.jpg
   opencv 无法使用时所提供的替代笼罩图片
4. html.txt 爬取网页的中途文件
5. Data.json美国疫情地图传输中的零时文件
6. HGKT_CNKI.TTF 词云所使用的字体文件

### **Reference:**
1. https://www.bilibili.com/video/BV1X54y1R7cu?from=search&seid=17433072440613079399&spm_id_from=333.337.0.0
2. https://pyecharts.org/#/zh-cn/intro
3. https://gallery.pyecharts.org/#/README
4. https://gallery.pyecharts.org/#/Map/china_gdp_from_1993_to_2018
5. https://github.com/amueller/word_cloud/blob/master/examples/masked.py
6. https://github.com/pyecharts/pyecharts/issues/1372
7. https://blog.csdn.net/heyuexianzi/article/details/76851377

### 特别鸣谢:
   微信 pyecharts畅谈群 中 ”喝水提醒小助手“ 对我们理解pyecharts库所作出的贡献
   
*注意：本文中使用的pyecharts版本为1.3.1,亲测1.9版本运行会报错*
*注意：本文运行在python3.7环境中*

# **配置文件如下：[请阅读markdown源代码]**
packages in environment at D:\anaconda3\envs\DataAnalyse:

Name                      Version                   Build  Channel
anyio                     2.2.0            py37haa95532_2
argcomplete               1.12.3             pyhd3eb1b0_0
argon2-cffi               20.1.0           py37h2bbff1b_1
async_generator           1.10             py37h28b3542_0
attrs                     21.2.0             pyhd3eb1b0_0
babel                     2.9.1              pyhd3eb1b0_0
backcall                  0.2.0              pyhd3eb1b0_0
blas                      1.0                         mkl
bleach                    4.0.0              pyhd3eb1b0_0
bottleneck                1.3.2            py37h2a96729_1
brotli                    1.0.9                ha925a31_2
brotlipy                  0.7.0           py37h2bbff1b_1003
ca-certificates           2021.10.26           haa95532_2
certifi                   2021.10.8        py37haa95532_0
cffi                      1.15.0           py37h2bbff1b_0
charset-normalizer        2.0.4              pyhd3eb1b0_0
colorama                  0.4.4              pyhd3eb1b0_0
cryptography              35.0.0           py37h71e12ea_0
cycler                    0.11.0             pyhd3eb1b0_0
debugpy                   1.5.1            py37hd77b12b_0
decorator                 5.1.0              pyhd3eb1b0_0
defusedxml                0.7.1              pyhd3eb1b0_0
entrypoints               0.3                      py37_0
et_xmlfile                1.1.0            py37haa95532_0
fonttools                 4.28.3                   pypi_0    pypi
freetype                  2.10.4               hd328e21_0
hdf5                      1.8.20               hac2f561_1
icc_rt                    2019.0.0             h0cc432a_1
icu                       58.2                 ha925a31_3
idna                      3.3                pyhd3eb1b0_0
importlib-metadata        4.8.2            py37haa95532_0
importlib_metadata        4.8.2                hd3eb1b0_0
intel-openmp              2021.4.0          haa95532_3556
ipykernel                 6.4.1            py37haa95532_1
ipython                   7.29.0           py37hd4e2768_0
ipython_genutils          0.2.0              pyhd3eb1b0_1
jedi                      0.18.0           py37haa95532_1
jinja2                    3.0.3                    pypi_0    pypi
jpeg                      9d                   h2bbff1b_0
json5                     0.9.6              pyhd3eb1b0_0
jsonschema                3.2.0              pyhd3eb1b0_2
jupyter_client            7.0.6              pyhd3eb1b0_0
jupyter_core              4.9.1            py37haa95532_0
jupyter_server            1.4.1            py37haa95532_0
jupyterlab                3.2.1              pyhd3eb1b0_1
jupyterlab_pygments       0.1.2                      py_0
jupyterlab_server         2.8.2              pyhd3eb1b0_0
kiwisolver                1.3.2                    pypi_0    pypi
libiconv                  1.15                 h1df5818_7
libopencv                 3.4.2                h20b85fd_0
libpng                    1.6.37               h2a8f88b_0
libtiff                   4.2.0                hd0e1b90_0
libwebp                   1.2.0                h2bbff1b_0
libxml2                   2.9.12               h0ad7f3c_0
libxslt                   1.1.34               he774522_0
lxml                      4.6.3            py37h9b66d53_0
lz4-c                     1.9.3                h2bbff1b_1
m2w64-gcc-libgfortran     5.3.0                         6
m2w64-gcc-libs            5.3.0                         7
m2w64-gcc-libs-core       5.3.0                         7
m2w64-gmp                 6.1.0                         2
m2w64-libwinpthread-git   5.0.0.4634.697f757               2
markupsafe                2.0.1            py37h2bbff1b_0
matplotlib                3.5.0            py37haa95532_0
matplotlib-base           3.5.0            py37h6214cd6_0
matplotlib-inline         0.1.2              pyhd3eb1b0_2
mistune                   0.8.4           py37hfa6e2cd_1001
mkl                       2021.4.0           haa95532_640
mkl-service               2.4.0            py37h2bbff1b_0
mkl_fft                   1.3.1            py37h277e83a_0
mkl_random                1.2.2            py37hf11a4ad_0
msys2-conda-epoch         20160418                      1
munkres                   1.1.4                      py_0
nbclassic                 0.2.6              pyhd3eb1b0_0
nbclient                  0.5.3              pyhd3eb1b0_0
nbconvert                 6.1.0            py37haa95532_0
nbformat                  5.1.3              pyhd3eb1b0_0
nest-asyncio              1.5.1              pyhd3eb1b0_0
notebook                  6.4.6            py37haa95532_0
numexpr                   2.7.3            py37hb80d3ca_1
numpy                     1.21.4                   pypi_0    pypi
numpy-base                1.21.2           py37h0829f74_0
olefile                   0.46                     py37_0
opencv                    3.4.2            py37h40b0b35_0
openpyxl                  3.0.9              pyhd3eb1b0_0
openssl                   1.1.1l               h2bbff1b_0
packaging                 21.3               pyhd3eb1b0_0
pandas                    1.3.4            py37h6214cd6_0
pandocfilters             1.4.3            py37haa95532_1
parso                     0.8.2              pyhd3eb1b0_0
pickleshare               0.7.5           pyhd3eb1b0_1003
pillow                    8.4.0                    pypi_0    pypi
pip                       21.3.1                   pypi_0    pypi
prettytable               2.4.0                    pypi_0    pypi
prometheus_client         0.12.0             pyhd3eb1b0_0
prompt-toolkit            3.0.20             pyhd3eb1b0_0
py-opencv                 3.4.2            py37hc319ecb_0
pycparser                 2.21               pyhd3eb1b0_0
pyecharts                 1.3.1                    pypi_0    pypi
pygments                  2.10.0             pyhd3eb1b0_0
pyopenssl                 21.0.0             pyhd3eb1b0_1
pyparsing                 3.0.6                    pypi_0    pypi
pyqt                      5.9.2            py37h6538335_2
pyrsistent                0.18.0           py37h196d8e1_0
pysocks                   1.7.1                    py37_1
python                    3.7.11               h6244533_0
python-dateutil           2.8.2              pyhd3eb1b0_0
pytz                      2021.3             pyhd3eb1b0_0
pywin32                   228              py37hbaba5e8_1
pywinpty                  0.5.7                    py37_0
pyzmq                     22.3.0           py37hd77b12b_2
qt                        5.9.7            vc14h73c81de_0
requests                  2.26.0             pyhd3eb1b0_0
send2trash                1.8.0              pyhd3eb1b0_1
setuptools                59.5.0                   pypi_0    pypi
setuptools-scm            6.3.2                    pypi_0    pypi
simplejson                3.17.6                   pypi_0    pypi
sip                       4.19.8           py37h6538335_0
six                       1.16.0             pyhd3eb1b0_0
sniffio                   1.2.0            py37haa95532_1
sqlite                    3.36.0               h2bbff1b_0
terminado                 0.9.4            py37haa95532_0
testpath                  0.5.0              pyhd3eb1b0_0
tk                        8.6.11               h2bbff1b_0
tomli                     1.2.2                    pypi_0    pypi
tornado                   6.1              py37h2bbff1b_0
traitlets                 5.1.1              pyhd3eb1b0_0
typing-extensions         4.0.1                    pypi_0    pypi
typing_extensions         3.10.0.2           pyh06a4308_0
urllib3                   1.26.7             pyhd3eb1b0_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
wcwidth                   0.2.5              pyhd3eb1b0_0
webencodings              0.5.1                    py37_1
wheel                     0.37.0             pyhd3eb1b0_1
win_inet_pton             1.1.0            py37haa95532_0
wincertstore              0.2              py37haa95532_2
winpty                    0.4.3                         4
wordcloud                 1.8.1                    pypi_0    pypi
xz                        5.2.5                h62dcd97_0
zipp                      3.6.0              pyhd3eb1b0_0
zlib                      1.2.11               h62dcd97_4
zstd                      1.4.9                h19a0ad4_0