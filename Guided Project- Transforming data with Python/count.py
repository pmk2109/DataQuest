import read
from collections import Counter

df = read.load_data()
headlines = df.headline

headline_list = ""
for i in range(len(headlines)):
    headline_list += str(headlines[i]).strip("!@^&*():;<>,.?/[]{}+=|-_ ") + " "
headline_list = headline_list.lower()
headline_list = headline_list.split(" ")

headline_clean = []
for i in range(len(headline_list)):
    if headline_list[i] in "!@^&*():;<>,.?/[]{}+=|-_ ":
        pass
    else:
        headline_clean.append(headline_list[i])

headline_dict = Counter(headline_clean)
headline_count_list = sorted(headline_dict, key=headline_dict.get, reverse=True)
print(headline_count_list[:100])