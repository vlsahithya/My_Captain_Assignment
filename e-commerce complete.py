{% load static %}
<html>
    <head>
        <title>
            ProjectGurukul Online Shopping Project
        </title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    </head>
    <body>        
        {% include 'website/navbar.html' %}
        {% block content %}   
        {% endblock %}
        <br>
       
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    </body>
</html>

{% extends 'website/dependencies.html' %}
 
{% block content %}
 
<div class="container ">
<h1>Products</h1>
<div class="card-columns" style="padding: 10px; margin: 20px;">
{% for p  in products%}
    <div class="card" style="width: 18rem; border:5px black solid">
        <img class="card-img-top" src="{{p.image.url}}" alt="Card image cap">
        <div class="card-body">
        <h5 class="card-title">{{p.name}}</h5>
        <p class="card-text">{{p.description}}</p>
        </div>
    </div>
 {% endfor %}
 
</div>
{% endblock %}

{% load static %}
 
<style>
  .greet{
    font-size: 18px;
    color: #fff;
    margin-right: 20px;
  }
</style>
 
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
 
    <ul class="navbar-nav">
      
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'home' %}">Home</a>
      </li>
      {% if request.user.is_staff %}
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'addProduct' %}">Add Product</a>
      </li>
      {% else %}
      <li class="nav-item">
        <a class="nav-link" href="{% url 'placeOrder' request.user.customer.id %}">Cart</a>
      </li>
      {% endif %}
      <li class="nav-item">
        <a class="nav-link" href="{% url 'login' %}">Login</a>
      </li>
    </ul>
  </div>
 
  <span class="greet">Hello, {{request.user}}</span>
  <span ><a  class="greet" href="{% url 'logout' %}">Logout</a></span>
 
</nav>

{% extends 'website/dependencies.html' %}
 
{% block content %}
 
<div class="jumbotron container row">
    <div class="col-md-6">
        <div class="card card-body">
           <form action="" method="POST" enctype="multipart/form-data">
              {% csrf_token %}
                {{form.as_p}}
                <br>
             <input type="submit" name="submit">
             </form>
            </div>
        </div>
    </div>
 
</div>
{% endblock %}

{% extends 'website/dependencies.html' %}
 
{% block content %}
 
<div class="jumbotron container row">
    <div class="col-md-6">
        <div class="card card-body">
           <form action="" method="POST" enctype="multipart/form-data">
              {% csrf_token %}
                {{form.as_p}}
                <br>
             <input type="submit" name="submit">
             </form>
            </div>
        </div>
    </div>
 
</div>
{% endblock %}

{% extends 'website/dependencies.html' %}
{% load static%}
{% block content %}
<div class="container jumbotron">
    <form method="POST" action="" >
        {% csrf_token %}
        {{form.as_p}}
        {{customerform.as_p}} 
       
        <input class="btn btn-success" type="submit" value="Register Account">
    </form>
</div>
{% endblock %}

{% extends 'website/dependencies.html' %}
{% load static%}
{% block content %}
<div class="container jumbotron">
    <form method="POST" action="">
        {% csrf_token %}
        <p><input type="text" name="username" placeholder="Username..."></p>
        <p><input type="password" name="password" placeholder="Password..." ></p>
        <input class="btn btn-success" type="submit" value="Login">
        <p>Do not have an account  <a href='{% url 'register' %}'>Register</a></p>
    </form>
</div>
{% endblock %}
