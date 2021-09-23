import typing

import FreeCAD
import Robot


# WaypointPy.xml
class Waypoint(FreeCAD.Persistence):
    """
    This class can be imported.
    Waypoint class
    """

    def __init__(self, Pos: FreeCAD.Placement, type: str = None, name: str = None, vel: object = None, cont: int = None, tool: int = None, base: int = None, acc: object = None):
        """Waypoint class"""

    @property
    def Base(self) -> int:
        """Describe which Base frame to use for that point"""

    @Base.setter
    def Base(self, value: int): ...

    @property
    def Cont(self) -> bool:
        """Control the continuity to the next waypoint in the trajectory"""

    @Cont.setter
    def Cont(self, value: bool): ...

    @property
    def Name(self) -> str:
        """Name of the waypoint"""

    @Name.setter
    def Name(self, value: str): ...

    @property
    def Pos(self) -> object:
        """End position (destination) of the waypoint"""

    @Pos.setter
    def Pos(self, value: object): ...

    @property
    def Tool(self) -> int:
        """Describe which tool frame to use for that point"""

    @Tool.setter
    def Tool(self, value: int): ...

    @property
    def Type(self) -> str:
        """Type of the waypoint[PTP|LIN|CIRC|WAIT]"""

    @Type.setter
    def Type(self, value: str): ...

    @property
    def Velocity(self) -> float:
        """
        Control the velocity to the next waypoint in the trajectory
        In Case of PTP 0-100% Axis speed
        In Case of LIN m/s
        In Case of WAIT s wait time
        """

    @Velocity.setter
    def Velocity(self, value: float): ...


# Robot6AxisPy.xml
class Robot6Axis(FreeCAD.Persistence):
    """
    This class can be imported.
    Robot6Axis class
    """

    @property
    def Axis1(self) -> float:
        """Pose of Axis 1 in degrees"""

    @Axis1.setter
    def Axis1(self, value: float): ...

    @property
    def Axis2(self) -> float:
        """Pose of Axis 2 in degrees"""

    @Axis2.setter
    def Axis2(self, value: float): ...

    @property
    def Axis3(self) -> float:
        """Pose of Axis 3 in degrees"""

    @Axis3.setter
    def Axis3(self, value: float): ...

    @property
    def Axis4(self) -> float:
        """Pose of Axis 4 in degrees"""

    @Axis4.setter
    def Axis4(self, value: float): ...

    @property
    def Axis5(self) -> float:
        """Pose of Axis 5 in degrees"""

    @Axis5.setter
    def Axis5(self, value: float): ...

    @property
    def Axis6(self) -> float:
        """Pose of Axis 6 in degrees"""

    @Axis6.setter
    def Axis6(self, value: float): ...

    @property
    def Base(self) -> object:
        """Actual Base system in respect to the robot world system"""

    @Base.setter
    def Base(self, value: object): ...

    @property
    def Tcp(self) -> object:
        """Tool center point frame. Where the tool of the robot is"""

    @Tcp.setter
    def Tcp(self, value: object): ...


# TrajectoryPy.xml
class Trajectory(FreeCAD.Persistence):
    """
    This class can be imported.
    Trajectory class
    """

    def __init__(self, arg1: list = None, /):
        """Trajectory class"""

    @property
    def Duration(self) -> float:
        """duration of the trajectory"""

    @property
    def Length(self) -> float:
        """length of the trajectory"""

    @property
    def Waypoints(self) -> list:
        """waypoints of this trajectory"""

    @Waypoints.setter
    def Waypoints(self, value: list): ...

    def deleteLast(self, n: int = None, /):
        """
        deleteLast(n) - delete n waypoints at the end
                  deleteLast()  - delete the last waypoint
        """

    @typing.overload
    def insertWaypoints(self, arg1: FreeCAD.Placement, /): ...

    @typing.overload
    def insertWaypoints(self, arg1: Robot.Waypoint, /): ...

    @typing.overload
    def insertWaypoints(self, arg1: list, /):
        """adds one or a list of waypoint to the end of the trajectory"""

    def position(self, arg1: float, /):
        """returns a Frame to a given time in the trajectory"""

    def velocity(self, arg1: float, /):
        """returns the velocity to a given time in the trajectory"""


