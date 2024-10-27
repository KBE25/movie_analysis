<img src="image/film1.jpg">

[Credit: college.unc.edu](https://college.unc.edu/2020/05/take-a-film-adventure/)

# Movie Success Analysis 

**Author: <a href="https://www.linkedin.com/in/karina-basto-eyzaguirre-203a0445/"> Karina Basto-Eyzaguirre</a>**

## Business Understanding
This analysis has been conducted as my company has decided to create a new movie studio and I have the goal to provide insights that will guide my stakeholders to inform the studio's decision on its first production. To support this I will analyze movie data to identify trends in successful films. I will focus on ROI and profit, examining factors like release month, genre, studio, and key personnel. 

## Data Understanding
To analyze movie performance, I used a mix of datasets (CSV files and SQL databases) from four sources: 
- <a href="https://www.boxofficemojo.com/">Box Office Mojo:</a> This dataset contains information 3,387 lines of data related to movies, studios, domestic gross revenue, foreign gross revenue and release year. From this dataset I used the studio information to determine the studios that are associated with movies with the highest ROI.
- <a href="https://www.imdb.com/">IMDB:</a> This is a database from containing 8 tables with comprehensive data about movies, directors, actors, actresses and writers. From this database I leveraged 4 tables: movie_basics, movie_ratings, principals and persons to determine the key people in a movie that and movie gender that will return the highest ROI. I also leverage the information from movies to determine the release month with highest profit. The main table movie_basics contains 146,144 lines of movie information.
- <a href="https://www.themoviedb.org/">The Movie:</a> This is a dataset with 26,517 lines of information on popularity and rating. I leveraged the popularity information from this dataset to understadn the relationship between popularity and ROI.
- <a href="https://www.the-numbers.com/">The Numbers:</a> This is a dataset with 5,782 lines of information on domestic and international gross revenue. The finantial information from this table was the one that I leveraged for all the profit and ROI analysis.

The mix of datasets contains information between 1946 and 2019. All this data provides insights into studio performance, key personnel, genre popularity, release timing, and financial metrics like ROI and profit. By analyzing these factors, I aim to identify key trends and inform strategic decisions for the new movie studio.

## Data Preparation
Before I started the data cleaning, I did initial checks on the notebook <a href="https://github.com/KBE25/movie_analysis/blob/main/Datasets_analysis.ipynb">Data_analysis</a>. This initial step allow me to decide which databses to use for the analysis.

To complete most of the cleaning I leverager a <a href="https://github.com/KBE25/movie_analysis/blob/main/helper.py"> helper.py file </a> to be able to complete the following steps:
- Removing Duplicates
- Cleaning columns: removing and renaming relevant columns
- Create a new_genre column
- Removing Outliers
- Complete Feature Engineering to calculate ROI, Profit and do final cleaning.

After I made all the cleanings and preparations, I merged different tables to be able to have merged dataset to conclude my analysis.

## Exploratory Data Analysis
Exploratory data analysis was conducted by using Domestic and International ROI and Profit to determine the following:
- Domestic and International Profit per Release Month
- Domestic and International ROI per Movie Production Studio
- Domestic and International ROI per Movie Genre
- Compare Popularity and ROI per Movie Genre
- Domestic and International ROI per Director, Actor, Actress and Writer.

## Conclusions
***Movie Profit Per Release Month***
Key Months to release movies are June with an average domestic profit of \$18.58\$M while the average international profit is \$104.87\$M. Also, November with an average domestic profit is \$14.21\$M while the average international profit is \$104.49\$M.

***ROI per Movie Production Studio***

The Top Movie Production studios to consider based on Highest ROI are the following:
- <a href="https://www.fd1.com/">FD Productions</a> with an average Domestic ROI of 5.24 and an average International ROI of 10.32. 
- <a href="https://www.blumhouse.com/films">BH Tilt division from Blumhouse</a> with an average Domestic ROI of 3.74 and an average International ROI of 6.89.
  
***ROI per Movie Genre***

Based on our analysis, the key Movie Genres to focus on are the following:
- Musical with an average Domestic ROI of 6.79 and an average International ROI of 22.25.
- Horror with an average Domestic ROI of 5.19 and an average International ROI of 10.71.
- Animation with an average Domestic ROI of 5.40 and an average International ROI of 9.69.

***ROI vs Popularity per Movie Genre***

- Based on average Domestic ROI and Popularity, both Musical and Horror have the highest ratings.
- Based on average International ROI and Popularity, both Musical and Horror have the highest average ROI. However when it comes to popularity, Musical also has the highest score but horror does not

***ROI per Director, Actor, Actress and Writer***

Based on the highest average Domestic and International ROI, the best Directors, Actors, Actresses and Writers to partner with in order to produce a succesful movie:
- The Directors to partner with are Levan Gabriadze, Tod Williams and Jamie Brucker.
- The Actors to partner with are Ionut Grama, Simon Quarterman and James Jude Courtney.
- The Actresses to partner with are Fernanda Andrade, Andi Matichak, Courtney Halverson and Heather Sossaman.
- The Writers to partner with are Matthew Peterman, Jeff Fradley and Leigh Whannel.

When assessing the combined number of movies of the top 15 Directors, Actors, Actresses and Writers with highest average ROI, I determine that the most popular Movie Genre is Horror.

## Recommendations
Based on the above analysis my recommendations are the following:

1. Focus on Horror or related Movie Genres due to its high ROI and potential for low-budget, high-impact films.
   
2. Invest in partnering with High ROI Talent (Directors, Writers, Actors and Actresses) in the Horror Movie Genre

3. Focus on releasing movies on key months such as a June and November as historically are the most with the highest average Domestic and International Profit.

#### Limitations of the analysis
1. Dataset limitations due to merging reduced the number of movies analyzed.
2. Simplifying genre categorization might have misclassified some movies.
3. The analysis focuses on a limited set of factors, potentially overlooking other influential variables.
   
## For More Information:
See the full analysis in the <a href="https://github.com/KBE25/movie_analysis/blob/main/final_notebook.ipynb">Jupyter Notebook</a>.
The business information can also be found in <a href="">this presentation. </a>

For additional info, contact Karina Basto-Eyzaguirre at karinabastoe@gmail.com.

### Repository Structure
- <a href="https://github.com/KBE25/movie_analysis/blob/main/.gitignore"> .gitignore </a>
- <a href="https://github.com/KBE25/movie_analysis/blob/main/Datasets_analysis.ipynb"> Datasets_analysis.ipynb </a>
- <a href="https://github.com/KBE25/movie_analysis/blob/main/README.md"> README.md </a>
- <a href="https://github.com/KBE25/movie_analysis/blob/main/final_notebook.ipynb"> final_notebook.ipynb </a>
- <a href="https://github.com/KBE25/movie_analysis/blob/main/helper.py"> helper.py </a>
- <a href=""> presentation </a>

### Resources
- <a href="https://www.fd1.com/">FD Productions</a>
- <a href="https://www.blumhouse.com/films">BH Tilt division from Blumhouse</a>
- <a href="https://d-nb.info/1234464950/34#:~:text=Film%20popularity%20is%20an%20important,to%20direct%20and%20satisfy%20them."> Measuring Film Popularity</a>
- <a href="https://hbr.org/2021/10/the-psychology-behind-why-we-love-or-hate-horror#:~:text=For%20instance%2C%20watching%20a%20horror,parts%20of%20the%20human%20condition."> The Psychology Behind why we love or hate horror by Harvard Business Review</a>
- <a href="https://americanfilmmarket.com/what-the-data-says-producing-low-budget-horror-films/"> What the data says: Producing low budget Horror Filsm by American Film Market</a>