// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from action_state:action/Jointstate.idl
// generated code does not contain a copyright notice

#ifndef ACTION_STATE__ACTION__DETAIL__JOINTSTATE__BUILDER_HPP_
#define ACTION_STATE__ACTION__DETAIL__JOINTSTATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "action_state/action/detail/jointstate__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_Goal_right_back_thigh
{
public:
  explicit Init_Jointstate_Goal_right_back_thigh(::action_state::action::Jointstate_Goal & msg)
  : msg_(msg)
  {}
  ::action_state::action::Jointstate_Goal right_back_thigh(::action_state::action::Jointstate_Goal::_right_back_thigh_type arg)
  {
    msg_.right_back_thigh = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

class Init_Jointstate_Goal_right_back_foot
{
public:
  explicit Init_Jointstate_Goal_right_back_foot(::action_state::action::Jointstate_Goal & msg)
  : msg_(msg)
  {}
  Init_Jointstate_Goal_right_back_thigh right_back_foot(::action_state::action::Jointstate_Goal::_right_back_foot_type arg)
  {
    msg_.right_back_foot = std::move(arg);
    return Init_Jointstate_Goal_right_back_thigh(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

class Init_Jointstate_Goal_right_front_thigh
{
public:
  explicit Init_Jointstate_Goal_right_front_thigh(::action_state::action::Jointstate_Goal & msg)
  : msg_(msg)
  {}
  Init_Jointstate_Goal_right_back_foot right_front_thigh(::action_state::action::Jointstate_Goal::_right_front_thigh_type arg)
  {
    msg_.right_front_thigh = std::move(arg);
    return Init_Jointstate_Goal_right_back_foot(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

class Init_Jointstate_Goal_right_front_foot
{
public:
  explicit Init_Jointstate_Goal_right_front_foot(::action_state::action::Jointstate_Goal & msg)
  : msg_(msg)
  {}
  Init_Jointstate_Goal_right_front_thigh right_front_foot(::action_state::action::Jointstate_Goal::_right_front_foot_type arg)
  {
    msg_.right_front_foot = std::move(arg);
    return Init_Jointstate_Goal_right_front_thigh(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

class Init_Jointstate_Goal_left_back_thigh
{
public:
  explicit Init_Jointstate_Goal_left_back_thigh(::action_state::action::Jointstate_Goal & msg)
  : msg_(msg)
  {}
  Init_Jointstate_Goal_right_front_foot left_back_thigh(::action_state::action::Jointstate_Goal::_left_back_thigh_type arg)
  {
    msg_.left_back_thigh = std::move(arg);
    return Init_Jointstate_Goal_right_front_foot(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

class Init_Jointstate_Goal_left_back_foot
{
public:
  explicit Init_Jointstate_Goal_left_back_foot(::action_state::action::Jointstate_Goal & msg)
  : msg_(msg)
  {}
  Init_Jointstate_Goal_left_back_thigh left_back_foot(::action_state::action::Jointstate_Goal::_left_back_foot_type arg)
  {
    msg_.left_back_foot = std::move(arg);
    return Init_Jointstate_Goal_left_back_thigh(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

class Init_Jointstate_Goal_left_front_thigh
{
public:
  explicit Init_Jointstate_Goal_left_front_thigh(::action_state::action::Jointstate_Goal & msg)
  : msg_(msg)
  {}
  Init_Jointstate_Goal_left_back_foot left_front_thigh(::action_state::action::Jointstate_Goal::_left_front_thigh_type arg)
  {
    msg_.left_front_thigh = std::move(arg);
    return Init_Jointstate_Goal_left_back_foot(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

class Init_Jointstate_Goal_left_front_foot
{
public:
  Init_Jointstate_Goal_left_front_foot()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Jointstate_Goal_left_front_thigh left_front_foot(::action_state::action::Jointstate_Goal::_left_front_foot_type arg)
  {
    msg_.left_front_foot = std::move(arg);
    return Init_Jointstate_Goal_left_front_thigh(msg_);
  }

private:
  ::action_state::action::Jointstate_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_Goal>()
{
  return action_state::action::builder::Init_Jointstate_Goal_left_front_foot();
}

}  // namespace action_state


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_Result_result
{
public:
  Init_Jointstate_Result_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_state::action::Jointstate_Result result(::action_state::action::Jointstate_Result::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_Result>()
{
  return action_state::action::builder::Init_Jointstate_Result_result();
}

}  // namespace action_state


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_Feedback_partial_result
{
public:
  Init_Jointstate_Feedback_partial_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_state::action::Jointstate_Feedback partial_result(::action_state::action::Jointstate_Feedback::_partial_result_type arg)
  {
    msg_.partial_result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_Feedback>()
{
  return action_state::action::builder::Init_Jointstate_Feedback_partial_result();
}

}  // namespace action_state


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_SendGoal_Request_goal
{
public:
  explicit Init_Jointstate_SendGoal_Request_goal(::action_state::action::Jointstate_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::action_state::action::Jointstate_SendGoal_Request goal(::action_state::action::Jointstate_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_SendGoal_Request msg_;
};

class Init_Jointstate_SendGoal_Request_goal_id
{
public:
  Init_Jointstate_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Jointstate_SendGoal_Request_goal goal_id(::action_state::action::Jointstate_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Jointstate_SendGoal_Request_goal(msg_);
  }

private:
  ::action_state::action::Jointstate_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_SendGoal_Request>()
{
  return action_state::action::builder::Init_Jointstate_SendGoal_Request_goal_id();
}

}  // namespace action_state


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_SendGoal_Response_stamp
{
public:
  explicit Init_Jointstate_SendGoal_Response_stamp(::action_state::action::Jointstate_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::action_state::action::Jointstate_SendGoal_Response stamp(::action_state::action::Jointstate_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_SendGoal_Response msg_;
};

class Init_Jointstate_SendGoal_Response_accepted
{
public:
  Init_Jointstate_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Jointstate_SendGoal_Response_stamp accepted(::action_state::action::Jointstate_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Jointstate_SendGoal_Response_stamp(msg_);
  }

private:
  ::action_state::action::Jointstate_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_SendGoal_Response>()
{
  return action_state::action::builder::Init_Jointstate_SendGoal_Response_accepted();
}

}  // namespace action_state


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_GetResult_Request_goal_id
{
public:
  Init_Jointstate_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::action_state::action::Jointstate_GetResult_Request goal_id(::action_state::action::Jointstate_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_GetResult_Request>()
{
  return action_state::action::builder::Init_Jointstate_GetResult_Request_goal_id();
}

}  // namespace action_state


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_GetResult_Response_result
{
public:
  explicit Init_Jointstate_GetResult_Response_result(::action_state::action::Jointstate_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::action_state::action::Jointstate_GetResult_Response result(::action_state::action::Jointstate_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_GetResult_Response msg_;
};

class Init_Jointstate_GetResult_Response_status
{
public:
  Init_Jointstate_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Jointstate_GetResult_Response_result status(::action_state::action::Jointstate_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Jointstate_GetResult_Response_result(msg_);
  }

private:
  ::action_state::action::Jointstate_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_GetResult_Response>()
{
  return action_state::action::builder::Init_Jointstate_GetResult_Response_status();
}

}  // namespace action_state


namespace action_state
{

namespace action
{

namespace builder
{

class Init_Jointstate_FeedbackMessage_feedback
{
public:
  explicit Init_Jointstate_FeedbackMessage_feedback(::action_state::action::Jointstate_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::action_state::action::Jointstate_FeedbackMessage feedback(::action_state::action::Jointstate_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::action_state::action::Jointstate_FeedbackMessage msg_;
};

class Init_Jointstate_FeedbackMessage_goal_id
{
public:
  Init_Jointstate_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Jointstate_FeedbackMessage_feedback goal_id(::action_state::action::Jointstate_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Jointstate_FeedbackMessage_feedback(msg_);
  }

private:
  ::action_state::action::Jointstate_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::action_state::action::Jointstate_FeedbackMessage>()
{
  return action_state::action::builder::Init_Jointstate_FeedbackMessage_goal_id();
}

}  // namespace action_state

#endif  // ACTION_STATE__ACTION__DETAIL__JOINTSTATE__BUILDER_HPP_
