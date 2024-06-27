from serp_extractor import extract_serp, dataframe_creator
import logging
import awswrangler as wr
import click


@click.command()
@click.option('--api_key', type=str)
def main(api_key: str) -> str:

    logging.getLogger().setLevel(logging.INFO)
    logging.info(f"Running SERP extractor...")
    serp_output = extract_serp(api_key)
    serp_dataframe = dataframe_creator(serp_output)

    logging.info(f"Connecting to AWS...")
    logging.info(f"Saving file on S3 bucket...")
    wr.s3.to_csv(serp_dataframe, "s3://mi-playground-bucket/outputs/serp_output.csv", index=False)
    logging.info(f"Results saved!")


main()
