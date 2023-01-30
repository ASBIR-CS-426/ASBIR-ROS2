// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from rclpy_message_converter_msgs:msg/TestArray.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "rclpy_message_converter_msgs/msg/detail/test_array__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace rclpy_message_converter_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TestArray_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) rclpy_message_converter_msgs::msg::TestArray(_init);
}

void TestArray_fini_function(void * message_memory)
{
  auto typed_message = static_cast<rclpy_message_converter_msgs::msg::TestArray *>(message_memory);
  typed_message->~TestArray();
}

size_t size_function__TestArray__data(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TestArray__data(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__TestArray__data(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void resize_function__TestArray__data(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TestArray_message_member_array[1] = {
  {
    "data",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rclpy_message_converter_msgs::msg::TestArray, data),  // bytes offset in struct
    nullptr,  // default value
    size_function__TestArray__data,  // size() function pointer
    get_const_function__TestArray__data,  // get_const(index) function pointer
    get_function__TestArray__data,  // get(index) function pointer
    resize_function__TestArray__data  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TestArray_message_members = {
  "rclpy_message_converter_msgs::msg",  // message namespace
  "TestArray",  // message name
  1,  // number of fields
  sizeof(rclpy_message_converter_msgs::msg::TestArray),
  TestArray_message_member_array,  // message members
  TestArray_init_function,  // function to initialize message memory (memory has to be allocated)
  TestArray_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TestArray_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TestArray_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace rclpy_message_converter_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<rclpy_message_converter_msgs::msg::TestArray>()
{
  return &::rclpy_message_converter_msgs::msg::rosidl_typesupport_introspection_cpp::TestArray_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, rclpy_message_converter_msgs, msg, TestArray)() {
  return &::rclpy_message_converter_msgs::msg::rosidl_typesupport_introspection_cpp::TestArray_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif