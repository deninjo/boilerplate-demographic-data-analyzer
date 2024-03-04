import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = men['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df['education'] == 'Bachelors'
    percentage_bachelors = ((bachelors.sum()/df['education'].count())*100).round(1)


    # percentage with salary >50K
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    education_levels = ['Bachelors', 'Masters', 'Doctorate']
    filtered_df = df[df['education'].isin(education_levels)]
    higher_education_rich = (((filtered_df['salary'] == '>50K').sum()/df['education'].count())*100).round(1)
    
    # What percentage of people without advanced education make more than 50K?
    education_levels = ['Bachelors', 'Masters', 'Doctorate']
    filtered_df = df[~df['education'].isin(education_levels)]
    lower_education_rich = (((filtered_df['salary'] == '>50K').sum()/df['education'].count())*100).round(1)
    
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hrs = df[df['hours-per-week'] == df['hours-per-week'].min()]
    num_min_workers = (((min_hrs['salary'] == '>50K').sum()/df['salary'].count())*100).round(1)

    rich_percentage = (((df['salary'] == ">50K").sum()/df['salary'].count())*100).round(1)

    # What country has the highest percentage of people that earn >50K?
    high_sal = df[df['salary'] == '>50K']
    high_sal = pd.DataFrame(high_sal['native-country'].value_counts())
    highest_earning_country = high_sal.index[0]
    highest_earning_country_percentage = (((high_sal['native-country'].value_counts().max())/high_sal['native-country'].count())*100).round(1)


    # Identify the most popular occupation for those who earn >50K in India.
    high_sal_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_occ = pd.DataFrame(high_sal_india['occupation'].value_counts())
    top_IN_occupation = top_occ.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
