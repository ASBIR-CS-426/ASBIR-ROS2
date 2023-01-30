// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rclpy_message_converter_msgs:srv/NestedUint8ArrayTestService.idl
// generated code does not contain a copyright notice

#ifndef RCLPY_MESSAGE_CONVERTER_MSGS__SRV__DETAIL__NESTED_UINT8_ARRAY_TEST_SERVICE__TRAITS_HPP_
#define RCLPY_MESSAGE_CONVERTER_MSGS__SRV__DETAIL__NESTED_UINT8_ARRAY_TEST_SERVICE__TRAITS_HPP_

#include "rclpy_message_converter_msgs/srv/detail/nested_uint8_array_test_service__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'input'
#include "rclpy_message_converter_msgs/msg/detail/nested_uint8_array_test_message__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>()
{
  return "rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request";
}

template<>
inline const char * name<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>()
{
  return "rclpy_message_converter_msgs/srv/NestedUint8ArrayTestService_Request";
}

template<>
struct has_fixed_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>
  : std::integral_constant<bool, has_fixed_size<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>::value> {};

template<>
struct has_bounded_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>
  : std::integral_constant<bool, has_bounded_size<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>::value> {};

template<>
struct is_message<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'output'
// already included above
// #include "rclpy_message_converter_msgs/msg/detail/nested_uint8_array_test_message__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>()
{
  return "rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response";
}

template<>
inline const char * name<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>()
{
  return "rclpy_message_converter_msgs/srv/NestedUint8ArrayTestService_Response";
}

template<>
struct has_fixed_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>
  : std::integral_constant<bool, has_fixed_size<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>::value> {};

template<>
struct has_bounded_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>
  : std::integral_constant<bool, has_bounded_size<rclpy_message_converter_msgs::msg::NestedUint8ArrayTestMessage>::value> {};

template<>
struct is_message<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService>()
{
  return "rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService";
}

template<>
inline const char * name<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService>()
{
  return "rclpy_message_converter_msgs/srv/NestedUint8ArrayTestService";
}

template<>
struct has_fixed_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService>
  : std::integral_constant<
    bool,
    has_fixed_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>::value &&
    has_fixed_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>::value
  >
{
};

template<>
struct has_bounded_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService>
  : std::integral_constant<
    bool,
    has_bounded_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>::value &&
    has_bounded_size<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>::value
  >
{
};

template<>
struct is_service<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService>
  : std::true_type
{
};

template<>
struct is_service_request<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Request>
  : std::true_type
{
};

template<>
struct is_service_response<rclpy_message_converter_msgs::srv::NestedUint8ArrayTestService_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // RCLPY_MESSAGE_CONVERTER_MSGS__SRV__DETAIL__NESTED_UINT8_ARRAY_TEST_SERVICE__TRAITS_HPP_
