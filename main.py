from os import wait
import feature_extraction
import json, csv
from pandas import read_csv
from tqdm import tqdm

phishing_list = []
legit_list = []
with open('dataset/phishtank.json') as f:
    object_list = json.load(f)
    for _object in object_list:
        phishing_list.append(_object['url'])

data = read_csv('dataset/majestic_million.csv')
legit_list = data['Domain'].tolist()

dataset = []
for phish in tqdm(phishing_list, total=len(phishing_list)):
    data_to_append = feature_extraction.generate_data_set(phish)
    data_to_append.append(1)
    dataset.append(data_to_append)
    #print(type(feature_extraction.generate_data_set(phish).append(1)))
  
    #print(type(feature_extraction.generate_data_set(phish)))

#for data in dataset[0:len(phishing_list)]:
#    data.append(1)
    
for legit in tqdm(legit_list, total=len(legit_list)):
    data_to_append = feature_extraction.generate_data_set(legit)
    data_to_append.append(0)
    dataset.append(data_to_append)
    
organizer_feature_train = []
organizer_dataset_train = read_csv('dataset/train.csv')
train_urls = organizer_dataset_train['domain'].tolist()
i=0
for train_url in train_urls:
    data_to_append = feature_extraction.generate_data_set(train_url)
    if (i==0 or i in range(3,6) or i in range(8,10)):
        data_to_append.append(1)
    else:
        data_to_append.append(0)
    organizer_feature_train.append(data_to_append)
    i+=1

with open('dataset/organizer_feature_train.csv', 'w') as f:
    write = csv.writer(f)
    for data in tqdm(organizer_feature_train, total=len(organizer_feature_train)):
        write.writerow(data)

with open('dataset/new_dataset.csv', 'w') as f:
    write = csv.writer(f)
    for data in tqdm(dataset, total=len(dataset)):
        write.writerow(data)
        
#feature_extraction.generate_data_set(url)
