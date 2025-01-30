Movie Dataset Analysis

This project performs Exploratory Data Analysis (EDA) on a movie dataset using Pandas, Seaborn, Matplotlib, and WordCloud to generate various visualizations and insights.

Features & Visualizations

1. Top 10 Movies by Popularity (Bar Chart)


2. Popularity vs Vote Average (Scatter Plot)


3. Correlation Heatmap


4. Proportion of Movies by Language (Pie Chart)


5. Popularity Trend Over Years (Line Plot)


6. Distribution of Vote Averages (Histogram)


7. Vote Average by Language (Box Plot)


8. Word Cloud of Movie Overviews



Dataset

The dataset should be a CSV file (your_dataset.csv) containing columns such as:

title (Movie Title)

popularity (Popularity Score)

vote_average (Average Rating)

vote_count (Total Votes)

release_date (Release Date)

original_language (Movie Language)

overview (Movie Description)



Installation & Usage

1. Clone the Repository

git clone https://github.com/rahilmulani025/Movie-analysis.git
cd movie-analysis

2. Install Dependencies

Ensure you have Python installed. Install required libraries:

pip install pandas matplotlib seaborn wordcloud

3. Run the Script

Place your dataset (your_dataset.csv) in the project folder and execute:

python eda_movie_analysis.py

Example Visualizations

Bar Chart: Top 10 most popular movies

Heatmap: Shows correlation between popularity, votes, and rating

Word Cloud: Highlights frequently used words in movie overviews


License

This project is open-source and free to use.
