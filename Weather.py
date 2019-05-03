import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_2014.csv'
with open(filename_1) as file_1:
    with open(filename_2) as  file_2:
        reader_1 = csv.reader(file_1)
        reader_2 = csv.reader(file_2)
        header_row_1 = next(reader_1)
        header_row_2 = next(reader_2)

        high_temp_1 = []
        dates_1= []
        low_temp_1 = []
        for row in reader_1:
            try:
                high = round((int(row[1]) - 32) * 5 / 9)
                date = datetime.strptime(row[0], '%Y-%m-%d')
                low = round((int(row[3]) - 32) * 5 / 9)
            except:
                print(date,'missing data')
            else:
                high_temp_1.append(high)
                low_temp_1.append(low)
                dates_1.append(date)

        high_temp_2 = []
        dates_2 = []
        low_temp_2 = []
        for row in reader_2:
            try:
                high = round((int(row[1]) - 32) * 5 / 9)
                date = datetime.strptime(row[0], '%Y-%m-%d')
                low = round((int(row[3]) - 32) * 5 / 9)
            except:
                print(date, 'missing data')
            else:
                high_temp_2.append(high)
                low_temp_2.append(low)
                dates_2.append(date)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.title("Temperature in Sitka and Death Valey in 2014")
    plt.xlabel("Date")
    plt.ylabel("Celcius deegres")
    plt.plot(dates_1, high_temp_1, c='red',linewidth = 1)
    plt.plot(dates_1, low_temp_1, c='blue',linewidth = 1)
    plt.fill_between(dates_1,high_temp_1,low_temp_1,facecolor = 'blue',alpha = 0.1)
    plt.plot(dates_2, high_temp_2, c='yellow', linewidth=1)
    plt.plot(dates_2, low_temp_2, c='green', linewidth=1)
    plt.fill_between(dates_2, high_temp_2, low_temp_2, facecolor='green', alpha=0.1)
    plt.tick_params(axis='both', which='major', labelsize=16)
    fig.autofmt_xdate()
    plt.show()
