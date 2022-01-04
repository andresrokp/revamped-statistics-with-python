import pandas as pd;
from tabulate import tabulate;

url = "nhanes_2015_2016.csv";
df = pd.read_csv(url);

print(df.columns);



shape = df.shape;

df2 = df.loc[0:10, 'SEQN':'RIDAGEYR'];
# LESSON LEARNT : datafrme to html - https://towardsdatascience.com/pretty-displaying-tricks-for-columnar-data-in-python-2fe3b3ed9b83
tableHTML = tabulate(df2, headers='keys', tablefmt='html');

render = f"""
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
        <a href="/index.html"> <button>Home</button> </a>
        <a href="nhanesDataBasics.py"> <button>Code</button> </a>
        <h1>Data Render by andresrokp</h1>
        <hr>
        <h3>Data shape:</h3>
        {shape}
        <hr>
        <h3>Data Frame Columns:</h3>
        {df.columns}
        <hr>
        <hr>
        {tableHTML}
    </body>
</html>
"""
# LESSON LEARNT : insert variable into html - https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
#                                           - https://stackoverflow.com/questions/11764900/using-locals-and-format-method-for-strings-are-there-any-caveats

with open('afrp-nhanesDataRender.html', 'w') as f:
    f.write(render);
