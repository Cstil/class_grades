def read_data():
    import csv
    import numpy as np
    columns = np.loadtxt('grades1.csv',delimiter=',',skiprows=0,unpack=True,dtype='str')
    grades = columns[1].astype(float)
    return grades
print read_data()
