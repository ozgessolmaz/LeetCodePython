import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows, columns = players.shape
    return [rows, columns]

data = [
    [846,'Mason',21,'Forward','RealMadrid'],
    [749,'Riley',30,'Winger','Barcelona'],
    [155,'Bob',30,'Striker','ManchesterUnited'],
    [583,'Bob',28,'Goalkeeper','Liverpool'],
    [388,'Isabella',32,'Midfielder','BayernMunich'],
    [883,'Zachary',24,'Defender','Chelsea'],
    [355,'Ava',23,'Striker','Juventus'],
    [247,'Thomas',18,'Striker','ParisSaint-Germain'],
    [761,'Jack',27,'Midfielder','ManchesterCity'],
    [642,'Charlie',33,'Center-back','Arsenal']
]

df = pd.DataFrame(data, columns=["player_id","name","age","position","team"])

result = getDataframeSize(df)
print(result)
