from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
template_folder='views')

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name'] # Ambil data dari form dengan name = 'name'
        email = request.form['email'] # Ambil data dari form dengan name = 'email'
        message = request.form['message'] # Ambil data dari form dengan name = 'message'
        # print(f"Name : {name}, Email: {email}, Message: {message}") # Cetak data yang diterima pada terminal
        # return redirect(url_for('contact')) # Redirect untik menghindari resubmit form

        # Buat pesan konfirmasi
        confirmation_message = f"Thank you, {name}. Your message has been sent successfully!."

        # Render template dengan pesan konfirmasi dan data form
        return render_template('contact.html', confirmation_message=confirmation_message, name=name, email=email,
        message=message)
    
    title = "Contact Page"
    return render_template('contact.html', title=title)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)