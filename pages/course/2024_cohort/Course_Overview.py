import streamlit as st

# REMOVED: from st_pages import add_page_title, hide_pages
# REASON: These conflict with st.navigation().

# Optional: Add a main title if the markdown below isn't enough
# st.title("Course Overview")

st.markdown("### 🧙‍♂️ Data Engineering Zoomcamp 2024 Cohort")

st.video("https://www.youtube.com/watch?v=AtRhA-NfS24")

st.markdown("""
* [Pre-launch Q&A stream](https://www.youtube.com/watch?v=91b8u9GmqB4)
* Launch stream with course overview (TODO)
* [Deadline calendar](https://docs.google.com/spreadsheets/d/e/2PACX-1vQACMLuutV5rvXg5qICuJGL-yZqIV0FBD84CxPdC5eZHf8TfzB-CJT_3Mo7U7oGVTXmSihPgQxuuoku/pubhtml)
* [Course Google calendar](https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)
* [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing)            

---
            
### 🏅 Course Leaderboard """)
            
st.info("You can find the course leaderboard [here](https://courses.datatalks.club/de-zoomcamp-2024/leaderboard)!")
            
st.markdown("""
---
               
### 📄 Syllabus

#### Module 1: Containerization and Infrastructure as Code
* Course overview
* Introduction to GCP
* Docker and docker-compose
* Running Postgres locally with Docker
* Setting up infrastructure on GCP with Terraform
* Preparing the environment for the course
* Homework

#### Module 2: Workflow Orchestration
* Data Lake
* Workflow orchestration
* Workflow orchestration
* Workflow orchestration with Mage
* Homework

#### Workshop 1: Data Ingestion
            
#### Module 3: Data Warehouse
* Data Warehouse
* BigQuery
* Partitioning and clustering
* BigQuery best practices
* Internals of BigQuery
* BigQuery Machine Learning

#### Module 4: Analytics engineering
* Basics of analytics engineering
* dbt (data build tool)
* BigQuery and dbt
* Postgres and dbt
* dbt models
* Testing and documenting
* Deployment to the cloud and locally
* Visualizing the data with google data studio and metabase

#### Module 5: Batch processing
* Batch processing
* What is Spark
* Spark Dataframes
* Spark SQL
* Internals: GroupBy and joins

#### Module 6: Streaming
* Introduction to Kafka
* Schemas (avro)
* Kafka Streams
* Kafka Connect and KSQL

#### Workshop 2: Stream Processing with SQL
            
#### Project
Putting everything we learned to practice
* Week 1 and 2: working on your project
* Week 3: reviewing your peers

---

### 📝 Architecture diagram""", unsafe_allow_html=True)

st.image("https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/architecture/photo1700757552.jpeg")

st.markdown("""
---

### 🛠️ Technologies
* **Google Cloud Platform (GCP)**: Cloud-based auto-scaling platform by Google
  * **Google Cloud Storage (GCS)**: Data Lake
  * **BigQuery**: Data Warehouse
* **Terraform**: Infrastructure-as-Code (IaC)
* **Docker**: Containerization
* **SQL**: Data Analysis & Exploration
* **Mage**: Workflow Orchestration     
* **dbt**: Data Transformation
* **Spark**: Distributed Processing
* **Kafka**: Streaming

---

### ⚒️ Tools

For this course, you'll need to have the following software installed on your computer:

* Docker and Docker-Compose
* Python 3 (e.g. via [Anaconda](https://www.anaconda.com/products/individual))
* Google Cloud SDK
* Terraform

See Week 1 for more details about installing these tools""", unsafe_allow_html=True)

st.info("""**Note:** NYC TLC changed the format of the data we use to parquet. But you can still access the csv files [here](https://github.com/DataTalksClub/nyc-tlc-data).""")

st.markdown("---")

st.markdown("""
### 💌 Supporters and partners

Thanks to the course sponsors for making it possible to run this course

<p align="center">
  <a href="https://mage.ai/">
    <img height="120" src="https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/mage.svg">
  </a>
</p>


<p align="center">
  <a href="https://dlthub.com/">
    <img height="90" src="https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/dlthub.png">
  </a>
</p>

<p align="center">
  <a href="https://risingwave.com/">
    <img height="90" src="https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/rising-wave.png">
  </a>
</p>

Do you want to support our course and our community? Please reach out to [alexey@datatalks.club](alexey@datatalks.club)
            
---
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
            
##### 🖼️ Course UI was made by [Paul Kimani](https://github.com/paul-kimani)""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)