// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rclpy_message_converter_msgs:msg/Uint8Array3TestMessage.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rclpy_message_converter_msgs/msg/detail/uint8_array3_test_message__rosidl_typesupport_introspection_c.h"
#include "rclpy_message_converter_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rclpy_message_converter_msgs/msg/detail/uint8_array3_test_message__functions.h"
#include "rclpy_message_converter_msgs/msg/detail/uint8_array3_test_message__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__init(message_memory);
}

void Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_fini_function(void * message_memory)
{
  rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_member_array[1] = {
  {
    "data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage, data),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_members = {
  "rclpy_message_converter_msgs__msg",  // message namespace
  "Uint8Array3TestMessage",  // message name
  1,  // number of fields
  sizeof(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage),
  Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_member_array,  // message members
  Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_init_function,  // function to initialize message memory (memory has to be allocated)
  Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_type_support_handle = {
  0,
  &Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rclpy_message_converter_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rclpy_message_converter_msgs, msg, Uint8Array3TestMessage)() {
  if (!Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_type_support_handle.typesupport_identifier) {
    Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Uint8Array3TestMessage__rosidl_typesupport_introspection_c__Uint8Array3TestMessage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
