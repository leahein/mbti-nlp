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

def main():
    for user in get_users():
        sentiment = sentiment_text(user['posts'])
        normalized_magnitude = len(user['posts']) / sentiment.magnitude
        pdb.set_trace()
        print('--------------------------------------------')
        print('Judging Function: {}'.format(user['type'][2]))

        print('Score: {}'.format(sentiment.score))
        print('Raw Magnitude: {}'.format(sentiment.magnitude))

        print('Normalized Magnitude: {}'.format(normalized_magnitude))
        print('--------------------------------------------')


if __name__ == '__main__':
    main()
