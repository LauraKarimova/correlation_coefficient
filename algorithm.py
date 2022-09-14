# Import the libraries necessary for the algorithms to work: csv, numpy, scipy, matplotlib.
import csv
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

# Creation of an empty array array_AAPL, and subsequent loading of data from a csv file aapl.csv (AAPL stock price historical data).
array_AAPL = []
File_CSV = open('aapl.csv')
Data_CSV = csv.reader(File_CSV)
for row in Data_CSV:
    for now in row:
        array_AAPL.append(now)

# Creation of an empty array array_MSFT, and subsequent loading of data from a csv file msft.csv (MSFT stock price historical data).
array_MSFT = []
File_CSV_1 = open('msft.csv')
Data_CSV_1 = csv.reader(File_CSV_1)
for row_ms in Data_CSV_1:
    for now_ms in row_ms:
        array_MSFT.append(now_ms)
     
# Creation of an empty array array_AAL, and subsequent loading of data from a csv file aal.csv (AAL stock price historical data).
array_AAL = []
File_CSV_2 = open('aal.csv')
Data_CSV_2 = csv.reader(File_CSV_2)
for row_aal in Data_CSV_2:
    for now_aal in row_aal:
        array_AAL.append(now_aal)

#Changing type of the arrays.
array_AAPL_new = np.array(array_AAPL, dtype=np.float32)
array_MSFT_new = np.array(array_MSFT, dtype=np.float32)
array_AAL_new = np.array(array_AAL, dtype=np.float32)

#Using the corrcoef function of the library numpy, calculate the correlation coefficient between the two arrays array_AAPL_new and array_AAL_new.
r = np.corrcoef(array_AAPL_new, array_AAL_new)

#In order to confirm coefficient value, perform calculations using the Scipy library (Pearson's r, Spearman's rho and Kendall's tau).
# Pearson's r
scipy.stats.pearsonr(array_AAPL_new, array_AAL_new)

# Spearman's rho
scipy.stats.spearmanr(array_AAPL_new, array_AAL_new)

# Kendall's tau
scipy.stats.kendalltau(array_AAPL_new, array_AAL_new)

#Building the regression line using matplotlib library (strong positive straight-line correlation of assets).
plt.style.use('ggplot')
slope, intercept, r, p, stderr = scipy.stats.linregress(array_AAPL_new, array_MSFT_new)
line2 = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
line2

#Building a scatterplot based on the value of the correlation coefficient.
fig2, ax2 = plt.subplots()
ax2.plot(array_AAPL_new, array_MSFT_new, linewidth=0, marker='s', label='Data points')
ax2.plot(array_AAPL_new, intercept + slope * array_AAPL_new, label=line2)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend(facecolor='white')
plt.show()

#Building the regression line using matplotlib library (negative correlation of assets).
plt.style.use('ggplot')
slope, intercept, r, p, stderr = scipy.stats.linregress(array_AAPL_new, array_AAL_new)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
line

#Building a scatterplot based on the value of the correlation coefficient.
fig, ax = plt.subplots()
ax.plot(array_AAPL_new, array_AAL_new, linewidth=0, marker='s', label='Data points')
ax.plot(array_AAPL_new, intercept + slope * array_AAPL_new, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()
