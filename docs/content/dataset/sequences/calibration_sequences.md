# Calibration Sequences

TBC

<!-- Calibration sequences are designed to help researchers test and calibrate their SLAM algorithms in controlled conditions.

## Purpose of Calibration Sequences

Calibration sequences serve several important purposes:

- :material-tune: **Algorithm Initialization**: Initialize and test algorithms in simple, controlled environments
- :material-tune-variant: **Parameter Tuning**: Standardized data for tuning algorithm parameters
- :material-radar: **Sensor Evaluation**: Evaluate different sensor characteristics and their impact
- :material-file-compare: **Reference Data**: Compare algorithm behavior across different sensors and configurations

## Available Calibration Sequences

The IILABS 3D dataset includes the following calibration sequences:

### Straight Line

![Straight Line Sequence](../../assets/images/sequences/straight_line.jpg){ loading=lazy }

**Description**: A simple straight-line trajectory where the robot moves forward for approximately 5 meters and then returns along the same path.

**Purpose**: This sequence is useful for testing basic odometry estimation and evaluating drift in the simplest case of linear motion.

**Duration**: Approximately 30 seconds

**Challenges**: Minimal - designed for basic algorithm testing

### Square

![Square Sequence](../../assets/images/sequences/square.jpg){ loading=lazy }

**Description**: The robot follows a square trajectory with 2-meter sides, returning to the starting position.

**Purpose**: This sequence tests the algorithm's ability to handle 90-degree turns and maintain consistent odometry through multiple direction changes.

**Duration**: Approximately 60 seconds

**Challenges**: Sharp turns, maintaining orientation accuracy

### Circle

![Circle Sequence](../../assets/images/sequences/circle.jpg){ loading=lazy }

**Description**: The robot follows a circular trajectory with a radius of approximately 1.5 meters, completing two full circles.

**Purpose**: This sequence tests the algorithm's ability to handle continuous curvature and maintain consistent odometry through gradual direction changes.

**Duration**: Approximately 45 seconds

**Challenges**: Continuous curvature, maintaining orientation during circular motion

### Figure Eight

![Figure Eight Sequence](../../assets/images/sequences/figure_eight.jpg){ loading=lazy }

**Description**: The robot follows a figure-eight trajectory, combining aspects of both circular and straight-line motion.

**Purpose**: This sequence tests the algorithm's ability to handle complex trajectories with varying curvature.

**Duration**: Approximately 60 seconds

**Challenges**: Varying curvature, crossing paths

### Static

![Static Sequence](../../assets/images/sequences/static.jpg){ loading=lazy }

**Description**: The robot remains stationary while sensors collect data.

**Purpose**: This sequence is useful for evaluating sensor noise characteristics and testing the algorithm's ability to maintain a stable position estimate when not moving.

**Duration**: Approximately 30 seconds

**Challenges**: Distinguishing between sensor noise and actual movement -->