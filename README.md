# Thinking Machine Data Science
Thinking Machines Solutions

<!-- Approach -->
## Approach to the project development / Development Journey
* Before anything else, I check the dataset and the schema of the tables. I noticed its a large dataset spanning million/s rows of data particularly on the factual tables.
* Initially extracted using bigquery client and then converted into pandas dataframe. I hit the limitations of how pandas dataframe are slow in a large datasets, therefore quickly transition to pyspark.