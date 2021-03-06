
import matplotlib.pyplot as plt
import numpy as np
iter_list = []
loss_train_list = []
acc_train_list = []
loss_val_list = []
acc_val_list = []

loss_train_list1 = []
acc_train_list1 = []
loss_val_list1 = []
acc_val_list1 = []

loss_train_list2 = []
acc_train_list2 = []
loss_val_list2 = []
acc_val_list2 = []

loss_train_list3 = []
acc_train_list3 = []
loss_val_list3 = []
acc_val_list3 = []

loss_train_list4 = []
acc_train_list4 = []
loss_val_list4 = []
acc_val_list4 = [] 

loss_train_list5 = []
acc_train_list5 = []
loss_val_list5 = []
acc_val_list5 = []
with open('../log/batch_32.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split("  ")
        iter, loss_train, acc_train, loss_val, acc_val = line[:5]
        iter_list.append(int(iter.split(':')[1]))
        loss_train_list.append(float(loss_train.split(':')[1]))
        acc_train_list.append(float(acc_train.split(':')[1]))
        loss_val_list.append(float(loss_val.split(':')[1]))
        acc_val_list.append(float(acc_val.split(':')[1]))
with open('../log/batch_64.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split("  ")
        iter, loss_train1, acc_train1, loss_val1, acc_val1 = line[:5]
        loss_train_list1.append(float(loss_train1.split(':')[1]))
        acc_train_list1.append(float(acc_train1.split(':')[1]))
        loss_val_list1.append(float(loss_val1.split(':')[1]))
        acc_val_list1.append(float(acc_val1.split(':')[1]))

with open('../log/batch_128.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split("  ")
        iter, loss_train2, acc_train2, loss_val2, acc_val2 = line[:5]
        loss_train_list2.append(float(loss_train2.split(':')[1]))
        acc_train_list2.append(float(acc_train2.split(':')[1]))
        loss_val_list2.append(float(loss_val2.split(':')[1]))
        acc_val_list2.append(float(acc_val2.split(':')[1]))
with open('../log/batch_256.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split("  ")
        iter, loss_train3, acc_train3, loss_val3, acc_val3 = line[:5]
        loss_train_list3.append(float(loss_train3.split(':')[1]))
        acc_train_list3.append(float(acc_train3.split(':')[1]))
        loss_val_list3.append(float(loss_val3.split(':')[1]))
        acc_val_list3.append(float(acc_val3.split(':')[1]))
with open('../log/batch_512.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split("  ")
        print(line[0])
        iter, loss_train4, acc_train4, loss_val4, acc_val4 = line[:5]
        loss_train_list4.append(float(loss_train4.split(':')[1]))
        acc_train_list4.append(float(acc_train4.split(':')[1]))
        loss_val_list4.append(float(loss_val4.split(':')[1]))
        acc_val_list4.append(float(acc_val4.split(':')[1]))
# with open('../log/batch_1024.txt', 'r') as file:
#     for line in file.readlines():
#         line = line.strip().split("  ")
#         iter, loss_train5, acc_train5, loss_val5, acc_val5 = line[:]
#         loss_train_list5.append(float(loss_train5.split(':')[1]))
#         acc_train_list5.append(float(acc_train5.split(':')[1]))
#         loss_val_list5.append(float(loss_val5.split(':')[1]))
#         acc_val_list5.append(float(acc_val5.split(':')[1]))
ax1 = plt.subplot(2, 2, 1, frameon=True)
plt.plot(iter_list, loss_train_list, '--', label="32")
plt.plot(iter_list, loss_train_list1, '-.', label="64")
plt.plot(iter_list, loss_train_list2, ':', label='128')
plt.plot(iter_list, loss_train_list3, '--', label='256')
plt.plot(iter_list, loss_train_list4, label='512')
# plt.plot(iter_list, loss_train_list5, ':', label='1024')
plt.title('training_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
# plt.legend()
ax2 = plt.subplot(2, 2, 2, frameon=True)
plt.plot(iter_list, acc_train_list, '--', label="32")
plt.plot(iter_list, acc_train_list1, '-.', label="64")
plt.plot(iter_list, acc_train_list2, ':', label='128')
plt.plot(iter_list, acc_train_list3, '--', label='256')
plt.plot(iter_list, acc_train_list4, '-.', label='512')
# plt.plot(iter_list, acc_train_list5, ':', label='1024')
plt.title('training_acc(top1)')
plt.xlabel('epochs')
plt.ylabel('acc')

ax3 = plt.subplot(2, 2, 3, frameon=True)
plt.plot(iter_list, loss_val_list, '--', label="32")
plt.plot(iter_list, loss_val_list1, '-.', label="64")
plt.plot(iter_list, loss_val_list2, ':', label='128')
plt.plot(iter_list, loss_val_list3, '--', label='256')
plt.plot(iter_list, loss_val_list4, '-.', label='512')
# plt.plot(iter_list, loss_val_list5, ':', label='1024')
plt.title('val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
# plt.legend()
ax4 = plt.subplot(2, 2, 4, frameon=True)
plt.plot(iter_list, acc_val_list, '--', label="32")
plt.plot(iter_list, acc_val_list1, '-.', label="64")
plt.plot(iter_list, acc_val_list2, ':', label='128')
plt.plot(iter_list, acc_val_list3, '--', label='256')
plt.plot(iter_list, acc_val_list4, '-.', label='512')
# plt.plot(iter_list, acc_val_list5, ':', label='1024')
plt.title('val_acc(top1)')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend()
plt.tight_layout()
plt.show()
