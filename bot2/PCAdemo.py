
import numpy as np
import csv
def pca(X,k):
#    数据标准化
  n_samples, n_features = X.shape
#  计算协方差矩阵
  mean=np.array([np.mean(X[:,i]) for i in range(n_features)])
#  计算向量矩阵
  norm_X=X-mean
  scatter_matrix=np.dot(np.transpose(norm_X),norm_X)
#  对角矩阵
  eig_val, eig_vec = np.linalg.eig(scatter_matrix)
  eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(n_features)]
#  计算贡献率
  feature=np.array([ele[1] for ele in eig_pairs[:k]])
  data=np.dot(norm_X,np.transpose(feature))
  return data



with open('user_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    lst1 = [];
    lst2 = [];
    lst3 = [];
    for row in reader:
        if row[0]=='1 'and row[26]=='1':
            lst1.append(row)
        elif row[0]=='2 ' and row[26]=='1':
            lst2.append(row)
        elif row[0]=='3 'and row[26]=='1':
            lst3.append(row)
#    品牌1
    lst_1 = []
    for i in range(len(lst1)):
        lst_1.append(eval(lst1[i][1]))
    lst_2 = []
    for i in range(len(lst1)):
        lst_2.append(eval(lst1[i][2]))
    lst_3 = []
    for i in range(len(lst1)):
        lst_3.append(eval(lst1[i][3]))
    lst_4 = []
    for i in range(len(lst1)):
        lst_4.append(eval(lst1[i][4]))
    lst_5 = []
    for i in range(len(lst1)):
        lst_5.append(eval(lst1[i][5]))
    lst_6 = []
    for i in range(len(lst1)):
        lst_6.append(eval(lst1[i][6]))
    lst_7 = []
    for i in range(len(lst1)):
        lst_7.append(eval(lst1[i][7]))
    lst_8 = []
    for i in range(len(lst1)):
        lst_8.append(eval(lst1[i][8]))
    lst_9 = []
    for i in range(len(lst1)):
        lst_9.append(eval(lst1[i][9]))
    lst_10 = []
    for i in range(len(lst1)):
        lst_10.append(eval(lst1[i][10]))
    lst_11 = []
    for i in range(len(lst1)):
        lst_11.append(eval(lst1[i][11]))
    lst_12 = []
    for i in range(len(lst1)):
        lst_12.append(eval(lst1[i][12]))
    lst_13 = []
    for i in range(len(lst1)):
        lst_13.append(eval(lst1[i][13]))
    lst_14 = []
    for i in range(len(lst1)):
        lst_14.append(eval(lst1[i][14]))
    lst_15 = []
    for i in range(len(lst1)):
        lst_15.append(eval(lst1[i][15]))
    lst_16 = []
    for i in range(len(lst1)):
        lst_16.append(eval(lst1[i][16]))
    lst_17 = []
    for i in range(len(lst1)):
        lst_17.append(eval(lst1[i][17]))
    lst_18 = []
    for i in range(len(lst1)):
        lst_18.append(eval(lst1[i][18]))
    lst_19 = []
    for i in range(len(lst1)):
        lst_19.append(eval(lst1[i][19]))
    lst_20 = []
    for i in range(len(lst1)):
        lst_20.append(eval(lst1[i][20]))
    lst_21 = []
    for i in range(len(lst1)):
        lst_21.append(eval(lst1[i][21]))
    lst_22 = []
    for i in range(len(lst1)):
        lst_22.append(eval(lst1[i][22]))
    lst_23 = []
    for i in range(len(lst1)):
        lst_23.append(eval(lst1[i][23]))
    lst_24 = []
    for i in range(len(lst1)):
        lst_24.append(eval(lst1[i][24]))
    lst_25 = []
    for i in range(len(lst1)):
        lst_25.append(eval(lst1[i][25]))
    
#    品牌1
    print("-"*50)
    print("品牌1")
    X = np.array([lst_1,lst_2,lst_3,lst_4,lst_5,
                  lst_6,lst_7,lst_8,lst_9,lst_10,
                  lst_11,lst_12,lst_13,lst_14,lst_15,
                  lst_16,lst_17,lst_18,lst_19,lst_20,
                  lst_21,lst_22,lst_23,lst_24,lst_25])  
    print(pca(X,1))
#    品牌2
    lst_1 = []
    for i in range(len(lst2)):
        lst_1.append(eval(lst2[i][1]))
    lst_2 = []
    for i in range(len(lst2)):
        lst_2.append(eval(lst2[i][2]))
    lst_3 = []
    for i in range(len(lst2)):
        lst_3.append(eval(lst2[i][3]))
    lst_4 = []
    for i in range(len(lst2)):
        lst_4.append(eval(lst2[i][4]))
    lst_5 = []
    for i in range(len(lst2)):
        lst_5.append(eval(lst2[i][5]))
    lst_6 = []
    for i in range(len(lst2)):
        lst_6.append(eval(lst2[i][6]))
    lst_7 = []
    for i in range(len(lst2)):
        lst_7.append(eval(lst2[i][7]))
    lst_8 = []
    for i in range(len(lst2)):
        lst_8.append(eval(lst2[i][8]))
    lst_9 = []
    for i in range(len(lst2)):
        lst_9.append(eval(lst2[i][9]))
    lst_10 = []
    for i in range(len(lst2)):
        lst_10.append(eval(lst2[i][10]))
    lst_11 = []
    for i in range(len(lst2)):
        lst_11.append(eval(lst2[i][11]))
    lst_12 = []
    for i in range(len(lst2)):
        lst_12.append(eval(lst2[i][12]))
    lst_13 = []
    for i in range(len(lst2)):
        lst_13.append(eval(lst2[i][13]))
    lst_14 = []
    for i in range(len(lst2)):
        lst_14.append(eval(lst2[i][14]))
    lst_15 = []
    for i in range(len(lst2)):
        lst_15.append(eval(lst2[i][15]))
    lst_16 = []
    for i in range(len(lst2)):
        lst_16.append(eval(lst2[i][16]))
    lst_17 = []
    for i in range(len(lst2)):
        lst_17.append(eval(lst2[i][17]))
    lst_18 = []
    for i in range(len(lst2)):
        lst_18.append(eval(lst2[i][18]))
    lst_19 = []
    for i in range(len(lst2)):
        lst_19.append(eval(lst2[i][19]))
    lst_20 = []
    for i in range(len(lst2)):
        lst_20.append(eval(lst2[i][20]))
    lst_21 = []
    for i in range(len(lst2)):
        lst_21.append(eval(lst2[i][21]))
    lst_22 = []
    for i in range(len(lst2)):
        lst_22.append(eval(lst2[i][22]))
    lst_23 = []
    for i in range(len(lst2)):
        lst_23.append(eval(lst2[i][23]))
    lst_24 = []
    for i in range(len(lst2)):
        lst_24.append(eval(lst2[i][24]))
    lst_25 = []
    for i in range(len(lst2)):
        lst_25.append(eval(lst2[i][25]))

    print("-"*50)
    print("品牌2")
    X = np.array([lst_1,lst_2,lst_3,lst_4,lst_5,
                  lst_6,lst_7,lst_8,lst_9,lst_10,
                  lst_11,lst_12,lst_13,lst_14,lst_15,
                  lst_16,lst_17,lst_18,lst_19,lst_20,
                  lst_21,lst_22,lst_23,lst_24,lst_25])  
    print(pca(X,1))
#    品牌3
    lst_1 = []
    for i in range(len(lst3)):
        lst_1.append(eval(lst3[i][1]))
    lst_2 = []
    for i in range(len(lst3)):
        lst_2.append(eval(lst3[i][2]))
    lst_3 = []
    for i in range(len(lst3)):
        lst_3.append(eval(lst3[i][3]))
    lst_4 = []
    for i in range(len(lst3)):
        lst_4.append(eval(lst3[i][4]))
    lst_5 = []
    for i in range(len(lst3)):
        lst_5.append(eval(lst3[i][5]))
    lst_6 = []
    for i in range(len(lst3)):
        lst_6.append(eval(lst3[i][6]))
    lst_7 = []
    for i in range(len(lst3)):
        lst_7.append(eval(lst3[i][7]))
    lst_8 = []
    for i in range(len(lst3)):
        lst_8.append(eval(lst3[i][8]))
    lst_9 = []
    for i in range(len(lst3)):
        lst_9.append(eval(lst3[i][9]))
    lst_10 = []
    for i in range(len(lst3)):
        lst_10.append(eval(lst3[i][10]))
    lst_11 = []
    for i in range(len(lst3)):
        lst_11.append(eval(lst3[i][11]))
    lst_12 = []
    for i in range(len(lst3)):
        lst_12.append(eval(lst3[i][12]))
    lst_13 = []
    for i in range(len(lst3)):
        lst_13.append(eval(lst3[i][13]))
    lst_14 = []
    for i in range(len(lst3)):
        lst_14.append(eval(lst3[i][14]))
    lst_15 = []
    for i in range(len(lst3)):
        lst_15.append(eval(lst3[i][15]))
    lst_16 = []
    for i in range(len(lst3)):
        lst_16.append(eval(lst3[i][16]))
    lst_17 = []
    for i in range(len(lst3)):
        lst_17.append(eval(lst3[i][17]))
    lst_18 = []
    for i in range(len(lst3)):
        lst_18.append(eval(lst3[i][18]))
    lst_19 = []
    for i in range(len(lst3)):
        lst_19.append(eval(lst3[i][19]))
    lst_20 = []
    for i in range(len(lst3)):
        lst_20.append(eval(lst3[i][20]))
    lst_21 = []
    for i in range(len(lst3)):
        lst_21.append(eval(lst3[i][21]))
    lst_22 = []
    for i in range(len(lst3)):
        lst_22.append(eval(lst3[i][22]))
    lst_23 = []
    for i in range(len(lst3)):
        lst_23.append(eval(lst3[i][23]))
    lst_24 = []
    for i in range(len(lst3)):
        lst_24.append(eval(lst3[i][24]))
    lst_25 = []
    for i in range(len(lst3)):
        lst_25.append(eval(lst3[i][25]))

    print("-"*50)
    print("品牌3")
    X = np.array([lst_1,lst_2,lst_3,lst_4,lst_5,
                  lst_6,lst_7,lst_8,lst_9,lst_10,
                  lst_11,lst_12,lst_13,lst_14,lst_15,
                  lst_16,lst_17,lst_18,lst_19,lst_20,
                  lst_21,lst_22,lst_23,lst_24,lst_25])  
    print(pca(X,1))
