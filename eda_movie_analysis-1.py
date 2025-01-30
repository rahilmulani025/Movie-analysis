import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset
df = pd.read_csv("your_dataset.csv")

# Handle missing values
df.dropna(subset=['popularity', 'vote_average', 'vote_count', 'release_date', 'original_language', 'overview'], inplace=True)

# Ensure numeric data types
df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
df['vote_count'] = pd.to_numeric(df['vote_count'], errors='coerce')

# Convert release_date to datetime format
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# 1. Bar Chart: Top 10 movies by popularity
top_movies = df.nlargest(10, 'popularity')
plt.figure(figsize=(10, 6))
sns.barplot(x=top_movies['popularity'], y=top_movies['title'], palette='viridis')
plt.title('Top 10 Movies by Popularity')
plt.xlabel('Popularity')
plt.ylabel('Movie Title')
plt.show()

# 2. Scatter Plot: Popularity vs Vote Average
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='popularity', y='vote_average', alpha=0.6)
plt.title('Popularity vs Vote Average')
plt.xlabel('Popularity')
plt.ylabel('Vote Average')
plt.show()

# 3. Heatmap: Correlation between numerical features
plt.figure(figsize=(10, 6))
correlation = df[['popularity', 'vote_average', 'vote_count']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 4. Pie Chart: Proportion of movies by original language (Top 10 Languages)
top_languages = df['original_language'].value_counts().nlargest(10)
plt.figure(figsize=(8, 8))
top_languages.plot.pie(autopct='%1.1f%%', startangle=140, cmap='Set3')
plt.title('Proportion of Movies by Language (Top 10)')
plt.ylabel('')
plt.show()

# 5. Line Plot: Popularity trend over release date (sorted)
popularity_trend = df.groupby(df['release_date'].dt.year)['popularity'].mean().sort_index()
plt.figure(figsize=(10, 6))
popularity_trend.plot()
plt.title('Average Popularity Trend Over Years')
plt.xlabel('Year')
plt.ylabel('Average Popularity')
plt.grid()
plt.show()

# 6. Histogram: Distribution of vote average
plt.figure(figsize=(8, 6))
sns.histplot(df['vote_average'], bins=20, kde=True, color='blue')
plt.title('Distribution of Vote Average')
plt.xlabel('Vote Average')
plt.ylabel('Frequency')
plt.show()

# 7. Box Plot: Vote Average by Original Language (Filtered for Top 10 Languages)
df_filtered = df[df['original_language'].isin(top_languages.index)]
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_filtered, x='original_language', y='vote_average', palette='Set2')
plt.title('Vote Average by Language (Top 10)')
plt.xlabel('Original Language')
plt.ylabel('Vote Average')
plt.xticks(rotation=45)
plt.show()

# 8. Word Cloud: Most frequent words in overview
text = " ".join(str(overview) for overview in df['overview'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Movie Overviews')
plt.show()
