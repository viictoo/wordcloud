import requests
prepare = __import__('cleaner')
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from collections import Counter


# get URL
pumpkin = requests.get("https://www.alxafrica.com/about/")
 
# display status code
print(pumpkin.status_code)

# store content into variable
pumpkin_text = BeautifulSoup(pumpkin.content, 'html.parser').text
pumpkin_text = prepare.clean(pumpkin_text)

# check first 100 characters after cleaning
pumpkin_text[:100]

pumpkin_text = Counter(pumpkin_text)
# print(pumpkin_text)

# Importing mask
pumpkin_mask = np.array(Image.open('assets/black_alx.jpg'))

# Plot the wordcloud with the mask applied
wc = WordCloud(background_color='black', mask= pumpkin_mask, 
            #    colormap = 'copper'
               colormap = 'RdYlGn'
               ).generate_from_frequencies(pumpkin_text)
plt.figure(figsize=[10,10])
plt.tight_layout()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()



