import pandas as pd
import os

def load_data(base_path="data"):
    data = {}
    data["materials"] = pd.read_csv(os.path.join(base_path, "material_master.csv"))
    data["stock"] = pd.read_csv(os.path.join(base_path, "stock_levels.csv"))
    data["orders"] = pd.read_csv(os.path.join(base_path, "material_orders.csv"))
    data["sales"] = pd.read_csv(os.path.join(base_path, "sales_orders.csv"))
    data["dispatch"] = pd.read_csv(os.path.join(base_path, "dispatch_parameters.csv"))
    data["suppliers"] = pd.read_csv(os.path.join(base_path, "suppliers.csv"))
    return data
