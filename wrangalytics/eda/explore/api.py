def debug(x):
    print(x)

def getStringColumns(df, show=True):
    df = df.select_dtypes(include='object')
    if show:
        display(df)
    return df

def columnNamesByType(df, type='object', show=True):
    colNames = df.select_dtypes(include=type).columns.values
    if show:
        display(colNames)
    return colNames

def getUniqueColValuesByType(df, type='object', show=True):
    colNames = df.select_dtypes(include=type).columns.values
    if show:
        for col in colNames:
            display(col, df[col].unique())
    return colNames

def getRowIndex(df, show=True):
    idx = df.index
    if show:
        display(df.index)
    return idx

def getColumnIndex(df, show=True):
    idx = df.index
    if show:
        display(df.columns)
    return idx

def getUniqueValsBySeries(series, show=True):
    unique = series.unique()
    if show:
        display(series.name, unique)
    return unique

def displayUniqueValsByListSeries(df, list):
    for col in list:
        display(col, df[col].unique())

def getIndexes(df, show=True):
    d = dict();
    d['row_idx'] = df.index
    d['col_idx'] = df.columns
    if show:
        display(d)
    return d

def displayDfFeatureCardinality(df):
    """
    Check cardinality for each feature

    Args
    -----
    - Pandas func: pd.Series.nunique

    Notes 
    ------
    - Ensure cardinality makes sense for both continuous and categorical features
    - Watch out for cardinality equal to 1 or greater than 50
    - Remove feature if cardinality is equal to 1 since no predictive power
    """
    display(df.apply(pd.Series.nunique))

def getFeatureCardinality(series, show=True):
    card = series.nunique
    if show:
        display(card)
    return card

def analyzeTypes(df):
    getDfTypeCounts(df)
    getDfColTypes(df)

def analyzeCardinality(df):
    return True

def analyzeOutliers(df):
    return True

def getType(x, show=True):
    # Use 'is a' syntax to return boolean
    input_type = type(x)
    if show:
        display(input_type)
    return input_type

def getSeriesTypeName(series, show=True):
    name = series.dtype.name
    if show:
        display(name)
    return name

def getDfColTypes(df, show=True):
    df_types = df.dtypes
    if show:
        display(df_types)
    return df_types

def getDfTypeCounts(df, show=True):
    df_type_cnts = df.get_dtype_counts()
    if show:
        display(df_type_cnts)
    return df_type_cnts

def getSeriesType(series, show=True):
    s_type = series.dtype
    if show:
        display(s_type)
    return  s_type