Django's template system is used to separate design
from Python by creating a template that can use a view.\
Your project's TEMPLATE setup describes how Django will
load and display templates. The default settings file configures 
the backend of Django templates with the APP_DIR parameter set to True.
By convention DjangoTemplates searches for the “templates”
subdirectory in each of the INSTALLED_APPS.\

A separate folder with the application name should be created
for each application in the templates folder.