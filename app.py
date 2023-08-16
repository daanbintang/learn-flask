from flask import Flask, render_template, request, redirect, url_for, session
from forms import Siswa

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DEV'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/input-data/', methods=['GET', 'POST'])
def input_data():
    form = Siswa()
    if form.validate_on_submit():
        datas = [
            {'nama': request.form['nama'],
             'email': request.form['email'],
             'jurusan': request.form['jurusan']}
        ]
        return render_template('data_siswa.html', datas=datas)
    return render_template('input_data.html', form=form)


@app.route('/data-siswa/')
def data_siswa():
    return render_template('data_siswa.html')


if __name__ == '__main__':
    app.run(debug=True)
