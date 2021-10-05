

#coding:windows-1252
'''
app to be added:
[title of app, key words/description, catergory]
'''
import nltk

'''
{folder x:
[[title of app,
key words/description,
category], [...]], folder y: [[...]]}
'''

'''
total_res_dict = {folder 1:[dict_match_score, word_sim_score]...folder 2:...}
for each folder in folders:
    total sim_word_score = 0
    for each app in folder:
       if(<30 percent of key words match)
            sim score += 1
        elif(30-60 percent of key words match)
            sim score +=2
        elif(60-100)
            sim score += 3
        if(any part of app to be added title is in app title)
            sim score += 3
    dict_match score = 0 //dictionary of folder 
    if(category of app to be added is in dict)
        add the count of the category to dict_match
    //some thoughts to consider: maybe look into the percent of the folder that has the desired app category?
    total_res_dict.update(folder:[dict_match_score, word_sim_score])
then search total_res_dict for greatest (average? -how we weight these two vars is still up in the air) of dict_match_score and word_sim_score
and assign the app to be added to the corresponding folder
'''



from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import numpy as np
dict_of_folders = {'putting effort': [{'title': ['Evernote - stay organized'], 'keywords': ['Evernote', 'Productivity', 'Utilities', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Productivity']}, {'title': ['iTranslate - Language Translator & Dictionary'], 'keywords': ['iTranslate', 'Productivity', 'Reference', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Productivity']}, {'title': ['Mint: Personal Finance, Budget, Bills & Money'], 'keywords': ['Mint.com', 'Finance', 'Productivity', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Finance']}, {'title': ['Indeed Job Search'], 'keywords': ['Indeed Inc.', 'Business', 'Utilities', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Business']}], 'weather and stuff': [{'title': ['WeatherBug - Local Weather, Radar, Maps, Alerts'], 'keywords': ['WeatherBug', 'Weather', 'Lifestyle', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Weather']}, {'title': ['iStellar'], 'keywords': ['AstroArts Inc.', 'Navigation', 'Education', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Navigation']}, {'title': ['The Weather Channel: Forecast, Radar & Alerts'], 'keywords': ['The Weather Channel Interactive', 'Weather', 'Lifestyle', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Weather']}], 'eh stuff': [{'title': ['TripAdvisor Hotels Flights Restaurants'], 'keywords': ['Tripadvisor', 'Travel', 'Lifestyle', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Travel']}, {'title': ['Lifesum – Inspiring healthy lifestyle app'], 'keywords': ['Lifesum AB', 'Health &amp; Fitness', 'Lifestyle', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Health &amp; Fitness']}, {'title': ['Amazon App: shop, scan, compare, and read reviews'], 'keywords': ['AMZN Mobile LLC', 'Shopping', 'Lifestyle', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Shopping']}, {'title': ['HomeBudget with Sync'], 'keywords': ['Anishu', 'Finance', 'Lifestyle', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Finance']}], 'screwing around': [{'title': ['Shanghai Mahjong'], 'keywords': ['MobileAge LLC', 'Games', 'Entertainment', 'Puzzle', 'Board', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Games']}, {'title': ['Ms. PAC-MAN'], 'keywords': ['BANDAI NAMCO Entertainment America Inc.', 'Games', 'Entertainment', 'Casual', 'Family', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Games']}, {'title': [':) Sudoku +'], 'keywords': ['Jason Linhart', 'Games', 'Entertainment', 'Board', 'Puzzle', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Games']}, {'title': ['Fish Tycoon'], 'keywords': ['LDW Software', 'LLC', 'Games', 'Family', 'Entertainment', 'Simulation', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['LLC']}, {'title': ['iFart - The Original Fart Sounds App'], 'keywords': ['InfoMedia', 'Entertainment', 'Utilities', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch'], 'cat': ['Entertainment']}]}

app_to_be_added = {'title': ['Among Us!'], 'keywords':['Among Us!', 'InnerSloth LLC', 'Games', 'Action', 'Simulation', 'ios apps', 'app', 'appstore', 'app store', 'iphone', 'ipad', 'ipod touch', 'itouch', 'itunes'], 'cat': ["Games"]}
#[['folder', [file, file2]]]

def find_folder(dict_of_folders, app_to_be_added):
    arr = []
    dict_fin = {}
    for folder in dict_of_folders:
        dict_cat = {}
        total_sim_score = 0
        total_cat_score = 0
        for dic in dict_of_folders[folder]:
            for key in dic:
                if key == 'title':
                    title_of_app_to_be_added = app_to_be_added['title']
                    text_tokens_app_to_be_added = word_tokenize(title_of_app_to_be_added[0])
                    tokens_without_sw_app_to_be_added = [word for word in text_tokens_app_to_be_added if
                                                         not word in stopwords.words()]
                    text_tokens_app = word_tokenize(dic[key][0])
                    tokens_without_sw_app = [word for word in text_tokens_app if not word in stopwords.words()]
                    parsed_app_to_be_added = [elem for elem in tokens_without_sw_app_to_be_added if
                                              elem.isalpha() == True]
                    parsed_app = [elem for elem in tokens_without_sw_app if elem.isalpha() == True]
                    common_elements = np.intersect1d(parsed_app_to_be_added, parsed_app)
                    if (len(common_elements) > 0):
                        total_sim_score = total_sim_score + 3
                if key == 'keywords':
                    common_elements = np.intersect1d(dic[key], app_to_be_added['keywords'])
                    percent = len(common_elements) / len(app_to_be_added['keywords'])
                    if (percent <= .50):
                        total_sim_score += 1
                    elif (percent > .50 and percent <= .75):
                        total_sim_score += 2
                    else:
                        total_sim_score += 3
                if key == 'cat':
                    category = dic[key][0]
                    if category in dict_cat:
                        dict_cat[category] += 1
                    else:
                        dict_cat[category] = 1
        for item in dict_cat:
            if item == app_to_be_added['cat'][0]:
                total_cat_score = dict_cat[item]
        dict_res = {folder: total_cat_score + total_sim_score}
        dict_fin.update(dict_res)
    folder_to_be = max(dict_res, key=dict_res.get)
    for folder in dict_of_folders:
        apps = []
        for dic in dict_of_folders[folder]:
            apps.append(dic['title'][0])
        arr.append([folder, apps])
    for index, elem in enumerate(arr):
        if(elem[0] == folder_to_be):
            arr[index][1].append(app_to_be_added['title'][0])
    return max(dict_res, key=dict_res.get), arr

print(find_folder(dict_of_folders, app_to_be_added))

'''
('screwing around', [['putting effort', ['Evernote - stay organized', 'iTranslate - Language Translator & Dictionary', 'Mint: Personal Finance, Budget, Bills & Money', 'Indeed Job Search']], ['weather and stuff', ['WeatherBug - Local Weather, Radar, Maps, Alerts', 'iStellar', 'The Weather Channel: Forecast, Radar & Alerts']], ['eh stuff', ['TripAdvisor Hotels Flights Restaurants', 'Lifesum – Inspiring healthy lifestyle app', 'Amazon App: shop, scan, compare, and read reviews', 'HomeBudget with Sync']], ['screwing around', ['Shanghai Mahjong', 'Ms. PAC-MAN', ':) Sudoku +', 'Fish Tycoon', 'iFart - The Original Fart Sounds App', 'Among Us!']]])


'''
