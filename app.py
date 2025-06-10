# from flask import Flask, render_template, request, redirect, session, jsonify, url_for
# from model import interpret_dream
# from database import init_db, register_user, validate_user, save_dream, get_dreams

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace in production
# init_db()

# # 🔁 Splash screen
# @app.route('/')
# def splash():
#     return render_template('splash.html')  # shows splash screen for 3s then redirects to /landing

# # 🏠 Landing page (Login/Register options)
# @app.route('/landing')
# def landing():
#     return render_template('landing.html')

# # 🔐 Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user_id = validate_user(request.form['username'], request.form['password'])
#         if user_id:
#             session['user_id'] = user_id
#             return redirect('/dashboard')
#     return render_template('login.html')

# # 🧾 Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         success = register_user(request.form['username'], request.form['password'])
#         if success:
#             return redirect('/login')
#     return render_template('register.html')

# # 📋 Dashboard with user's dream history
# # @app.route('/dashboard')
# # def dashboard():
# #     if 'user_id' in session:
# #         dreams = get_dreams(session['user_id'])
# #         return render_template('index.html', dreams=dreams)
# #     return redirect('/login')
# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         user_info = {
#             'name': 'John Doe',
#             'email': 'john@example.com',
#             'phone': '+1234567890'
#         }
#         return render_template('index.html', dreams=dreams, **user_info)
#     return redirect('/login')

# # 🚪 Logout
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login')

# # ✨ Interpret dream (AJAX or fetch)
# @app.route('/interpret', methods=['POST'])
# def interpret():
#     dream_text = ''
#     if request.is_json:
#         data = request.get_json()
#         dream_text = data.get('dream_text', '')
#     else:
#         dream_text = request.form.get('dream', '')

#     result = interpret_dream(dream_text)

#     if 'user_id' in session:
#         save_dream(session['user_id'], dream_text, result)

#     return jsonify({'interpretation': result})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, session, jsonify, url_for
# from model import interpret_dream
# from database import init_db, register_user, validate_user, save_dream, get_dreams

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace in production
# init_db()

# # 🗁 Splash screen
# @app.route('/')
# def splash():
#     return render_template('splash.html')  # shows splash screen for 3s then redirects to /landing

# # 🏠 Landing page (Login/Register options)
# @app.route('/landing')
# def landing():
#     return render_template('landing.html')

# # 🔐 Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username and password:
#             user_id = validate_user(username, password)
#             if user_id:
#                 session['user_id'] = user_id
#                 session['username'] = username
#                 return redirect('/dashboard')
#         return render_template('login.html', error="Invalid credentials")
#     return render_template('login.html')

# # 🧾 Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         success = register_user(request.form['username'], request.form['password'])
#         if success:
#             return redirect('/login')
#     return render_template('register.html')

# # 📋 Dashboard with user's dream history
# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         user_info = {
#             'name': 'John Doe',
#             'email': 'john@example.com',
#             'phone': '+1234567890'
#         }
#         return render_template('index.html', dreams=dreams, **user_info)
#     return redirect('/login')

# # 🚪 Logout
# @app.route('/logout', methods=['POST'])
# def logout():
#     session.clear()
#     return redirect('/login')

# # ✨ Interpret dream (AJAX or fetch)
# @app.route('/interpret', methods=['POST'])
# def interpret():
#     dream_text = ''
#     if request.is_json:
#         data = request.get_json()
#         dream_text = data.get('dream_text', '')
#     else:
#         dream_text = request.form.get('dream', '')

#     result = interpret_dream(dream_text)

#     if 'user_id' in session:
#         save_dream(session['user_id'], dream_text, result)

#     return jsonify({'interpretation': result})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, session, jsonify, url_for
# from model import interpret_dream
# from database import init_db, register_user, validate_user, save_dream, get_dreams, get_user_info

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace in production
# init_db()

# # 🗁 Splash screen
# @app.route('/')
# def splash():
#     return render_template('splash.html')  # shows splash screen for 3s then redirects to /landing

# # 🏠 Landing page (Login/Register options)
# @app.route('/landing')
# def landing():
#     return render_template('landing.html')

