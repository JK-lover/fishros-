// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from p4_interfaces_python:srv/FaceDetector.idl
// generated code does not contain a copyright notice

#ifndef P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__TRAITS_HPP_
#define P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__TRAITS_HPP_

#include "p4_interfaces_python/srv/detail/face_detector__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'image'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<p4_interfaces_python::srv::FaceDetector_Request>()
{
  return "p4_interfaces_python::srv::FaceDetector_Request";
}

template<>
inline const char * name<p4_interfaces_python::srv::FaceDetector_Request>()
{
  return "p4_interfaces_python/srv/FaceDetector_Request";
}

template<>
struct has_fixed_size<p4_interfaces_python::srv::FaceDetector_Request>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::Image>::value> {};

template<>
struct has_bounded_size<p4_interfaces_python::srv::FaceDetector_Request>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::Image>::value> {};

template<>
struct is_message<p4_interfaces_python::srv::FaceDetector_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<p4_interfaces_python::srv::FaceDetector_Response>()
{
  return "p4_interfaces_python::srv::FaceDetector_Response";
}

template<>
inline const char * name<p4_interfaces_python::srv::FaceDetector_Response>()
{
  return "p4_interfaces_python/srv/FaceDetector_Response";
}

template<>
struct has_fixed_size<p4_interfaces_python::srv::FaceDetector_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<p4_interfaces_python::srv::FaceDetector_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<p4_interfaces_python::srv::FaceDetector_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<p4_interfaces_python::srv::FaceDetector>()
{
  return "p4_interfaces_python::srv::FaceDetector";
}

template<>
inline const char * name<p4_interfaces_python::srv::FaceDetector>()
{
  return "p4_interfaces_python/srv/FaceDetector";
}

template<>
struct has_fixed_size<p4_interfaces_python::srv::FaceDetector>
  : std::integral_constant<
    bool,
    has_fixed_size<p4_interfaces_python::srv::FaceDetector_Request>::value &&
    has_fixed_size<p4_interfaces_python::srv::FaceDetector_Response>::value
  >
{
};

template<>
struct has_bounded_size<p4_interfaces_python::srv::FaceDetector>
  : std::integral_constant<
    bool,
    has_bounded_size<p4_interfaces_python::srv::FaceDetector_Request>::value &&
    has_bounded_size<p4_interfaces_python::srv::FaceDetector_Response>::value
  >
{
};

template<>
struct is_service<p4_interfaces_python::srv::FaceDetector>
  : std::true_type
{
};

template<>
struct is_service_request<p4_interfaces_python::srv::FaceDetector_Request>
  : std::true_type
{
};

template<>
struct is_service_response<p4_interfaces_python::srv::FaceDetector_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__TRAITS_HPP_
