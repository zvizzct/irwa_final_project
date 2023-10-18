from utils import convert_jsonlines_to_json, build_terms, create_index, search, load_tweets

def main():
    # convert_jsonlines_to_json("data/Rus_Ukr_war_data.jsonl", "data/Rus_Ukr_war_data.json")

    tweets = load_tweets("data/Rus_Ukr_war_data.json")

    index, tweet_index = create_index(tweets)

    term_to_search = "NATO"
    results = search(term_to_search, index)

    # print(f"Resultados para '{term_to_search}': {results}")

    print("Insert your query (i.e.: Ukraine War):\n")
    query = input()
    docs = search(query, index)
    top = 10

    print("\n======================\nSample of {} results out of {} for the searched query:\n".format(top, len(docs)))
    for d_id in docs[:top]:
        print("tweet_id= {} - Tweet: {}".format(d_id, tweet_index[d_id]['Tweet']))
        print("-"*50)


if __name__ == "__main__":
    main()
