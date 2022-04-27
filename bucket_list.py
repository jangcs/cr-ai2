# https://soundprovider.tistory.com/entry/GCP-Python%EC%97%90%EC%84%9C-GCP-Cloud-Storage-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0#--%--GCP%EC%--%--%--%ED%-C%-C%EC%-D%BC%--%EC%--%AC%EB%A-%AC%EA%B-%B-

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./gcp-test-710302-880fc36e6747.json"

from google.cloud import storage

storage_client = storage.Client()
buckets = list(storage_client.list_buckets())

for bucket in buckets:
	print(bucket)


