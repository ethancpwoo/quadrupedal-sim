// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from action_state:action/Jointstate.idl
// generated code does not contain a copyright notice

#ifndef ACTION_STATE__ACTION__DETAIL__JOINTSTATE__STRUCT_HPP_
#define ACTION_STATE__ACTION__DETAIL__JOINTSTATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_Goal __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_Goal __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_Goal_
{
  using Type = Jointstate_Goal_<ContainerAllocator>;

  explicit Jointstate_Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_front_foot = 0.0f;
      this->left_front_thigh = 0.0f;
      this->left_back_foot = 0.0f;
      this->left_back_thigh = 0.0f;
      this->right_front_foot = 0.0f;
      this->right_front_thigh = 0.0f;
      this->right_back_foot = 0.0f;
      this->right_back_thigh = 0.0f;
    }
  }

  explicit Jointstate_Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_front_foot = 0.0f;
      this->left_front_thigh = 0.0f;
      this->left_back_foot = 0.0f;
      this->left_back_thigh = 0.0f;
      this->right_front_foot = 0.0f;
      this->right_front_thigh = 0.0f;
      this->right_back_foot = 0.0f;
      this->right_back_thigh = 0.0f;
    }
  }

  // field types and members
  using _left_front_foot_type =
    float;
  _left_front_foot_type left_front_foot;
  using _left_front_thigh_type =
    float;
  _left_front_thigh_type left_front_thigh;
  using _left_back_foot_type =
    float;
  _left_back_foot_type left_back_foot;
  using _left_back_thigh_type =
    float;
  _left_back_thigh_type left_back_thigh;
  using _right_front_foot_type =
    float;
  _right_front_foot_type right_front_foot;
  using _right_front_thigh_type =
    float;
  _right_front_thigh_type right_front_thigh;
  using _right_back_foot_type =
    float;
  _right_back_foot_type right_back_foot;
  using _right_back_thigh_type =
    float;
  _right_back_thigh_type right_back_thigh;

  // setters for named parameter idiom
  Type & set__left_front_foot(
    const float & _arg)
  {
    this->left_front_foot = _arg;
    return *this;
  }
  Type & set__left_front_thigh(
    const float & _arg)
  {
    this->left_front_thigh = _arg;
    return *this;
  }
  Type & set__left_back_foot(
    const float & _arg)
  {
    this->left_back_foot = _arg;
    return *this;
  }
  Type & set__left_back_thigh(
    const float & _arg)
  {
    this->left_back_thigh = _arg;
    return *this;
  }
  Type & set__right_front_foot(
    const float & _arg)
  {
    this->right_front_foot = _arg;
    return *this;
  }
  Type & set__right_front_thigh(
    const float & _arg)
  {
    this->right_front_thigh = _arg;
    return *this;
  }
  Type & set__right_back_foot(
    const float & _arg)
  {
    this->right_back_foot = _arg;
    return *this;
  }
  Type & set__right_back_thigh(
    const float & _arg)
  {
    this->right_back_thigh = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_Goal
    std::shared_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_Goal
    std::shared_ptr<action_state::action::Jointstate_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_Goal_ & other) const
  {
    if (this->left_front_foot != other.left_front_foot) {
      return false;
    }
    if (this->left_front_thigh != other.left_front_thigh) {
      return false;
    }
    if (this->left_back_foot != other.left_back_foot) {
      return false;
    }
    if (this->left_back_thigh != other.left_back_thigh) {
      return false;
    }
    if (this->right_front_foot != other.right_front_foot) {
      return false;
    }
    if (this->right_front_thigh != other.right_front_thigh) {
      return false;
    }
    if (this->right_back_foot != other.right_back_foot) {
      return false;
    }
    if (this->right_back_thigh != other.right_back_thigh) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_Goal_

// alias to use template instance with default allocator
using Jointstate_Goal =
  action_state::action::Jointstate_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state


#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_Result __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_Result __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_Result_
{
  using Type = Jointstate_Result_<ContainerAllocator>;

  explicit Jointstate_Result_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  explicit Jointstate_Result_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  // field types and members
  using _result_type =
    bool;
  _result_type result;

  // setters for named parameter idiom
  Type & set__result(
    const bool & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_Result
    std::shared_ptr<action_state::action::Jointstate_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_Result
    std::shared_ptr<action_state::action::Jointstate_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_Result_ & other) const
  {
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_Result_

// alias to use template instance with default allocator
using Jointstate_Result =
  action_state::action::Jointstate_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state


#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_Feedback __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_Feedback_
{
  using Type = Jointstate_Feedback_<ContainerAllocator>;

  explicit Jointstate_Feedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->partial_result = false;
    }
  }

  explicit Jointstate_Feedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->partial_result = false;
    }
  }

  // field types and members
  using _partial_result_type =
    bool;
  _partial_result_type partial_result;

  // setters for named parameter idiom
  Type & set__partial_result(
    const bool & _arg)
  {
    this->partial_result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_Feedback
    std::shared_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_Feedback
    std::shared_ptr<action_state::action::Jointstate_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_Feedback_ & other) const
  {
    if (this->partial_result != other.partial_result) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_Feedback_

// alias to use template instance with default allocator
using Jointstate_Feedback =
  action_state::action::Jointstate_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state


// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'goal'
#include "action_state/action/detail/jointstate__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_SendGoal_Request __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_SendGoal_Request_
{
  using Type = Jointstate_SendGoal_Request_<ContainerAllocator>;

  explicit Jointstate_SendGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit Jointstate_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    action_state::action::Jointstate_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const action_state::action::Jointstate_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_SendGoal_Request
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_SendGoal_Request
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_SendGoal_Request_

// alias to use template instance with default allocator
using Jointstate_SendGoal_Request =
  action_state::action::Jointstate_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_SendGoal_Response __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_SendGoal_Response_
{
  using Type = Jointstate_SendGoal_Response_<ContainerAllocator>;

  explicit Jointstate_SendGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit Jointstate_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_SendGoal_Response
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_SendGoal_Response
    std::shared_ptr<action_state::action::Jointstate_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_SendGoal_Response_

// alias to use template instance with default allocator
using Jointstate_SendGoal_Response =
  action_state::action::Jointstate_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state

namespace action_state
{

namespace action
{

struct Jointstate_SendGoal
{
  using Request = action_state::action::Jointstate_SendGoal_Request;
  using Response = action_state::action::Jointstate_SendGoal_Response;
};

}  // namespace action

}  // namespace action_state


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_GetResult_Request __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_GetResult_Request_
{
  using Type = Jointstate_GetResult_Request_<ContainerAllocator>;

  explicit Jointstate_GetResult_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit Jointstate_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_GetResult_Request
    std::shared_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_GetResult_Request
    std::shared_ptr<action_state::action::Jointstate_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_GetResult_Request_

// alias to use template instance with default allocator
using Jointstate_GetResult_Request =
  action_state::action::Jointstate_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state


// Include directives for member types
// Member 'result'
// already included above
// #include "action_state/action/detail/jointstate__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_GetResult_Response __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_GetResult_Response_
{
  using Type = Jointstate_GetResult_Response_<ContainerAllocator>;

  explicit Jointstate_GetResult_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit Jointstate_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    action_state::action::Jointstate_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const action_state::action::Jointstate_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_GetResult_Response
    std::shared_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_GetResult_Response
    std::shared_ptr<action_state::action::Jointstate_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_GetResult_Response_

// alias to use template instance with default allocator
using Jointstate_GetResult_Response =
  action_state::action::Jointstate_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state

namespace action_state
{

namespace action
{

struct Jointstate_GetResult
{
  using Request = action_state::action::Jointstate_GetResult_Request;
  using Response = action_state::action::Jointstate_GetResult_Response;
};

}  // namespace action

}  // namespace action_state


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "action_state/action/detail/jointstate__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__action_state__action__Jointstate_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__action_state__action__Jointstate_FeedbackMessage __declspec(deprecated)
#endif

namespace action_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Jointstate_FeedbackMessage_
{
  using Type = Jointstate_FeedbackMessage_<ContainerAllocator>;

  explicit Jointstate_FeedbackMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit Jointstate_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    action_state::action::Jointstate_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const action_state::action::Jointstate_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__action_state__action__Jointstate_FeedbackMessage
    std::shared_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__action_state__action__Jointstate_FeedbackMessage
    std::shared_ptr<action_state::action::Jointstate_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Jointstate_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const Jointstate_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Jointstate_FeedbackMessage_

// alias to use template instance with default allocator
using Jointstate_FeedbackMessage =
  action_state::action::Jointstate_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace action_state

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace action_state
{

namespace action
{

struct Jointstate
{
  /// The goal message defined in the action definition.
  using Goal = action_state::action::Jointstate_Goal;
  /// The result message defined in the action definition.
  using Result = action_state::action::Jointstate_Result;
  /// The feedback message defined in the action definition.
  using Feedback = action_state::action::Jointstate_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = action_state::action::Jointstate_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = action_state::action::Jointstate_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = action_state::action::Jointstate_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct Jointstate Jointstate;

}  // namespace action

}  // namespace action_state

#endif  // ACTION_STATE__ACTION__DETAIL__JOINTSTATE__STRUCT_HPP_
