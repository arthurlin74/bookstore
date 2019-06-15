import numpy as np
import pandas as pd
a = pd.read_csv('test1_data.csv', encoding="utf8", delimiter=',',dtype=str)
print(a)
df = pd.DataFrame(a)

df.replace('…',0,inplace=True)
df.replace('—',0,inplace=True)
print('取代無效值-----------------')
print(df)

df2 = df.drop(columns=['年度','經常性薪資-女/男','專業人員-女/男','技術員及助理專業人員-女/男','事務支援人員-女/男',
                       '服務及銷售工作人員-女/男','技藝_機械設備操作及組裝人員-女/男','基層技術工及勞力工-女/男'], )
print('刪除列---------------------')
print(df2)

z = {'經常性薪資-薪資': '經常性',
'專業人員-薪資': '專業人員',
'技術員及助理專業人員-薪資': '技術員及助理',
'事務支援人員-薪資': '事務人員',
'服務及銷售工作人員-薪資': '服務銷售',
'技藝_機械設備操作及組裝人員-薪資': '機械設備操作',
'基層技術工及勞力工-薪資': '基層勞力'}

print('更名--------------')
df2.rename(columns=z)
