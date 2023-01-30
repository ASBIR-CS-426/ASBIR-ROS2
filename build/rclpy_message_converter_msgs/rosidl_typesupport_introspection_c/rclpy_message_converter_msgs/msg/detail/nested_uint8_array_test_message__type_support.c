// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rclpy_message_converter_msgs:msg/NestedUint8ArrayTestMessage.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rclpy_message_converter_msgs/msg/detail/nested_uint8_array_test_message__rosidl_typesupport_introspection_c.h"
#include "rclpy_message_converter_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rclpy_message_converter_msgs/msg/detail/nested_uint8_array_test_message__functions.h"
#include "rclpy_message_converter_msgs/msg/detail/nested_uint8_array_test_message__struct.h"


// Include directives for member types
// Member `arrays`
#include "rclpy_message_converter_msgs/msg/uint8_array_test_message.h"
// Member `arrays`
#include "rclpy_message_converter_msgs/msg/detail/uint8_array_test_message__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rclpy_message_converter_msgs__msg__NestedUint8ArrayTestMessage__init(message_memory);
}

void NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_fini_function(void * message_memory)
{
  rclpy_message_converter_msgs__msg__NestedUint8ArrayTestMessage__fini(message_memory);
}

size_t NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__size_function__Uint8ArrayTestMessage__arrays(
  const void * untyped_member)
{
  const rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence * member =
    (const rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence *)(untyped_member);
  return member->size;
}

const void * NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__get_const_function__Uint8ArrayTestMessage__arrays(
  const void * untyped_member, size_t index)
{
  const rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence * member =
    (const rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence *)(untyped_member);
  return &member->data[index];
}

void * NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__get_function__Uint8ArrayTestMessage__arrays(
  void * untyped_member, size_t index)
{
  rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence * member =
    (rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence *)(untyped_member);
  return &member->data[index];
}

bool NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__resize_function__Uint8ArrayTestMessage__arrays(
  void * untyped_member, size_t size)
{
  rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence * member =
    (rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence *)(untyped_member);
  rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence__fini(member);
  return rclpy_message_converter_msgs__msg__Uint8ArrayTestMessage__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_member_array[1] = {
  {
    "arrays",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rclpy_message_converter_msgs__msg__NestedUint8ArrayTestMessage, arrays),  // bytes offset in struct
    NULL,  // default value
    NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__size_function__Uint8ArrayTestMessage__arrays,  // size() function pointer
    NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__get_const_function__Uint8ArrayTestMessage__arrays,  // get_const(index) function pointer
    NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__get_function__Uint8ArrayTestMessage__arrays,  // get(index) function pointer
    NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__resize_function__Uint8ArrayTestMessage__arrays  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_members = {
  "rclpy_message_converter_msgs__msg",  // message namespace
  "NestedUint8ArrayTestMessage",  // message name
  1,  // number of fields
  sizeof(rclpy_message_converter_msgs__msg__NestedUint8ArrayTestMessage),
  NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_member_array,  // message members
  NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_init_function,  // function to initialize message memory (memory has to be allocated)
  NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_type_support_handle = {
  0,
  &NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rclpy_message_converter_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rclpy_message_converter_msgs, msg, NestedUint8ArrayTestMessage)() {
  NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rclpy_message_converter_msgs, msg, Uint8ArrayTestMessage)();
  if (!NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_type_support_handle.typesupport_identifier) {
    NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &NestedUint8ArrayTestMessage__rosidl_typesupport_introspection_c__NestedUint8ArrayTestMessage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
