# Clickbait: News Headline Classification
Stack: Pandas | Python | Random Forest  | Tableau | XGBoost

## Objective
Classifying news networks by sensational headline score using Natural Language Processing. In doing so, also determine which news networks have the most clickbait headlines and find out what criteria best determines sensationalism.

## Rationale
Everyone encounters so much information everyday, so I wanted to originally combat news misinformation. However, developing a fact checking algorithm seemed non-feasible so I tackled sensationalized news headlines, or in modern terms - 'clickbait'. Clickbait is described by dictionary.com as "a sensationalized headline...designed to entice people".

## Process
### Collecting Info
![image](https://github.com/seansjj/news_headline_classification/assets/141446128/451ecc27-f2d0-4822-9048-b557cef80fa8)

Using the News API, I gathered headlines from 4 sources to form a baseline. Reports from All Sides, a media bias company served as a guideline in labeling Associated Press (AP), Reuters as Non-Sensational class of 0 and Buzzfeed, Entertaintment Weekly (EW) a sensational class of 1. The news dataset was from Kaggle, which someone used News API to collect data. It featured over 46000 headlines from 29 unique news sources. 

### Cleaning Data
The API data was relatively clean, so not much processing was required. Only simple tasks such as dropping duplicates, simplifying column names, and using a language detection library to remove non-english headlines was required.

### Creating Features
![image](https://github.com/seansjj/news_headline_classification/assets/141446128/3b80e551-8531-4aa8-a257-2866e9e0ce07)

Headlines were pre-processed for language analysis functions by removing the case, punctuation, non-letter characters, stop words, then changing words into their base form. The 6 features then used original or processed headlines including:
- Words in Headline
- Average Word Length: Measures how many letters in each headline word
- Average Key Word Length: Measures how many letters in each processed headline word
- Buzzword Ratio: List of common buzzwords (ex.scandal/shocking) was added to a list of top 20 most common words from buzzfeed, EW
- Unique Ratio: Ratio of unique words to total words in headline
- Uppercase Ratio: Ratio of capitalized words to total words in headline
  
### Visualizing Trends
The following plots were generated to identify patterns and trends for investigation:
- Heatmap to see correlations between both features and sensational class
- Histplots to see value distributions of features
- Boxplots to make note of extreme outliers in any features
- Scatterplot to analyze the headline length, unique ratio relationship

Afterwards, log transformation was applied on skewed distributions noted during the histplots and all features had standard scaling applied.

![image](https://github.com/seansjj/news_headline_classification/assets/141446128/da8b218c-6cf0-434b-b221-c8e72b7c0b2a)

### Evaluating Models
For this classification project, both Random Forest and XGBoost was considered. The model used train/test splits of 80/20 and was evaluated using accuracy, precision, recall via a confusion matrix and a classification report.

### Improving Predictions
Both models used random search first to find the a broad range of viable hyperparameters, then narrowed down the range using grid search.
For Random Forest, the following hyperparameters were investigated:
- Max Depth
- N Estimators
- Max Features
- Min Samples Leaf
- Min Samples Split

While for XGBoost, the following hyperparameters were investigated:
- Max Depth
- Min Child Weight
- Gamma
- Subsample
- Col Sample By Tree
- Scale POS Weight

Eventually the best parameters were found and models were evaluated with each added features and hyperparameter change. Eventually Random Forest Classifier was chosen because of its superior accuracy (0.83 to 0.81).

## Results
![image](https://github.com/seansjj/news_headline_classification/assets/141446128/7f2ac491-9b81-4e58-80a1-a41222b805a8)

The visualization shows the top 5 most and least sensational new sources by average sensational class. The 0.5 threshold represented by a red line shows that sources above tend to be more sensationalized on average, and below would tend to be non-sensational. The colours and values on top of the bars show the number of headlines per source, with the type of news reporting labeled as well. One thing intresting of notes is that both finance news sources were most and least sensational. Looking into this, the ETF Daily News on the left reports on very short stock price updates featuring just stocks and companies tend to be capitalized, while marketscreener on the right reports finance in more a traditional reporting manner.

![image](https://github.com/seansjj/news_headline_classification/assets/141446128/611b99f1-3332-487e-b79d-ef7730734736)

The most significant criteria in determining sensationalism was shown to be uppercase ratio, buzzword ratio, and average word length. The uppercase ratio is hypothesized because named entities such as people or organizations, or if a headline wants to display excitement - headlines tend to be capitalized. Buzzwords tend to be adjectives, adverbs that are used to over describe headlines. For average word length, short words seem to grab attention easier than longer words such as denounced or admendment.

## Future Improvements
There were a few challenges to this project. The Flesch-Kincaid Index is a measure for the ease of readibility that was added to the model, however the formula did not function as properly because it required a minimum 100 words - longer than every headline. Another issue was that functions required frequent bugfixing such as ratios going over 1.0 or unique words counting common words like 'the' or sensational words counting the 'day' in 'Friday'. This made me learning automatic unittesting through PyTest rather than manually testing every function.

A few ways to improve predictions for this model whether via methods or new features include:
- Integrated Unsupervised Learning: Adding clustering algorithms such as K-Means or DBScan would classify the originally unlabed global news dataset so we can make our analysis on the groupings
- Sentimental Analysis Score: Determining if highly positive or negative sentimental scores tend to have more sensational headlines
- TF-IDF: Analyzing if the importance of certain words compared to the entire dataset can be used to determine sensationalism
- Part of Speech (POS) tagging: Using a NLTK librbary to train and tag word categories in a headline (noun, verb, adjective) to see if headlines w/ more adjectives, adverbs tend to be more sensational

## Credits
- Kumar Saksham for their [Global News Dataset](https://www.kaggle.com/datasets/everydaycodings/global-news-dataset)https://www.kaggle.com/datasets/everydaycodings/global-news-dataset
- Nakatani Shuyo for their language detection library, [langdetect](https://pypi.org/project/langdetect/)https://pypi.org/project/langdetect/
