import matplotlib.pyplot as plt

D = { 'CNTT': 500, 'Toan': 310,
'Hoa': 150, 'Sinh': 280, 'Giao Duc': 340}

plt.bar(range(len(D)), list(D.values()),color='g')
plt.xticks(range(len(D)), D.keys())

plt.title('Số lượng Sinh viên')
plt.show()
