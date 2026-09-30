# NIR-II Temporal Compressive Wide-Field Microscope (TCWM)

Official reconstruction code for our paper:

**NIR-II Temporal Compressive Wide-Field Microscope (TCWM) Achieving Fluorescent Dynamic Imaging Beyond Camera Frame Rate**  
Xuan You, Xiaolong Liu, Wei Liu, Peijin Zhang, Yuhuang Zhang, Yalun Wang, Jianguo Wang, and Jun Qian  
*Laser & Photonics Reviews*, 2026  
[[Paper](https://onlinelibrary.wiley.com/doi/10.1002/lpor.202502999)]

## Overview

This repository provides the reconstruction code used in our NIR-II temporal compressive wide-field microscope (TCWM).

TCWM enables high-speed NIR-II fluorescence imaging by temporally encoding multiple frames into a single camera exposure and reconstructing the high-speed image sequence computationally.

The reconstruction framework is based on [EfficientSCI](https://github.com/ucaswangls/EfficientSCI). For the TCWM experiments, EfficientSCI was adapted and fine-tuned using experimentally acquired masks from the TCWM system for reconstruction of experimental fluorescence measurements.

## Installation

Clone this repository:

```bash
git clone https://github.com/XavierYX/EfficientSCI.git
cd EfficientSCI
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The original EfficientSCI implementation requires Python 3 and PyTorch 1.9 or later. A CUDA-enabled GPU is recommended for training and reconstruction.

## Data and Checkpoints

The checkpoints and datasets used for the TCWM reconstruction experiments are not included in this repository because of their file sizes.

They can be downloaded from:

**[BaiduNetdisk](https://pan.baidu.com/s/1EGIKDW7nIR2XSDMazY8Lfg?pwd=3kpg)**  
Extraction code: `3kpg`

After downloading, place the corresponding folders in the root directory of the repository:

```text
EfficientSCI/
├── checkpoints/
├── test_datasets/
├── cacti/
├── configs/
├── docs/
├── tools/
├── requirements.txt
└── README.md
```

The `checkpoints/` and `test_datasets/` directories are excluded from Git tracking because of their file sizes.

## Usage

The code follows the original EfficientSCI training and reconstruction framework.

For reconstruction using a trained checkpoint, the general command is:

```bash
python tools/test.py configs/EfficientSCI/efficientsci_base.py \
    --weights=checkpoints/efficientsci_base.pth
```

Please modify the configuration, dataset path, and checkpoint path according to the corresponding TCWM experiment when necessary.

For further details about the network architecture and the original training framework, please refer to the [EfficientSCI repository](https://github.com/ucaswangls/EfficientSCI).

## Acknowledgement

This repository is adapted from **EfficientSCI: Densely Connected Network with Space-time Factorization for Large-scale Video Snapshot Compressive Imaging** by Lishun Wang, Miao Cao, and Xin Yuan.

We sincerely thank the authors of EfficientSCI for making their code publicly available. Their implementation provides the reconstruction framework used in our TCWM work.

## Citation

If you find this work or code useful for your research, please consider citing our paper:

```bibtex
@article{you2026tcwm,
  title   = {NIR-II Temporal Compressive Wide-Field Microscope (TCWM) Achieving Fluorescent Dynamic Imaging Beyond Camera Frame Rate},
  author  = {You, Xuan and Liu, Xiaolong and Liu, Wei and Zhang, Peijin and Zhang, Yuhuang and Wang, Yalun and Wang, Jianguo and Qian, Jun},
  journal = {Laser \& Photonics Reviews},
  pages   = {e02999},
  year    = {2026},
  doi     = {10.1002/lpor.202502999}
}
```

Please also cite the original EfficientSCI work:

```bibtex
@inproceedings{wang2023efficientsci,
  title     = {EfficientSCI: Densely Connected Network with Space-Time Factorization for Large-Scale Video Snapshot Compressive Imaging},
  author    = {Wang, Lishun and Cao, Miao and Yuan, Xin},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages     = {18477--18486},
  year      = {2023}
}
```