# RobotObjectPy.xml
class RobotObject(FreeCAD.DocumentObject):
    """Robot document object"""

    @property
    def Axis1(self):
        """
        Property group: Robot kinematic.
        Axis 1 angle of the robot in degre.
        """

    @Axis1.setter
    def Axis1(self, value): ...

    @property
    def Axis2(self):
        """
        Property group: Robot kinematic.
        Axis 2 angle of the robot in degre.
        """

    @Axis2.setter
    def Axis2(self, value): ...

    @property
    def Axis3(self):
        """
        Property group: Robot kinematic.
        Axis 3 angle of the robot in degre.
        """

    @Axis3.setter
    def Axis3(self, value): ...

    @property
    def Axis4(self):
        """
        Property group: Robot kinematic.
        Axis 4 angle of the robot in degre.
        """

    @Axis4.setter
    def Axis4(self, value): ...

    @property
    def Axis5(self):
        """
        Property group: Robot kinematic.
        Axis 5 angle of the robot in degre.
        """

    @Axis5.setter
    def Axis5(self, value): ...

    @property
    def Axis6(self):
        """
        Property group: Robot kinematic.
        Axis 6 angle of the robot in degre.
        """

    @Axis6.setter
    def Axis6(self, value): ...

    @property
    def Base(self):
        """
        Property group: Robot kinematic.
        Property TypeId: App::PropertyPlacement.
        Actual base frame of the robot.
        """

    @Base.setter
    def Base(self, value): ...

    @property
    def Error(self) -> str:
        """
        Property group: Robot kinematic.
        Property TypeId: App::PropertyString.
        Robot error while moving.
        """

    @Error.setter
    def Error(self, value: str): ...

    @property
    def Home(self) -> dict[int, float | int] | typing.Iterable[float | int] | typing.Sequence[float | int]:
        """
        Property group: Robot kinematic.
        Property TypeId: App::PropertyFloatList.
        Axis position for home.
        """

    @Home.setter
    def Home(self, value: dict[int, float | int] | typing.Iterable[float | int] | typing.Sequence[float | int]): ...

    @property
    def RobotKinematicFile(self):
        """
        Property group: Robot definition.
        Property TypeId: App::PropertyFileIncluded.
        Included file with kinematic definition of the robot Axis.
        """

    @RobotKinematicFile.setter
    def RobotKinematicFile(self, value): ...

    @property
    def RobotVrmlFile(self):
        """
        Property group: Robot definition.
        Property TypeId: App::PropertyFileIncluded.
        Included file with the VRML representation of the robot.
        """

    @RobotVrmlFile.setter
    def RobotVrmlFile(self, value): ...

    @property
    def Tcp(self):
        """
        Property group: Robot kinematic.
        Property TypeId: App::PropertyPlacement.
        Tcp of the robot.
        """

    @Tcp.setter
    def Tcp(self, value): ...

    @property
    def Tool(self):
        """
        Property group: Robot kinematic.
        Property TypeId: App::PropertyPlacement.
        Tool frame of the robot (Tool).
        """

    @Tool.setter
    def Tool(self, value): ...

    @property
    def ToolBase(self):
        """
        Property group: Robot definition.
        Property TypeId: App::PropertyPlacement.
        Defines where to connect the ToolShape.
        """

    @ToolBase.setter
    def ToolBase(self, value): ...

    @property
    def ToolShape(self) -> FreeCAD.DocumentObject | None:
        """
        Property group: Robot definition.
        Property TypeId: App::PropertyLink.
        Link to the Shape is used as Tool.
        """

    @ToolShape.setter
    def ToolShape(self, value: FreeCAD.DocumentObject | None): ...


# AppRobot.cpp
def simulateToFile(Robot: Robot.Robot6Axis, Trajectory: Robot.Trajectory, TickSize: float, FileName: str, /):
    """simulateToFile(Robot,Trajectory,TickSize,FileName) - runs the simulation and write the result to a file."""
