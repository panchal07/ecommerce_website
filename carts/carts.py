from flask import Flask, render_template, session, request, redirect, url_for, flash
from shop import app,db

@app.route('/addcart', methods=['GET', 'POST'])
def AddCart():
    try:
        pass
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)
