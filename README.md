 # Stock market Efficiency: Streamlining MicroServered Pipeline with SQS-Powered Data Flow
 
Project Title :Stock market Efficiency: Streamlining MicroServered Pipeline with SQS-Powered Data Flow.
Technologies used in this project : REST API , SQS , Lambda , DynamoDB ,Python.

Project Overview:
The project centers around developing a REST API that fetches stock data from the "Rapid API" website 
After we hit the api link every 1 min with the Python script and send the data to AWS SQS
Once 10 records accumulate in the SQS queue, a separate AWS Lambda function named "Processor" is triggered to process this data. 
The processed data, containing information about stock price, then inserted into a dynamo db database and should send a mail notification of that data.n

Components and Workflow:
REST API Endpoint: A REST API endpoint is developed to establish a connection with the "Rapid API" website. It fetches real-time data of various stock market data, adhering to the 1-minute update interval.
Python Script: A Python script has been created to continuously call the REST API every 1 second and transmit the acquired data to an AWS Simple Queue Service (SQS) queue.
AWS SQS Queue: The fetched data is then transmitted to an AWS SQS queue. The queue acts as a buffer, temporarily storing incoming data. This queuing mechanism decouples the data ingestion process from the subsequent processing steps, ensuring data integrity and availability.
AWS Lambda "Processor" Function: Once 10 records accumulate in the SQS queue, the AWS Lambda "Processor" function is automatically triggered. This function's role is to retrieve the queued data and perform data transformation operations and we only need to get the stock price, high , low .
Data Processing: The "Processor" function filters the incoming data, selecting only the records related to stock price, high , low. This selective data processing optimizes storage and subsequent analysis efforts.
Dynamo db Database: The processed data is then inserted into a dynamo db database. And update regularly.We have to insert the price of the stock and the time and date at which it is inserted into.

conclusion:
As a data engineer, successfully deploying this real-time stock data processing pipeline marks a substantial advancement in bolstering our company's stock trading prowess. 
The architecture's focus on reliability, scalability, and optimal resource usage seamlessly fits the dynamic stock trading landscape. By leveraging AWS services and contemporary data engineering, we've laid a strong groundwork for sustained progress and innovation in the realm of stock trading.




