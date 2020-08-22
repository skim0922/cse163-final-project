'''
File for testing data and result validity
'''

from clean_data import filter_data
from clean_data import test_dataset
from analysis import regression_significance
from analysis import make_regression_model


def test_problem_one(clean_data, test_data):
    '''
    Tests problem one by comparing the p-values of both the
    test dataset and full dataset. Also prints out the
    r-squared values of the regressions with the full dataset.
    '''
    # race vs.poor mental health plot
    # regression and r-squared
    race_model_full = make_regression_model(data=clean_data,
                                            x_col='RACE_ELL_ORIGINS_'
                                                  'PERCENTILE',
                                            y_col='PCT_ADULTMENTAL'
                                                  'HEALTHNOTGOOD')
    race_model_test = make_regression_model(data=test_data,
                                            x_col='RACE_ELL_ORIGINS_'
                                                  'PERCENTILE',
                                            y_col='PCT_ADULTMENTAL'
                                                  'HEALTHNOTGOOD')
    check_significance(race_model_full, race_model_test, 'one part 1')
    print('Race correlation coefficient: ', race_model_full.rsquared)

    # socioeconomic vs poor mental health plot
    # regression and r-squared
    socioecon_model_full = make_regression_model(data=clean_data,
                                                 x_col='SOCIOECONOMIC_'
                                                       'PERCENTILE',
                                                 y_col='PCT_ADULT'
                                                 'MENTALHEALTHNOTGOOD')
    socioecon_model_test = make_regression_model(data=test_data,
                                                 x_col='SOCIOECONOMIC_'
                                                       'PERCENTILE',
                                                 y_col='PCT_ADULT'
                                                 'MENTALHEALTHNOTGOOD')
    # print(str(socioecon_model.summary()))
    # regression_significance(socioecon_model.pvalues)
    check_significance(socioecon_model_full, socioecon_model_test,
                       'one part 2')
    print('Socioeconomic correlation coefficient: ',
          socioecon_model_full.rsquared)


def test_problem_two(clean_data, test_data):
    '''
    Tests problem two by comparing the p-values of both the
    test dataset and full dataset. Also prints out the
    r-squared value of the regression with the full dataset.
    '''

    # ELL vs educ attainment less than a bachelors
    ell_vs_educ_model_full = make_regression_model(data=clean_data,
                                                   x_col='PCT_ENGLISH_LESS'
                                                         'THAN_VERY_WELL',
                                                   y_col='PCT_LESS_BACHELOR_'
                                                         'DEGREE')
    ell_vs_educ_model_test = make_regression_model(data=test_data,
                                                   x_col='PCT_ENGLISH_LESS'
                                                         'THAN_VERY_WELL',
                                                   y_col='PCT_LESS_BACHELOR_'
                                                         'DEGREE')
    check_significance(ell_vs_educ_model_full, ell_vs_educ_model_test, 'two')
    # calculate correlation coefficient
    print('Correlation coefficient: ', ell_vs_educ_model_full.rsquared)


def test_problem_three(clean_data):
    '''
    Takes in cleaned data and creates a regression model
    to calculate correlation coefficient
    '''
    # calculate actual correlation coefficient
    size_quintile_model = make_regression_model(data=clean_data,
                                                x_col='COMPOSITE_PERCENTILE',
                                                y_col='ACRES_TOTAL')
    print('Problem: three')
    print('Correlation coefficient: ', size_quintile_model.rsquared)


def test_problem_four(clean_data, test_data):
    '''
    Tests problem one by comparing the p-values of both the
    test dataset and full dataset. Also prints out the
    r-squared value of the regression with the full dataset.
    '''
    # socioeconomic percentile vs. educational attainment
    socioecon_vs_educ_model_full = make_regression_model(data=clean_data,
                                                         x_col='SOCIOECONOMIC_'
                                                               'PERCENTILE',
                                                         y_col='PCT_LESS_'
                                                               'BACHELOR_'
                                                               'DEGREE')
    socioecon_vs_educ_model_test = make_regression_model(data=test_data,
                                                         x_col='SOCIOECONOMIC_'
                                                               'PERCENTILE',
                                                         y_col='PCT_LESS_'
                                                               'BACHELOR_'
                                                               'DEGREE')
    check_significance(socioecon_vs_educ_model_full,
                       socioecon_vs_educ_model_test,
                       'four')
    # calculate correlation coefficient
    print('Correlation coefficient: ', socioecon_vs_educ_model_full.rsquared)


def test_problem_five(clean_data):
    '''
    Takes in cleaned data and calculates difference in percentage
    of people of color and English language learners by their
    socioeconomic quintile.
    '''
    poc_grouped = clean_data.groupby('SOCIOECONOMIC'
                                     '_QUINTILE')['PCT_PEOPLE_OF_COLOR'].sum()
    ell_grouped = clean_data.groupby('SOCIOECONOMIC'
                                     '_QUINTILE')['PCT_ENGLISH_'
                                                  'LESSTHAN_VERY_WELL'].sum()
    lowest_diff = poc_grouped['Lowest'] - ell_grouped['Lowest']
    second_low_diff = poc_grouped['Second lowest'] - ell_grouped['Second '
                                                                 'lowest']
    middle_diff = poc_grouped['Middle'] - ell_grouped['Middle']
    second_high_diff = poc_grouped['Second highest'] - ell_grouped['Second '
                                                                   'highest']
    highest_diff = poc_grouped['Highest'] - ell_grouped['Highest']
    print('Problem: five')
    print('Lowest quintile difference: ', lowest_diff)
    print('Second lowest quintile difference: ', second_low_diff)
    print('Middle quintile difference: ', middle_diff)
    print('Second highest quintile difference: ', second_high_diff)
    print('Highest quintile difference: ', highest_diff)


def check_significance(full_model_name, test_model_name, problem_num):
    '''
    Takes in the name for the models containing both the full set of data
    and the test data and checks to ensure that they are both indicating the
    same significance level
    '''
    full_significance = regression_significance(full_model_name.pvalues)
    test_significance = regression_significance(test_model_name.pvalues)
    print('Problem: ' + problem_num)
    if full_significance == test_significance:
        print('Both sets indicate the same significance level for this '
              'regression')
    else:
        print('Sets do not indicate the same significance level for '
              'this regression')


def main():
    clean_data = filter_data()
    test_data = test_dataset()
    test_problem_one(clean_data, test_data)
    test_problem_two(clean_data, test_data)
    test_problem_three(clean_data)
    test_problem_four(clean_data, test_data)
    test_problem_five(clean_data)


if __name__ == '__main__':
    main()
