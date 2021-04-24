# %%
import pandas as pd 
import altair as alt 
import numpy as np
import altair_saver

# %%
url = 'https://github.com/byuidatascience/data4soils/raw/master/data-raw/cfbp_handgrenade/cfbp_handgrenade.csv'
dat = pd.read_csv(url)

# %%
bob = (alt
.Chart(dat)
.encode(x ='hmx', y = 'rdx')
.mark_circle())

bob

# %%
bob.save('bob.png')
# %%