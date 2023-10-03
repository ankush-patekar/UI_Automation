# UI_Automation
Selenium Hybrid Framework (https://www.youtube.com/playlist?list=PLUDwpEzHYYLt2RzOb-_eafLAP0VSoyJhf)
(Python, Selenium, PyTest,POM, HTML Reports)

Create new project and install prerequisites
Selenium
PyTest:	Python unittest framework
Pytest-html:	PyTest html reports
Pytest-xdict:	run test Parallel
Openpyxl :	MS Excel support
Allure-pytest:	To generate allure reports

Create folder str
Project Name
	|
	pageObject(Package)
	|
	testCases(Package)
	|
	utilities(Package)
	|
	testData(Folder)
	|
	Configuration(Folder)
	|
	Logs(Folder)
	|
	Screenshots(Folder)
	|
	Reports(Folder)
	|
	Run.bat


Automating Login Test cases
Create ‘LoginPage’ class object under pageObject(Package) 
Create ‘LoginTest ’class object under testCases(Package)
Create ‘conftest.py’  under testCases(Package)

Capture screenshot on failed TCs
Update ‘LoginTest’ with screenshot under ‘testCases’

Read common values from .ini file
Add ‘Config.ini’ file in ‘configuration’ Folder
Create ‘readUtility.py’ under utilities to read common data from .ini file
Replace hard coded values in Login TC

Adding Logs to TCs
Add ‘customLogger.py’ under utilities package
Add logs into Login TCs

Run TC on desired/cross/parallel browser
Update ‘contest.py’ with required Fixtures which will accept cmd line arg(browser name)
Pass browser name as arg in cmd line 
	To run the TCs on desired browser
		pytest -s -v testCases\test_login.py --browser chrome
	To run TCs parallel
		pytest -s -v -n=3 testCases\test_login.py --browser chrome

Generate Pytest HTML Reports
Update contest.py with pytest hooks
	To generate HTML reports run below cmd
		pytest -s -v --html=Reports\report.html testCases\test_login.py --browser edge

Automating Data driven TCs
Prepare the data in excel sheet and kept it under testData folder
Create ‘Xlutilis.py’ utility class under utilities package
Create login_datadriven test under testCases 
Run the TCs

Adding New TCs
Add new customer
Search customer by email
Search customer by name


Grouping TCs
Add markers to every test method
@pytest.mark.sanity
@pytest.merk.regression
Add marker entries in pytest.ini file
[pytest]
markers=
	sanity
	regression 

	To run group of TCs at atime
	-m “santy”
	-m “regression”
	-m “ sanity or regression”
	-m “ sanity and regression”

	pytest -s -v -m "sanity" .\testCases --browser chrome

Run tests in cmd using batch file
Create run.bat file (location:alog with all packages and folder)
Open run.bat in notepad and add multiple cmds
Run that file by double click


Push the code in to git and GitHub repo
	1st round:
	—------------------
	
	Initial setup(only one time)
		i.git init —-> create an empty repo(Local)
		
		ii. Clone the repo from github
		Git clone <repo link>

	Before doing first time commit we have to execute below cmd
		git config –global user.name “Ankush”
		git config –global user.email “patekarankush34@gmail.com”


		iii. git status
		iv. git add .       —> add all changed files in staging area

		

		


