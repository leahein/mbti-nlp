from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums

import csv

import pdb



def get_users():
    with open('mbti.csv') as csv_file:
        mbti_users = csv.DictReader(csv_file)
        for user in mbti_users:
            yield user

def sentiment_text(text):
    client = language.LanguageServiceClient()

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
)

    return client.analyze_sentiment(document).document_sentiment

def analyze_users():
    for user in get_users():
        judging_function = user['type'][2]
        sentiment = sentiment_text(user['posts'])
        word_count = len(user['posts'].split(' '))
        normalized_magnitude = sentiment.magnitude / word_count
        pdb.set_trace()
        yield (
            user['type'],
            judging_function,
            sentiment.score
            sentiment.magnitude
            normalized_magnitude,
        )

def main():
    with open('sentiments.csv', 'w') as csv_file:
        sentiment_writer = csv.writer(csv_file)
        sentiment_writer.writerow(
            [
                'Type',
                'Thinking / Feeling',
                'Score'
                'Raw Magnitude',
                'Normalized Magnitude',
            ]
        )
        for user_analysis in analyze_users():
            sentiment_writer.writerow(user_analysis)

if __name__ == '__main__':
    main()
