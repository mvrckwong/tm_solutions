from config import *
import pandas as pd
from explore_dataset import CountMissingData, VisualizeMissing

COUNT_MISSING_DATA_DIR = OUTPUT_DIR / "02_count_missing"
if not COUNT_MISSING_DATA_DIR.exists():
    COUNT_MISSING_DATA_DIR.mkdir()
    
GRAPH_MISSING_DATA_DIR = OUTPUT_DIR / "03_graph_missing"
if not GRAPH_MISSING_DATA_DIR.exists():
    GRAPH_MISSING_DATA_DIR.mkdir()


csv_files = [x for x in DATA_DIR.glob("*.csv")]

for index, file in enumerate(csv_files):
    file_name = file.stem.split("-")[-1]
    
    df = pd.read_csv(file,dtype=str)
    
    # Get the missing data count and percentage based on input dataframe
    df_missing_data = CountMissingData(df).get()
    df_missing_data.to_csv(COUNT_MISSING_DATA_DIR / f"{file_name}.csv")
    
    graph_missing = VisualizeMissing(
        df, name=file_name, 
        export_plot=True, 
        show_plot=False,
        process_null=True,
        process_zero=True,
        output_path=GRAPH_MISSING_DATA_DIR
    )
    graph_missing.Bar(show=False)
    graph_missing.Matrix(show=False)
    graph_missing.Heatmap(show=False)