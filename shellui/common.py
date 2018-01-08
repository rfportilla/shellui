''' Common classes '''


class ReadOnlyCachedProperty(object):
  '''Decorator for creating readonly cached properties.  In other words, it
  allows you to create a property that generates a value (however that is) and
  cache it so that it doesn't need to be generated again.  To force
  regeneration, delete the property (del obj.prop).

  provided by: Lex Scarisbrick (lscarisb) <lscarisb@cisco.com>
  '''
  def __init__(self, method, name=None):
    self.method = method
    self.name = name or method.__name__
    self.__doc__ = method.__doc__

  def __get__(self, inst, cls):
    if inst is None:
      result = self
    elif self.name in inst.__dict__:
      result = inst.__dict__[self.name]
    else:
      result = self.method(inst)
      inst.__dict__[self.name] = result
    return result

  def __set__(self, inst, value):
    raise AttributeError('property is read-only')

  def __delete__(self, inst):
    del inst.__dict__[self.name]
