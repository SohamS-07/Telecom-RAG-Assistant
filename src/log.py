import pandas as pd
import os
from datetime import datetime

def log_query(question,answer,docs):
    sources=" ,".join(sorted({doc.metadata["source"] for doc in docs}))
    entry={"Timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Question":question,
           "Answer":answer,"Sources":sources}
    file="search_history.csv"
    if os.path.exists(file):
        df=pd.read_csv(file)
        df=pd.concat([df,pd.DataFrame([entry])],ignore_index=True)
    else:
        df=pd.DataFrame([entry])
    df.to_csv(file,index=False)
