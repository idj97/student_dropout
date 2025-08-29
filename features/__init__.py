import pandas as pd
from .application_mode import *
from .occupation import *
from .qualification import *

def collapse_hcard_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["application_mode"] = [map_application_mode(m) for m in df["application_mode"].values]
    df["previous_qualification"] = [map_qualification(q) for q in df["previous_qualification"]]
    df["mother_qualification"] = [map_qualification(q) for q in df["mother_qualification"]]
    df["father_qualification"] = [map_qualification(q) for q in df["father_qualification"]]
    df["mother_occupation"] = [map_occupation(o) for o in df["mother_occupation"]]
    df["father_occupation"] = [map_occupation(o) for o in df["father_occupation"]]
    return df
