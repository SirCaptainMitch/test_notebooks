comp_style_vectors = ['Fight', 'Macro', 'Artillery', 'Protect', 'Pick']
map_style_vectors = ['Fight', 'Macro', 'Artillery', 'Protect', 'Pick']
roles = ['Bruiser', 'Healer', 'Melee Assassin', 'Ranged Assassin', 'Support', 'Tank']
general = [
    'GamesPlayed'
    , 'GamesPlayedLastNinetyDays'
    , 'TotalWins'
    , 'MeanGamesPerDay'
    , 'MeanGamesPerWeek'
    , 'MeanGamesPerMonth'
]

kills = dict([
    ('Bruiser', .75)
    , ('Healer', .5)
    , ('Tank', .75)
    , ('Support', .25)
    , ('Melee Assassin', 1)
    , ('Ranged Assassin', 1)
])

assists = dict([
    ('Bruiser', .75)
    , ('Healer', .5)
    , ('Tank', .75)
    , ('Support', .5)
    , ('Melee Assassin', 1)
    , ('Ranged Assassin', 1)
])

takedowns = dict([
    ('Bruiser', .75)
    , ('Healer', .5)
    , ('Tank', .75)
    , ('Support', .5)
    , ('Melee Assassin', 1)
    , ('Ranged Assassin', 1)
])

Deaths = dict([
    ('Bruiser', 1)
    , ('Healer', 1)
    , ('Tank', 1)
    , ('Support', 1)
    , ('Melee Assassin', 1)
    , ('Ranged Assassin', 1)
])

general_role_values = [
    'Bruiser'
    , 'Healer'
    , 'Melee Assassin'
    , 'Ranged Assassin'
    , 'Support'
    , 'Tank'
]

stat_vectors = [
    'Kills'
    , 'Assists'
    , 'Takedowns'
    , 'Deaths'
    , 'Level'
    , 'HeroDamage'
    , 'SiegeDamage'
    , 'StructureDamage'
    , 'MinionDamage'
    , 'CreepDamage'
    , 'SummonDamage'
    , 'TimeCcEnemyHeroes'
    , 'Healing'
    , 'SelfHealing'
    , 'DamageTaken'
    , 'ExperienceContribution'
    , 'HighestKillStreak'
    , 'TownKills'
    , 'Multikill'
    , 'TimeSpentDead'
    , 'MercCampCaptures'
    , 'WatchTowerCaptures'
    , 'MetaExperience'
    , 'ProtectionAllies'
    , 'SilencingEnemies'
    , 'RootingEnemies'
    , 'StunningEnemies'
    , 'ClutchHeals'
    , 'Escapes'
    , 'Vengeance'
    , 'OutnumberedDeaths'
    , 'TeamfightEscapes'
    , 'TeamfightHealing'
    , 'TeamfightDamageTaken'
    , 'TeamfightHeroDamage'
    , 'PhysicalDamage'
    , 'SpellDamage'
    , 'RegenGlobes'
    , 'TimeonFire'
]
