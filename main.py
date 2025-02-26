from flask import Flask, render_template, request, session

# Создание экземпляра Flask-приложения
app = Flask(__name__)

# Устанавливаем секретный ключ для сессий (используется для хранения данных между запросами)
app.secret_key = "secret"

# Главная страница (форма для заполнения резюме)
@app.route('/', methods=['GET', 'POST'])
def form():
    """
    Отображает форму для заполнения резюме.
    """
    return render_template('form.html')

# Обработчик формы и предпросмотр резюме
@app.route('/preview', methods=['POST'])
def preview():
    """
    Получает данные из формы, очищает старые данные сессии, сохраняет новые
    и передает их в шаблон 'resume.html' для предпросмотра.
    """
    session.clear()  # Очищаем старые данные перед загрузкой новых
    session['resume_data'] = {}  # Создаем пустой словарь для хранения данных резюме

    # Список полей, которые пользователь может включать/исключать
    optional_fields = ["name", "email", "telegram", "linkedin", "phone"]

    # Проверяем, какие из полей были отмечены пользователем (если чекбокс активен)
    for field in optional_fields:
        if request.form.get(f"include_{field}"):  # Если чекбокс отмечен
            session['resume_data'][field] = request.form.get(field, "")  # Сохраняем значение поля

    # Получаем списковые данные (технические навыки, опыт работы, языки)
    session['resume_data']['technical_stack'] = request.form.getlist("technical_stack")
    session['resume_data']['work_experience'] = request.form.getlist("work_experience")
    session['resume_data']['languages'] = request.form.getlist("languages")

    # Сохраняем выбранный пользователем цвет оформления резюме
    session['resume_color'] = request.form.get("resume_color", "blue")

    # Передаем данные в шаблон 'resume.html' для отображения предпросмотра резюме
    return render_template('resume.html', resume_color=session['resume_color'], **session['resume_data'])

# Финальная версия резюме для печати
@app.route('/finalize')
def finalize():
    """
    Отображает окончательную версию резюме без кнопок редактирования.
    Готова к печати или сохранению в PDF.
    """
    return render_template('finalize.html', resume_color=session['resume_color'], **session['resume_data'])

# Запуск веб-сервера Flask
if __name__ == '__main__':
    app.run(debug=True)  # Включаем режим отладки, чтобы видеть ошибки в терминале
