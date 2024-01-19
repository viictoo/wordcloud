# Word Cloud Visualization

## Introduction

This project aims to visualize the frequency of words in a dataset using a word cloud. The word cloud is a popular data visualization technique that represents textual data. It uses size and color to represent the importance and frequency of a word in the text.

## Features

- Removes stop words to reduce noise and enhance the relevance of the word cloud.
- Allows customization of the word cloud, including color, font, layout, scaling, spacing, exclusion of specific words, and angles.
- Uses the `nltk` library for stop words removal and the `matplotlib` and `wordcloud` libraries for generating and displaying the word cloud.

## Installation

To install the necessary libraries, use pip:

```bash
pip install -r requirements.txt
```

## Usage
1. Start mysql and import the dataset from an sqldump like the 
provided in the assets folder
```bash
cat assets/metal_bands.sql | mysql -u root -p databaseName
```
2.Run the script, For example:

```bash
python3 wordcloud.py
```

2. The script will display the word cloud using `matplotlib`.

## Customization

You can customize the word cloud by modifying the parameters in the `WordCloud()` function. For example, to change the width and height of the word cloud, modify the `width` and `height` parameters:

```python
wordcloud = WordCloud(width=1000, height=500).generate_from_frequencies(word_freq)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.
