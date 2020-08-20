'''
File to perform data analysis
'''

from clean_data import filter_data
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


def plot_problem_one(clean_data):
    # filtered data
    # race vs.poor mental health plot
    sns.lmplot(x='RACE_ELL_ORIGINS_PERCENTILE',
               y='PCT_ADULTMENTALHEALTHNOTGOOD',
               scatter=True, data=clean_data, fit_reg=True)
    plt.xlabel('Race, ELL, and Origins Index Percentile')
    plt.ylabel('Percentage of Adults Without Good Mental Health')
    plt.title('Race, English Language Learners(ELL), and Origins Index'
              'Percentile vs Percentage of Adults Without Good Mental Health')
    plt.savefig('race_vs_mentalhealth.png', bbox_inches='tight')
    # regression and r-squared
    race_model = make_regression_model(data=clean_data,
                                       x_col='RACE_ELL_ORIGINS_PERCENTILE',
                                       y_col='PCT_ADULTMENTALHEALTHNOTGOOD')
    # print(str(race_model.summary()))
    regression_significance(race_model.pvalues)

    # socioeconomic vs poor mental health plot
    sns.lmplot(x='SOCIOECONOMIC_PERCENTILE',
               y='PCT_ADULTMENTALHEALTHNOTGOOD',
               scatter=True, data=clean_data, fit_reg=True)
    plt.xlabel('Socioeconomic Disadvantage Index Percentile')
    plt.ylabel('Percentage of Adults Without Good Mental Health')
    plt.title('Socioeconomic Disadvantage Index'
              'Percentile vs Percentage of Adults Without Good Mental Health')
    plt.savefig('socioecon_vs_mentalhealth.png', bbox_inches='tight')
    # regression and r-squared
    socioecon_model = make_regression_model(data=clean_data,
                                            x_col='SOCIOECONOMIC_PERCENTILE',
                                            y_col='PCT_ADULT'
                                            'MENTALHEALTHNOTGOOD')
    # print(str(socioecon_model.summary()))
    regression_significance(socioecon_model.pvalues)

    # comparison
    if race_model.rsquared > socioecon_model.rsquared:
        print('The Race, English Language Learners(ELL), and Origins Index'
              'has a stronger correlation with having poor mental health')
    elif race_model.rsquared < socioecon_model.rsquared:
        print('The Socioeconomic Disadvantage Index Percentile has a '
              'stronger correlation with having poor mental health')
    else:
        print('Both race and socioeconomic status have the same'
              'correlation with having poor mental health')


def plot_problem_two(clean_data):
    # ELL vs educ attainment less than a bachelors
    sns.lmplot(x='PCT_ENGLISH_LESSTHAN_VERY_WELL',
               y='PCT_LESS_BACHELOR_DEGREE',
               scatter=True, data=clean_data, fit_reg=True)
    plt.xlabel('Percentage of English Language Learners')
    plt.ylabel('Percentage of People with an Educational Attainment Less Than'
               'a Bachelors Degree')
    plt.title('Percentage of English Language Learners vs Percentage of People'
              'with an Educational Attainment Less Than a Bachelors Degree')
    plt.savefig('/Users/sahana/Desktop/github/cse163-final-project/'
                'ell_vs_educ.png')
    ell_vs_educ_model = make_regression_model(data=clean_data,
                                              x_col='PCT_ENGLISH_LESS'
                                              'THAN_VERY_WELL',
                                              y_col='PCT_LESS_BACHELOR_DEGREE')
    regression_significance(ell_vs_educ_model)


def plot_problem_three(clean_data):
    # total acres vs. index quintile
    sns.catplot(x='COMPOSITE_QUINTILE',
                y='ACRES_TOTAL',
                data=clean_data,
                kind='bar',
                order=['Lowest', 'Second lowest', 'Middle',
                       'Second highest', 'Highest'])
    plt.xlabel('Composite Index Quintile (Level of Priority)')
    plt.ylabel('Total Acres')
    plt.xticks(rotation=-45)
    plt.title('Total Neighborhood Acres by Composite Index Quintile')
    plt.savefig('size_vs_quintile.png', bbox_inches='tight')


def plot_problem_four(clean_data):
    # socioeconomic percentile vs. educational attainment
    sns.lmplot(x='SOCIOECONOMIC_PERCENTILE',
               y='PCT_LESS_BACHELOR_DEGREE',
               scatter=True,
               fit_reg=True,
               data=clean_data)
    plt.xlabel('Socioeconomic Disadvantage Percentile')
    plt.ylabel('Percent of People with Less than Bachelors Degree')
    plt.title('Socioeconomic Disadvantage vs. Educational Attainment')
    plt.savefig('socioecon_vs_education.png', bbox_inches='tight')
    # regression analysis
    socioecon_vs_educ_model = make_regression_model(data=clean_data,
                                                    x_col='SOCIOECONOMIC_'
                                                          'PERCENTILE',
                                                    y_col='PCT_LESS_'
                                                          'BACHELOR_DEGREE')
    regression_significance(socioecon_vs_educ_model.pvalues)


def plot_problem_five(clean_data):
    # Percent POC & ELL vs. socioeconomic index
    fig, [ax1, ax2] = plt.subplots(2, figsize=(10, 10), ncols=1)
    sns.barplot(x='SOCIOECONOMIC_QUINTILE',
                y='PCT_PEOPLE_OF_COLOR',
                data=clean_data,
                order=['Lowest', 'Second lowest', 'Middle',
                       'Second highest', 'Highest'],
                ax=ax1)
    ax1.set_xlabel('Socioeconomic Disadvantage Quintile')
    ax1.set_ylabel('Percent of People of Color')
    ax1.set_title('Percent of POC by Socioeconomic Disadvantage Quintile')
    sns.barplot(x='SOCIOECONOMIC_QUINTILE',
                y='PCT_ENGLISH_LESSTHAN_VERY_WELL',
                data=clean_data,
                order=['Lowest', 'Second lowest', 'Middle',
                       'Second highest', 'Highest'],
                ax=ax2)
    ax2.set_xlabel('Socioeconomic Disadvantage Quintile')
    ax2.set_ylabel('Percent of English Language Learners')
    ax2.set_title('Percent of ELL by Socioeconomic Disadvantage Quintile')
    fig.savefig('poc&ell_vs_socioecon.png', bbox_inches='tight')


def make_regression_model(data, x_col, y_col):
    x = sm.add_constant(data[x_col])
    model = sm.OLS(data[y_col], x).fit()
    return model


def regression_significance(abs_p_values):
    abs_x, abs_y = abs_p_values
    p_value = abs_y/2
    alpha = 0.05
    if p_value < alpha:
        print('reject null hypothesis and '
              'accept alternative hypothesis')
    else:
        print('accept null hypothesis')


def main():
    clean_data = filter_data()
    plot_problem_one(clean_data)
    plot_problem_two(clean_data)
    plot_problem_three(clean_data)
    plot_problem_four(clean_data)
    plot_problem_five(clean_data)


if __name__ == '__main__':
    main()
