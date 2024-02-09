# Getting the base image
FROM apache/airflow:2.7.1

# Copying the requirements
COPY requirements.txt /opt/requirements.txt

# Upgrade to the latest pip
RUN pip install --no-cache-dir --upgrade pip

# Install the latest dependencies
RUN pip install --no-cache-dir -r /opt/requirements.txt

# Install OpenJDK-11
USER root
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Insert JAVA_GATEWAY_EXITED environment variable with a default value
ENV JAVA_GATEWAY_EXITED 1

# Switch back to airflow user if needed
USER airflow
