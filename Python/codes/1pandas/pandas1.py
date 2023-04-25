import numpy as np
import pandas as pd

dict1 = {
    "name": ['Ajay','Sumil','Sarthak','Sujal','Surya'],
    "marks": [50,55,60,70,58],
    "city": ['Virar','Bhayander','Chembur','Mahim','Kalagaon']
    }
df = pd.DataFrame(dict1)
print(df)
df.to_csv('pandas1.csv')
