from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return HttpResponse(
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>body{
    background-color: blue ;
    color:white;
    }
    </style>
    <title>Document</title>
</head>
<body>
  <h1> hola mundo trolo </h1>  
  <p>Esto es un parrafo</p>
    <ul>
        <li>1. Hola ceci</li>
        <li>2. Hola pofi</li>
        <li>3.Hola alvi</li>
        <li>4.Hola trolos</li>
    </ul>
</body>
</html>
        
                       """
                       )