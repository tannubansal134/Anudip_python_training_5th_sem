'''Problem Statement
Ratings given by users for movies are stored below.
Sample Data
ratings = { 
"Inception": 4.8, 
"Avatar": 4.3, 
"Titanic": 4.5, 
"Joker": 4.7, 
"Frozen": 3.8, 
"Interstellar": 4.9, 
"Dune": 4.6, 
"Up": 4.1, 
"Coco": 4.4, 
"Cars": 3.9 
}
Tasks
1.Display movies rated above 4.5.
2.Find the highest-rated movie.
3.Find the lowest-rated movie.
4.Calculate average rating.
5.Create a recommendation list (rating ≥ 4.5).
'''
# Dictionary containing movie rating
#-------------------------------------------------------
ratings = {
    "Inception": 4.8,
    "Avatar": 4.3,
    "Titanic": 4.5,
    "Joker": 4.7,
    "Frozen": 3.8,
    "Interstellar": 4.9,
    "Dune": 4.6,
    "Up": 4.1,
    "Coco": 4.4,
    "Cars": 3.9
}

# Display movies rated above 4.5
#-----------------------------------------------------
print("Movies Rated Above 4.5:")
for movie, rating in ratings.items():
    if rating > 4.5:
        print(movie)

# Find highest-rated movie
#-----------------------------------------------------
highest_movie = max(ratings, key=ratings.get)
highest_rating = ratings[highest_movie]

# Find lowest-rated movie
#-----------------------------------------------------
lowest_movie = min(ratings, key=ratings.get)
lowest_rating = ratings[lowest_movie]

# Calculate average rating
#-----------------------------------------------------
total = sum(ratings.values())
average = total / len(ratings)

# Create recommendation list (rating >= 4.5)
#-----------------------------------------------------
recommended = []
for movie, rating in ratings.items():
    if rating >= 4.5:
        recommended.append(movie)

# Display results
#-----------------------------------------------------
print("\nHighest Rated Movie:", highest_movie, "(", highest_rating, ")")
print("Lowest Rated Movie:", lowest_movie, "(", lowest_rating, ")")
print("Average Rating:", round(average, 2))
print("Recommended Movies:", recommended)