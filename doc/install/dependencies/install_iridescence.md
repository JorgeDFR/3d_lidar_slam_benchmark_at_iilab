# Install Iridescence on Ubuntu

This guide provides step-by-step instructions to install Iridescence from source on Ubuntu 22.04.

- **Official Documentation**: [Iridescence Github Repository](https://github.com/koide3/iridescence)
- **Tested OS**: [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy)
- **Last Updated**: November 22, 2024
- **Required by**: GLIM

## Installation Steps

### Step 1: Install Dependencies

Begin by installing the necessary dependencies using the following command:

```sh
sudo apt-get install -y libglm-dev libglfw3-dev libpng-dev libjpeg-dev libeigen3-dev
```

### Step 2: Install gtsam_points

Now download and install the Iridescence using the following commands:

```sh
# Clone the repository
git clone https://github.com/koide3/iridescence --recursive

# Create and navigate to the build directory
mkdir -p iridescence/build && cd iridescence/build

# Configure the build
cmake .. -DCMAKE_BUILD_TYPE=Release

# Compile the source code
make -j4

# Install the compiled libraries
sudo make install
```

If you need Python bindings for Iridescence, follow these optional steps:

```sh
# [Optional] Build and install python bindings
cd .. && pip install .

# [Optional 2] Install stubs for autocomplete
pip install pybind11-stubgen
cd ~/.local/lib/python3.12/site-packages
pybind11-stubgen -o . --ignore-invalid=all pyridescence
```
