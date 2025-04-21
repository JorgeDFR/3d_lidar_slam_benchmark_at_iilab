# Benchmark Sequences

TBC

<!-- Benchmark sequences are designed to evaluate the performance of SLAM algorithms in realistic indoor scenarios.

## Purpose of Benchmark Sequences

Benchmark sequences are designed to challenge SLAM algorithms with realistic indoor navigation scenarios. They serve several important purposes:

- :material-speedometer: **Performance Evaluation**: Evaluate algorithms in challenging real-world conditions
- :material-compare: **Algorithm Comparison**: Compare different algorithms under identical conditions
- :material-shield-check: **Robustness Testing**: Test algorithm resilience against various challenges
- :material-chart-line: **Research Advancement**: Identify strengths and weaknesses of current approaches

## Available Benchmark Sequences

The IILABS 3D dataset includes the following benchmark sequences:

### Nav A Diff

![Nav A Diff Sequence](../../../assets/dataset/sequences/bench_nav_a_diff_trajectory.png)

**Description**: A trajectory with differential drive navigation in area A of the iiLab.

**Purpose**: This sequence tests the algorithm's ability to handle standard navigation with differential drive kinematics.

**Duration**: Approximately 3 minutes

**Challenges**: Basic navigation, maintaining accurate odometry

### Nav A Omni

![Nav A Omni Sequence](../../../assets/dataset/sequences/bench_nav_a_omni_trajectory.png)

**Description**: A trajectory with omnidirectional movement in area A of the iiLab.

**Purpose**: This sequence tests the algorithm's ability to handle complex movement patterns including sideways and rotational motion.

**Duration**: Approximately 3 minutes

**Challenges**: Omnidirectional movement, maintaining orientation during complex maneuvers

### Loop

![Loop Sequence](../../../assets/dataset/sequences/bench_loop_trajectory.png)

**Description**: A trajectory that includes a large loop around the main area of the iiLab, returning to the starting position.

**Purpose**: This sequence tests the algorithm's loop closure capabilities and global consistency.

**Duration**: Approximately 3 minutes

**Challenges**: Loop closure, maintaining global consistency

### Slippage

![Slippage Sequence](../../../assets/dataset/sequences/bench_slippage_trajectory.png)

**Description**: A trajectory that includes areas with slippery surfaces causing wheel slippage.

**Purpose**: This sequence tests the algorithm's robustness to odometry errors caused by wheel slippage.

**Duration**: Approximately 2 minutes

**Challenges**: Wheel slippage, odometry errors, maintaining accurate pose estimation

### Ramp

<div class="grid" markdown>

![](../../../assets/dataset/sequences/bench_ramp_photo_1.png)

![](../../../assets/dataset/sequences/bench_ramp_photo_2.png)

</div>

**Description**: A trajectory that includes navigating up and down a ramp.

**Purpose**: This sequence tests the algorithm's ability to handle elevation changes and maintain accurate pose estimation during inclines and declines.

**Duration**: Approximately 2 minutes

**Challenges**: Elevation changes, maintaining accurate pose during inclines

### Elevator

<div class="grid" markdown>

![](../../../assets/dataset/sequences/bench_elevator_nn0_trajectory.png)

![](../../../assets/dataset/sequences/bench_elevator_nn1_trajectory.png)

![](../../../assets/dataset/sequences/bench_elevator_photo.png)

</div>

**Description**: A trajectory that includes entering and exiting an elevator, with a period of time inside the closed elevator.

**Purpose**: This sequence tests the algorithm's robustness to sudden changes in the environment and ability to recover from temporary loss of features.

**Duration**: Approximately 4 minutes

**Challenges**: Sudden environment changes, feature loss, recovery, vertical motion -->