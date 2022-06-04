from flask import Flask, render_template, request, escape, session, copy_current_request_context
from vsearch import functions

from Database import UseDatabase, ConnectionError, CredentialsError
from checker import check_logged_in
import sys
from threading import Thread

app = Flask(__name__)

app.config['dbconfig']= {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout()-> str:
    session.pop('logged_in')
    return 'You are now logged out'



@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res,))

    """ returns letters from a word"""
    phrase= request.form['phrase']
    letters = request.form['letters']
    title='Here are your results: '
    results = str(set(letters).intersection(set(phrase)))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except ConnectionError as err:
        print("some error occured ", str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    return render_template('results.html',
                           the_phrase= phrase,
                           the_letters= letters,
                           the_title= title,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='welcome to vodils web app')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL="""select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles= (('Phrase','Letters', 'Remote_addr', 'User_agent', 'Results'))
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents,)

app.secret_key= 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug= True)



