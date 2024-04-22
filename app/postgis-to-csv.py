#!/bin/python 

# Code originally developed by Ye Hong: https://github.com/irmlma/mobility-simulation

import sqlalchemy
from sqlalchemy import text
import pandas
import os

# Variables
login_user = os.environ["LOGIN_USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
port = os.environ["PORT"]
database = os.environ["DATABASE"]
query = os.environ["QUERY"]
output_filename = os.environ["OUTPUT_FILENAME"]
geom_col = os.environ["GEOM_COL"]

# Query
engine = sqlalchemy.create_engine(
    f"postgresql://{login_user}:{password}@{host}:{port}/{database}"
)

with engine.connect() as conn:
    df = pd.read_sql(text(query), conn)
    gdf = gpd.read_postgis(text(query), conn, geom_col=geom_col)

engine.dispose()

# Storing CSV
output_filename = os.path.join("/odtp/odtp-output/", os.environ["OUTPUT_FILENAME"])

df.to_csv(output_filename, index=False)