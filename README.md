# IRWA Final Project

## Summary

This project aims to build a search engine based on a document corpus consisting of tweets related to the Russo-Ukrainian War. The engine has been developed following academic learnings from theoretical classes, seminars and lab exercises. Currently, the focus is on Part 1: Text Processing and Exploratory Data Analysis.

## How to run the code

1. Setup

   - Ensure all the required libraries are installed. If not, install them using `pip`.
   - Rename the file extension from `.json` to `.jsonl` for the file containing tweets in the `data/` directory.

2. Execute the Search Engine:

   - Uncomment the line `convert_jsonlines_to_json("data/Rus_Ukr_war_data.jsonl", "data/Rus_Ukr_war_data.json")` in `main.py` if you need to convert the input file from `.jsonl` to `.json` format.
   - Execute `main.py` using the command:
     - `python main.py`
   - The program will prompt you to enter a search query. For example, "NATO".
   - It will then display a sample of 10 results from the matching tweets.

## Functions Overview

- `convert_jsonlines_to_json(input_file, output_file)`: Converts a `.jsonl` file to a `.json` format.
- `build_terms(tweet)`: Processes a tweet to extract and preprocess terms.
- `create_index(tweets)`: Generates an inverted index and tweet index from a list of tweets.
- `load_tweets(file_path)`: Loads tweets from a `.json` file into a list.
- `search(query, index)`: Queries the inverted index and returns matching tweet IDs.
