from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label for="new-movie">
            I want to add
            <input type="text" id="new-movie" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# TODO:
# Create the HTML for the form below so the user can check off a movie from their list 
# when they've watched it.
# Name the action for the form '/crossoff' and make its method 'post'.

# a form for crossing off watched movies
crossoff_form = """
        <form action="/crossoff" method="post">
            <label for="crossoff_movie">
            I want to cross off</label>
            <select name="crossoff_movie">
                <option value="Harry Potter and the Sorcerer's Stone">Harry Potter and the Sorcerer's Stone</option>
                <option value="Harry Potter and the Chamber of Secrets">Harry Potter and the Chamber of Secrets</option>
                <option value="Harry Potter and the Prisoner of Azkaban">Harry Potter and the Prisoner of Azkaban</option>
            </select>
            from my Watchlist.
            
            <input type="submit" value="Cross It Off"/>
        </form>
"""

# TODO:
# Finish filling in the function below so that the user will see a message like:
# "Star Wars has been crossed off your watchlist".
# And create a route above the function definition to receive and handle the request from 
# your crossoff_form.
@app.route("/crossoff", methods=['POST','GET'])
def crossoff_movie():
    crossed_off_movie = request.form['crossoff_movie']  

    crossoff_element = "<strike>" + crossed_off_movie + "</strike>"
    sentence = crossoff_element + " has been crossed off your Watchlist."
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content 

# TODO:
# modify the crossoff_form above to use a dropdown (<select>) instead of
# an input text field (<input type="text"/>)

@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # build the response string
    content = page_header + edit_header + add_form + crossoff_form + page_footer

    return content


app.run()
