# -*- coding: utf-8 -*-
from instapush import Instapush, App
app = App(appid='5549b895a4c48a9e26ae6a1f', secret='c7ded18ff7885c95773ff2d02149f960')
app.notify(event_name='general', trackers={ 'msg': 'From Python'})