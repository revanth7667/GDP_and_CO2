import pandas as pd
import matplotlib.pyplot as plt
import seaborn

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

data_req = data[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

data_req = data_req.rename(
    columns={
        "Mortality rate, infant (per 1,000 live births)": "morality",
        "GDP per capita (constant 2010 US$)": "gdp",
        "Country Name": "country",
    }
)

plt.scatter(
    x=data_req.morality,
    y=data_req.gdp,
)
plt.show()
