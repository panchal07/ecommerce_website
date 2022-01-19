from flask import Flask, render_template, redirect, request, url_for, flash, session
from shop import db, app, photos
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets
import os

@app.route('/')
def home():
    products = Addproduct.query.filter(Addproduct.stock>0)
    return render_template('products/index.html',products=products)

@app.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get(id)
    return render_template('products/single_page.html',product=product)

@app.route('/women')
def women():
    return render_template('products/Women.html',title="Women Category")

@app.route('/men')
def men():
    return render_template('products/Men.html',title="Men's Category")

@app.route('/kids')
def kids():
    return render_template('products/Kids.html',title="Kids Section")

@app.route('/accessories')
def accessories():
    return render_template('products/Accessories.html',title="Accessories page")

@app.route('/aboutus')
def aboutus():
    return render_template('products/About_us.html',title="About us page")

@app.route('/addBrand',methods=['GET', 'POST'])
def addBrand():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getBrand = request.form.get('brand')
        brand = Brand(name=getBrand)
        db.session.add(brand)
        flash(f'The Brand {getBrand} was added to the database', 'success')
        db.session.commit()
        return redirect(url_for('addBrand'))
    return render_template('products/addBrand.html',brands = 'brands')


@app.route('/updatebrand/<int:id>',methods=['GET', 'POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
    updatebrand = Brand.query.get(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatebrand.name = brand
        flash(f'Your Brand has been updated','success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('products/updateBrand.html',title = "Update brand page", updatebrand=updatebrand)

@app.route('/deletebrand/<int:id>',methods=['POST'])
def deletebrand(id):
    brand = Brand.query.get(id)
    if request.method == 'POST':
        db.session.delete(brand)
        db.session.commit()
        flash(f'The brand {brand.name} was deleted from database', 'success')
        return redirect(url_for('admin'))
    flash(f'The brand {brand.name} cannot be deleted','warning')
    return redirect(url_for('admin'))


@app.route('/addCategory',methods=['GET', 'POST'])
def addCategory():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getCategory = request.form.get('category')
        cat = Category(name=getCategory)
        db.session.add(cat)
        flash(f'The category {getCategory} was added to the database', 'success')
        db.session.commit()
        return redirect(url_for('addCategory'))
    return render_template('products/addBrand.html',category = 'category')

@app.route('/updatecat/<int:id>',methods=['GET', 'POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
    updatecat = Category.query.get(id)
    category = request.form.get('category')
    if request.method == 'POST':
        updatecat.name = category
        flash(f'Your category has been updated','success')
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/updateBrand.html',title = "Update category page", updatecat=updatecat)

@app.route('/deletecat/<int:id>',methods=['POST'])
def deletecat(id):
    category = Category.query.get(id)
    if request.method == 'POST':
        db.session.delete(category)
        db.session.commit()
        flash(f'The category {category.name} was deleted from database', 'success')
        return redirect(url_for('admin'))
    flash(f'The category {category.name} cannot be deleted','warning')
    return redirect(url_for('admin'))

@app.route('/addProduct',methods=['GET', 'POST'])
def addProduct():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        discription = form.discription.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        p = Addproduct(name=name,price=price,discount=discount,stock=stock,colors=colors,discription=discription,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(p)
        flash(f'The product {name} is added to the database','success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addProducts.html',title = "Add product page", form = form, brands=brands, categories=categories)


@app.route('/updateproduct/<int:id>',methods=['GET','POST'])
def updateproduct(id):
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Addproduct.query.get(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = Addproducts(request.form)
    if request.method == 'POST':
        product.name = form.name.data
        product.price = form.price.data
        product. discount = form.discount
        product.brand_id = brand
        product.category_id = category
        product.colors = form.colors
        product.discription = form.discription
        db.session.commit()
        flash(f'Your product has been updated','success')
        return redirect('admin')

    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.discription.data = product.discription
    # brand = product.brand.name
    # category = product.category.name
    return render_template('products/updateproduct.html',form=form,brands=brands,categories=categories,product=product)
