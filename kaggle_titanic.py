

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# csv 파일 불러오기
df_train = pd.read_csv('input/train.csv')
df_test = pd.read_csv('input/test.csv')
df_gender_submission = pd.read_csv('input/gender_submission.csv')

print(df_train.head())
print("-" * 100)
print(df_test.head())
print("-" * 100)
print(df_gender_submission.head())
print("-" * 100)

# 데이터 정보 살펴보기
print(df_train.info())
print("-" * 100)
print(df_test.info())

"""### train 결손값 Age, Cabin, Embarked 해당

### test도 결손값 동일
"""