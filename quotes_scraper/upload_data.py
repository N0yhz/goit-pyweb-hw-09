from pymongo import MongoClient
import json

def load_data_to_mogodb():
    client = MongoClient('mongodb+srv://n0yhz:module08@qouteset1.13lvt.mongodb.net/')
    db = client['test']
    quotes_collection = db['quote']
    authors_collection = db['author']

    with open('quotes.json', encoding='utf-8') as json_file:
        quotes_data = json.load(json_file)
        print("Quotes data loaded:", quotes_data)  # Print quotes data for debugging
        for quote in quotes_data:
            print("Processing quote:", quote)  # Print each quote being processed
            # Check if 'quote' key exists
            if 'quote' in quote:
                # Check if the quote already exists in the collection
                if not quotes_collection.find_one({'quote': quote['quote']}):
                    quotes_collection.insert_one(quote)
            else:
                print(f"Warning: 'quote' key not found in data: {quote}")

    with open('authors.json', encoding='utf-8') as json_file:
        authors_data = json.load(json_file)
        for author in authors_data:
            if 'name' in author:
                if not authors_collection.find_one({'name': author['name']}):
                    authors_collection.insert_one(author)

    print('Data loaded successfully!')

if __name__ == "__main__":
    load_data_to_mogodb()