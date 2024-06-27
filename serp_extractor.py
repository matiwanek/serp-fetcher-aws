from serpapi import GoogleSearch
import csv
import pandas as pd
import logging
from datamodel import Links
import yaml


def extract_serp(api_key: str) -> str:

    serp_results = []
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    for query in csv.reader(open('query.csv')):

        params = {
            "q": query,
            "location": config['location'],
            "hl": config['hl'],
            "num": config['num'],
            "gl": config['gl'],
            "google_domain": config['google_domain'],
            "api_key": api_key
        }
        logging.info(f"Sending query: {query[0]} to SERP API")
        for link in (GoogleSearch(params).get_dict())['organic_results']:

            serp_results.append({'query': query[0], 'position_num': link['position'], 'link': link['link'],
                                 'link_title': link['title']})

    return serp_results


def dataframe_creator(serp_results: dict) -> dict:

    df = pd.DataFrame(columns=[Links.query, Links.position_num, Links.link, Links.link_title])

    logging.info(f"Adding results to DataFrame")
    for result in serp_results:

        new_df = pd.DataFrame([result])
        df = pd.concat([df, new_df], ignore_index=True)

    logging.info(f"DataFrame created...")

    return df
