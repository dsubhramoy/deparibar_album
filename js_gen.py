import pandas as pd
cate1 = pd.read_excel("master_database.xlsx",sheet_name="cate")

videos = pd.read_excel("master_database.xlsx",sheet_name="videos")
videos = videos.sort_values(by=['category','description'])

cate_line = 'let category = \'{\"cate\":[\'+\n'
    
for index, row in cate1.iterrows():
    cate_line += '\'{' +f'\"clr\":\"rgb(255, 1, 90)\",\"description\":  \"{row["description"]} \", \"link\":\"{row["link"]}\",\"image\":\"{row["image"]}\"' +'},\'+\n'
cate_line= cate_line[:-4]+ ']}\''  
vid_line = 'let videos = \'{\"vid\":[\'+\n'

for index, row in videos.iterrows():
    vid_line += '\'{' +f'\"cat\":\"{row["category"]}\",\"description\":  \"{row["description"]} \", \"link\":\"{row["link"]}\",\"image\":\"{row["image"]}\"' +'},\'+\n'
vid_line= vid_line[:-4]+ ']}\''  

fp = open('data.js','w')
fp.write(vid_line)
fp.write('\n\n')
fp.write(cate_line)
fp.close()