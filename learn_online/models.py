from django.db import models

# Create your models here.

class Experts():
    
    def __init__( self):
        pass
    
    def all( self  ):
        all_expert = [
            { 'name': 'John' , 'designation': 'Programmer', 'pic': 'img/team-2.jpg', 'fb': 'https://fb.com/john',  'instagram': 'https://in.com/john' },
            { 'name': 'Robert' , 'designation': 'Manager', 'pic': 'img/team-1.jpg', 'instagram': 'https://in.com/john' },
            { 'name': 'Lloyd' , 'designation': 'Sr Programmer', 'pic': 'img/team-3.jpg', 'tw': 'https://tw.com/Lloyd',  'instagram': 'https://in.com/Lloyd' },
            { 'name': 'Ducsan' , 'designation': 'Tester', 'pic': 'img/team-2.jpg' , 'tw': 'https://tw.com/Ducsan',  'instagram': 'https://in.com/Ducsan', 'fb': 'https://fb.com/john',  'instagram': 'https://in.com/john'  },
            { 'name': 'Ron' , 'designation': 'Programmer', 'pic': 'img/team-1.jpg', 'fb': 'https://fb.com/Ron',  'instagram': 'https://in.com/Ron' },
            { 'name': 'Wayne' , 'designation': 'Desinger', 'pic': 'img/team-3.jpg', 'fb': 'https://fb.com/Wayne',  'instagram': 'https://in.com/Wayne' },
        ]
        return all_expert
