# generated from rosidl_generator_py/resource/_idl.py.em
# with input from action_state:action/Jointstate.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Jointstate_Goal(type):
    """Metaclass of message 'Jointstate_Goal'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__goal

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_Goal(metaclass=Metaclass_Jointstate_Goal):
    """Message class 'Jointstate_Goal'."""

    __slots__ = [
        '_left_front_foot',
        '_left_front_thigh',
        '_left_back_foot',
        '_left_back_thigh',
        '_right_front_foot',
        '_right_front_thigh',
        '_right_back_foot',
        '_right_back_thigh',
    ]

    _fields_and_field_types = {
        'left_front_foot': 'float',
        'left_front_thigh': 'float',
        'left_back_foot': 'float',
        'left_back_thigh': 'float',
        'right_front_foot': 'float',
        'right_front_thigh': 'float',
        'right_back_foot': 'float',
        'right_back_thigh': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.left_front_foot = kwargs.get('left_front_foot', float())
        self.left_front_thigh = kwargs.get('left_front_thigh', float())
        self.left_back_foot = kwargs.get('left_back_foot', float())
        self.left_back_thigh = kwargs.get('left_back_thigh', float())
        self.right_front_foot = kwargs.get('right_front_foot', float())
        self.right_front_thigh = kwargs.get('right_front_thigh', float())
        self.right_back_foot = kwargs.get('right_back_foot', float())
        self.right_back_thigh = kwargs.get('right_back_thigh', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.left_front_foot != other.left_front_foot:
            return False
        if self.left_front_thigh != other.left_front_thigh:
            return False
        if self.left_back_foot != other.left_back_foot:
            return False
        if self.left_back_thigh != other.left_back_thigh:
            return False
        if self.right_front_foot != other.right_front_foot:
            return False
        if self.right_front_thigh != other.right_front_thigh:
            return False
        if self.right_back_foot != other.right_back_foot:
            return False
        if self.right_back_thigh != other.right_back_thigh:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def left_front_foot(self):
        """Message field 'left_front_foot'."""
        return self._left_front_foot

    @left_front_foot.setter
    def left_front_foot(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_front_foot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_front_foot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_front_foot = value

    @builtins.property
    def left_front_thigh(self):
        """Message field 'left_front_thigh'."""
        return self._left_front_thigh

    @left_front_thigh.setter
    def left_front_thigh(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_front_thigh' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_front_thigh' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_front_thigh = value

    @builtins.property
    def left_back_foot(self):
        """Message field 'left_back_foot'."""
        return self._left_back_foot

    @left_back_foot.setter
    def left_back_foot(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_back_foot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_back_foot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_back_foot = value

    @builtins.property
    def left_back_thigh(self):
        """Message field 'left_back_thigh'."""
        return self._left_back_thigh

    @left_back_thigh.setter
    def left_back_thigh(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_back_thigh' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_back_thigh' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_back_thigh = value

    @builtins.property
    def right_front_foot(self):
        """Message field 'right_front_foot'."""
        return self._right_front_foot

    @right_front_foot.setter
    def right_front_foot(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_front_foot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_front_foot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_front_foot = value

    @builtins.property
    def right_front_thigh(self):
        """Message field 'right_front_thigh'."""
        return self._right_front_thigh

    @right_front_thigh.setter
    def right_front_thigh(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_front_thigh' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_front_thigh' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_front_thigh = value

    @builtins.property
    def right_back_foot(self):
        """Message field 'right_back_foot'."""
        return self._right_back_foot

    @right_back_foot.setter
    def right_back_foot(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_back_foot' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_back_foot' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_back_foot = value

    @builtins.property
    def right_back_thigh(self):
        """Message field 'right_back_thigh'."""
        return self._right_back_thigh

    @right_back_thigh.setter
    def right_back_thigh(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_back_thigh' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_back_thigh' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_back_thigh = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Jointstate_Result(type):
    """Metaclass of message 'Jointstate_Result'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__result

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_Result(metaclass=Metaclass_Jointstate_Result):
    """Message class 'Jointstate_Result'."""

    __slots__ = [
        '_result',
    ]

    _fields_and_field_types = {
        'result': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.result = kwargs.get('result', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'result' field must be of type 'bool'"
        self._result = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Jointstate_Feedback(type):
    """Metaclass of message 'Jointstate_Feedback'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__feedback

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_Feedback(metaclass=Metaclass_Jointstate_Feedback):
    """Message class 'Jointstate_Feedback'."""

    __slots__ = [
        '_partial_result',
    ]

    _fields_and_field_types = {
        'partial_result': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.partial_result = kwargs.get('partial_result', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.partial_result != other.partial_result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def partial_result(self):
        """Message field 'partial_result'."""
        return self._partial_result

    @partial_result.setter
    def partial_result(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'partial_result' field must be of type 'bool'"
        self._partial_result = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Jointstate_SendGoal_Request(type):
    """Metaclass of message 'Jointstate_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__send_goal__request

            from action_state.action import Jointstate
            if Jointstate.Goal.__class__._TYPE_SUPPORT is None:
                Jointstate.Goal.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_SendGoal_Request(metaclass=Metaclass_Jointstate_SendGoal_Request):
    """Message class 'Jointstate_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'action_state/Jointstate_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['action_state', 'action'], 'Jointstate_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from action_state.action._jointstate import Jointstate_Goal
        self.goal = kwargs.get('goal', Jointstate_Goal())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            from action_state.action._jointstate import Jointstate_Goal
            assert \
                isinstance(value, Jointstate_Goal), \
                "The 'goal' field must be a sub message of type 'Jointstate_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Jointstate_SendGoal_Response(type):
    """Metaclass of message 'Jointstate_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__send_goal__response

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_SendGoal_Response(metaclass=Metaclass_Jointstate_SendGoal_Response):
    """Message class 'Jointstate_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
    ]

    _fields_and_field_types = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accepted = kwargs.get('accepted', bool())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self):
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


class Metaclass_Jointstate_SendGoal(type):
    """Metaclass of service 'Jointstate_SendGoal'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__jointstate__send_goal

            from action_state.action import _jointstate
            if _jointstate.Metaclass_Jointstate_SendGoal_Request._TYPE_SUPPORT is None:
                _jointstate.Metaclass_Jointstate_SendGoal_Request.__import_type_support__()
            if _jointstate.Metaclass_Jointstate_SendGoal_Response._TYPE_SUPPORT is None:
                _jointstate.Metaclass_Jointstate_SendGoal_Response.__import_type_support__()


class Jointstate_SendGoal(metaclass=Metaclass_Jointstate_SendGoal):
    from action_state.action._jointstate import Jointstate_SendGoal_Request as Request
    from action_state.action._jointstate import Jointstate_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Jointstate_GetResult_Request(type):
    """Metaclass of message 'Jointstate_GetResult_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_GetResult_Request(metaclass=Metaclass_Jointstate_GetResult_Request):
    """Message class 'Jointstate_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Jointstate_GetResult_Response(type):
    """Metaclass of message 'Jointstate_GetResult_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__get_result__response

            from action_state.action import Jointstate
            if Jointstate.Result.__class__._TYPE_SUPPORT is None:
                Jointstate.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_GetResult_Response(metaclass=Metaclass_Jointstate_GetResult_Response):
    """Message class 'Jointstate_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'action_state/Jointstate_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['action_state', 'action'], 'Jointstate_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from action_state.action._jointstate import Jointstate_Result
        self.result = kwargs.get('result', Jointstate_Result())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from action_state.action._jointstate import Jointstate_Result
            assert \
                isinstance(value, Jointstate_Result), \
                "The 'result' field must be a sub message of type 'Jointstate_Result'"
        self._result = value


class Metaclass_Jointstate_GetResult(type):
    """Metaclass of service 'Jointstate_GetResult'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__jointstate__get_result

            from action_state.action import _jointstate
            if _jointstate.Metaclass_Jointstate_GetResult_Request._TYPE_SUPPORT is None:
                _jointstate.Metaclass_Jointstate_GetResult_Request.__import_type_support__()
            if _jointstate.Metaclass_Jointstate_GetResult_Response._TYPE_SUPPORT is None:
                _jointstate.Metaclass_Jointstate_GetResult_Response.__import_type_support__()


class Jointstate_GetResult(metaclass=Metaclass_Jointstate_GetResult):
    from action_state.action._jointstate import Jointstate_GetResult_Request as Request
    from action_state.action._jointstate import Jointstate_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Jointstate_FeedbackMessage(type):
    """Metaclass of message 'Jointstate_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__jointstate__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__jointstate__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__jointstate__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__jointstate__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__jointstate__feedback_message

            from action_state.action import Jointstate
            if Jointstate.Feedback.__class__._TYPE_SUPPORT is None:
                Jointstate.Feedback.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Jointstate_FeedbackMessage(metaclass=Metaclass_Jointstate_FeedbackMessage):
    """Message class 'Jointstate_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'action_state/Jointstate_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['action_state', 'action'], 'Jointstate_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from action_state.action._jointstate import Jointstate_Feedback
        self.feedback = kwargs.get('feedback', Jointstate_Feedback())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self):
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        if __debug__:
            from action_state.action._jointstate import Jointstate_Feedback
            assert \
                isinstance(value, Jointstate_Feedback), \
                "The 'feedback' field must be a sub message of type 'Jointstate_Feedback'"
        self._feedback = value


class Metaclass_Jointstate(type):
    """Metaclass of action 'Jointstate'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('action_state')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'action_state.action.Jointstate')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__jointstate

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from action_state.action import _jointstate
            if _jointstate.Metaclass_Jointstate_SendGoal._TYPE_SUPPORT is None:
                _jointstate.Metaclass_Jointstate_SendGoal.__import_type_support__()
            if _jointstate.Metaclass_Jointstate_GetResult._TYPE_SUPPORT is None:
                _jointstate.Metaclass_Jointstate_GetResult.__import_type_support__()
            if _jointstate.Metaclass_Jointstate_FeedbackMessage._TYPE_SUPPORT is None:
                _jointstate.Metaclass_Jointstate_FeedbackMessage.__import_type_support__()


class Jointstate(metaclass=Metaclass_Jointstate):

    # The goal message defined in the action definition.
    from action_state.action._jointstate import Jointstate_Goal as Goal
    # The result message defined in the action definition.
    from action_state.action._jointstate import Jointstate_Result as Result
    # The feedback message defined in the action definition.
    from action_state.action._jointstate import Jointstate_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from action_state.action._jointstate import Jointstate_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from action_state.action._jointstate import Jointstate_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from action_state.action._jointstate import Jointstate_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
