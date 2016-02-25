# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "moveit_simple_grasps: 8 messages, 0 services")

set(MSG_I_FLAGS "-Imoveit_simple_grasps:/home/cobra/cobra_ws/src/moveit_simple_grasps/msg;-Imoveit_simple_grasps:/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg;-Igeometry_msgs:/opt/ros/hydro/share/geometry_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/hydro/share/actionlib_msgs/cmake/../msg;-Istd_msgs:/opt/ros/hydro/share/std_msgs/cmake/../msg;-Imoveit_msgs:/opt/ros/hydro/share/moveit_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/hydro/share/sensor_msgs/cmake/../msg;-Itrajectory_msgs:/opt/ros/hydro/share/trajectory_msgs/cmake/../msg;-Ishape_msgs:/opt/ros/hydro/share/shape_msgs/cmake/../msg;-Iobject_recognition_msgs:/opt/ros/hydro/share/object_recognition_msgs/cmake/../msg;-Ioctomap_msgs:/opt/ros/hydro/share/octomap_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(moveit_simple_grasps_generate_messages ALL)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionResult.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionFeedback.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_cpp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
)

### Generating Services

### Generating Module File
_generate_module_cpp(moveit_simple_grasps
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(moveit_simple_grasps_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(moveit_simple_grasps_generate_messages moveit_simple_grasps_generate_messages_cpp)

# target for backward compatibility
add_custom_target(moveit_simple_grasps_gencpp)
add_dependencies(moveit_simple_grasps_gencpp moveit_simple_grasps_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_grasps_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionResult.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionFeedback.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_lisp(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
)

### Generating Services

### Generating Module File
_generate_module_lisp(moveit_simple_grasps
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(moveit_simple_grasps_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(moveit_simple_grasps_generate_messages moveit_simple_grasps_generate_messages_lisp)

# target for backward compatibility
add_custom_target(moveit_simple_grasps_genlisp)
add_dependencies(moveit_simple_grasps_genlisp moveit_simple_grasps_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_grasps_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionResult.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionFeedback.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/hydro/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/Grasp.msg;/opt/ros/hydro/share/std_msgs/cmake/../msg/Header.msg;/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsResult.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectory.msg;/opt/ros/hydro/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/hydro/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Vector3Stamped.msg;/opt/ros/hydro/share/moveit_msgs/cmake/../msg/GripperTranslation.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)
_generate_msg_py(moveit_simple_grasps
  "/home/cobra/cobra_ws/devel/share/moveit_simple_grasps/msg/GenerateGraspsGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/cobra/cobra_ws/src/moveit_simple_grasps/msg/GraspGeneratorOptions.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/hydro/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
)

### Generating Services

### Generating Module File
_generate_module_py(moveit_simple_grasps
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(moveit_simple_grasps_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(moveit_simple_grasps_generate_messages moveit_simple_grasps_generate_messages_py)

# target for backward compatibility
add_custom_target(moveit_simple_grasps_genpy)
add_dependencies(moveit_simple_grasps_genpy moveit_simple_grasps_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_grasps_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_grasps
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(moveit_simple_grasps_generate_messages_cpp geometry_msgs_generate_messages_cpp)
add_dependencies(moveit_simple_grasps_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
add_dependencies(moveit_simple_grasps_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(moveit_simple_grasps_generate_messages_cpp moveit_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_grasps
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(moveit_simple_grasps_generate_messages_lisp geometry_msgs_generate_messages_lisp)
add_dependencies(moveit_simple_grasps_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
add_dependencies(moveit_simple_grasps_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(moveit_simple_grasps_generate_messages_lisp moveit_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_grasps
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(moveit_simple_grasps_generate_messages_py geometry_msgs_generate_messages_py)
add_dependencies(moveit_simple_grasps_generate_messages_py actionlib_msgs_generate_messages_py)
add_dependencies(moveit_simple_grasps_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(moveit_simple_grasps_generate_messages_py moveit_msgs_generate_messages_py)
