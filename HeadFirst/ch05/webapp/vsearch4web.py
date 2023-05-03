import html
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from flask import Flask, render_template, request, escape, session, copy_current_request_context
from vsearch import search4letters
from login_checker import check_logged_in
from threading import Thread
from time import sleep

app = Flask(__name__)

app.secret_key = 'secretPassword' #Sin esto, session no funciona!

app.config['dbconfig'] = {'host': '0.0.0.0',
            'port': 33060,
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',}

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are logged in!'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are NOT logged in!'

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req, res: str) -> None:
        """Log details of the web request and the results."""
        sleep(15) #This makes log_request really slow.
        with UseDatabase(app.config['dbconfig']) as cursor:

            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                'Chrome', #req.user_agent returns a non valid DB value.
                                res))


    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results!'
    try:
        t= Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print(f"******Login failed with this error:--> {err}")
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



@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:    
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall() #Devuelve una lista de tuplas.
        #raise Exception("some unknown exception.")
        return render_template('viewlog.html',
                            the_title='View Log',
                            the_data = contents,
                            the_row_titles=['Phrase', 'Letters', 'Ip', 'Browser', 'Results'])
    except ConnectionError as err:
        print("Is your database switched on? Error:", str(err))
    except CredentialsError as err:
        print('User-id / Password issues. Error: ', str(err))
    except SQLError as err:
        print("is your query correct? Error: ", str(err))

    except Exception as err:
        print("Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)