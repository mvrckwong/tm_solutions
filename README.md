# Thinking Machine Data Science
Thinking Machines Solutions

<!-- Approach -->
## Approach to the project development / development journey

* The approach to the development is to highlight end-to-end while creating insights for the project, therefore highlighting extraction, transformation, and loading, while using existing skillsets.
* Before anything else, I check the dataset and the schema of the tables. I noticed its a large dataset spanning million/s rows of data particularly on the factual tables.
* I extracted the data using bigquery client and then converted into pandas dataframe. I hit the limitations of how pandas dataframe are slow in a large datasets, therefore the development transition to pyspark.
* From pyspark, I want to transition to PowerBi to understand the data model of the tables, and how each tables are connected. PowerBi has a model view tool to do that, which connects the relationship of your tables.
* Initially coded everything on a MacOS, but realized that I need to quickly transition to a WindowsOS. At this time, I develop a basic docker image and airflow to manage the project and the OS, so transitioning to one of the OS would be easier. Also this direction will be used to showcase my skills in this domain area.
* I've quickly abandon this direction mainly to much dependencies needs to be setup particurly on pyspark. I did not anticipate the setup time for pyspark to be working properly. (HADOOP_HOME, JAVA_HOME, etc.)
* Finally, finished the analysis with python - created basic



- The project's approach emphasized an end-to-end journey focusing on extraction, transformation, and loading (ETL), aiming to create insights from a large dataset using existing skill sets.
## Technologies Used

- BigQuery
- Pandas
- PySpark
- PowerBI
- Docker*
- Airflow*
- Python