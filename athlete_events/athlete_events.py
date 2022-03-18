import matplotlib.pyplot as plt
import pandas as pd

def print_menu():
    print("==========================================")
    print("Please, enter the numbers of the filters you would like to use (e.g. 234 if you want to filter by age, team and year):")
    print("1.Sex\n2.Age\n3.Team\n4.Year\n5.Sport\n")

def get_menu_choice():
    choice = input("> ")
    flag = True
    while flag: #while input is greater than 5 choices and not all digits
        flag =  False
        if len(choice) > 5:
            print("Too many options") 
            flag = True
        else: 
            for i in choice:
                if i.isdigit() == False:
                    print(f"{i} is not a valid choice.")
                    flag = True #flag raised if inputs contain non valid 
                    break
            
                elif (int(i) < 1 or int(i) > 5) and i.isdigit(): #if i is an integer but not in correct range of inputs
                    print(f"{i} is not a valid choice.")
                    flag = True #flag raised if inputs contain non valid 
                    break
    
        if flag == True:
            print_menu()
            choice = input("> ")

    choice_list = [d for d in choice]
    return choice_list

def validate_choice(choice_list):
    choice_dict = {} #dictionary to hold the users filter type and filter choice in key and value e.g. Age: 24
    for choice in choice_list:
        flag = True
        if choice == '1':
            while flag:
                flag = False
                sex = input("Enter 'F' for female, 'M' for male: ")
                sex = sex.title()
                if sex != 'F' and sex != 'M':
                    print("Invalid input")
                    flag = True

            choice_dict.update({"Sex": sex})

        elif choice == '2':
            while flag:
                flag = False
                try:
                    age = input("Please enter age in years: ")
                    age = int(age)
                    choice_dict.update({"Age": age})
                except ValueError:
                    print("That is not a number")
                    flag = True

        elif choice == '3':
            team = input("Please enter the team/country: ")
            team = team.lower() #format string to all lowercase
            team = team.title() #format string to capitilize first letter of each word
            choice_dict.update({"Team": team})
        
        elif choice == '4':
            while flag:
                flag = False
                try:
                    year = input("Please enter the year of the Olympic: ")
                    year = int(year)
                    choice_dict.update({"Year": year})
                except ValueError:
                    print("That is not a number")
                    flag = True

        elif choice == '5':
            sport = input("Please enter the sport: ")
            sport = sport.lower() #format string to all lowercase
            sport = sport.title() #format string to capitilize first letter of each word
            choice_dict.update({"Sport": sport})

    return choice_dict

def filtering(df, choice_list):
    filters_dict = validate_choice(choice_list) #gets the desired filter choice from each column returns as a dict
    filtered_df = df.loc[(df[list(filters_dict)] == pd.Series(filters_dict)).all(axis=1)] #creates another seires from the filters and compares with the main data frame to see where there is a match in ALL columns and then locate those indexs
    if len(filtered_df) != 0:
        return filtered_df, len(filtered_df)
    else:
        print("No records found")
        return 0, 0

def plotting(f_df, df_length):
    print(f"{df_length} records found.")
    if df_length < 100:
        f_df.plot(kind = 'scatter', x = 'ID', y = 'Weight', color = 'red')
        plt.savefig('scatter.png')
        print("File scatter.png saved")
    
    elif df_length >= 100:
        bins = 12
        plt.hist(f_df['Weight'], bins)
        plt.savefig('hist.png')
        print("File hist.png has been saved.")

def main():
    df = pd.read_csv("athlete_events.csv")
    print_menu() 
    choice_list = get_menu_choice() #gets a list of the users desired filter (columns) choices
    f_df, df_l = filtering(df, choice_list)
    print("==========================================")
    if df_l != 0:
        plotting(f_df, df_l)
    else:
        print("Nothing to plot\nProgram terminating")
    print("==========================================")

if __name__ == "__main__":
    main()