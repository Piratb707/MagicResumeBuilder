from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/preview', methods=['POST'])  # Проверяем, что обработчик принимает POST-запрос
def preview():
    session['resume_data'] = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "telegram": request.form.get("telegram"),
        "linkedin": request.form.get("linkedin"),
        "summary": request.form.get("summary"),
        "education": request.form.get("education"),
        "technical_stack": request.form.getlist("technical_stack"),  # Список технологий
        "work_experience": request.form.get("work_experience"),
        "languages": request.form.getlist("languages")  # Список языков
    }
    return render_template('resume.html', **session['resume_data'])

if __name__ == '__main__':
    app.run(debug=True)
