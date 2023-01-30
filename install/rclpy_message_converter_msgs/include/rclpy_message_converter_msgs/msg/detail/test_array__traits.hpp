// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rclpy_message_converter_msgs:msg/TestArray.idl
// generated code does not contain a copyright notice

#ifndef RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__TEST_ARRAY__TRAITS_HPP_
#define RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__TEST_ARRAY__TRAITS_HPP_

#include "rclpy_message_converter_msgs/msg/detail/test_array__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rclpy_message_converter_msgs::msg::TestArray>()
{
  return "rclpy_message_converter_msgs::msg::TestArray";
}

template<>
inline const char * name<rclpy_message_converter_msgs::msg::TestArray>()
{
  return "rclpy_message_converter_msgs/msg/TestArray";
}

template<>
struct has_fixed_size<rclpy_message_converter_msgs::msg::TestArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<rclpy_message_converter_msgs::msg::TestArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<rclpy_message_converter_msgs::msg::TestArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // RCLPY_MESSAGE_CONVERTER_MSGS__MSG__DETAIL__TEST_ARRAY__TRAITS_HPP_
