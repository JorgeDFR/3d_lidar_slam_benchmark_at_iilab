# Indoor Benchmark of 3D LIDAR SLAM in iilab - Industry and Innovation Laboratory

This repository provides the complete benchmark suite and documentation for evaluating 3D LiDAR-based SLAM algorithms in indoor environments, using the IILABS 3D dataset collected at the Industry and Innovation Laboratory (iilab).

## Project Overview

- **IILABS 3D Dataset:** A novel, sensor-rich, indoor dataset for benchmarking 3D LiDAR-based SLAM algorithms.
- **Sensors:** Includes four heterogeneous 3D LiDARs (Livox Mid-360, Ouster OS1-64, RoboSense RS-Helios-5515, Velodyne VLP-16), IMU, 2D LiDAR, and wheel encoders.
- **Ground Truth:** High-precision, sub-millimeter ground truth from a 24-camera OptiTrack MoCap system.
- **Benchmark:** Comparative evaluation of nine state-of-the-art SLAM algorithms using standardized metrics (ATE, RTE, RRE).
- **Reproducibility:** Docker-based workflows for ROS1 and ROS2, with ready-to-use scripts and configuration files.

## Project Links

- **[Project Webpage](https://jorgedfr.github.io/3d_lidar_slam_benchmark_at_iilab/):**
The main documentation and results site for the benchmark, including usage instructions, dataset details, sensor specifications, and benchmark results.

- **[IILABS 3D Dataset](https://rdm.inesctec.pt/dataset/nis-2025-001):**
  The official data repository for the IILABS 3D dataset, containing all calibration and benchmark sequences, sensor data, and ground truth.

- **[Dataset Toolkit](https://github.com/JorgeDFR/iilabs3d-toolkit):**
  A Python package providing utilities for downloading, managing, and evaluating the IILABS 3D dataset. Includes tools for sequence download, conversion, and evaluation.

- **[YouTube Playlist](https://www.youtube.com/playlist?list=PL__T3ljZgf9tR-B4t1Kc1U7aTt-duUs-3):**
  Videos demonstrating the dataset sequences, benchmark experiments and SLAM algorithms performance.

- **Docker Images ([ROS 1](https://hub.docker.com/r/jorgedfr/3d_slam_ros1) / [ROS 2](https://hub.docker.com/r/jorgedfr/3d_slam_ros2)):**
  Prebuilt Docker images for reproducing the benchmark results with the selected 3D SLAM algorithms.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jorgedfr/3d_lidar_slam_benchmark_at_iilab.git
   cd 3d_lidar_slam_benchmark_at_iilab
   git submodule update --init --recursive
   ```

2. **Read the Documentation:**
   Full setup, usage, and dataset details are available on the [project website](https://jorgedfr.github.io/3d_lidar_slam_benchmark_at_iilab/).

3. **Run with Docker (Recommended):**
   See the [Docker instructions](docs/content/benchmark/docker.md) or the website for step-by-step setup for ROS1/ROS2 environments.

## Repository Structure

- `docs/` — Documentation source for the GitHub Pages site (MkDocs)
- `docker/` — Dockerfiles and compose files for ROS1/ROS2 environments
- `slam_benchmark_ros1_conf/` & `slam_benchmark_ros2_conf/` — ROS launch/configuration files for SLAM algorithms
- `external/` — External dependencies and interfaces

## License

Distributed under the _BSD 3-Clause License_.
See [LICENSE](/LICENSE) for more information.

## References

If you use the IILABS 3D dataset in a work that leads to a
scientific publication, we would appreciate it if you would kindly cite
our article and/or dataset in your manuscript.

### Article

TBC

<!--
**Plain Text**

J.D. Ribeiro, R.B. Sousa, J.G. Martins, A.S. Aguiar, F.N. Santos and H.M. Sobreira,
"Indoor Benchmark of 3D LiDAR SLAM at iilab - Industry and Innovation Laboratory",
_TBD_, 2025, pp. TBD, doi: TBD.

**BibTex**

```bibtex
@ARTICLE{ribeiro:2025:benchmark,
  author    = {J.D. Ribeiro and R.B. Sousa and J.G. Martins and A.S. Aguiar and F.N. Santos and H.M. Sobreira},
  title     = {{I}ndoor {B}enchmark of {3D} {LiDAR} {SLAM} at iilab - {I}ndustry and {I}nnovation {L}aboratory},
  journal   = {TBD},
  year      = {2025},
  volume    = {},
  number    = {},
  pages     = {--},
  doi       = {},}
```
-->

### Dataset

**Plain Text**

J.D. Ribeiro, R.B. Sousa, J.G. Martins, A.S. Aguiar, F.N. Santos and H.M. Sobreira,
"IILABS 3D: iilab Indoor LiDAR-based SLAM Dataset", \[Dataset\], INESC TEC, 2025,
doi: [10.25747/VHNJ-WM80](https://doi.org/10.25747/VHNJ-WM80).

**BibTex**

```bibtex
@MISC{ribeiro:2025:iilabs3d:dataset,
  author    = {J.D. Ribeiro and R.B. Sousa and J.G. Martins and A.S. Aguiar and F.N. Santos and H.M. Sobreira},
  title     = {{IILABS 3D}: iilab {I}ndoor {LiDAR}-based {SLAM} {D}ataset},
  year      = {2025},
  publisher = {INESC TEC},
  doi       = {10.25747/VHNJ-WM80},
  note      = {[Dataset]},}
```

## Contacts

If you have any questions or you want to know more about this work, please
contact one of the following contributors:

- Jorge Diogo Ribeiro
  ([jorge.d.ribeiro@inesctec.pt](mailto:jorge.d.ribeiro@inesctec.pt))
  _(Corresponding Author)_
  ([github](https://github.com/jorgedfr/),
  [gitlab](https://gitlab.inesctec.pt/jorge.d.ribeiro),
  [orcid](https://orcid.org/0009-0008-9373-982X),
  [google-scholar](https://scholar.google.pt/citations?user=xp6I4DMAAAAJ&hl))
- Ricardo B. Sousa
  ([rbs@fe.up.pt](mailto:rbs@fe.up.pt))
  ([github](https://github.com/sousarbarb/),
  [gitlab](https://gitlab.inesctec.pt/ricardo.b.sousa),
  [orcid](https://orcid.org/0000-0003-4537-5095),
  [google-scholar](https://scholar.google.pt/citations?user=Bz2FMqYAAAAJ))
- João G. Martins
  ([joao.g.martins@inesctec.pt](mailto:joao.g.martins@inesctec.pt))
  ([gitlab](https://gitlab.inesctec.pt/joao.g.martins),
  [orcid](https://orcid.org/0000-0002-6567-4802)
  [google-scholar](https://scholar.google.pt/citations?user=9zJiajsAAAAJ))
- André S. Aguiar
  ([andre.s.aguiar@inesctec.pt](mailto:andre.s.aguiar@inesctec.pt))
  ([gitlab](https://gitlab.inesctec.pt/andre.s.aguiar/),
  [orcid](https://orcid.org/0000-0001-6909-0209),
  [google-scholar](https://scholar.google.pt/citations?user=bcT07qcAAAAJ))
- Filipe N. Santos
  ([filipe.n.santos@inesctec.pt](mailto:filipe.n.santos@inesctec.pt))
  ([gitlab](https://gitlab.inesctec.pt/filipe.n.santos/),
  [orcid](https://orcid.org/0000-0002-8486-6113),
  [google-scholar](https://scholar.google.pt/citations?user=1XaOP0gAAAAJ))
- Héber Miguel Sobreira
  ([heber.m.sobreira@inesctec.pt](mailto:heber.m.sobreira@inesctec.pt))
  ([gitlab](https://gitlab.inesctec.pt/heber.m.sobreira/),
  [orcid](https://orcid.org/0000-0002-8055-1093),
  [google-scholar](https://scholar.google.pt/citations?user=iNhGcpsAAAAJ))

## Institutions

- [INESC TEC - Institute for Systems and Computer Engineering, Technology and Science](https://www.inesctec.pt/en/)
- [Faculty of Engineering, University of Porto (FEUP)](https://sigarra.up.pt/feup/en/)

## Funding

This work is co-financed by Component 5 - Capitalization and Business
Innovation, integrated in the Resilience Dimension of the Recovery and
Resilience Plan within the scope of the Recovery and Resilience
Mechanism (MRR) of the European Union (EU), framed in the Next Generation EU,
for the period 2021-2026, within project GreenAuto, with reference 54.

**GreenAuto: Green innovation for the Automotive Industry**

- **Operation Code:** 02/C05-i01.02/2022.PC644867037-00000013
- **Beneficiary:** Peugeot Citröen Automóveis Portugal, S.A.
- **Work Package:** WP10 - Automated logistics for the automotive industry
- **Product, Processes, or Services (PPS):**
  PPS18 - 3D navigation system for mobile robotic equipment
- **Consortium Partners:**
    - [Flowbotic Mobile Systems, Lda](https://www.flowbotic.eu/) _(leader)_
    - [Faculty of Engineering, University of Porto (FEUP)](https://www.up.pt/feup/en/)
    - [INESC TEC - Institute for Systems and Computer Engineering, Technology and Science](https://www.inesctec.pt/en/)
    - [STAR](https://starinstitute.pt/)
    - [Kaizen](https://kaizen.com/pt-pt/)
    - [Institute for Systems and Robotics (ISR)-Coimbra](https://www.isr.uc.pt/)
- **Timeline:** October 2021 - December 2025
- **Duration:** 51 months
- **URL:**
  [https://transparencia.gov.pt/en/fundos-europeus/prr/beneficiarios-projetos/projeto/02/C05-i01.02/2022.PC644867037-00000013/](https://transparencia.gov.pt/en/fundos-europeus/prr/beneficiarios-projetos/projeto/02/C05-i01.02/2022.PC644867037-00000013/)