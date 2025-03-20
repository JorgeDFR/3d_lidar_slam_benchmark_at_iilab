# Install GTSAM on Ubuntu

This guide provides step-by-step instructions to install GTSAM from source (version 4.2a9) on Ubuntu 22.04.

- **Official Documentation**: [GTSAM Github Repository](https://github.com/borglab/gtsam)
- **Tested OS**: [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy)
- **Last Updated**: November 22, 2024
- **Required by**: GLIM

## Installation Steps

### Step 1: Install Dependencies

Begin by installing the necessary dependencies using the following commands:

```sh
# Install CMake
sudo apt install cmake 

# Install Boost
sudo apt install libboost-all-dev
```

### Step 2: Install GTSAM (version 4.2a9)

Now download and install the GTSAM using the following commands:

```sh
# Clone the repository
git clone https://github.com/borglab/gtsam

# Move into the repository directory and checkout the 4.2a9 version
cd gtsam && git checkout 4.2a9

# Create and navigate to the build directory
mkdir -p build && cd build

# Configure the build with recommended settings
cmake .. -DGTSAM_BUILD_EXAMPLES_ALWAYS=OFF \
         -DGTSAM_BUILD_TESTS=OFF \
         -DGTSAM_WITH_TBB=OFF \
         -DGTSAM_USE_SYSTEM_EIGEN=ON \
         -DGTSAM_BUILD_WITH_MARCH_NATIVE=OFF

# Compile the source code
make -j4

# Install the compiled libraries
sudo make install
```