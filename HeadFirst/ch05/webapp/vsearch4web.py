import html
from DBcm import UseDatabase
from flask import Flask, render_template, request, escape, session
from vsearch import search4letters
from login_checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'secretPassword' #Sin esto, session no funciona!

dbconfig = {'host': '0.0.0.0',
            'port': 33060,
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',}


def log_request(req, res: str) -> None:
    """Log details of the web request and the results."""
    with UseDatabase(dbconfig) as cursor:

        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            'Chrome', #req.user_agent returns a non valid DB value.
                            res))

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results!'
    log_request(request, results)
    return render_template('results.html',
                           the_results = results,
                           the_title = title,
                           the_phrase = phrase,
                           the_letters = letters)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web')

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are logged in!'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are NOT logged in!'


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':

    with UseDatabase(dbconfig) as cursor:    
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall() #Devuelve una lista de tuplas.
  
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_data = contents,
                           the_row_titles=['Phrase', 'Letters', 'Ip', 'Browser', 'Results'])

if __name__ == '__main__':
    app.run(debug=True)