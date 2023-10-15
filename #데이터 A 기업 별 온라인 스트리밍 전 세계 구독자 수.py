#데이터 A 기업 별 온라인 스트리밍 전 세계 구독자 수
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Arial'
matplotlib.rcParams['font.size'] = 8

labels = ['Paramount', 'HBO', 'iQlYl', 'Tencent Video', 'Disney Plus', 'Amazon Prime', 'Netflix']
values = ['61,000,000', '95,800,000', '101,000,000', '120,000,000', '146,100,000', '200,000,000', '238,400,000']
colors = ['y', 'b', 'lawngreen', 'orange', 'aqua', 'deepskyblue', 'r']

plt.bar(labels, values, color=colors)
plt.title('Streaming Company Total Subscriber')
plt.xlabel('Streaming Companies')
plt.ylabel('Subscriber (unit: person)')
