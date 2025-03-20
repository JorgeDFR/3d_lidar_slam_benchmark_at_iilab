# Install GTSAM-points on Ubuntu

This guide provides step-by-step instructions to install GTSAM-points from source on Ubuntu 22.04.

- **Official Documentation**: [GTSAM Github Repository](https://github.com/koide3/gtsam_points)
- **Tested OS**: [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy)
- **Last Updated**: November 22, 2024
- **Required by**: GLIM

## Installation Steps

### Step 1: Install Dependencies

Begin by installing the necessary dependencies using the following commands:

```sh
# Install CMake
sudo apt install cmake 

# Install Eigen
sudo apt install libeigen3-dev

# Install nanoflann
sudo apt install libnanoflann-dev

# Install TBB
sudo apt install libtbb-dev
```

Additionally, ensure you have the following components:

- [**GTSAM**](/doc/install/dependencies/install_gtsam.md)
- [**OpenMP**](https://www.openmp.org) (Optional)
- [**CUDA**](https://developer.nvidia.com/cuda-toolkit) (Optional)
- [**Iridescence**](/doc/install/dependencies/install_iridescence.md) (Optional)

### Step 2: Install gtsam_points

Now download and install the gtsam_points using the following commands:

```sh
# Clone the repository
git clone https://github.com/koide3/gtsam_points

# Create and navigate to the build directory
mkdir -p gtsam_points/build && cd gtsam_points/build

# Configure the build
cmake .. -DCMAKE_BUILD_TYPE=Release

# Optional cmake arguments
# cmake .. \
#   -DBUILD_DEMO=OFF \
#   -DBUILD_TESTS=OFF \
#   -DBUILD_WITH_CUDA=OFF \
#   -DBUILD_WITH_MARCH_NATIVE=OFF

# Compile the source code
make -j4

# Install the compiled libraries
sudo make install
```