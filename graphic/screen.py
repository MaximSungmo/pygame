# screen.py

#자기와 동일한 directory의 모듈을 사용하려고 하는 경우
# from graphic import render
from . import render


def screen():
    print('screen called')
    render.render()

