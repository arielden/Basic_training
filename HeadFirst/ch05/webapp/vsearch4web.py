import html
import mysql.connector
from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)

def log_request(req, res: str) -> None:
    dbconfig = {'host': '0.0.0.0',
                'port': 33060,
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB',}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          'Chrome', #req.user_agent returns a non valid DB value.
                          res))
  
    conn.commit()
    cursor.close()
    conn.close()

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

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return render_template('viewlog.html',
                           the_title='Here you are in the logs page',
                           the_data = contents,
                           the_row_titles=['Form Data', 'Remote_addr', 'User_agent', 'Results'])

if __name__ == '__main__':
    app.run(debug=True)