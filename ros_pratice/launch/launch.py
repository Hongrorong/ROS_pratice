import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

          Node(package='turtlesim',
               node_executable='turtlesim_node',
               node_name='turtlesim_node',
               output='screen'),

          Node(package='ros_pratice',
               node_executable='info_pub',
               node_name='info_pub',
               output='screen'),

          Node(package='ros_pratice',
               node_executable='info_sub',
               node_name='info_sub',
               output='screen'),
    ])
