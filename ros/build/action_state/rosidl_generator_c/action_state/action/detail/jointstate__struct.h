// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from action_state:action/Jointstate.idl
// generated code does not contain a copyright notice

#ifndef ACTION_STATE__ACTION__DETAIL__JOINTSTATE__STRUCT_H_
#define ACTION_STATE__ACTION__DETAIL__JOINTSTATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_Goal
{
  float left_front_foot;
  float left_front_thigh;
  float left_back_foot;
  float left_back_thigh;
  float right_front_foot;
  float right_front_thigh;
  float right_back_foot;
  float right_back_thigh;
} action_state__action__Jointstate_Goal;

// Struct for a sequence of action_state__action__Jointstate_Goal.
typedef struct action_state__action__Jointstate_Goal__Sequence
{
  action_state__action__Jointstate_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_Result
{
  bool result;
} action_state__action__Jointstate_Result;

// Struct for a sequence of action_state__action__Jointstate_Result.
typedef struct action_state__action__Jointstate_Result__Sequence
{
  action_state__action__Jointstate_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_Feedback
{
  bool partial_result;
} action_state__action__Jointstate_Feedback;

// Struct for a sequence of action_state__action__Jointstate_Feedback.
typedef struct action_state__action__Jointstate_Feedback__Sequence
{
  action_state__action__Jointstate_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "action_state/action/detail/jointstate__struct.h"

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  action_state__action__Jointstate_Goal goal;
} action_state__action__Jointstate_SendGoal_Request;

// Struct for a sequence of action_state__action__Jointstate_SendGoal_Request.
typedef struct action_state__action__Jointstate_SendGoal_Request__Sequence
{
  action_state__action__Jointstate_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} action_state__action__Jointstate_SendGoal_Response;

// Struct for a sequence of action_state__action__Jointstate_SendGoal_Response.
typedef struct action_state__action__Jointstate_SendGoal_Response__Sequence
{
  action_state__action__Jointstate_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} action_state__action__Jointstate_GetResult_Request;

// Struct for a sequence of action_state__action__Jointstate_GetResult_Request.
typedef struct action_state__action__Jointstate_GetResult_Request__Sequence
{
  action_state__action__Jointstate_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "action_state/action/detail/jointstate__struct.h"

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_GetResult_Response
{
  int8_t status;
  action_state__action__Jointstate_Result result;
} action_state__action__Jointstate_GetResult_Response;

// Struct for a sequence of action_state__action__Jointstate_GetResult_Response.
typedef struct action_state__action__Jointstate_GetResult_Response__Sequence
{
  action_state__action__Jointstate_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "action_state/action/detail/jointstate__struct.h"

/// Struct defined in action/Jointstate in the package action_state.
typedef struct action_state__action__Jointstate_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  action_state__action__Jointstate_Feedback feedback;
} action_state__action__Jointstate_FeedbackMessage;

// Struct for a sequence of action_state__action__Jointstate_FeedbackMessage.
typedef struct action_state__action__Jointstate_FeedbackMessage__Sequence
{
  action_state__action__Jointstate_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} action_state__action__Jointstate_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ACTION_STATE__ACTION__DETAIL__JOINTSTATE__STRUCT_H_
