import os
from airflow import DAG
from airflow import configuration as conf
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta


# Load configuration
process_directory = os.path.join(conf.get('core', 'process_folder'))


# Set configure
default_args = {
    'owner': 'michael',
    'depends_on_past': False,
    'start_date': datetime(2018, 4, 20),
    'email': ['michael.kao@fao.org'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
    'catchup_by_default': False
}

# Create dag
dag = DAG('the_reading_machine',
          default_args=default_args,
          schedule_interval='@daily')

########################################################################
# Create nodes
########################################################################

# Article scrapping
# --------------------
scraper_dir = os.path.join(process_directory, 'article_scraper')
article_scraper_command = 'cd {}; python processor.py'.format(scraper_dir)
article_scraper = BashOperator(bash_command=article_scraper_command,
                               task_id='article_scraper',
                               params=default_args,
                               dag=dag)
db_raw_article = DummyOperator(task_id='db_raw_article', dag=dag)

# Article processing
# --------------------
article_processing_script_path = os.path.join(
    process_directory, 'article_processing/processor.py')
article_processing_command = 'python {}'.format(
    article_processing_script_path)
article_processing = BashOperator(bash_command=article_processing_command,
                                  task_id='article_processing',
                                  params=default_args,
                                  dag=dag)
db_processed_article = DummyOperator(task_id='db_processed_article', dag=dag)


# Price Extraction
# --------------------
price_scraper_script_path = os.path.join(
    process_directory, 'price_extraction/processor.py')
price_scraper_command = 'python {}'.format(
    price_scraper_script_path)
price_scraper = BashOperator(bash_command=price_scraper_command,
                             task_id='price_extraction',
                             params=default_args,
                             dag=dag)
db_raw_price = DummyOperator(task_id='db_raw_price', dag=dag)


# Sentiment scoring
# --------------------
sentiment_scoring_script_path = os.path.join(
    process_directory, 'sentiment_scoring/processor.py')
sentiment_scoring_command = 'python {}'.format(
    sentiment_scoring_script_path)
sentiment_scoring = BashOperator(bash_command=sentiment_scoring_command,
                                 task_id='sentiment_scoring',
                                 params=default_args,
                                 dag=dag)
db_sentiment_scoring = DummyOperator(task_id='db_sentiment_scoring', dag=dag)

# Topic Modelling
# --------------------
topic_modelling_script_path = os.path.join(
    process_directory, 'topic_modelling/processor.py')
topic_modelling_command = 'python {}'.format(
    topic_modelling_script_path)
topic_modelling = BashOperator(bash_command=topic_modelling_command,
                               task_id='topic_modelling',
                               params=default_args,
                               dag=dag)
db_topic_modelling = DummyOperator(task_id='db_topic_modelling', dag=dag)


# Data harmonisation
# --------------------
data_harmonisation_script_path = os.path.join(
    process_directory, 'data_harmonisation/processor.py')
data_harmonisation_command = 'python {}'.format(
    data_harmonisation_script_path)
data_harmonisation = BashOperator(bash_command=data_harmonisation_command,
                                  task_id='data_harmonisation',
                                  params=default_args,
                                  dag=dag)
db_data_harmonisation = DummyOperator(task_id='db_data_harmonisation', dag=dag)

# Compute the market force
# --------------------
compute_market_force_script_path = os.path.join(
    process_directory, 'compute_market_force/processor.py')
compute_market_force_command = 'python {}'.format(
    compute_market_force_script_path)
compute_market_force = BashOperator(bash_command=compute_market_force_command,
                                    task_id='compute_market_force',
                                    params=default_args,
                                    dag=dag)


########################################################################
# Create dependency
########################################################################

db_raw_article.set_upstream(article_scraper)
db_raw_price.set_upstream(price_scraper)

article_processing.set_upstream(db_raw_article)
db_processed_article.set_upstream(article_processing)

sentiment_scoring.set_upstream(db_processed_article)
topic_modelling.set_upstream(db_processed_article)

db_sentiment_scoring.set_upstream(sentiment_scoring)
db_topic_modelling.set_upstream(topic_modelling)

data_harmonisation.set_upstream(db_sentiment_scoring)
data_harmonisation.set_upstream(db_topic_modelling)

db_data_harmonisation.set_upstream(data_harmonisation)
compute_market_force.set_upstream(db_data_harmonisation)
