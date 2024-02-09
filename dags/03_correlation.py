from config import *
import pandas as pd

from explore_dataset import EvaluateDataset

EVALUATE_DATA_DIR = OUTPUT_DIR / "04_evaluate"
if not EVALUATE_DATA_DIR.exists():
    EVALUATE_DATA_DIR.mkdir()

# Get the following dataset.
orders_df = pd.read_csv(DATA_DIR / "thelook_ecommerce-orders.csv")
order_items_df = pd.read_csv(DATA_DIR / "thelook_ecommerce-order_items.csv")
products_df = pd.read_csv(DATA_DIR / "thelook_ecommerce-products.csv")

# Joining together - merging orders, order_items and products
result_df = pd.merge(
    order_items_df, orders_df, how="left",
    left_on="order_id", right_on="order_id"
)
result_df = pd.merge(
    result_df, products_df, how="left",
    left_on="product_id", right_on="id"
)

# Label Encoding
col_label = ["category", "brand", "department"]
for column in col_label:
    result_df[column] = result_df[column].astype('category').cat.codes.astype('int64')

eval_data = EvaluateDataset(
    input_df=result_df, data_name="correlation_merged_data",
    export_plot=True, show_plot=False, output_path=EVALUATE_DATA_DIR
)

eval_data.get_all_corr()
eval_data.get_all_hist()

# category
# brand 
# department

