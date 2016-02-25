
(cl:in-package :asdf)

(defsystem "moveit_simple_grasps-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :moveit_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "GraspGeneratorOptions" :depends-on ("_package_GraspGeneratorOptions"))
    (:file "_package_GraspGeneratorOptions" :depends-on ("_package"))
    (:file "GenerateGraspsActionGoal" :depends-on ("_package_GenerateGraspsActionGoal"))
    (:file "_package_GenerateGraspsActionGoal" :depends-on ("_package"))
    (:file "GenerateGraspsFeedback" :depends-on ("_package_GenerateGraspsFeedback"))
    (:file "_package_GenerateGraspsFeedback" :depends-on ("_package"))
    (:file "GenerateGraspsResult" :depends-on ("_package_GenerateGraspsResult"))
    (:file "_package_GenerateGraspsResult" :depends-on ("_package"))
    (:file "GenerateGraspsAction" :depends-on ("_package_GenerateGraspsAction"))
    (:file "_package_GenerateGraspsAction" :depends-on ("_package"))
    (:file "GenerateGraspsGoal" :depends-on ("_package_GenerateGraspsGoal"))
    (:file "_package_GenerateGraspsGoal" :depends-on ("_package"))
    (:file "GenerateGraspsActionResult" :depends-on ("_package_GenerateGraspsActionResult"))
    (:file "_package_GenerateGraspsActionResult" :depends-on ("_package"))
    (:file "GenerateGraspsActionFeedback" :depends-on ("_package_GenerateGraspsActionFeedback"))
    (:file "_package_GenerateGraspsActionFeedback" :depends-on ("_package"))
  ))