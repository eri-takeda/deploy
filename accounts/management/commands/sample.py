from typing import Any
from django.core.management.base import BaseCommand, CommandParser



class Command(BaseCommand):
    help='ユーザ情報を表示するバッチです'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='名前')
        parser.add_argument('age', type=int)
        parser.add_argument('--birthday', default='2020-02-02')
        parser.add_argument('three_words',nargs=3)
        parser.add_argument('--active', action='store_true')
        parser.add_argument('--color', choices=['blue','red','yellow'])


    def handle(self, *args, **options): 
        name = options['name']
        age = options['age']
        birthday = options['birthday']
        three_words = options['three_words']
        active=options['active']
        
        print(
            f'name = {name}, age = {age}, birthday= {birthday}, three_words = {three_words}'
            )
        print(active)
        color = options['color']
        if  color == "blue":
            print('青')
        elif color == "red":
            print('赤')
        elif color == "yellow":
            print('黄')
            
