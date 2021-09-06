"""
Напишете програма, която изчислява колко часове ще са необходими на един архитект,
за да изготви проектите на няколко строителни обекта.
Изготвянето на един проект отнема три часа.
Вход
От конзолата се четат 2 реда:
1.	Името на архитекта - текст;
2.	Брой на проектите - цяло число.
Изход
На конзолата се отпечатва:
•	"The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."


"""



def needed_time_for_the_projects(architect_name, projects_count, time):
    print(f"The architect {architect_name} will need {projects_count*time} hours to complete {projects_count} project/s.")


architect_name = input()
projects_count = int(input())
time = 3

needed_time_for_the_projects(architect_name, projects_count, time)