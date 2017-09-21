# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
seconds = int(input())

hours = int(seconds/3600)
minutes = int((seconds%3600)/60)
seconds = seconds % 60



print("%d:%d:%d" %(hours,minutes,seconds))