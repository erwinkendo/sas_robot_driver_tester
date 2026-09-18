import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    config_file = LaunchConfiguration('config_file')
    ur_example_name = LaunchConfiguration('ur_example_name')

    ur_example_name_arg = DeclareLaunchArgument(
        'ur_example_name',
        default_value='ur3e',
        description='Name of the UR example'
    )

    real_robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('sas_robot_driver_ur'), 'launch'),
            '/robot_launch.py']),
        launch_arguments=[
            ('name', ur_example_name),
            ('config_file', config_file),
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'config_file',
            default_value=os.path.join(get_package_share_directory('sas_ur_control_template'), 'config', 'config.yaml')
        ),
        ur_example_name_arg,
        real_robot_launch,
        Node(
            package='sas_ur_control_template',
            executable='joint_interface_example.py',
            output='screen',
            emulate_tty=True,
            name='sas_ur_control_template_joint_interface_example_py',
            parameters=[config_file]
        )
    ])
