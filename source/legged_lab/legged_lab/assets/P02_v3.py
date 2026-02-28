"""Configuration for P02_v3 robot."""

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils import configclass

from legged_lab.assets import ISAAC_ASSET_DIR     #Purpose:specify an absolute path


@configclass
class P02v3ArticulationCfg(ArticulationCfg):
    """Configuration for P02_v3 articulations."""

    joint_sdk_names: list[str] = None
    soft_joint_pos_limit_factor = 0.9  #软限位


@configclass
class P02v3UsdFileCfg(sim_utils.UsdFileCfg):
    #force_usd_conversion: bool = True            #开启USD转换,不用开启，直接用的是简化碰撞模型的.usd，如果直接用的是.urdf文件才需要
    activate_contact_sensors: bool = True
    rigid_props = sim_utils.RigidBodyPropertiesCfg(
        disable_gravity=False,
        retain_accelerations=False,
        linear_damping=0.0,
        angular_damping=0.0,
        max_linear_velocity=1000.0,
        max_angular_velocity=1000.0,
        max_depenetration_velocity=1.0,
    )
    articulation_props = sim_utils.ArticulationRootPropertiesCfg(
        enabled_self_collisions=True, #待修改
        solver_position_iteration_count=8, 
        solver_velocity_iteration_count=4
    )
    """ delete all following URDF conversion parameters """
    # fix_base: bool = False
    # merge_fixed_joints: bool = False
    make_instanceable: bool = False
    # self_collision: bool = True
    # joint_drive = sim_utils.UrdfConverterCfg.JointDriveCfg(
    # gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=None, damping=None)
    # )

GP2_V3_CFG = P02v3ArticulationCfg(
    spawn=P02v3UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/gp2_v3/data/Robots/P02_v3/gp2_v3_simple_collision.usd",
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.73),
        joint_pos={
            "left_hip_pitch_joint": 0.0,
            "left_hip_roll_joint": 0.0,
            "left_hip_yaw_joint": 0.0,
            "left_knee_joint": 0.0,
            "left_ankle_pitch_joint": 0.0,
            "left_ankle_roll_joint": 0.0,
            "right_hip_pitch_joint": 0.0,
            "right_hip_roll_joint": 0.0,
            "right_hip_yaw_joint": 0.0,
            "right_knee_joint": 0.0,
            "right_ankle_pitch_joint": 0.0,
            "right_ankle_roll_joint": 0.0,
            "waist_yaw_joint": 0.0,
            "left_shoulder_pitch_joint": 0.0,
            "left_shoulder_roll_joint": 0.1,
            "left_shoulder_yaw_joint": 0.0,
            "left_elbow_joint": 1.43,
            "right_shoulder_pitch_joint": 0.0,
            "right_shoulder_roll_joint": -0.1,
            "right_shoulder_yaw_joint": 0.0,
            "right_elbow_joint": 1.43,
        },
        joint_vel={".*": 0.0},
    ),
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                "(left|right)_hip_pitch_joint",
                "(left|right)_hip_roll_joint",
                "(left|right)_hip_yaw_joint",
                "(left|right)_knee_joint",
            ],
            effort_limit_sim={
                "(left|right)_hip_pitch_joint": 88,
                "(left|right)_hip_roll_joint": 88,
                "(left|right)_hip_yaw_joint": 88,
                "(left|right)_knee_joint": 139,
            },
            velocity_limit_sim={
                "(left|right)_hip_pitch_joint": 32,
                "(left|right)_hip_roll_joint": 32,
                "(left|right)_hip_yaw_joint": 32,
                "(left|right)_knee_joint": 20,
            },
            stiffness={
                "(left|right)_hip_roll_joint": 100,
                "(left|right)_hip_pitch_joint": 150,
                "(left|right)_hip_yaw_joint": 100,
                "(left|right)_knee_joint": 180,
            },
            damping={
                "(left|right)_hip_pitch_joint": 5,
                "(left|right)_hip_roll_joint": 4,
                "(left|right)_hip_yaw_joint": 4,
                "(left|right)_knee_joint": 10,
            },
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[
                "(left|right)_ankle_pitch_joint",
                "(left|right)_ankle_roll_joint",
            ],
            effort_limit_sim={
                "(left|right)_ankle_pitch_joint": 50,
                "(left|right)_ankle_roll_joint": 50,
            },
            velocity_limit_sim={
                "(left|right)_ankle_pitch_joint": 37,
                "(left|right)_ankle_roll_joint": 37,
            },
            stiffness={
                "(left|right)_ankle_pitch_joint": 80,
                "(left|right)_ankle_roll_joint": 40,
            },
            damping={
                "(left|right)_ankle_pitch_joint": 8,
                "(left|right)_ankle_roll_joint": 4,
            },
        ),
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[
                "(left|right)_shoulder_pitch_joint",
                "(left|right)_shoulder_roll_joint",
                "(left|right)_shoulder_yaw_joint",
                "(left|right)_elbow_joint",
            ],
            effort_limit_sim={
                "(left|right)_shoulder_pitch_joint": 25,
                "(left|right)_shoulder_roll_joint": 25,
                "(left|right)_shoulder_yaw_joint": 25,
                "(left|right)_elbow_joint": 25,
            },
            velocity_limit_sim={
                "(left|right)_shoulder_pitch_joint": 37,
                "(left|right)_shoulder_roll_joint": 37,
                "(left|right)_shoulder_yaw_joint": 37,
                "(left|right)_elbow_joint": 37,
            },
            stiffness={
                "(left|right)_shoulder_pitch_joint": 30,
                "(left|right)_shoulder_roll_joint": 20,
                "(left|right)_shoulder_yaw_joint": 20,
                "(left|right)_elbow_joint": 30,
            },
            damping={
                "(left|right)_shoulder_pitch_joint": 4,
                "(left|right)_shoulder_roll_joint": 4,
                "(left|right)_shoulder_yaw_joint": 4,
                "(left|right)_elbow_joint": 4,
            },
        ),
        "waist": ImplicitActuatorCfg(
            joint_names_expr=["waist_yaw_joint"],
            effort_limit_sim={"waist_yaw_joint": 50},
            velocity_limit_sim={"waist_yaw_joint": 20},
            stiffness={"waist_yaw_joint": 150},
            damping={"waist_yaw_joint": 6},
        ),
    },
    joint_sdk_names=[
        "left_hip_pitch_joint",
        "left_hip_roll_joint",
        "left_hip_yaw_joint",
        "left_knee_joint",
        "left_ankle_pitch_joint",
        "left_ankle_roll_joint",
        "right_hip_pitch_joint",
        "right_hip_roll_joint",
        "right_hip_yaw_joint",
        "right_knee_joint",
        "right_ankle_pitch_joint",
        "right_ankle_roll_joint",
        "waist_yaw_joint",
        "left_shoulder_pitch_joint",
        "left_shoulder_roll_joint",
        "left_shoulder_yaw_joint",
        "left_elbow_joint",
        "right_shoulder_pitch_joint",
        "right_shoulder_roll_joint",
        "right_shoulder_yaw_joint",
        "right_elbow_joint",
    ],
)