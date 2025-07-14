import pandas as pd
import logging, sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 23: Logging
logging.info(" Data loaded with %d rows", len(df))