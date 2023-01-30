// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from rclpy_message_converter_msgs:msg/Uint8ArrayTestMessage.idl
// generated code does not contain a copyright notice
#include "rclpy_message_converter_msgs/msg/detail/uint8_array_test_message__rosidl_typesupport_fastrtps_cpp.hpp"
#include "rclpy_message_converter_msgs/msg/detail/uint8_array_test_message__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace rclpy_message_converter_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rclpy_message_converter_msgs
cdr_serialize(
  const rclpy_message_converter_msgs::msg::Uint8ArrayTestMessage & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: data
  {
    cdr << ros_message.data;
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rclpy_message_converter_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  rclpy_message_converter_msgs::msg::Uint8ArrayTestMessage & ros_message)
{
  // Member: data
  {
    cdr >> ros_message.data;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rclpy_message_converter_msgs
get_serialized_size(
  const rclpy_message_converter_msgs::msg::Uint8ArrayTestMessage & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: data
  {
    size_t array_size = ros_message.data.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.data[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rclpy_message_converter_msgs
max_serialized_size_Uint8ArrayTestMessage(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: data
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _Uint8ArrayTestMessage__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const rclpy_message_converter_msgs::msg::Uint8ArrayTestMessage *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Uint8ArrayTestMessage__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<rclpy_message_converter_msgs::msg::Uint8ArrayTestMessage *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Uint8ArrayTestMessage__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const rclpy_message_converter_msgs::msg::Uint8ArrayTestMessage *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Uint8ArrayTestMessage__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_Uint8ArrayTestMessage(full_bounded, 0);
}

static message_type_support_callbacks_t _Uint8ArrayTestMessage__callbacks = {
  "rclpy_message_converter_msgs::msg",
  "Uint8ArrayTestMessage",
  _Uint8ArrayTestMessage__cdr_serialize,
  _Uint8ArrayTestMessage__cdr_deserialize,
  _Uint8ArrayTestMessage__get_serialized_size,
  _Uint8ArrayTestMessage__max_serialized_size
};

static rosidl_message_type_support_t _Uint8ArrayTestMessage__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Uint8ArrayTestMessage__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace rclpy_message_converter_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_rclpy_message_converter_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<rclpy_message_converter_msgs::msg::Uint8ArrayTestMessage>()
{
  return &rclpy_message_converter_msgs::msg::typesupport_fastrtps_cpp::_Uint8ArrayTestMessage__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, rclpy_message_converter_msgs, msg, Uint8ArrayTestMessage)() {
  return &rclpy_message_converter_msgs::msg::typesupport_fastrtps_cpp::_Uint8ArrayTestMessage__handle;
}

#ifdef __cplusplus
}
#endif