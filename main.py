from flask import Flask, render_template, request, redirect
app = Flask('app')

contacts = []

@app.route('/')
def index():
  return render_template(
    'index.html',
    contacts = contacts
  )

@app.route('/create', methods=['POST'])
def inicio():
  nome = request.form.get('name')
  email = request.form.get('email')
  tel = request.form.get('phone')
  contacts.append({'name': nome, 'email': email, 'phone': tel})
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  contacts.pop(index)
  return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  title = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts[id]['name'] = title
  contacts[id]['email'] = email
  contacts[id]['phone'] = phone
  return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')