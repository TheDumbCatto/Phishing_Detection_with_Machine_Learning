from os import wait
import feature_extraction_more_qualitative
import json, csv
from pandas import read_csv
from tqdm import tqdm

phishing_list = []
legit_list = []
urls = read_csv('dataset/unlabeled_private_test_hackathon_vcs_2023.csv')['x'].tolist()
tlds = []
with open('tlds.txt', 'r') as f:
    tlds = f.readlines()

popular_urls = read_csv('dataset/majestic_million.csv')['Domain'].tolist()[0:201]
test_data = []
for url in tqdm(urls, total=len(urls)):
    data = feature_extraction_more_qualitative.generate_data_set(url, tlds, popular_urls)
    test_data.append(data)

fields = ['domain','having_IP_address','domain_length','URL_length','use_shortening_service','having_At_symbol','having_double_slash_redirecting','number_of_dashes','number_of_sub_domains','using_weird_ports','having_https_token_in_URL','randomness_of_URL','having_HTML_tag_in_URL','having_brand_name_in_path','having_brand_name_in_domain','entropy_of_special_characters','having_suspicious_words_in_URL','having_TLD_in_domain_name','having_more_than_1_TLD_in_URL','result']
with open('dataset/private_test_features.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    for data in tqdm(test_data, total=len(test_data)):
        write.writerow(data)
#with open('dataset/phishtank.json') as f:
#    i=1
#    object_list = json.load(f)
#    for _object in object_list:
#        if i==5001: break
#        phishing_list.append(_object['url'])
#        i += 1
#
#data = read_csv('dataset/majestic_million.csv')
#legit_list = data['Domain'].tolist()[0:5000]
#tlds = []
#with open('tlds.txt', 'r') as f:
#    tlds = f.readlines()
#
#popular_urls = read_csv('dataset/majestic_million.csv')['Domain'].tolist()[0:201]
#dataset = []
#for phish in tqdm(phishing_list, total=len(phishing_list)):
#    data_to_append = feature_extraction_more_qualitative.generate_data_set(phish, tlds, popular_urls)
#    data_to_append.append(1)
#    dataset.append(data_to_append)
###    
#for legit in tqdm(legit_list, total=len(legit_list)):
#    data_to_append = feature_extraction_more_qualitative.generate_data_set('https://'+legit, tlds, popular_urls)
#    data_to_append.append(0)
#    dataset.append(data_to_append)
    
#organizer_feature_train = []
#organizer_dataset_train = read_csv('dataset/labeled_public_test_hackathon_vcs_2023.csv')
#train_urls = organizer_dataset_train['x'].tolist()
#labels = organizer_dataset_train['y'].tolist()
#i=0
#for train_url in train_urls:
#    data_to_append = feature_extraction_more_qualitative.generate_data_set(train_url, tlds, popular_urls)
#    data_to_append.append(labels[i])
#    organizer_feature_train.append(data_to_append)
#    i+=1

#kaggle_train = []
#kaggle_train_input = read_csv('dataset/dataset_phishing.csv')
#train_urls = kaggle_train_input['url'].tolist()
#labels = kaggle_train_input['status'].tolist()
#i=0
#for train_url in tqdm(train_urls, total=len(train_urls)):
#    data_to_append = feature_extraction_more_qualitative.generate_data_set(train_url, tlds, popular_urls)
#    if(labels[i]=='legitimate'): data_to_append.append(0)
#    else: data_to_append.append(1)
#    dataset.append(data_to_append)
#    i+=1
#
#fields = ['domain','having_IP_address','domain_length','URL_length','use_shortening_service','having_At_symbol','having_double_slash_redirecting','number_of_dashes','number_of_sub_domains','using_weird_ports','having_https_token_in_URL','randomness_of_URL','having_HTML_tag_in_URL','having_brand_name_in_path','having_brand_name_in_domain','entropy_of_special_characters','having_suspicious_words_in_URL','having_TLD_in_domain_name','having_more_than_1_TLD_in_URL','result']
#with open('dataset/organizer_feature_train.csv', 'w') as f:
#    write = csv.writer(f)
#    write.writerow(fields)
#    for data in tqdm(organizer_feature_train, total=len(organizer_feature_train)):
#        write.writerow(data)
#
#with open('dataset/qualitative_feature_labeled_public_test_hackathon_vcs_2023_feature.csv', 'w') as f:
#    write = csv.writer(f)
#    write.writerow(fields)
#    for data in tqdm(organizer_feature_train, total=len(organizer_feature_train)):
#with open('dataset/feature_kaggle_dataset.csv', 'w') as f:
#    write = csv.writer(f)
#    write.writerow(fields)
#    for data in tqdm(kaggle_train, total=len(kaggle_train)):
#        write.writerow(data)
#with open('dataset/qualitative_11kkaggle_5kphishing_5kclean_dataset.csv', 'w') as f:
#    write = csv.writer(f)
#    write.writerow(fields)
#    for data in tqdm(dataset, total=len(dataset)):
#        write.writerow(data)
        
#feature_extraction.generate_data_set(url)
