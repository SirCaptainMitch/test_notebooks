# %%
import sqlalchemy as sa
import pandas as pd

from scripts.database import engine

meta_data = sa.MetaData(bind=engine)
sa.MetaData.reflect(meta_data)

# %%
Player = meta_data.tables['Player']
TeamRollup = meta_data.tables['TeamRollup']

# %%
players = pd.read_sql(sql=sa.select(Player), con=engine)
players.head()

#%%
## Gather aliased accounts
child_players = players[(players.MasterPlayerId != players.PlayerId)]
child_players.head()

#%%
team = pd.read_sql(sql=sa.select(TeamRollup), con=engine)
team.head(20)

#%%
