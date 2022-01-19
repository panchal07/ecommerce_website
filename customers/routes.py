from flask import Flask, render_template, redirect, request, url_for, flash, session
from shop import db, app, photos, bcrypt
from .forms import CustomerRegistrationForm, CustomerLogin
from .models import Register1
import secrets
import os

@app.route('/customer/register', methods=['GET', 'POST'])
def customer_register():
    form = CustomerRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register1(name=form.name.data,username=form.username.data,email=form.email.data,password=hash_password, country = form.country.data,
        state=form.state.data, contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        db.session.commit()
        flash(f'Welcome {form.name.data} ! Thank you for registering', 'success')
        # db.session.commit()
        return redirect(url_for('customerLogin'))
    return render_template('customer/register.html',form=form)

@app.route('/customer/login', methods=['GET', 'POST'])
def customerLogin():
    form = CustomerLogin(request.form)
    if request.method == 'POST' and form.validate():
        user = Register1.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data}! You are now logged in', 'success')
            return redirect(request.args.get('next') or url_for('home'))
        else:
            flash('Wrong Password. Please try again', 'danger')

    return render_template('customer/login.html', form=form, title="Login Page")
