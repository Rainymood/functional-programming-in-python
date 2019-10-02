import pandas as pd

df = pd.DataFrame({'col1':[1,2,3], 'col2':[10, 20, 30]})
#    col1  col2
# 0     1    10
# 1     2    20
# 2     3    30

df['col3'] = list(map(lambda x: x * 2, df['col2']))
#    col1  col2  col3
# 0     1    10    20
# 1     2    20    40
# 2     3    30    60