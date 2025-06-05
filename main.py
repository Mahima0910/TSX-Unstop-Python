from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/profile')
def home():
    return render_template('profile.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Handle form submission (you can store this data or send emails)
        print(f"New Contact Submission:\nName: {name}\nEmail: {email}\nMessage: {message}")

        return redirect('/')  # Redirect after submission
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
