'''
File for testing data
'''

from clean_data import filter_data
from clean_data import test_dataset
import statsmodels.api as sm


def test_problem_one(clean_data, test_data):
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


def test_problem_two(clean_data, test_data):
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


def test_problem_four(clean_data, test_data):
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


def make_regression_model(data, x_col, y_col):
    x = sm.add_constant(data[x_col])
    model = sm.OLS(data[y_col], x).fit()
    return model


def regression_significance(p_values):
    x, y = p_values
    p_value = y/2
    alpha = 0.05
    return p_value < alpha


def check_significance(full_model_name, test_model_name, problem_num):
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
    test_problem_four(clean_data, test_data)


if __name__ == '__main__':
    main()
