# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:13:14 2019

@author: hazal
"""
import math
#185112023 Hazal Özge Yılmaz
""" Bir bölümde bulunan 13 akademisyen vardır. 
Aynı ayda doğmuş olan en az kaç akademisyen olduğunu 
güvercin yuvası prensibine göre hesaplayınız."""

# Güvercin Yuvası Prensibine göre
# yuva = n
#güvercin= m olsun

n= 12
m=13


if m > n:

 x= math.ceil(m/n)
print(" 13 akademisyenden en az ",x, "tanesi aynı ayda dogmustur")


