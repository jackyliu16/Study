"""
Author： 刘逸珑
Time：   2021/12/8 21:09
"""
import openpyxl
from wordcloud import WordCloud # 不知道为什么在3.9中会出现安装失败

def generate_pic(frequency,filename):
    wordcloud = WordCloud(font_path="C:\Windows\Fonts\HGKT_CNKI.TTF",
                          background_color="white",
                          width=1920, height=1080)
    # 生成词云
    wordcloud.generate_from_frequencies(frequency)
    # 保存词云
    wordcloud.to_file("{}.png".format(filename))

# Read Data
wb = openpyxl.load_workbook('../data.xlsx')
# 获取工作表
ws = wb['国内疫情']
frequencyIn = {}
for row in ws.values:
    if row[0] == "省份":
        pass
    else:
        frequencyIn[row[0]] = float(row[1])      # 生成一个以省份为key，确诊人数为value的字典

generate_pic(frequencyIn, "国内疫情词云")



frequencyOut = {}
# 加入中国确诊人数
ChinaAccount = 0
for key,value in frequencyIn.items():
    ChinaAccount += float(value)
frequencyOut['中国'] = ChinaAccount

# wb.sheetnames = 工作表名称
sheet_name = wb.sheetnames
for each_sheet in sheet_name:     # 由于不同洲的数据被保存在不同的工作簿中，因此需要先对于工作表进行遍历
    if "洲" in each_sheet:
        ws = wb[each_sheet]
        for row in ws.values:
            if row[0] == "国家":
                pass
            else:
                frequencyOut[row[0]] = float(row[1])

generate_pic(frequencyOut,"世界疫情词云")
