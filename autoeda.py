from dataprep.eda import create_report
import pandas as pd

df = pd.read_csv('indian-weather-repository-daily-snapshot\IndianWeatherRepository.csv')
create_report(df).show_browser()