# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_asbir_image_compression_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED asbir_image_compression_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(asbir_image_compression_FOUND FALSE)
  elseif(NOT asbir_image_compression_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(asbir_image_compression_FOUND FALSE)
  endif()
  return()
endif()
set(_asbir_image_compression_CONFIG_INCLUDED TRUE)

# output package information
if(NOT asbir_image_compression_FIND_QUIETLY)
  message(STATUS "Found asbir_image_compression: 0.0.0 (${asbir_image_compression_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'asbir_image_compression' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${asbir_image_compression_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(asbir_image_compression_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_dependencies-extras.cmake")
foreach(_extra ${_extras})
  include("${asbir_image_compression_DIR}/${_extra}")
endforeach()
