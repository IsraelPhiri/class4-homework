
# Using an official Ubuntu as a parent image
FROM ubuntu:latest

RUN apt-get update

#Install python3 to run my_csv_reader.py
RUN apt-get -y install python3

#Copy my_csv_reader.py into the container
COPY my_csv_reader.py .

#Copy housing.data file into the container
COPY housing.data .

# Run my_csv_reader.py when the container launches
CMD ["python3","-u", "my_csv_reader.py"]
