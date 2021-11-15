#survey page
from ._anvil_designer import survey_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class survey_page(survey_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.username
    # Any code you write here will run when the form opens.
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    user = self.username.text
    score = 0
    
    score += int(self.question1_1.get_group_value())
    score += int(self.question2_1.get_group_value())
    score += int(self.question3_1.get_group_value())
    score += int(self.question4_1.get_group_value())
    score += int(self.question5_1.get_group_value())
    score += int(self.question6_1.get_group_value())
    score += int(self.question7_1.get_group_value())
    score += int(self.question8_1.get_group_value())
    score += int(self.question9_1.get_group_value())
    score += int(self.question10_1.get_group_value())
    
    data = anvil.server.call('user_data', user, score)
    
    open_form('result')
    
    #information page
    from ._anvil_designer import information_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class information_page(information_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   
    # Any code you write here will run when the form opens.
    
    
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    open_form('survey_page')

#result page
from ._anvil_designer import resultTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..survey_page import survey_pageTemplate

class result(resultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('start_page')

  def display(self, **event_args):
    record = app_tables.question_answers.get(user=survey_pageTemplate.user)
    self.score = record['score']
    dis = self.data_row_panel_1.item(self.score)
    
#server module
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

# Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Question10

@anvil.server.callable
def user_data(user, score):
  app_tables.question_answers.add_row(
    user = user,
    score = score)
  
@anvil.server.callable
def answer_data(score):
  app_tables.question_answers.add_row(
  score = score
  )
 
 
#need to work on result page display and datastore and use for information page
