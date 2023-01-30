// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rclpy_message_converter_msgs:msg/Uint8Array3TestMessage.idl
// generated code does not contain a copyright notice

#ifndef RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__UINT8_ARRAY3_TEST_MESSAGE__TRAITS_HPP_
#define RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__UINT8_ARRAY3_TEST_MESSAGE__TRAITS_HPP_

#include "rclpy_message_converter_msgs/msg/detail/uint8_array3_test_message__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rclpy_message_converter_msgs::msg::Uint8Array3TestMessage>()
{
  return "rclpy_message_converter_msgs::msg::Uint8Array3TestMessage";
}

template<>
inline const char * name<rclpy_message_converter_msgs::msg::Uint8Array3TestMessage>()
{
  return "rclpy_message_converter_msgs/msg/Uint8Array3TestMessage";
}

template<>
struct has_fixed_size<rclpy_message_converter_msgs::msg::Uint8Array3TestMessage>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<rclpy_message_converter_msgs::msg::Uint8Array3TestMessage>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<rclpy_message_converter_msgs::msg::Uint8Array3TestMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__UINT8_ARRAY3_TEST_MESSAGE__TRAITS_HPP_
