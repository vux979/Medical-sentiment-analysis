import json
import os
from tqdm import tqdm
import gc
import re
import pandas as pd

s = "./yelp_academic_dataset_business.json"# kaggle 上下载的yelp数据

data_business = []

with open(s, 'r', encoding='UTF-8') as load_f:
    for line in tqdm(load_f):
        data_business.append(json.loads(line))
        
# 找到 categories 中包括 str1 & str2 这两个类的商店
str1 = 'Health & Medical'
str2 = 'Doctors'

business_hmd = []
for i in tqdm(range(len(data_business))):
    if data_business[i]["categories"] != None: # categories 不为空值
        flag = data_business[i]["categories"].rfind(str1) # 找不到 str1 就返回 -1
        if flag != -1:
            flag = data_business[i]["categories"].rfind(str2) # 找不到 str2 就返回 -1
            if flag != -1:
                business_hmd.append(data_business[i])
                
del(data_business) # 清内存，删除列表
gc.collect()

business_hmd_id = []
for element in tqdm(business_hmd):
    business_hmd_id.append(element["business_id"])
len(business_hmd_id)

s = "./yelp_academic_dataset_review.json"
reviews_hmd = []
with open(s, 'r', encoding='UTF-8') as load_f:
  for line in tqdm(load_f):
    line_dict = json.loads(line)
    if line_dict['business_id'] in business_hmd_id:
      reviews_hmd.append(line_dict)
      
pos = []
neg = []
mid = []

def cleanReview(subject):
    newSubject = re.sub(r'\n', '', subject)
    newSubject = re.sub(r"\'", "'", newSubject)
    return newSubject

for element in tqdm(reviews_hmd):
    if element['stars'] >= 4.0:
        pos.append(cleanReview(element['text']))
    elif element['stars'] <=2.0:
        neg.append(cleanReview(element['text']))
    else:
        mid.append(cleanReview(element['text']))

df_pos = pd.DataFrame(columns=['']) # 创建dataframe， 定义一个没有名字的空列
df_neg = pd.DataFrame(columns=[''])
df_mid = pd.DataFrame(columns=[''])

df_pos[''] = pos # 给空列赋值
df_neg[''] = neg
df_mid[''] = mid

# 保存数据
df_pos.to_excel('.\pos.xls', index=False, header=0) # 不保存索引和列名
df_neg.to_excel('.\\neg.xls', index=False, header=0)
df_mid.to_excel('.\\mid.xls', index=False, header=0)

df_pos_30000 = df_pos[:30000]
df_neg_30000 = df_neg[:30000]
df_pos_30000.to_excel('.\pos_30000.xls', index=False, header=0)
df_neg_30000.to_excel('.\\neg_30000.xls', index=False, header=0)
