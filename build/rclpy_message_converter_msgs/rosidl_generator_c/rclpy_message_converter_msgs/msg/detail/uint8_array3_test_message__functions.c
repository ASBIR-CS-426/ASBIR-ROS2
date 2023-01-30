// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rclpy_message_converter_msgs:msg/Uint8Array3TestMessage.idl
// generated code does not contain a copyright notice
#include "rclpy_message_converter_msgs/msg/detail/uint8_array3_test_message__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__init(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * msg)
{
  if (!msg) {
    return false;
  }
  // data
  return true;
}

void
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__fini(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * msg)
{
  if (!msg) {
    return;
  }
  // data
}

bool
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__are_equal(const rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * lhs, const rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // data
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->data[i] != rhs->data[i]) {
      return false;
    }
  }
  return true;
}

bool
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__copy(
  const rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * input,
  rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // data
  for (size_t i = 0; i < 3; ++i) {
    output->data[i] = input->data[i];
  }
  return true;
}

rclpy_message_converter_msgs__msg__Uint8Array3TestMessage *
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * msg = (rclpy_message_converter_msgs__msg__Uint8Array3TestMessage *)allocator.allocate(sizeof(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage));
  bool success = rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__destroy(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__init(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * data = NULL;

  if (size) {
    data = (rclpy_message_converter_msgs__msg__Uint8Array3TestMessage *)allocator.zero_allocate(size, sizeof(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__fini(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence *
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * array = (rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence *)allocator.allocate(sizeof(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__destroy(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__are_equal(const rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * lhs, const rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence__copy(
  const rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * input,
  rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(rclpy_message_converter_msgs__msg__Uint8Array3TestMessage);
    rclpy_message_converter_msgs__msg__Uint8Array3TestMessage * data =
      (rclpy_message_converter_msgs__msg__Uint8Array3TestMessage *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!rclpy_message_converter_msgs__msg__Uint8Array3TestMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}