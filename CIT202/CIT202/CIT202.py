#import csv module for reading dataset sets of comma seperated values (csv)
#using dataset from https://www.kaggle.com/datasets/shubhamsadawarti/instagram-analysis
# dataset created by SHUBHAM SADAWARTI on kaggle for instagram analysis
# it was implemented in this project

import csv

def store_hashtags(path):
    print("STORING KNOWN HASHTAGS FROM DATASET")
    #store hashtags read from csv dataset with respective id in a dictionary
    hashtags_with_id={}
    with open(path,"r") as file:
        reader=csv.reader(file)
        # variable fields contain fieldnames and is not needed
        fields=next(reader)
        for row in reader:
            hashtags_with_id[row[0]]=row[1]
    return hashtags_with_id

def get_posts_data(path):
    print("COLLECTING POSTS DATA FROM DATASET ")
    #returns post data read from dataset
    with open(path,"r") as file:
        reader=csv.reader(file)
        fieldName=next(reader)
        return list(reader)

def get_hashtags(posts_data,data_index=1):
    print("PARSING HASHTAGS FROM POST DATA")
    #get hashtags from post data and stores their id in a list
    hashtags_id_list=[]
    for row in posts_data:
        hashtags_id_list.append(row[data_index])
    return hashtags_id_list

def count_hashtags(hashtags_id_list,hashtags_with_id):
    print("COUNTING HASHTAGS INTO DICTIONARY")
    #counts hashtags and stores its name as a key and number as value in dictionary
    hashtag_counter={}
    for hashtag_id in hashtags_id_list:
        hashtag=hashtags_with_id[hashtag_id]
        if hashtag not in hashtag_counter:
            hashtag_counter[hashtag]=1
        else:
            hashtag_counter[hashtag]+=1
    return hashtag_counter

def analyze_hashtag_counter(hashtag_counter,popular=10):
    #analsis of the hashtag counter dictionary and prints out most popular
    temp_arr=[]
    for hashtag,count in hashtag_counter.items():
        temp_arr.append((count,hashtag))
    temp_arr.sort(reverse=True)
    print(f"\nPRINTING {popular} POPULAR HASHTAGS")
    for count,hashtag in temp_arr:
        print(f"#{hashtag} used {count} times")
        popular-=1
        if popular <1:
            break
    return True

def get_mentions(path):
    print("SORTING MENTIONS")
    # get number of mentions from dataset
    mentions_list=[]
    with open(path,"r") as file:
        reader=csv.reader(file)
        fieldName=next(reader)
        data=list(reader)
        for row in data:
            # index 4 is where mentions data is located
            # index 1 is for name of mentions
            mentions_list.append((int(row[4]),row[1]))
    mentions_list.sort(reverse=True)
    return mentions_list

def analyze_mentions(mentions_data_list,popular=10):
    #this function prints analyzed datatabout mentions
    print(f"\nPRINTING {popular} POPULAR MENTIONS")
    for count,mentions in mentions_data_list:
        print(f"@{mentions}  mentioned  {count} times")
        popular-=1
        if popular<1:
            break
    return True

def main():
    # this function calls other major functions
    # popular variable contols number of items are printed out
    popular=5
    hashtag_with_id=store_hashtags("dataset/tags.csv")
    post_data=get_posts_data("dataset/photo_tags.csv")
    hashtags_by_id=get_hashtags(post_data)
    hashtag_count=count_hashtags(hashtags_by_id,hashtag_with_id)
    mentions_data_list=get_mentions("dataset/users.csv")
    status1=analyze_hashtag_counter(hashtag_count,popular)
    status2=analyze_mentions(mentions_data_list,popular)
    # status1 and status 2 are bool that verify analysis ran without error
    if status1 and status2:
        print("\nProgram ran without errors")

main()