# # 🔐 Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username and password:
#             user_id = validate_user(username, password)
#             if user_id:
#                 session['user_id'] = user_id
#                 session['username'] = username
#                 return redirect('/dashboard')
#         return render_template('login.html', error="Invalid credentials")
#     return render_template('login.html')

# # 🧾 Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         success = register_user(request.form['username'], request.form['password'])
#         if success:
#             return redirect('/login')
#     return render_template('register.html')

# # 📋 Dashboard with user's dream history
# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         user_info = get_user_info(session['user_id']) or {}
#         return render_template('index.html', dreams=dreams, **user_info)
#     return redirect('/login')

# # 🚪 Logout
# @app.route('/logout', methods=['POST'])
# def logout():
#     session.clear()
#     return redirect('/login')

# # ✨ Interpret dream (AJAX or fetch)
# @app.route('/interpret', methods=['POST'])
# def interpret():
#     dream_text = ''
#     if request.is_json:
#         data = request.get_json()
#         dream_text = data.get('dream_text', '')
#     else:
#         dream_text = request.form.get('dream', '')

#     result = interpret_dream(dream_text)

#     if 'user_id' in session:
#         save_dream(session['user_id'], dream_text, result)

#     return jsonify({'interpretation': result})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, session, jsonify, url_for
# from model import interpret_dream
# from database import init_db, register_user, validate_user, save_dream, get_dreams, get_user_info

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace in production
# init_db()

# # 🗁 Splash screen
# @app.route('/')
# def splash():
#     return render_template('splash.html')  # shows splash screen for 3s then redirects to /landing

# # 🏠 Landing page (Login/Register options)
# @app.route('/landing')
# def landing():
#     return render_template('landing.html')

# # 🔐 Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username and password:
#             user_id = validate_user(username, password)
#             if user_id:
#                 session['user_id'] = user_id
#                 session['username'] = username
#                 return redirect('/dashboard')
#         return render_template('login.html', error="Invalid credentials")
#     return render_template('login.html')

# # 🧾 Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         success = register_user(request.form['username'], request.form['password'])
#         if success:
#             return redirect('/login')
#     return render_template('register.html')

# # 📋 Dashboard with user's dream history
# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         user_info = get_user_info(session['user_id']) or {'name': session.get('username'), 'email': None, 'phone': None}
#         return render_template('index.html', dreams=dreams, **user_info)
#     return redirect('/login')

# # 🚪 Logout
# @app.route('/logout', methods=['POST'])
# def logout():
#     session.clear()
#     return redirect('/login')

# # ✨ Interpret dream (AJAX or fetch)
# @app.route('/interpret', methods=['POST'])
# def interpret():
#     dream_text = ''
#     if request.is_json:
#         data = request.get_json()
#         dream_text = data.get('dream_text', '')
#     else:
#         dream_text = request.form.get('dream', '')

#     result = interpret_dream(dream_text)

#     if 'user_id' in session:
#         save_dream(session['user_id'], dream_text, result)

#     return jsonify({'interpretation': result})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, session, jsonify, url_for
# from model import interpret_dream
# from database import init_db, register_user, validate_user, save_dream, get_dreams, get_user_info

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace in production
# init_db()

# # 🗁 Splash screen
# @app.route('/')
# def splash():
#     return render_template('splash.html')  # shows splash screen for 3s then redirects to /landing

# # 🏠 Landing page (Login/Register options)
# @app.route('/landing')
# def landing():
#     return render_template('landing.html')

# # 🔐 Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username and password:
#             user_id = validate_user(username, password)
#             if user_id:
#                 session['user_id'] = user_id
#                 session['username'] = username
#                 return redirect('/dashboard')
#         return render_template('login.html', error="Invalid credentials")
#     return render_template('login.html')

# # 🧾 Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         success = register_user(request.form['username'], request.form['password'])
#         if success:
#             return redirect('/login')
#     return render_template('register.html')

# # 📋 Dashboard with user's dream history
# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         user_info = get_user_info(session['user_id']) or {}
#         return render_template('index.html', dreams=dreams, **user_info)
#     return redirect('/login')

# # 📚 History page
# @app.route('/history')
# def history():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         return render_template('history.html', dreams=dreams)
#     return redirect('/login')

