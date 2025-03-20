# Install Livox-SDK on Ubuntu

This guide provides step-by-step instructions to install Livox-SDK from source (version 2.3.0) on Ubuntu 20.04.

- **Official Documentation**: [GTSAM Github Repository](https://github.com/Livox-SDK/Livox-SDK)
- **Tested OS**: [Ubuntu 20.04.6 LTS](https://releases.ubuntu.com/focal)
- **Last Updated**: November 22, 2024
- **Required by**: Fast-LIO

## Installation Steps

### Step 1: Install Dependencies

Begin by installing the necessary dependencies using the following command:

```sh
# Install CMake
sudo apt install cmake
```

### Step 2: Install Livox-SDK (version 2.3.0)

Now download and install the Livox-SDK using the following commands:

```sh
# Clone the repository
git clone https://github.com/Livox-SDK/Livox-SDK

# Create and navigate to the build directory
mkdir -p Livox-SDK/build && cd Livox-SDK/build

# Configure the build
cmake .. 

# Compile the source code
make -j4

# Install the compiled libraries
sudo make install
```