// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from p4_interfaces_python:srv/FaceDetector.idl
// generated code does not contain a copyright notice

#ifndef P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__STRUCT_H_
#define P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.h"

// Struct defined in srv/FaceDetector in the package p4_interfaces_python.
typedef struct p4_interfaces_python__srv__FaceDetector_Request
{
  sensor_msgs__msg__Image image;
} p4_interfaces_python__srv__FaceDetector_Request;

// Struct for a sequence of p4_interfaces_python__srv__FaceDetector_Request.
typedef struct p4_interfaces_python__srv__FaceDetector_Request__Sequence
{
  p4_interfaces_python__srv__FaceDetector_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} p4_interfaces_python__srv__FaceDetector_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'top'
// Member 'right'
// Member 'bottom'
// Member 'left'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in srv/FaceDetector in the package p4_interfaces_python.
typedef struct p4_interfaces_python__srv__FaceDetector_Response
{
  int16_t number;
  float use_time;
  rosidl_runtime_c__int32__Sequence top;
  rosidl_runtime_c__int32__Sequence right;
  rosidl_runtime_c__int32__Sequence bottom;
  rosidl_runtime_c__int32__Sequence left;
} p4_interfaces_python__srv__FaceDetector_Response;

// Struct for a sequence of p4_interfaces_python__srv__FaceDetector_Response.
typedef struct p4_interfaces_python__srv__FaceDetector_Response__Sequence
{
  p4_interfaces_python__srv__FaceDetector_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} p4_interfaces_python__srv__FaceDetector_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // P4_INTERFACES_PYTHON__SRV__DETAIL__FACE_DETECTOR__STRUCT_H_
