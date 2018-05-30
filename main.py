# -*- coding:utf-8 -*-

from route import Route

route = Route(debug=True)

@route.GET("/")
def index(req, res):
  """
  GET / の処理
  """
  res.body = "OK"

@route.GET("/ping")
def ping(req, res):
  res.body = "Pong"

route.handle("GET", "/")
route.handle("GET", "/ping")
route.handle("GET", "/favicon.ico")
