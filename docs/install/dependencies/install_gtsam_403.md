# Install GTSAM on Ubuntu

This guide provides step-by-step instructions to install GTSAM from source (version 4.0.3) on Ubuntu 20.04.

- **Official Documentation**: [GTSAM Github Repository](https://github.com/borglab/gtsam)
- **Tested OS**: [Ubuntu 20.04.6 LTS](https://releases.ubuntu.com/focal/)
- **Last Updated**: November 22, 2024
- **Required by**: LeGO-LOAM, LIORF

## Installation Steps

### Step 1: Install Dependencies

Begin by installing the necessary dependencies using the following commands:

```sh
# Install CMake
sudo apt install cmake 

# Install Boost
sudo apt install libboost-all-dev
```

### Step 2: Install GTSAM (version 4.0.3)

Now download and install the GTSAM using the following commands:

```sh
# Add the GTSAM repository
sudo add-apt-repository ppa:borglab/gtsam-release-4.0

# Update package lists
sudo apt update

# Install GTSAM libraries
sudo apt install libgtsam-dev libgtsam-unstable-dev 
```