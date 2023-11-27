import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv("out.c_oddeleni_tabulky_bez_info_o_ridici.join_nehody_auta_bez_ridice.csv")

data = data[data["celkova_skoda"] < 500000]
data = data[data["celkova_skoda"] > 0]
formula = "celkova_skoda ~ znacka + stari_vozidla + lehce_zraneno + tezce_zraneno + delka_praxe + stav_ridice + pocet_vozidel + pohlavi_ridice + misto_nehody + pricina2 + viditelnost + stav_vozovky + vlastnik + cas2 + pracovni_den + vzdelani_ridice + delka_praxe + statni_prislusnost2"
mod = smf.ols(formula=formula, data=data)
# res - od result, nazev promenne
res = mod.fit()
print(res.summary())
sns.displot(data["celkova_skoda"], kde=True)
plt.show()