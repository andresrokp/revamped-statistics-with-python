import pandas as pd;
from tabulate import tabulate;

url = "nhanes_2015_2016.csv";
df = pd.read_csv(url);

print(df.columns);

df2 = df.loc[0:10, 'SEQN':'RIDAGEYR'];
# LESSON LEARNT : datafrme to html - https://towardsdatascience.com/pretty-displaying-tricks-for-columnar-data-in-python-2fe3b3ed9b83
tableHTML = tabulate(df2, headers='keys', tablefmt='html');

boilerplate = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="afrp-StylesDataRender.css">
    <title>Data Render</title>
</head>
<body>
"""

with open('afrp-nhanesDataRender.html', 'w') as f:
    f.write(boilerplate);
    f.write(tableHTML);
    f.write("</body></html>");
