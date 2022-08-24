# %%
import sqlalchemy as sa
import pandas as pd

from scripts.database import engine

meta_data = sa.MetaData(bind=engine)
sa.MetaData.reflect(meta_data)
# %%
Hero = meta_data.tables['Hero']
Battleground = meta_data.tables['Map']
Player = meta_data.tables['Player']

ReplayDetail = meta_data.tables['ReplayDetail']
ReplayPlayer = meta_data.tables['ReplayPlayer']
ReplayTalent = meta_data.tables['ReplayTalent']
ReplayDraft = meta_data.tables['ReplayDraft']
PeriodicExperience = meta_data.tables['PeriodicExperience']

# %%
replay_fingerprint = 'b73aeea6-cd7a-308c-1f0a-c9943d4c4477'

j = ReplayDetail.join(ReplayPlayer, ReplayPlayer.c.ReplayId == ReplayDetail.c.ReplayId) \
    .join(Player, Player.c.PlayerId == ReplayPlayer.c.PlayerId) \
    .join(Battleground, Battleground.c.MapId == ReplayDetail.c.MapId) \
    .join(Hero, Hero.c.HeroId == ReplayPlayer.c.HeroId)

query = sa.select(
    ReplayDetail.c.ReplayFingerPrint
    , Player.c.Battletag
    , Battleground.c.MapName
    , ReplayDetail.c.GameType
    , Hero.c.ShortName
    , Hero.c.NewRole
    , ReplayDetail.c.GameDate
    , ReplayDetail.c.GameLengthTimestamp
    , ReplayPlayer
    , Player.c.BlizzardId
    , Player.c.MasterPlayerId
).select_from(j).where(sa.and_(
    ReplayDetail.c.ReplayFingerPrint == replay_fingerprint
))

replay_player_detail_df = pd.read_sql(sql=query, con=engine)

replay_player_detail_df.head(20)

#%%
j = ReplayDetail.join(ReplayDraft, ReplayDraft.c.ReplayId == ReplayDraft.c.ReplayId) \
    .join(Hero, Hero.c.HeroId == ReplayDraft.c.HeroId)

query = sa.select(
    ReplayDetail.c.ReplayFingerPrint
    , ReplayDetail.c.DraftFirstTeam
    , ReplayDraft.c.PickType
    , ReplayDraft.c.ParsedAltName
    , ReplayDraft.c.DraftIndex
    , ReplayDraft.c.Team
    , Hero.c.ShortName
    , Hero.c.NewRole
    , Hero.c.HeroId
).select_from(j).where(sa.and_(
    ReplayDetail.c.ReplayFingerPrint == replay_fingerprint
))

replay_draft_detail_df = pd.read_sql(sql=query, con=engine)

replay_draft_detail_df.head(20)

#%%
