// generated from
// rosidl_typesupport_introspection_c/resource/rosidl_typesupport_introspection_c__visibility_control.h.in
// generated code does not contain a copyright notice

#ifndef P4_INTERFACES_PYTHON__MSG__ROSIDL_TYPESUPPORT_INTROSPECTION_C__VISIBILITY_CONTROL_H_
#define P4_INTERFACES_PYTHON__MSG__ROSIDL_TYPESUPPORT_INTROSPECTION_C__VISIBILITY_CONTROL_H_

#ifdef __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_p4_interfaces_python __attribute__ ((dllexport))
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_IMPORT_p4_interfaces_python __attribute__ ((dllimport))
  #else
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_p4_interfaces_python __declspec(dllexport)
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_IMPORT_p4_interfaces_python __declspec(dllimport)
  #endif
  #ifdef ROSIDL_TYPESUPPORT_INTROSPECTION_C_BUILDING_DLL_p4_interfaces_python
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_PUBLIC_p4_interfaces_python ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_p4_interfaces_python
  #else
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_PUBLIC_p4_interfaces_python ROSIDL_TYPESUPPORT_INTROSPECTION_C_IMPORT_p4_interfaces_python
  #endif
#else
  #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_p4_interfaces_python __attribute__ ((visibility("default")))
  #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_IMPORT_p4_interfaces_python
  #if __GNUC__ >= 4
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_PUBLIC_p4_interfaces_python __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_TYPESUPPORT_INTROSPECTION_C_PUBLIC_p4_interfaces_python
  #endif
#endif

#ifdef __cplusplus
}
#endif

#endif  // P4_INTERFACES_PYTHON__MSG__ROSIDL_TYPESUPPORT_INTROSPECTION_C__VISIBILITY_CONTROL_H_
