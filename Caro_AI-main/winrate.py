import matplotlib.pyplot as plt

depth = [1, 2, 3]
win_rate = [55, 78, 92]

plt.plot(depth, win_rate, marker='o')
plt.xlabel("Độ sâu tìm kiếm")
plt.ylabel("Tỷ lệ thắng (%)")
plt.title("Tỷ lệ thắng theo độ sâu tìm kiếm")
plt.grid(True)
plt.show()