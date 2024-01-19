import pymysql
import nltk
from collections import Counter
from nltk.corpus import stopwords
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Uncomment to Download stop words from nltk
#nltk.download('stopwords')

# Connect to the db
connection = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='holberton',
                           port=3306,

                           )
try:
   with connection.cursor() as cursor:
       # Execute the SQL query
       sql = "SELECT band_name FROM metal_bands"
       cursor.execute(sql)
       result = cursor.fetchall()
finally:
   connection.close()

# Convert list of tuples to list of strings
band_names = [' '.join(name) for name in result]

# Split band names into words
words = []
for name in band_names:
  words.extend(name.lower().split())

# remove stop words eg the, an, of, etc...
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Count frequency of each word
word_freq = Counter(filtered_words)

# print(word_freq)

path = 'path/to/assets/80sflyingV.png'
mask = np.array(Image.open(path))

# Generate simple word cloud
# wordcloud = WordCloud(
#         width = 800,
#         height = 800
#         ).generate_from_frequencies(word_freq)

# Uncomment to add image mask of your choice
wordcloud = WordCloud(scale=3,
                      colormap='RdYlGn',
                      mask=mask,
                      background_color='black',
                      contour_color='red',
                      contour_width=1
                      ).generate_from_frequencies(word_freq)

# Display the generated image
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.title('METAL')
plt.show()
