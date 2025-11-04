from sqlalchemy import create_engine
from config import get_db_url

def load_to_postgres(df, table_name="sales_agg"):
    """Load the transformed data into PostgreSQL."""
    engine = create_engine(get_db_url())
    with engine.begin() as conn:
        df.to_sql(table_name, con=conn, if_exists="replace", index=False)
    print(f"✅ Loaded {len(df)} rows into table '{table_name}'.")
