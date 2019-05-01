import pandas as pd

excel_file = "Subscriptions0726.xlsx"

cohort = "Momentum Cohort Analysis May 1-7.xlsx"

cohort_data = pd.read_excel(cohort)

subscriptions_data = pd.read_excel(excel_file)

emails0 = cohort_data['User'].values
emails1 = subscriptions_data['email'].values

matches = []

for e in emails0:
	for em in emails1:
		if em == e:
			matches.append(e)

print(matches)
print(len(matches))

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

news = Remove(matches)
print(news)
print(len(news))
