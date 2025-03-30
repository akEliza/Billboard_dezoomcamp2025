import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 数据
data = {
    'Feature': ['Lyrics Sentiment', 'TikTok Virality', 'Danceability', 'Acousticness', 'Energy'],
    'Correlation with Streams': [0.01334, -0.00691, 0.01000, -0.01161, 0.01270]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 创建热力图
# 创建热力图，不显示具体数字
plt.figure(figsize=(8, 4))
sns.heatmap(df.set_index('Feature').T, annot=False, cmap='coolwarm', center=0)
plt.title('Correlation of Music Features with Streams')
plt.show()

