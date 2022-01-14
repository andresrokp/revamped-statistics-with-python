import pandas as pd;
from tabulate import tabulate;

url = "./nhanes_2015_2016.csv";
df = pd.read_csv(url);

print(df.columns);

shape = df.shape;

df2 = df.loc[0:10, 'SEQN':'RIDAGEYR'];
# LESSON LEARNT : datafrme to html - https://towardsdatascience.com/pretty-displaying-tricks-for-columnar-data-in-python-2fe3b3ed9b83
tableHTML = tabulate(df2, headers='keys', tablefmt='html');

columns = df.columns;

datatypes = df.dtypes;

aSlice = df["DMDEDUC2"].head(10);

maxOfSlice = aSlice.max();

typeOfDF = type(df);
typeOfCol = type(df["DMDEDUC2"])
typeOfRow = type(df.iloc[2,:])

aRow = df.iloc[5,:];

severalRows = df.iloc[2:5, :];
severalColumns = df.iloc[:, 2:5].head(10);

nullsFromColumn = df["DMDEDUC2"].isnull().sum();
validsFromColumn = df["DMDEDUC2"].notnull().sum();

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
        <a href="../../index.html"> <button>Home</button> </a>
        <a href="nhanesDataBasics.py"> <button>Code</button> </a>
        
        <h1>Data Render by andresrokp</h1>
        <hr>

        <h3>Data shape:</h3>
        {shape}
        <hr>

        <h3>Data Frame Columns:</h3>
        <pre>{columns}</pre>
        <hr>

        <h3>Data types:</h3>
        <pre>{datatypes}</pre>
        <hr>

        <h3>Slice a column:</h3>
        <div class="code-container">
            <pre>slice = da["DMDEDUC2"] || da.loc[:, "DMDEDUC2"] || da.DMDEDUC2 || da.iloc[:, 9]  # DMDEDUC2 is in column 9</pre>
            <pre>slice.head(10)</pre>
        </div>
        <pre>{aSlice}</pre>
        <hr>

        <h3>Processing of the Series:</h3>
        <div class="code-container">
            <pre>slice.max()</pre>
        </div>
        <pre>{maxOfSlice}</pre>
        <hr>

        <h3>Type of the Series object:</h3>
        <div class="code-container">
            <pre>type(da) # The type of the variable</pre>
            <pre>type(da.DMDEDUC2) # The type of one column of the data frame</pre>
            <pre>type(da.iloc[2,:]) # The type of one row of the data frame</pre>
        </div>
        <pre>class 'pandas.core.frame.DataFrame'</pre>
        <pre>class 'pandas.core.series.Series'</pre>
        <pre>class 'pandas.core.series.Series'</pre>
        <hr>

        <h3>A row of the data frame:</h3>
        <div class="code-container">
            <pre>df.iloc[5,:]</pre>
        </div>
        <pre>{aRow}</pre>
        <hr>

        <h3>Several rows of the data frame:</h3>
        <div class="code-container">
            <pre>df.iloc[2:5, :]</pre>
        </div>
        <pre>{severalRows}</pre>
        <hr>

        <h3>Several columns of the data frame:</h3>
        <div class="code-container">
            <pre>df.iloc[:, 2:5].head(10)</pre>
        </div>
        <pre>{severalColumns}</pre>
        <hr>

        <h3>Nulls and valid values from a column:</h3>
        <div class="code-container">
            <pre>df["DMDEDUC2"].isnull().sum()</pre>
            <pre>df["DMDEDUC2"].notnull().sum()</pre>
        </div>
        <pre>{nullsFromColumn}</pre>
        <pre>{validsFromColumn}</pre>

        <hr>
        {tableHTML}
        <hr>
    </body>
</html>
"""
# LESSON LEARNT : insert variable into html - https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
#                                           - https://stackoverflow.com/questions/11764900/using-locals-and-format-method-for-strings-are-there-any-caveats

with open('./afrp-nhanesDataRender.html', 'w') as f:
    f.write(render);
