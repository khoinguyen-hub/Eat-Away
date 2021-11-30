# Eat-Away

This is an app that suggests places to eat using user inputs such as their favorite foods or any food that they are in the mood for. This app will ask for user inputs and search on google map for places that match those inputs. The goal of this app is to help users quickly search for places to eat while tailoring the search result to the either users' inputs or their account settings.

# How to contribute
- Select an issue that you would like to work on.
- Assign it to yourself or request someone to assign it to you buy leaving a comment and have @khoinguyen-hub in your comment.
- Follow '#Set up' and '#How to run the app' sections to get you started.
- Make sure to create a new branch before making any changes.
- Your commit messages should be descriptive of the changes you have made.
- You should only push changes that you've made or any additional files that you've added. DO NOT push any files that are generated from running the app such as 'venv' or 'app.cpython-38.pyc'.
- If you use new dependencies, remember to add them to 'requirements.txt'.
- Create a pull request after you finish making changes.
- Be sure to link your pull request to the # of the issue you are working on by either linking the issue or leave '#[issue number here]' in a comment in your pull request.
- Wait for review and make any changes if necessary.
- You can create new issue with a description and ask for approval by @khoinguyen-hub in your description.

# Set up
- Use any IDE that works for you, but I recommend using [Visual Studio Code](https://code.visualstudio.com/).
- Make sure to have [python 3.8 or higher](https://www.python.org/downloads/) installed in your system.
- Clone or fork and clone this repository to your local machine.
- Create a virtual environment to manage your dependencies for this project.
'py -3 -m venv venv'
or
'python3 -m venv venv'
then
'venv\Scripts\activate' to activate your virtual environment
- After activating your environment, install the dependencies:
'pip install -r requirements.txt'

# How to run the app
- First, make sure that all dependencies have installed correctly, especially flask.
- Go to app.py, then open up a new terminal by going to Termial -> New Terminal or 'Crtl+Shift+`' command in Visual Studio Code.
- Make sure that you are inside the Eat-Away directory. Use 'cd Eat-Away' command inside the terminal if you are not.
- Run the website with flask:
'$env:FLASK_APP = "app.py"'
'$env:FLASK_ENV = "development"'
'flask run'
- Click the link that the website is running on to access the app website.
-For more information about flask: https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application