# -*- coding: utf-8 -*-


from brainpy.base.base import BrainPyObject

__all__ = [
  'Encoder'
]


class Encoder(BrainPyObject):
  """Base class for encoding rate values as spike trains."""
  def __call__(self, *args, **kwargs):
    raise NotImplementedError

  def __repr__(self):
    return self.__class__.__name__