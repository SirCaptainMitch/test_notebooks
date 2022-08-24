#%%
import os
import sqlalchemy as sa

from scripts.database import engine
import pandas as pd
from sample_data import stat_vectors, comp_style_vectors, map_style_vectors, roles

#%%

BASE_DIR = os.path.abspath(os.path.dirname('../'))

meta_data = sa.MetaData(bind=engine)
sa.MetaData.reflect(meta_data)

hero_stats_path = f'{BASE_DIR}\\app\sample_data\hero_stats.csv'
comfort_path = f'{BASE_DIR}\\app\sample_data\player_comfort.csv'
#%%

#%%
