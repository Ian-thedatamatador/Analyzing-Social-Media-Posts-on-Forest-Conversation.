import re

def extract_hashtags(social_media_posts):
    # Use re.findall() to find all occurrences that match the pattern
    hashtags = re.findall(r'#\w+', social_media_posts)
    return hashtags

def extract_numbers (social_media_posts):
    # Use re.findall() to find all occurrences that match the pattern
    numbers =  re.findall (r'\d+', social_media_posts)
    return numbers

def count_specific_words (social_media_posts):
    # Use re.findall() to find all occurrences that match the pattern
    negative_words = re.findall (r'\billegal\b|\blogging\b',social_media_posts)
    return len(negative_words)


social_media_posts = """
Great news! The GreenWood Project has successfully planted 10000 trees in the Amazon Rainforest #GreenEarth #Conservation 
Update: ForestCoverApp shows a 12% increase in forest cover in the last 5 years. #TechForGood
Sad to see illegal logging in Madagascan rainforests. We need stricter laws! #SaveForests #ActNow
Celebrating World Environment Day with a pledge to plant 20000 trees. Join us! #EnvironmentDay #GoGreen
Interesting study published in NatureJournal: Rainforest biodiversity is crucial for ecological balance. #ScienceForNature
"""

# Call the function and print the result
hashtags = extract_hashtags(social_media_posts)
print (hashtags)

numbers = extract_numbers (social_media_posts)
print (numbers)

negative_words = count_specific_words(social_media_posts)
print (negative_words)

                     
