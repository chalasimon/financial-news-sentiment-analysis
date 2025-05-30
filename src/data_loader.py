import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)

    def load_data(self) -> pd.DataFrame:
        """
        Loads a CSV file into a pandas DataFrame.
        Returns:
            pd.DataFrame: Loaded dataset
        Raises:
            FileNotFoundError: If the file does not exist.
            pd.errors.ParserError: If the file cannot be parsed.
        """
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")
        
        try:
            df = pd.read_csv(self.filepath)
            return df
        except pd.errors.ParserError as e:
            raise pd.errors.ParserError(f"Error parsing the file: {e}")
