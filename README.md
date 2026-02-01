# Age\_Predict

## This repo is for age predict projection mission using ML model, which combine with GUI.

This program allow users predict the age using their own face image.
In UI, you can also choose with different model to estimate.


### Example 
<table>
  <tr>
    <td align="center">
      <img src="reference/prediction_windows_modelSelect_2.png" width="420"><br>
      <sub>Step 1: Model selection</sub>
    </td>
    <td align="center">
      <img src="reference/prediction_windows_modelSelect_6.png" width="420"><br>
      <sub>Step 2: Prediction result</sub>
    </td>
  </tr>
</table>

### Environment Setup
This program development on the environment below : 

Hardware : 

1. Nvidia RTX 5060
2. AMD I7 350

Attention. If your GPU is not the Nvidia Blackwell Gen, then you don’t have to follow the software requests below.
Just find the Tensorflow 2.10.0, which is the last version support GPU on windows directly, and everything can still work out.

Software : 

1. WSL2 with Ubuntu 24.04
2. Image : Nvidia NGC Tensorflow container 
3. Container : Docker desktop
4. Container Tool : Dev container in VS code
5. Requirement.txt with all ML tool you want to build in this container.
6. Docker file 
7. Devcontainer.json

### How to use install and use this program

### How to tweak this project for your own use 

### Known Issues and working on progress
The dataset used for age prediction training exhibits widespread issues with extreme data distribution.<br>
Certain age groups are underrepresented, while others are disproportionately overrepresented.<br>
This skewed distribution impairs the model's generalization capabilities during training, causing it to overfit specific age groups while underperforming on others.

Although this training addressed the imbalance by trimming age groups with excessive data and removing a few age groups with extremely sparse data at the tail end, achieving a more balanced overall distribution, this trimming approach may also result in insufficient training samples. Consequently, the model's performance in convergence and real-world application may fall short of expectations.

Therefore, there remains room for improvement in the model's training decisions. For instance: employing data augmentation to maintain sufficient sample size while achieving balanced distribution; or shifting to pre-trained models that demonstrate superior performance in image processing.
