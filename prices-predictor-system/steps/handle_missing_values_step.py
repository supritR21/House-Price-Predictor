import pandas as pd
from src.handle_missing_values import (
    DropMissingValuesStrategy,
    FillMissingValuesStrategy,
    MissingValuesHandler,
)
from zenml import step

@step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """
    Handles missing values using MissingValueHandler and the specified strategy.
    """

    if strategy == "drop":
        handler = MissingValuesHandler(DropMissingValuesStrategy(axis=0))
    elif strategy in ["mean", "median", "mode", "constant"]:
        handler = MissingValuesHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy: {strategy}")
    
    df_cleaned = handler.handle_missing_values(df)
    return df_cleaned