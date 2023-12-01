from yelpapi import YelpAPI
import pandas as pd
from textblob import TextBlob

api_key = "WVGpd1mx7xIuSuGh93Xgbmp1gN0GeV1mpY5YdwWmDNS27yQM4pnUPZ9_kpCqACsJbxl54E95yzTPZXaDMlnBu8LzbCSRKOhTGwtLO0ONfhv16LJrv374N6Bzu2pKZXYx"
yelp_api_instance = YelpAPI(api_key)
search_term = 'service'
location_term = 'El Paso, TX'

search_results = yelp_api_instance.search_query(
    term=search_term, location=location_term,
    sort_by='rating', limit=20,  
)

print(search_results)

for business in search_results['businesses']:
    print('\n')
    print(business)

# Assuming you have the business id for reviews, correct the next lines
id_for_reviews = 'taqueria-el-cometa-el-paso'  # Corrected typo in variable name
reviews_response = yelp_api_instance.reviews_query(id=id_for_reviews)  # Corrected typo in method name

# Assuming you want to print the reviews
for review in reviews_response['reviews']:
    blob = TextBlob(review['text'])
    print("\nReview: ", review['text'])
    print("Sentiment Polarity: ", blob.sentiment.polarity)

