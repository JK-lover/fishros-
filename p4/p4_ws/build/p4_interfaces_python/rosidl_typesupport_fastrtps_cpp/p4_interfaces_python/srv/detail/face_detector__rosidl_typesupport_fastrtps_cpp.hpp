// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from p4_interfaces_python:srv/FaceDetector.idl
// generated code does not contain a copyright notice

#ifndef P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "p4_interfaces_python/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "p4_interfaces_python/srv/detail/face_detector__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace p4_interfaces_python
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
cdr_serialize(
  const p4_interfaces_python::srv::FaceDetector_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  p4_interfaces_python::srv::FaceDetector_Request & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
get_serialized_size(
  const p4_interfaces_python::srv::FaceDetector_Request & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
max_serialized_size_FaceDetector_Request(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace p4_interfaces_python

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, p4_interfaces_python, srv, FaceDetector_Request)();

#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "p4_interfaces_python/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
// already included above
// #include "p4_interfaces_python/srv/detail/face_detector__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// already included above
// #include "fastcdr/Cdr.h"

namespace p4_interfaces_python
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
cdr_serialize(
  const p4_interfaces_python::srv::FaceDetector_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  p4_interfaces_python::srv::FaceDetector_Response & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
get_serialized_size(
  const p4_interfaces_python::srv::FaceDetector_Response & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
max_serialized_size_FaceDetector_Response(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace p4_interfaces_python

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, p4_interfaces_python, srv, FaceDetector_Response)();

#ifdef __cplusplus
}
#endif

#include "rmw/types.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "p4_interfaces_python/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_p4_interfaces_python
const rosidl_service_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, p4_interfaces_python, srv, FaceDetector)();

#ifdef __cplusplus
}
#endif

#endif  // P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
