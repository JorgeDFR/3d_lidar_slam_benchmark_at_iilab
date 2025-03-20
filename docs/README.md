# GitHub Pages

Public page of the repository based on GitHub actions through the template
**Material** (https://squidfunk.github.io/mkdocs-material/) from **MkDocs**
(https://www.mkdocs.org/) Markdown-based static site
generation.

## Setup

### GitHub Repository

```sh
mkdir ~/dev
cd ~/dev

git clone git@github.com:jorgedfr/3d_lidar_slam_benchmark_at_iilab.git
```

### Material for MkDocs

```sh
pip install mkdocs-material
```

## Usage

### Local

```sh
cd ~/dev/3d_lidar_slam_benchmark_at_iilab

mkdocs serve -a <localhost IP 127.0.0.1>:<PORT>
```
