import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks)

utm_source_counts = ad_clicks.groupby(['utm_source']).user_id.count().reset_index()
print(utm_source_counts)


ad_clicks['is_click'] = [not x for x in ad_clicks.ad_click_timestamp.isnull()]
print(ad_clicks)


clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True]+clicks_pivot[False])

print(clicks_pivot)

numbers_shown_AandB = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

print(numbers_shown_AandB)

numbers_isclick_AandB = ad_clicks.groupby(['is_click', 'experimental_group']).user_id.count().reset_index()

numbers_isclick_AandB_pivot =numbers_isclick_AandB.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()

numbers_isclick_AandB_pivot['percent_clicked'] = numbers_isclick_AandB_pivot[True] / (numbers_isclick_AandB_pivot[True]+numbers_isclick_AandB_pivot[False])

print(numbers_isclick_AandB_pivot)

a_clicks = ad_clicks[ad_clicks["experimental_group"]=="A"]
b_clicks = ad_clicks[ad_clicks["experimental_group"]=="B"]

a_clicks_byday = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b_clicks_byday = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()

a_clicks_byday_pivot = a_clicks_byday.pivot(columns='is_click', index='day', values='user_id').reset_index()
b_clicks_byday_pivot = b_clicks_byday.pivot(columns='is_click', index='day', values='user_id').reset_index()

a_clicks_byday_pivot['percent'] =a_clicks_byday_pivot[True]/(a_clicks_byday_pivot[True]+a_clicks_byday_pivot[False])
b_clicks_byday_pivot['percent'] =b_clicks_byday_pivot[True]/(b_clicks_byday_pivot[True]+b_clicks_byday_pivot[False])
print(a_clicks_byday_pivot)
print(b_clicks_byday_pivot)
