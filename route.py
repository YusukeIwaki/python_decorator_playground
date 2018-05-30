# -*- coding:utf-8 -*-

import functools
from collections import namedtuple

Request = namedtuple("Request", ("method", "path"))

class Response:
  pass

class Logger:
  def __init__(self, debug=False):
    self._debug = debug
  def debug(self, msg):
    if self._debug:
      print msg

  def info(self, msg):
    print msg

  def error(self, msg):
    print msg

class Route:
  def __init__(self, debug=False, logger_class=Logger):
    self.routes = {"GET": {}}
    self._debug = debug
    self.logger = logger_class(debug)
  
  def GET(self, path):
    def decorator(f):
      # デコる処理。デコる対象の関数定義時に呼ばれる
      @functools.wraps(f)
      def wrapfunc(req, res):
        # デコった関数が呼ばれた時に呼ばれる
        return f(req, res)
      self.routes["GET"][path] = wrapfunc
      return wrapfunc
    return decorator

  def handle(self, method, path):
    if not method in self.routes or not path in self.routes[method]:
      self.handle_undefined_route(method, path)
      return

    req = Request(
      path = path,
      method = method
    )
    res = Response()
    self.logger.info("%s %s"%(method, path))
    if self._debug:
      if self.routes[method][path].__doc__ is not None:
        self.logger.debug(self.routes[method][path].__doc__)
    return self.routes[method][path](req, res)

  def handle_undefined_route(self, method, path):
    self.logger.error("undefined: %s %s"%(method, path))