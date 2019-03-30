import pandas as pd

''' 1.创建DataFrame数据结构'''
data = {'Chinese': [66, 95, 93, 90, 80, 80],
        'English': [65, 85, 92, 88, 90, 90],
        'Math': [None, 98, 96, 77, 90, 90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'])
# print(df)

''' 2.去除重复行'''
df = df.drop_duplicates()
# print(df)

''' 3.列名重新排序'''
cols = ['English','Chinese', 'Math']
df = df.filter(cols, axis=1)
# print(df)

''' 4.列名重命名'''
df.rename(columns={'Chinese': '语文', 'English': '英语', 'Math': '数学'}, inplace=True)
# print(df)

def total_score(df):
	df['总分'] = df['语文'] + df['英语'] + df['数学']
	return df

''' 5.求成绩的和,使用apply方法'''
df = df.apply(total_score, axis=1)
# 或者可以用这个方法求和
# df['总分'] = df['语文'] + df['英语'] + df['数学']

''' 6.按照总分排序，从高到低，此时有缺失值'''
df.sort_values(['总分'], ascending=[False], inplace=True)
print(df)

''' 7.打印显示成绩单信息，张飞有空值, sum()对boolean可取和，axis=0压缩到行上，axis=1压缩至列上'''
print(df.isnull().sum(axis=1))
print(df.describe())
print(df)

''' 8.使用数学成绩均值填充张飞同学的 缺失值 '''
df['数学'].fillna(df['数学'].mean(), inplace=True)
# 再次求成绩的和并打印显示成绩单情况
df = df.apply(total_score, axis=1)
# df['Total'] = df.sum(axis=1)
print(df.isnull().sum())
print(df.describe())
print(df)