I chose to do analysis of the trends of user and critic scores on Rotten Tomatoes because I was interested to see if there was any relationships between genre or box office scores that would influence critics vs audiences. I collected this data myself from webscraping, and I specifically chose to use code from this page: "https://editorial.rottentomatoes.com/guide/oscars-best-and-worst-best-pictures/" because web scraping the whole website was taking too long. Help for this project comes from Stackoverflow, the professor, and my brother. The three questions I had going into this were: Does genre have an influence on whether or not something is an outlier, how do critic scores compare to audience scores, and how does the box office score influence ratings. I used a new type of data visualization that allows you to point to specific parts of the graph and get data off of those points, mostly for user scores which I learned from Stackoverflow. I needed this for researching the aformentioned outliers. Note that box office is in the millions. 

### Critics vs Audience Scores
<iframe src="fig1.html" width="100%" height="600"></iframe>

Critics vs Audience Scores was the first graph I made, and served as a 'baseline' to analyse the rest of the graphs. Nothing really stood out to me except some small outliers that seemed to all be Romance movies.

### Genre Analysis
<iframe src="fig2.html" width="100%" height="600"></iframe>

Critic Scores By Genre was where I saw most outliers, and I was suprised by the fact that Drama actually had more outliers than Romance did. Though it is not the only one, those two genres seem to be correlated with low score outliers.

### Rating Analysis
<iframe src="fig3.html" width="100%" height="600"></iframe>

Audience Scores by Rating was made when I got curious if there was an easier way to categorize that didn't involve as many categories unlike when sorting by genre. Unfortunately many of the movies I looked at were not rated because they were so old, so it was less helpful then I wanted.

### Critics vs Audience Avg
<iframe src="fig4.html" width="100%" height="600"></iframe>

Critic Avg vs Audience Avg was made to get a better look at critics vs audience without using the percentage system. Audiences tend to rate movies higher than critics do on average, but critics have a more even distribution of scores across the graph.

### Box Office Distribution
<iframe src="fig5.html" width="100%" height="600"></iframe>

Box Office Distribution is the simplest graph but I wanted a comparison across all movies. I was suprised by how little most movies made, I was expecting it to be more evenly distributed instead of skewed so far. Box office score doesn't really seem to have any correlation to scores, which suprised me.

# Week 9 Learning Log

### Rotten Tomatoes
How closely do critic scores align with audience scores? Are there genres where they diverge significantly?
Has the average movie rating trend changed over time (ex. are critics becoming harsher or more generous)?

### Sleep Habits
How do sleep habits change between high school and college?
Does having a job in high school have a noticeable effect on sleep, and how does it compare to college?

### SorrelsSouls
Of her shorts, which kinds of sculptures tend to be the most popular? Are there any trends?
How does her long form content compare to her short form content?

### Week 10 Update

I will be doing this project on my own. I will be working with Rotten Tomatoes to research into the questions listed above in the week 9 learning log. Specifically I would be working with critic and audience scores, which are easy to find but do not have a repository specific to them, so I would likely have to use some kind of web scraper to get what I need. I would like to cover how closely critic scores align with audience scores, if there are genres where they diverge significantly, and how the average movie rating trend has changed over time.

### Project Update Week 11

I have decided to work with the rotten tomatoes dataset. I have been able to retrieve some data from web scraping but I will need more time with the code to make sense of it as it does not yet have any identifiers like which genre which score came from. I am purely working with numbers, so a lot of the context from written reviews is left out of the data. I have learned that it appears audience scores tend to be higher, but I did not get much as I am still working with the code. This data is not an API so I have to be careful with how I use it.

### Week 12 Update

I cannot figure out how to embed plotly into the github repository, however I have created some plot code listed in testcode.py. So far I have seen basic linear trends in my scatterplots, but there are some outliers I would like to look more into. Most of my struggles so far are still with code wrangling.

### Week 14 Update

Finally got the graphs into the repository. I've gotten some written analysis down in a google doc though it's not done yet. I am either going to make some kind of regression line or alter a graph to include a different kind of cluster. I am likely going to do a regression line as that has some in-class examples I can learn from. I'm planning to use slides to present but if possible I'd like to get the analysis into the project web page so I can work from there.
