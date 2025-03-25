# 1 Install Behave: If you haven’t already, install Behave using pip:
# # pip install behave  ELLER python3 -m pip install behave
# 2. Directory Structure: Organize your project with the following structure:
#
# your_project/
# |
# |-- features/
# |   |__ steps/
# |   |   |__ step_definitions.py
# │   |__ environment.py
# │   |__ your_feature.feature
# |
# |_ models/
# |   |__ custom_models.py
# |
# |__ requirements.txt
# features/: This directory holds your .feature files, where you define your scenarios in the Gherkin language.
# steps/: Contains Python files with step definitions for the scenarios described in your feature files.
# environment.py: (Optional) Defines setup and teardown functions, among other hooks.
# models/: (Optional) A directory for custom models or types you might use in your steps.
# requirements.txt: Lists the project's dependencies.