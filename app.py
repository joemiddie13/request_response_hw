# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask
app = Flask(__name__)

# Hello, World!
@app.route('/')
def homepage():
  """Shows a greeting to the user."""
  return 'Are you there, world? It\'s me, Ducky!'

# Your User's Favorite Animal
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
  """Display a message to the user that changes based on their favorite animal."""
  return f'Wow, {users_animal} is my favorite animal, too!'

# Your User's Favorite Dessert
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
  """Display a message to the user that changes based on their favorite dessert."""
  return f"Nice! {users_dessert} is a great choice!"

# Mad Libs
@app.route('/madlibs/<adjective>/<noun>')
def adjective(adjective, noun):
  return f"Yesterday, an {adjective} {noun} went to the race track. All of the fans were so excited to see an {adjective} {noun} getting suited up!"

# Multiply Two Numbers
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
  if number1.isdigit() and number2.isdigit():
    first_number = int(number1)
    second_number = int(number2)
    return f"{first_number} x {second_number} = {first_number * second_number}"
  else:
    return "Invalid inputs! Insert two numbers."



if __name__ == '__main__':
  app.run(debug=True)