// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rclpy_message_converter_msgs:msg/NestedUint8ArrayTestMessage.idl
// generated code does not contain a copyright notice

#ifndef RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__NESTED_UINT8_ARRAY_TEST_MESSAGE__TRAITS_HPP_
#define RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__NESTED_UINT8_ARRAY_TEST_MESSAGE__TRAITS_HPP_

#include "rclpy_message_converter_msgs/msg/detail/nested_uint8_array_test_message__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>()
{
  return "rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage";
}

template<>
inline const char * name<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>()
{
  return "rclpy_message_converter_msgs/msg/NestedUint8ArrayTestMessage";
}

template<>
struct has_fixed_size<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__NESTED_UINT8_ARRAY_TEST_MESSAGE__TRAITS_HPP_
