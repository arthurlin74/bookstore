import numpy as np
import pandas as pd
a = pd.read_csv('test1_data.csv', encoding="utf8", delimiter=',',dtype=str)
print(a)
df = pd.DataFrame(a)

df.replace('�K',0,inplace=True)
df.replace('�X',0,inplace=True)
print('���N�L�ĭ�-----------------')
print(df)

df2 = df.drop(columns=['�~��','�g�`���~��-�k/�k','�M�~�H��-�k/�k','�޳N���ΧU�z�M�~�H��-�k/�k','�ưȤ䴩�H��-�k/�k',
                       '�A�ȤξP��u�@�H��-�k/�k','����_����]�ƾާ@�βոˤH��-�k/�k','��h�޳N�u�γҤO�u-�k/�k'], )
print('�R���C---------------------')
print(df2)

z = {'�g�`���~��-�~��': '�g�`��',
'�M�~�H��-�~��': '�M�~�H��',
'�޳N���ΧU�z�M�~�H��-�~��': '�޳N���ΧU�z',
'�ưȤ䴩�H��-�~��': '�ưȤH��',
'�A�ȤξP��u�@�H��-�~��': '�A�ȾP��',
'����_����]�ƾާ@�βոˤH��-�~��': '����]�ƾާ@',
'��h�޳N�u�γҤO�u-�~��': '��h�ҤO'}

print('��W--------------')
df2.rename(columns=z)
