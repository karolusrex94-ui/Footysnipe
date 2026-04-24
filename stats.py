import math
import numpy as np
from scipy.stats import poisson

class LeagueContext:
    def __init__(self, avg_home_goals, avg_away_goals, home_adv):
        self.avg_home_goals = avg_home_goals
        self.avg_away_goals = avg_away_goals
        self.home_adv = home_adv

class TeamStats:
    def __init__(self, name, goals_scored_avg, goals_conceded_avg, is_home, xg=None, xga=None, ppg=None, attack_adjustment=0.0, defense_adjustment=0.0):
        self.name = name
        self.gs = goals_scored_avg
        self.gc = goals_conceded_avg
        self.is_home = is_home
        self.xg = xg
        self.xga = xga
        self.ppg = ppg
        self.attack_adjustment = attack_adjustment
        self.defense_adjustment = defense_adjustment

def ppg_attack_multiplier(ppg):
    if ppg is None: return 1.0
    if ppg >= 1.8: return 1.05
    if ppg >= 1.0: return 1.00
    return 0.95

def poisson_prob(k, lam):
    return poisson.pmf(k, lam)

def chance_label(prob):
    if prob >= 0.7: return {"label": "High Chance", "color": ":green"}
    if prob >= 0.4: return {"label": "Medium Chance", "color": ":orange"}
    return {"label": "Low Chance", "color": ":red"}

def implied_odds(prob):
    return 1 / prob if prob > 0 else float('inf')
