import pandas as pd


def separate():
    df = pd.read_csv('apps.csv', encoding='windows-1252')
    ids = df['id']
    names = df['name']
    keywords = df['keywords'].str.split(', ')

    apps = []
    for i in range(0, names.size):
        keys = []
        keys.extend(keywords[i][1:])
        if "Inc." in keys:
            keys.remove("Inc.")
        if len(keys) > 1:
            apps.append({'title': [names[i]], 'keywords': keys[:-2], 'cat': keys[1]})

    dict = {'putting effort':[], 'weather and stuff':[], 'eh stuff':[], 'screwing around':[]}

    dict['screwing around'].append(apps[4])
    dict['screwing around'].append(apps[8])
    dict['screwing around'].append(apps[17])
    dict['screwing around'].append(apps[47])
    dict['weather and stuff'].append(apps[1])
    dict['weather and stuff'].append(apps[34])
    dict['weather and stuff'].append(apps[42])
    dict['screwing around'].append(apps[36])
    dict['putting effort'].append(apps[0])
    dict['putting effort'].append(apps[23])
    dict['putting effort'].append(apps[55])
    dict['putting effort'].append(apps[95])
    dict['eh stuff'].append(apps[13])
    dict['eh stuff'].append(apps[21])
    dict['eh stuff'].append(apps[48])
    dict['eh stuff'].append(apps[74])

    return dict
