import csv
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    # Get high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
            date = datetime.strptime(row[2], '%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {date}")
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)
    
import matplotlib.pyplot as plt
# Plot the high temperatures.

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c="green",alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
fig.autofmt_xdate()

# Format plot.
ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
