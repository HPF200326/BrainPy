import brainpy as bp
import brainpy.math as bm

import unittest


class TestParamDesc(unittest.TestCase):
  def test1(self):
    a = bp.dyn.Expon(1)
    self.assertTrue(not isinstance(a, bp.mixin.ParamDescInit[bp.dyn.Expon]))
    self.assertTrue(not isinstance(a, bp.mixin.ParamDescInit[bp.DynamicalSystem]))

  def test2(self):
    a = bp.dyn.Expon.desc(1)
    self.assertTrue(isinstance(a, bp.mixin.ParamDescInit[bp.dyn.Expon]))
    self.assertTrue(isinstance(a, bp.mixin.ParamDescInit[bp.DynamicalSystem]))


class TestJointType(unittest.TestCase):
  def test1(self):
    T = bp.mixin.JointType[bp.DynamicalSystem]
    self.assertTrue(isinstance(bp.dnn.Layer(), T))

    T = bp.mixin.JointType[bp.DynamicalSystem, bp.mixin.ParamDesc]
    self.assertTrue(isinstance(bp.dyn.Expon(1), T))

  def test2(self):
    T = bp.mixin.JointType[bp.DynamicalSystem, bp.mixin.ParamDesc]
    self.assertTrue(not isinstance(bp.dyn.Expon(1), bp.mixin.ParamDescInit[T]))
    self.assertTrue(isinstance(bp.dyn.Expon.desc(1), bp.mixin.ParamDescInit[T]))


class TestDelayRegister(unittest.TestCase):
  def test11(self):
    lif = bp.dyn.Lif(10)
    with self.assertWarns(UserWarning):
      lif.register_delay('pre.spike', 10, lif.spike)

    with self.assertWarns(UserWarning):
      lif.get_delay_data('pre.spike', 10)

  def test2(self):
    bp.share.save(i=0)
    lif = bp.dyn.Lif(10)
    lif.register_delay_at('a', 10.)
    data = lif.get_delay_at('a')
    self.assertTrue(bm.allclose(data, bm.zeros(10)))



