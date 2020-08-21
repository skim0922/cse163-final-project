'''
File to clean and filter data
'''
import pandas as pd


def filter_data():
    '''
    Creates a master dataframe with only necessary columns,
    drops na values.
    '''
    df = pd.read_csv('data/Racial_and_Social_Equity_Composite_Index.csv')
    df = df.dropna()
    data = df[['PCT_ADULTMENTALHEALTHNOTGOOD', 'RACE_ELL_ORIGINS_PERCENTILE',
               'SOCIOECONOMIC_PERCENTILE', 'PCT_ENGLISH_LESSTHAN_VERY_WELL',
               'PCT_PEOPLE_OF_COLOR', 'SOCIOECONOMIC_QUINTILE',
               'PCT_LESS_BACHELOR_DEGREE', 'ACRES_TOTAL', 'COMPOSITE_QUINTILE',
              'NAME10', 'COMPOSITE_PERCENTILE']]
    # rename column to shorten it
    data = data.replace({'Highest priority/Most disadvantaged': 'Highest'})
    return data


def test_dataset():
    '''
    Creates a smaller dataset to use for testing
    '''
    data = filter_data()
    test_data = data.loc[1:20, :]
    # print(test_data)
    return test_data


def main():
    filter_data()


if __name__ == '__main__':
    main()
