import matplotlib.pyplot as plt

depth = [1, 2, 3]
time = [0.0000, 0.5066, 1.25]

plt.plot(depth, time, marker='o')
plt.xlabel("Độ sâu tìm kiếm")
plt.ylabel("Thời gian tính toán trung bình (s)")
plt.title("Thời gian tính toán trung bình theo độ sâu tìm kiếm")
plt.grid(True)
plt.show()