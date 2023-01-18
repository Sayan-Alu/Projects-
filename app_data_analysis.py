

import csv

# Initialize variables to store the data
app_store_data = []
google_play_data = []

# Open and read the App Store data
with open('app_store_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        app_store_data.append(row)

# Open and read the Google Play data
with open('google_play_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        google_play_data.append(row)

# Extract the columns we need for analysis
app_store_data = [[row[0], row[5], row[9]] for row in app_store_data[1:]]
google_play_data = [[row[0], row[5], row[9]] for row in google_play_data[1:]]

# Function to find the average rating of an app
def average_rating(data):
    total_ratings = 0
    total_reviews = 0
    for row in data:
        total_ratings += float(row[1])
        total_reviews += int(row[2])
    average = total_ratings / total_reviews
    return average

# Find the average rating of apps on the App Store and Google Play
app_store_average = average_rating(app_store_data)
google_play_average = average_rating(google_play_data)

# Print the results
print('App Store average rating:', app_store_average)
print('Google Play average rating:', google_play_average)


