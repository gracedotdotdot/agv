# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from baxter_maintenance_msgs/TareEnable.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import baxter_maintenance_msgs.msg

class TareEnable(genpy.Message):
  _md5sum = "1d38ec0923789ab928453d933bef8c51"
  _type = "baxter_maintenance_msgs/TareEnable"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool isEnabled
string uid
TareData data

================================================================================
MSG: baxter_maintenance_msgs/TareData
bool tuneGravitySpring
"""
  __slots__ = ['isEnabled','uid','data']
  _slot_types = ['bool','string','baxter_maintenance_msgs/TareData']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       isEnabled,uid,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TareEnable, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.isEnabled is None:
        self.isEnabled = False
      if self.uid is None:
        self.uid = ''
      if self.data is None:
        self.data = baxter_maintenance_msgs.msg.TareData()
    else:
      self.isEnabled = False
      self.uid = ''
      self.data = baxter_maintenance_msgs.msg.TareData()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.isEnabled
      buff.write(_get_struct_B().pack(_x))
      _x = self.uid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.data.tuneGravitySpring
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.data is None:
        self.data = baxter_maintenance_msgs.msg.TareData()
      end = 0
      start = end
      end += 1
      (self.isEnabled,) = _get_struct_B().unpack(str[start:end])
      self.isEnabled = bool(self.isEnabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.uid = str[start:end].decode('utf-8')
      else:
        self.uid = str[start:end]
      start = end
      end += 1
      (self.data.tuneGravitySpring,) = _get_struct_B().unpack(str[start:end])
      self.data.tuneGravitySpring = bool(self.data.tuneGravitySpring)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.isEnabled
      buff.write(_get_struct_B().pack(_x))
      _x = self.uid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.data.tuneGravitySpring
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.data is None:
        self.data = baxter_maintenance_msgs.msg.TareData()
      end = 0
      start = end
      end += 1
      (self.isEnabled,) = _get_struct_B().unpack(str[start:end])
      self.isEnabled = bool(self.isEnabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.uid = str[start:end].decode('utf-8')
      else:
        self.uid = str[start:end]
      start = end
      end += 1
      (self.data.tuneGravitySpring,) = _get_struct_B().unpack(str[start:end])
      self.data.tuneGravitySpring = bool(self.data.tuneGravitySpring)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B