# # 🚪 Logout
# @app.route('/logout', methods=['POST'])
# def logout():
#     session.clear()
#     return redirect('/login')

# # ✨ Interpret dream (AJAX or fetch)
# @app.route('/interpret', methods=['POST'])
# def interpret():
#     dream_text = ''
#     if request.is_json:
#         data = request.get_json()
#         dream_text = data.get('dream_text', '')
#     else:
#         dream_text = request.form.get('dream', '')

#     result = interpret_dream(dream_text)

#     if 'user_id' in session:
#         save_dream(session['user_id'], dream_text, result)

#     return jsonify({'interpretation': result})

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, session, jsonify, url_for
# from model import interpret_dream
# from database import init_db, register_user, validate_user, save_dream, get_dreams, get_user_info

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace in production
# init_db()

# # 🗁 Splash screen
# @app.route('/')
# def splash():
#     return render_template('splash.html')  # shows splash screen for 3s then redirects to /landing

# # 🏠 Landing page (Login/Register options)
# @app.route('/landing')
# def landing():
#     return render_template('landing.html')

# # 🔐 Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username and password:
#             user_id = validate_user(username, password)
#             if user_id:
#                 session['user_id'] = user_id
#                 session['username'] = username
#                 return redirect('/dashboard')
#         return render_template('login.html', error="Invalid credentials")
#     return render_template('login.html')

# # 🧾 Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         success = register_user(request.form['username'], request.form['password'])
#         if success:
#             return redirect('/login')
#     return render_template('register.html')

# # 📋 Dashboard with user's dream history
# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         user_info = get_user_info(session['user_id']) or {}
#         return render_template('index.html', dreams=dreams, **user_info)
#     return redirect('/login')

# # 📚 History page
# @app.route('/history')
# def history():
#     if 'user_id' in session:
#         dreams = get_dreams(session['user_id'])
#         user_info = get_user_info(session['user_id']) or {}
#         print(dreams)
#         return render_template('history.html', dreams=dreams, **user_info)
#     return redirect('/login')

# # 🚪 Logout
# @app.route('/logout', methods=['POST'])
# def logout():
#     session.clear()
#     return redirect('/login')

# # ✨ Interpret dream (AJAX or fetch)
# @app.route('/interpret', methods=['POST'])
# def interpret():
#     dream_text = ''
#     if request.is_json:
#         data = request.get_json()
#         dream_text = data.get('dream_text', '')
#     else:
#         dream_text = request.form.get('dream', '')

#     result = interpret_dream(dream_text)

#     if 'user_id' in session:
#         save_dream(session['user_id'], dream_text, result)

#     return jsonify({'interpretation': result})

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, session, jsonify
from model import interpret_dream
from database import init_db, register_user, validate_user, save_dream, get_dreams, get_user_info

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this in production
init_db()

# Splash screen (auto-redirects to landing)
@app.route('/')
def splash():
    return render_template('splash.html')

# Landing page (Login/Register)
@app.route('/landing')
def landing():
    return render_template('landing.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user_id = validate_user(username, password)
            if user_id:
                session['user_id'] = user_id
                session['username'] = username
                return redirect('/dashboard')
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        success = register_user(request.form['username'], request.form['password'])
        if success:
            return redirect('/login')
    return render_template('register.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        dreams = get_dreams(session['user_id'])
        user_info = get_user_info(session['user_id']) or {}
        return render_template('index.html', dreams=dreams, **user_info)
    return redirect('/login')

# History
@app.route('/history')
def history():
    if 'user_id' in session:
        dreams = get_dreams(session['user_id'])
        return render_template('history.html', dreams=dreams)
    return redirect('/login')

# Logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/login')

# Interpret Dream (Fetch/AJAX)
@app.route('/interpret', methods=['POST'])
def interpret():
    dream_text = ''
    if request.is_json:
        data = request.get_json()
        dream_text = data.get('dream_text', '')
    else:
        dream_text = request.form.get('dream', '')

    result = interpret_dream(dream_text)

    if 'user_id' in session:
        save_dream(session['user_id'], dream_text, result)

    return jsonify({'interpretation': result})

if __name__ == '__main__':
    app.run(debug=True)
