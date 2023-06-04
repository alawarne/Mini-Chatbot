import tensorflow as tf
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import openai

# Set up OpenAI AIP credentials / Go to OpenaAI to get your own AIP Key
openai.api_key = "YOUR_OWN_OPENAI_API_KEY"

# Load the pre-trained sentiment analysis model 
# nltk.dowload('vader_lexicon)
sia = SentimentIntensityAnalyzer()

# Generate random text using openai
def generate_response(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.7
    )
    return response.choices[0].text.strip()

# Sentiment analysis on the generated text
def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0:
        return "Positive"
    else:
        return "Negative"
    

# Main program (conversation loop)
def main():
    print("Chatbot: Hi, I'm a chatbot. How can I assist you today?")

    while True:
        user_input = input("You: ")

        response = generate_response(user_input)
        sentiment = analyze_sentiment(response)

        print("Chatbot:", response)
        print("Sentiment Analysis:", sentiment)

        if user_input.lower() == "goodbye":
            break

if __name__ == '__main__':
    main()