# Age\_Predict

## This repo is for age predict projection mission using ML model, which combine with GUI.

This program allow users predict the age using their own face image.
In UI, you can also choose with different model to estimate.

### Memu
1. Example of Program
2. Environment Setup
3. Project Overview
4. How to install and use this program
5. How to tweak this project for your own use
6. Known Issues
7. Working On Progress
8. Reference 


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

### Project Overview
1. Dataset Analysis & Preprocessing <br>
The project first examined the distribution of the dataset used for model training and conducted data preprocessing to improve balance and effectiveness.

   - For overrepresented age groups, specific segments exceeding 1,000 records were reduced to 500 records.

   - For underrepresented or less impactful groups, only 30% of infant records were retained due to limited predictive value, while all data above 80 years old was removed because of insufficient facial features and low contribution to general prediction performance.

2. Dataset Splitting <br>
The processed data was divided into training, validation, and test sets at fixed proportions to ensure fairness and consistency during model evaluation.

3. Data Augmentation <br>
To improve the model’s generalization ability, minor image transformations were applied to the training data, including horizontal and vertical shifts of 0.1 and mirror flipping.

4. Baseline Model Training & Saving <br>
A basic CNN architecture was used as the initial training model, serving as a baseline for analyzing model behavior following the dataset rebalancing.<br>
Finally, save the trained model.

5. Use the Model to Estimate Age<br>
   - Open `GUI_AgePrediction.py` to launch the application.
   - Select the trained model in the GUI.
   - Choose an image for age estimation.
   - The predicted age will be displayed below the image.



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

### How to install and use this program

### How to tweak this project for your own use 

### Known Issues
The dataset used for age prediction training exhibits widespread issues with extreme data distribution.<br>
Certain age groups are underrepresented, while others are disproportionately overrepresented.<br>
This skewed distribution impairs the model's generalization capabilities during training, causing it to overfit specific age groups while underperforming on others.

Although this training addressed the imbalance by trimming age groups with excessive data and removing a few age groups with extremely sparse data at the tail end, achieving a more balanced overall distribution, this trimming approach may also result in insufficient training samples. Consequently, the model's performance in convergence and real-world application may fall short of expectations.

### Working On Progress
Therefore, there remains room for improvement in the model's training decisions. For instance: employing data augmentation to maintain sufficient sample size while achieving balanced distribution; or shifting to pre-trained models that demonstrate superior performance in image processing.

### Reference
Dataset Source : https://www.kaggle.com/datasets/jangedoo/utkface-new <br>
Kaggle Notebook : https://www.kaggle.com/code/eward96/age-and-gender-prediction-on-utkface <br>
The data preprocessing step adopted the image cropping strategy referenced from this Kaggle notebook to improve dataset distribution.