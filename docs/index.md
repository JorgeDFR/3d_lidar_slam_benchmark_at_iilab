# Indoor Benchmark of 3D LiDAR SLAM at iilab - Industry and Innovation Laboratory

!!! Abstract

    This paper presents the IILABS 3D dataset, a novel and publicly available resource designed to address current limitations in indoor benchmarking of 3D LiDAR-based Simultaneous Localization and Mapping (SLAM) algorithms. Existing SLAM datasets often focus on outdoor environments, rely on a single type of LiDAR sensor, or lack ground-truth data suitable for evaluating diverse indoor conditions. IILABS 3D fills this gap by providing a sensor-rich, indoor-exclusive dataset recorded in a controlled laboratory environment using a wheeled mobile robot platform. It includes four heterogeneous 3D LiDAR sensors -- Velodyne VLP-16, Ouster OS1-64, RoboSense RS-Helios-5515, and Livox Mid-360 -- featuring both mechanical spinning and non-repetitive scanning patterns, as well as an IMU and wheel odometry. The dataset also features calibration sequences, challenging benchmark trajectories, and high-precision ground-truth poses captured with a Motion Capture (MoCap) system. By combining diverse sensor technologies, extensive calibration data, and carefully designed indoor scenarios, IILABS 3D enables more comprehensive and reproducible evaluation of LiDAR-based SLAM algorithms, fostering innovation in autonomous navigation within complex indoor environments. The dataset information and associated tools are available at project webpage [jorgedfr.github.io/3d_lidar_slam_benchmark_at_iilab](https://jorgedfr.github.io/3d_lidar_slam_benchmark_at_iilab).

    **Keywords:**
    dataset,
    ground mobile robot,
    indoor environment,
    Light Detection and Ranging (LiDAR),
    Simultaneous Localization and Mapping (SLAM).

This repository hosts the complete documentation and supporting resources for the project 
["Indoor Benchmark of 3D LiDAR SLAM at iilab - Industry and Innovation Laboratory"](.).
The project evaluates state-of-the-art 3D LiDAR SLAM algorithms using data captured in 
indoor environments. To this end, the study introduces the novel 
[IILABS 3D dataset](https://rdm.inesctec.pt/dataset/nis-2025-001), which contains data from 
four diverse 3D LiDAR sensors (Velodyne VLP-16, Ouster OS1-64, RoboSense RS-Helios-5515, and Livox Mid-360), 
complemented by measurements from an IMU and wheel odometry.

In parallel with the dataset, the project presents a detailed benchmark analysis of nine 
leading SLAM algorithms. By comparing algorithm-generated odometry against high-accuracy 
ground-truth data using metrics such as ATE, RTE, and RRE, the study provides valuable insights 
into the performance, limitations, and integration of these algorithms in indoor environments.

The primary aim of this website and GitHub repository is to support researchers in developing, 
benchmarking, and applying 3D LiDAR-based SLAM solutions in indoor settings.
As a result, the website includes the following information:

- **[Usage](content/usage.md):** Step-by-step instructions for replicating the benchmark study 
  using the provided scripts and dataset.
- **[Dataset](content/dataset/index.md):** A detailed overview of the 
  [IILABS 3D dataset](https://rdm.inesctec.pt/dataset/nis-2025-001), 
  its structure, and key characteristics.
- **[Sensors](content/sensors/index.md):** Specifications and technical details 
  of the sensors used during data collection.
- **[Benchmark](content/benchmark/index.md):** A summary of the benchmark scripts, 
  experimental setup, and key results from the analysis.

Lastly, this work is within the scope of the
[Mobile Robotics Development Team (MRDT)](https://gitlab.inesctec.pt/mrdt/) in
the national project
[GreenAuto: Green innovation for the Automotive Industry](https://transparencia.gov.pt/en/fundos-europeus/prr/beneficiarios-projetos/projeto/02/C05-i01.02/2022.PC644867037-00000013/). [MRDT](https://gitlab.inesctec.pt/mrdt/) team is a
Research & Development (R&D) team from the
[CRIIS - Centre for Robotics in Industry and Intelligent Systems](https://www.inesctec.pt/en/centres/criis)
at the [iiLab - Industry and Innovation Laboratory](https://www.inesctec.pt/en/laboratories/iilab-industry-and-innovation-lab).

## Videos

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=zuZfPb23WqZMpGxl&amp;list=PL__T3ljZgf9tR-B4t1Kc1U7aTt-duUs-3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- **How To Watch**
    1. Press the :material-play: Play button
    2. Use the :material-skip-previous: Previous and :material-skip-next: Next
       buttons to navigate through the playlist
- **Playlist YouTube Link:**
  [https://www.youtube.com/playlist?list=PL__T3ljZgf9tR-B4t1Kc1U7aTt-duUs-3](https://www.youtube.com/playlist?list=PL__T3ljZgf9tR-B4t1Kc1U7aTt-duUs-3)

## Contacts

If you have any questions or you want to know more about this work, please
contact one of the following contributors:

- Jorge Diogo Ribeiro
  ([jorge.d.ribeiro@inesctec.pt](mailto:jorge.d.ribeiro@inesctec.pt))
  _(Corresponding Author)_
  [:fontawesome-brands-github:](https://github.com/jorgedfr/),
  [:fontawesome-brands-gitlab:](https://gitlab.inesctec.pt/jorge.d.ribeiro),
  [:fontawesome-brands-orcid:](https://orcid.org/0009-0008-9373-982X),
  [:fontawesome-brands-google-scholar:](https://scholar.google.pt/citations?user=xp6I4DMAAAAJ&hl)
- Ricardo B. Sousa
  ([rbs@fe.up.pt](mailto:rbs@fe.up.pt))
  [:fontawesome-brands-github:](https://github.com/sousarbarb/),
  [:fontawesome-brands-gitlab:](https://gitlab.inesctec.pt/ricardo.b.sousa),
  [:fontawesome-brands-orcid:](https://orcid.org/0000-0003-4537-5095),
  [:fontawesome-brands-google-scholar:](https://scholar.google.pt/citations?user=Bz2FMqYAAAAJ)
- João G. Martins
  ([joao.g.martins@inesctec.pt](mailto:joao.g.martins@inesctec.pt))
  [:fontawesome-brands-gitlab:](https://gitlab.inesctec.pt/joao.g.martins),
  [:fontawesome-brands-orcid:](https://orcid.org/0000-0002-6567-4802)
  [:fontawesome-brands-google-scholar:](https://scholar.google.pt/citations?user=9zJiajsAAAAJ)
- André S. Aguiar
  ([andre.s.aguiar@inesctec.pt](mailto:andre.s.aguiar@inesctec.pt))
  [:fontawesome-brands-gitlab:](https://gitlab.inesctec.pt/andre.s.aguiar/),
  [:fontawesome-brands-orcid:](https://orcid.org/0000-0001-6909-0209),
  [:fontawesome-brands-google-scholar:](https://scholar.google.pt/citations?user=bcT07qcAAAAJ)
- Filipe N. Santos
  ([filipe.n.santos@inesctec.pt](mailto:filipe.n.santos@inesctec.pt))
  [:fontawesome-brands-gitlab:](https://gitlab.inesctec.pt/filipe.n.santos/),
  [:fontawesome-brands-orcid:](https://orcid.org/0000-0002-8486-6113),
  [:fontawesome-brands-google-scholar:](https://scholar.google.pt/citations?user=1XaOP0gAAAAJ)
- Héber Miguel Sobreira
  ([heber.m.sobreira@inesctec.pt](mailto:heber.m.sobreira@inesctec.pt))
  [:fontawesome-brands-gitlab:](https://gitlab.inesctec.pt/heber.m.sobreira/),
  [:fontawesome-brands-orcid:](https://orcid.org/0000-0002-8055-1093),
  [:fontawesome-brands-google-scholar:](https://scholar.google.pt/citations?user=iNhGcpsAAAAJ)

## Institutions

<div class="grid cards" markdown>

- [![INESC TEC Logo](assets/logo/inesctec_logo_color-rgb.png)](https://www.inesctec.pt/en/)
- [![FEUP Logo](assets/logo/feup_logo_oficial.png)](https://sigarra.up.pt/feup/en/)

</div>

<!-- ## Acknowledgements

<div class="grid cards" markdown>

</div> -->

## Funding

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

## Citations

### Article

TBC

<!--
**Plain Text**

J.D. Ribeiro, R.B. Sousa, J.G. Martins, A.S. Aguiar, F.N. Santos and H.M. Sobreira,
"Indoor Benchmark of 3D LiDAR SLAM at iilab - Industry and Innovation Laboratory",
_IEEE Access_, 2025, pp. TBD, doi: TBD.

**BibTex**

```bibtex
@ARTICLE{ribeiro:2025:benchmark,
  author    = {J.D. Ribeiro and R.B. Sousa and J.G. Martins and A.S. Aguiar and F.N. Santos and H.M. Sobreira},
  title     = {{I}ndoor {B}enchmark of {3D} {LiDAR} {SLAM} at iilab - {I}ndustry and {I}nnovation {L}aboratory},
  journal   = {IEEE Access}, 
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