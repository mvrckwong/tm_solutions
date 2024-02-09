# getting the base image
FROM apache/airflow:2.7.1

# copying the requirements
COPY requirements.txt /opt/requirements.txt

# upgrade to the latest pip
RUN pip install --no-cache-dir --upgrade pip

# install to the latest dependencies
RUN pip install --no-cache-dir -r /opt/requirements.txt