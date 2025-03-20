# Install Ceres Solver on Ubuntu

This guide provides step-by-step instructions to install Ceres Solver (version 2.2.0) on Ubuntu 20.04.

- **Official Documentation**: [Ceres Solver Installation](http://ceres-solver.org/installation.html)
- **Tested OS**: [Ubuntu 20.04.6 LTS](https://releases.ubuntu.com/focal)
- **Last Updated**: November 22, 2024
- **Required by**: A-LOAM

## Installation Steps

### Step 1: Install Dependencies

Begin by installing the necessary dependencies using the following commands:

```sh
# Install CMake
sudo apt install cmake

# Install Google glog and gflags
sudo apt install libgoogle-glog-dev libgflags-dev

# Install ATLAS (for BLAS & LAPACK support)
sudo apt install libatlas-base-dev

# Install Eigen3
sudo apt install libeigen3-dev

# Install SuiteSparse (optional, but recommended for improved performance)
sudo apt install libsuitesparse-dev
```

### Step 2: Install Ceres Solver (version 2.2.0)

Now download and install the ceres solver using the following commands:

```sh
# Download last ceres solver version (2.2.0)
wget http://ceres-solver.org/ceres-solver-2.2.0.tar.gz

# Extract zip file
tar zxf ceres-solver-2.2.0.tar.gz

# Rename folder
mv ceres-solver-2.2.0 ceres-solver

# Create and navigate to the build directory
mkdir -p ceres-solver/build && cd ceres-solver/build

# Configure the build
cmake ..

# Compile the source code
make -j4

# Run tests (optional)
make test

# Install the compiled libraries
sudo make install
```