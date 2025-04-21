# Install Docker on Ubuntu

This guide provides step-by-step instructions for installing Docker on Ubuntu 20.04, including optional configurations for NVIDIA GPUs and Docker Compose Plugin installation.

## 1. Install Docker

Docker is an open-source platform used to automate the deployment, scaling, and management of applications within lightweight, portable containers. The installation of Docker on Ubuntu involves adding Docker's official repositories, installing Docker Engine, and configuring Docker to run on your system. This section will guide you through the installation process.

- **Official documentation**: [Docker Engine Webpage](https://docs.docker.com/engine/install/ubuntu/)

### Step-by-step instructions:
```sh
# Update the apt package index and install necessary dependencies
sudo apt-get install -y ca-certificates curl lsb-release

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# Make the key accessible by everyone
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the Docker repository to your system's APT sources
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the apt package index again
sudo apt-get update

# Install Docker Engine, CLI, and other related packages
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Post-installation steps (Optional):

To allow running Docker commands without the need for `sudo` privileges, you must add your user to the `docker` group. This step simplifies the process, especially if you plan to work with Docker frequently (more details [here](https://docs.docker.com/engine/install/linux-postinstall/)).

```sh
# Create the Docker group if it doesn't exist
sudo groupadd docker

# Add your user to the Docker group
sudo usermod -aG docker $USER
```

!!! warning "Log Out required"  
    You will need to log out and log back in for the changes to take effect, or you can reboot your machine.

## 2. Install NVIDIA Container Toolkit (Optional)

The NVIDIA Container Toolkit enables Docker to utilize NVIDIA GPUs for running GPU-accelerated workloads in containers. This is particularly useful when running graphical applications like ROS (Robot Operating System) with tools such as RViz, which require GPU resources for rendering 3D visualizations. By leveraging the NVIDIA Container Toolkit, you can ensure that the necessary GPU acceleration is available within Docker containers, enabling seamless performance for ROS packages that require graphical interfaces.

- **Official documentation**: [NVIDIA Container Toolkit Webpage](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

### Step-by-step instructions:
```sh
# Verify that your NVIDIA GPU is working
nvidia-smi

# Add the NVIDIA container toolkit repository's GPG key
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

# Add the NVIDIA container toolkit repository
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# Install the NVIDIA container toolkit package
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit

# Configure Docker to use NVIDIA runtime
sudo nvidia-ctk runtime configure --runtime=docker

# Restart Docker service
sudo systemctl restart docker
```

### GPU container configuration:

Every time you restart your system, you'll need to configure the X server to allow Docker containers to access the display. Use the following commands:
```sh
# Allow Docker containers to access the X server
xhost +local:docker
```

!!! warning "DISPLAY enviroment variable"  
    Adjust the DISPLAY enviroment variable (`:0`, `:1`, etc.) depending on your system’s display settings if it is not set.


## 3. Install Docker Compose Plugin (Optional)

Docker Compose is a tool designed to simplify the configuration and management of multi-container Docker applications. In the context of running ROS packages that require GPU support (such as those using RViz), Docker Compose can be used to easily define and configure the necessary containers in a `docker-compose.yml` file. This integration helps to simplify the process of setting up and managing containers that leverage the NVIDIA runtime, making it easier to configure GPU access and other dependencies needed for your ROS environment. The Docker Compose Plugin integrates directly with Docker, allowing you to orchestrate these containers with minimal configuration.

- **Official documentation**: [Docker Compose Plugin Webpage](https://docs.docker.com/compose/install/linux)

### Step-by-step instructions:
```sh
# Install the Docker Compose plugin
sudo apt-get update && apt-get install -y docker-compose-plugin
```