# **Billboard Music Dashboard**

## **📌 Objective**

This project aims to build a **Billboard Music Dashboard** to help public/musicians understand trending music genres and assist investors in making data-driven decisions.

## **📂 Dataset**

I use the **Billboard Top Songs Dataset** from Kaggle: [Billboard Top Songs Dataset](https://www.kaggle.com/datasets/samayashar/billboard-top-songs)

sample and illustration of the dataset:

| Song               | Artist                     | Streams                 | Daily Streams   | Genre       | Release Year               | Peak Position                                 | Weeks on Chart                 | Lyrics Sentiment                        | TikTok Virality                         | Danceability              | Acousticness                    | Energy                           |
| ------------------ | -------------------------- | ----------------------- | --------------- | ----------- | -------------------------- | --------------------------------------------- | ------------------------------ | --------------------------------------- | --------------------------------------- | ------------------------- | ------------------------------- | -------------------------------- |
| Track 14728        | EchoSync                   | 689815326               | 796199          | Trap        | 2021                       | 81                                            | 8                              | 0.2                                     | 17                                      | 0.11                      | 0.59                            | 0.6                              |
| Title of the track | Name of the performer/band | Total Number of streams | Streams per day | Music genre | Year the song was released | Highest Billboard/Spotify chart rank achieved | Total weeks spent on the chart | Sentiment analysis of lyrics (-1 to +1) | Popularity score based on Tiktok trends | How danceable the song is | Level of acoustic elements(0-1) | Overall energy level of the song |

------

## **🔗 Data Pipeline Architecture**

This project follows a **batch processing** approach. The data flows through the following steps:

1. **Data Ingestion:** Load data from Kaggle and store it in Google Cloud Storage (GCS). 
2. **Data Warehouse:** Use BigQuery to store and query data.
3. **Data Transformation:** Use dbt to model and transform data.
4. **Dashboard Visualization:** Create visualizations in Google Looker Studio.

------

## **⚙️ Environment Setup**

This project is conducted in a **WSL (Windows Subsystem for Linux) environment** using the following technologies:

- **Cloud:** Google Cloud (GCS + BigQuery)
- **Infrastructure as Code:** Terraform
- **Workflow Orchestration:** Airflow
- **Data Transformation:** DBT
- **BI Dashboard:** Google Looker Studio

------

## **1️⃣ Data Ingestion: Terraform + GCS**

### **📌 Install Terraform and Google Cloud SDK**

```bash
# Install Terraform
sudo apt update && sudo apt install terraform -y

# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

### **📌 Terraform Configuration**

```bash
# Authenticate Service Account
 gcloud auth application-default login

# Initialize Terraform
terraform init

# Preview infrastructure changes
terraform plan

# Create GCS Bucket and upload data
terraform apply

# Destroy resources if needed
terraform destroy
```

**Created** **GCS Bucket**: `dbt-learn-452007-terra-bucket` and uploaded the dataset.



![image-20250329143228410](pics\image-20250329143228410.png)

![image-20250329144717637](pics\image-20250329144717637.png)

------

## **2️⃣ Data Loading to BigQuery: Airflow ETL**

### **📌 Configure Airflow to connect with Google Cloud**

```bash
export AIRFLOW_HOME=~/airflow

# Add Google Cloud connection
airflow connections add google_cloud_default \
    --conn-type google_cloud_platform \
    --conn-extra '{
        "project": "dbt-learn-452007",
        "key_path": "/home/eliza/.google/credentials/google_credentials.json",
        "scope": ["https://www.googleapis.com/auth/cloud-platform"]
    }'
```



### **📌 Start Airflow**

```bash
airflow scheduler
airflow webserver
```

![image-20250329162859418](pics\image-20250329162859418.png)

Transferred data from GCS to BigQuery:

![image-20250329163006401](pics\image-20250329163006401.png)

------

## **3️⃣ Data Transformation: DBT**

Use **DBT** to model and transform the data.

```bash
# Clean DBT cache
dbt clean

# Run data transformation
dbt run --models music
```

![image-20250329180730049](pics\image-20250329180730049.png)

------

## **4️⃣ Data Visualization: Google Looker Studio**

The dashboard includes two main charts:

1. **Genre Distribution Chart** - Shows the popularity of different music genres.
2. **Time-Series Chart** - Displays music trends over the years.

🔗 **Live Dashboard:** [Billboard Music Dashboard](https://lookerstudio.google.com/reporting/fdbb81c9-03cf-487a-b38d-5ee90f8daa03) 

![image-20250329200627017](pics\image-20250329200627017.png)

------

## **5️⃣ Reproducibility**

To reproduce this project, follow these steps:

1. Install Terraform and Google Cloud SDK (See Section 1️⃣)
2. Deploy GCS Bucket using Terraform (See Section 1️⃣)
3. Configure Airflow and run ETL pipeline (See Section 2️⃣)
4. Run DBT transformations (See Section 3️⃣)
5. Open Looker Studio Dashboard to visualize the results (See Section 4️⃣)

------

## **6️⃣ Future Improvements**

-  Implement data quality checks using Great Expectations.
- Enable real-time streaming using Apache Kafka.
- Automate deployment with Terraform enhancements.
-  Implement a CI/CD pipeline for dashboard updates.

