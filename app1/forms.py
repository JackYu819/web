# -*- coding: utf-8 -*-
# @Author: yuxiangyu
# @Date:   2018-05-30 20:05:59
# @Last Modified by:   yuxiangyu
# @Last Modified time: 2018-05-30 20:07:04

from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
