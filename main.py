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
    data_to_append.append(-1)
    dataset.append(data_to_append)
    

with open('dataset/new_dataset.csv', 'w') as f:
    write = csv.writer(f)
    for data in tqdm(dataset, total=len(dataset)):
        write.writerow(data)
        
#feature_extraction.generate_data_set(url)
