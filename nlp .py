import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text
text= """
Natural language processing (NLP) is a field of artificial intelligence that gives computers the ability to read, understand, and generate human language.
It is used for a variety of applications such as sentiment analysis, text summarization, machine translation, and question answering.
NLP combines linguistics and machine learning to analyze and interpret human language in a way that is valuable.
"""
 
text1= """
Artificial Intelligence (AI) is transforming industries across the globe. From healthcare to finance, AI technologies are driving innovation and efficiency. 
Machine learning, natural language processing (NLP), and deep learning are all part of the AI revolution." 
" As AI continues to advance, its impact on automation, data analysis, and decision-making will continue to grow.
 The potential applications of AI are vast, making it one of the most exciting areas of research and development.
"""

text2= """
Maintaining a healthy lifestyle is essential for overall well-being. Regular exercise, a balanced diet, and adequate sleep are all critical components of a healthy life. Mental health is just as important as physical health, with stress management and mindfulness practices gaining popularity. 
A holistic approach to wellness can lead to increased energy, improved mood, and a stronger immune system.
 Health professionals recommend staying active, eating nutrient-rich foods, and practicing self-care to maintain long-term health.
 """
# Tokenizing the text
tokens = word_tokenize(text.lower())  # Convert text to lowercase and tokenize

# Removing punctuation and stopwords
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

# Clean tokens by removing stopwords and punctuation
cleaned_tokens = [word for word in tokens if word not in stop_words and word not in punctuation]

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize the cleaned tokens
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in cleaned_tokens]

# Join the lemmatized tokens back into a single string
cleaned_text_with_lemmas = " ".join(lemmatized_tokens)

# Create the WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text_with_lemmas)

# Display the generated WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # No axes for a cleaner look
plt.show()
