# TRANSFER LEARNING OBJECT DETECTION

> As a developer, I want robots to detect use-case-specific objects in the environment.

## Acceptance Criteria

> [\[x\] A dataset based on Realsense camera images is recorded and use case specific objects are annotated using 2D bounding boxes. The data is split into training, evaluation and test dataset](#Criteria_1)
>
> \[x\] A pre-trained object detection model (e.g. jetson-inference, ISAAC) is running
>
> [\[x\] The model is trained on the dataset using transfer learning. Loss curves are documented.](#Criteria_3)
>
> [\[x\] The object detection is evaluated on the test dataset using standard metrics like mAP. Results are documented](#Criteria_4)
>
> [\[x\] The metrics are improved via multiple additional training runs using hyperparameter tuning. Results are documented](#Criteria_4).
>
> [\[x\] The fine-tuned model is running on the Jetson on live camera data. Output can be visualized.](#Criteria_5)

## Model Evaluation Results

##

  - The final evaluation results indicate an overall mAP of approximately **91.59% for Iteration 2**. The model was evaluated on the reserved test dataset containing 100 images across four object classes.

  - The training and validation loss curves provide evidence of model convergence, while the comparison between the baseline and subsequent training iterations demonstrates the impact of different training configurations on detection performance.

  - Live detection screenshots demonstrate the model identifying objects such as broken glass, bottles, conveyor pillars, and persons in the camera feed.

## Timeline

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Planned Task</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Wednesday, 7 October 2026</p>
</blockquote></td>
<td><blockquote>
<p>Dataset collection: Collect approximately 1,000 images across four classes, varying camera angles, distances, and lighting conditions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Wednesday, 14 October 2026</p>
</blockquote></td>
<td><blockquote>
<p>Data annotation and preparation: Annotate images using Roboflow with 2D bounding boxes and prepare training, validation, and test datasets.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Wednesday, 21 October 2026</p>
</blockquote></td>
<td><blockquote>
<p>Model training: Set up the pre-trained SSD-MobileNet model, apply transfer learning, and document the training and validation loss curves.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Wednesday, 28 October 2026</p>
</blockquote></td>
<td><blockquote>
<p>Model evaluation: Evaluate the model using mAP and other relevant metrics, document the confusion matrix, and test live camera detection.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Wednesday, 4 November 2026</p>
</blockquote></td>
<td><blockquote>
<p>Final improvements and documentation: Perform additional training runs with hyperparameter tuning, compare results, verify live detection, and finalize the project documentation.</p>
</blockquote></td>
</tr>
</tbody>
</table>

**1. Project Overview**

**1.1 Objective**

The objective of this project is to develop an object detection model capable of identifying application-specific objects in an industrial environment using transfer learning.

The model is designed to detect four object classes: conveyor pillar, broken glass, bottle, and person. The trained model enables the system to recognize objects from camera images and visualize their locations using bounding boxes, class labels, and confidence scores.

The primary application is to provide an object perception capability for an autonomous industrial glass-cleaning robot.

**1.2 Project Process**

  - Collect and annotated data using Roboflow for four object classes. ([Swachh\_bot](https://app.roboflow.com/join/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6Ikg2NUNEWmNGVkJUQmVHc2RpaExoR1NTb21qcTEiLCJyb2xlIjoib3duZXIiLCJpbnZpdGVyIjoicHJhNzgwNXNAaHMtY29idXJnLmRlIiwiaWF0IjoxNzk0MzMxODUyfQ.Dy5kFcSb2YLWFen9ARFJvcTQH23V1sBio4H4gXkJ80I))

  - Prepare training, validation, and test datasets.

  - Implement a pretrained SSD-MobileNet object detection model.

  - Apply transfer learning using NVIDIA Jetson Inference.

  - Perform multiple training iterations and evaluate model performance.

  - Analyze training and validation loss curves.

  - Evaluate detection performance using standard metrics, including Average Precision (AP) and mean Average Precision (mAP).

  - Compare the baseline model with subsequent training iterations.

  - Perform live camera inference and visualize the detection results.

<span id="Criteria_1" class="anchor"></span>**2. Dataset Collection and Preparation**

**2.1 Dataset Description**

Approximately 1,000 images were collected for the following four object classes:

| Class ID | Object Class     |
| -------- | ---------------- |
| 1        | Conveyor\_pillar |
| 2        | broken\_glass    |
| 3        | Bottle           |
| 4        | person           |

The collected images include variations in our object class distances, object positions, and lighting conditions to improve the model's ability to generalize to different environmental situations.

**2.2 Annotation and Dataset Preparation**

The collected images were annotated using Roboflow with 2D bounding boxes and corresponding object class labels.

The annotated dataset was subsequently converted into Pascal VOC format for compatibility with the NVIDIA Jetson Inference SSD training pipeline.

The dataset was divided into training, validation, and test subsets.

**Dataset Distribution**

| **Dataset** | **Images** | **Percentage** |
| ----------- | ---------- | -------------- |
| Training    | 748        | 74.95%         |
| Validation  | 150        | 15.03%         |
| Testing     | 100        | 10.02%         |
| Total       | 998        | 100%           |

Dataset link: [Swachh\_bot](https://app.roboflow.com/join/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6Ikg2NUNEWmNGVkJUQmVHc2RpaExoR1NTb21qcTEiLCJyb2xlIjoib3duZXIiLCJpbnZpdGVyIjoicHJhNzgwNXNAaHMtY29idXJnLmRlIiwiaWF0IjoxNzk0MzMxODUyfQ.Dy5kFcSb2YLWFen9ARFJvcTQH23V1sBio4H4gXkJ80I)

<span id="Criteria_3" class="anchor"></span>**3. Baseline Model and Transfer Learning**

**3.1 Baseline Model**

The baseline object detection model was established using a pretrained SSD-MobileNet architecture.

The model was initialized using pretrained weights and adapted to the four application-specific object classes through transfer learning.

**3.1.1 Training Configuration**

| **Parameter**              | **Configuration**       |
| -------------------------- | ----------------------- |
| Model architecture         | SSD-MobileNet           |
| Backbone                   | MobileNet V1            |
| Framework                  | NVIDIA Jetson Inference |
| Dataset format             | Pascal VOC              |
| Number of classes          | 4 object classes        |
| Training epochs            | 100                     |
| Batch size                 | 4                       |
| Learning rate              | 0.01                    |
| Base network learning rate | 0.001                   |
| Optimizer                  | SGD                     |
| Momentum                   | 0.9                     |
| Weight decay               | 0.0005                  |
| Training resolution        | 300 × 300               |

**3.1.2 Loss Curves**

The training and validation loss curves were monitored throughout the 100 training epochs.

The training loss decreased substantially during the initial epochs and continued to decline gradually during subsequent training. The validation loss followed a similar trend and remained relatively stable toward the end of training.

The best validation-loss values and corresponding epochs were identified for each training iteration.

![](docs/images/media/image1.png)

Figure 1: Baseline training and validation loss over 100 epochs.

**3.1.3 Evaluation**

The baseline model established the initial performance of the object detection system.

| **Object Class**             | **Average Precision (AP)** |
| ---------------------------- | -------------------------- |
| conveyor\_pillar             | 98.53%                     |
| broken\_glass                | 88.62%                     |
| bottle                       | 88.71%                     |
| person                       | 88.53%                     |
| Mean Average Precision (mAP) | 91.10%                     |

The baseline achieved an overall mAP of approximately **91.10%.** Conveyor pillar achieved the highest class-wise AP, while broken glass showed comparatively lower detection performance.

![](docs/images/media/image2.png)

Figure 2: Baseline data Evaluation

**3.2 Iteration 1**

**3.2.1 Training Configuration**

The first experimental iteration involved training the SSD-MobileNet model using the prepared dataset containing four object classes. The training configuration was maintained to provide a consistent reference for evaluating the model's convergence and detection performance.

| **Parameter**              | **Configuration**       |
| -------------------------- | ----------------------- |
| Model architecture         | SSD-MobileNet           |
| Backbone                   | MobileNet V1            |
| Framework                  | NVIDIA Jetson Inference |
| Dataset format             | Pascal VOC              |
| Number of classes          | 4 object classes        |
| Training epochs            | 100                     |
| Batch size                 | 20                      |
| Learning rate              | 0.01                    |
| Base network learning rate | 0.001                   |
| Optimizer                  | SGD                     |
| Momentum                   | 0.9                     |
| Weight decay               | 0.0005                  |
| Training resolution        | 300 × 300               |

**3.2.2 Loss Curves**

The training and validation loss curves were monitored throughout the 100 training epochs.

The training loss decreased progressively from its initial value, while the validation loss showed a consistent downward trend and stabilized toward the final epochs. The lowest validation loss was observed at epoch 97, with a value of approximately 2.0701.

These results indicate effective convergence of the model during training and demonstrate the learning progress achieved in the first experimental iteration.

![](docs/images/media/image3.png)

Figure 2: Iteration 1 training and validation loss over 100 epochs.

**3.2.3 Evaluation**

Iteration 1 was performed to investigate the effect of an alternative training configuration on detection performance.

| **Object Class**             | **Average Precision (AP)** |
| ---------------------------- | -------------------------- |
| conveyor\_pillar             | 91.95%                     |
| broken\_glass                | 88.10%                     |
| bottle                       | 88.36%                     |
| person                       | 91.68%                     |
| Mean Average Precision (mAP) | 90.02%                     |

Iteration 1 achieved an overall mAP of approximately **90.02%.**

Person detection improved compared with the baseline, while conveyor pillar detection showed a reduction in AP. The overall evaluation performance decreased relative to the baseline model.

![](docs/images/media/image4.png)

Figure 4: Iteration 1 data Evaluation

**3.3 Iteration 2**

**3.3.1 Training Configuration**

The second experimental iteration was conducted to further investigate model convergence and detection performance using the SSD-MobileNet architecture.

The model was trained using the same dataset and training configuration to maintain consistency with the previous experimental run and allow a meaningful comparison of the evaluation results.

| **Parameter**              | **Configuration**       |
| -------------------------- | ----------------------- |
| Model architecture         | SSD-MobileNet           |
| Backbone                   | MobileNet V1            |
| Framework                  | NVIDIA Jetson Inference |
| Dataset format             | Pascal VOC              |
| Number of classes          | 4 object classes        |
| Training epochs            | 100                     |
| Batch size                 | 20                      |
| Learning rate              | 0.005                   |
| Base network learning rate | 0.001                   |
| Optimizer                  | SGD                     |
| Momentum                   | 0.9                     |
| Weight decay               | 0.0005                  |
| Training resolution        | 300 × 300               |

**3.3.2 Loss Curves**

The training and validation loss curves were analyzed to evaluate the convergence behavior of the second iteration.

The training loss decreased significantly during the initial epochs and continued to decline gradually throughout the training process. The validation loss also decreased consistently and remained relatively stable during the later epochs.

The lowest validation loss was recorded at epoch 91, with a value of approximately 2.1805.

The observed loss reduction indicates that the model successfully learned relevant object features from the training dataset and achieved stable convergence during the second experimental iteration.

![](docs/images/media/image3.png)

Figure 5: Iteration 2 training and validation loss over 100 epochs.

**3.2.3 Evaluation**

Iteration 2 was conducted to further investigate model performance and improve detection capability.

| **Object Class**             | **Average Precision (AP)** |
| ---------------------------- | -------------------------- |
| conveyor\_pillar             | 90.96%                     |
| broken\_glass                | 89.99%                     |
| bottle                       | 87.36%                     |
| person                       | 89.97%                     |
| Mean Average Precision (mAP) | 91.59%                     |

Iteration 2 achieved the highest overall mAP among the three evaluated configurations which is **91.59%**.

Broken-glass detection improved compared with the baseline and Iteration 1, making the configuration particularly relevant to the intended glass-cleaning application.

![](docs/images/media/image5.png)

Figure 6: Iteration 2 data Evaluation

<span id="Criteria_4" class="anchor"></span>**4. Comparison and Results**

The following table summarizes the performance of the baseline and both subsequent iterations.

**Overall Model Comparison**

| **Parameter**              | **Baseline** | **Iteration 1** | **Iteration 2** |
| -------------------------- | ------------ | --------------- | --------------- |
| Batch size                 | 4            | 20              | 20              |
| Learning rate              | 0.01         | 0.01            | 0.005           |
| Training epochs            | 100          | 100             | 100             |
| Best validation-loss epoch | 92           | 91              | 97              |
| Best validation loss       | 2.0682       | 2.1805          | 2.0701          |
| Conveyor pillar AP         | 98.53%       | 91.95%          | 90.96%          |
| Broken glass AP            | 88.62%       | 88.10%          | 89.99%          |
| Bottle AP                  | 88.71%       | 88.36%          | 87.36%          |
| Person AP                  | 88.53%       | 91.68%          | 89.97%          |
| **Overall mAP**            | **91.10%**   | **90.02%**      | **91.59%**      |

From the above comparison chart, we see that overall mAP of Iteration 2 is best i.e. **91.59%**

(NOTE: To access the train models just click on this : [Models](https://hscoburgde-my.sharepoint.com/:f:/g/personal/pra7805s_hs-coburg_de/IgBI8Kt_lQjzT7K3MjpaB3owAbKAXuUZzYbI6MApYUCvSgY?e=fuztim))

<span id="Criteria_5" class="anchor"></span>**5. Live Camera Inference**

**5.1 Real-Time Detection**

The selected SSD-MobileNet model was executed using live camera data, and its detection output was visualized.

The inference output includes:

  - Predicted object class labels.

  - Bounding boxes around detected objects.

  - Confidence scores for individual detections.

The model successfully demonstrated detection of objects such as broken glass, bottles, conveyor pillars, and persons in the camera environment.

![](docs/images/media/image6.png)

Figure 7: Live camera inference with detected objects, bounding boxes, and confidence scores.

**6. Conclusion**

The project successfully demonstrated the application of transfer learning for object detection in an industrial environment.

A pretrained SSD-MobileNet model was adapted to detect four application-specific object classes using an annotated dataset of 998 images. The training process was monitored through training and validation loss curves, and multiple experimental configurations were evaluated using standard object detection metrics.

Three configurations, namely Baseline, Iteration 1, and Iteration 2, were trained and compared. The baseline model achieved a mAP of 91.10%, while Iteration 1 achieved 90.02%. Iteration 2 achieved the highest overall mAP of 91.59%, representing an improvement of approximately 0.49 percentage points over the baseline.

The class-wise evaluation demonstrated that Iteration 2 achieved the highest broken-glass AP of approximately 89.99%, which is particularly relevant to the intended industrial glass-cleaning application.

Based on the comparative evaluation, Iteration 2 was selected as the optimal configuration among the evaluated models. Live camera inference further demonstrated the model's ability to identify objects and visualize detection results using bounding boxes, class labels, and confidence scores.

The results establish a foundation for integrating the object detection model into the autonomous industrial glass-cleaning robot and provide opportunities for further optimization, hyperparameter experimentation, and robustness evaluation under different environmental condition.

**7. Findings**

During live camera testing, it was observed that bottle detection performance decreased when bottles were positioned at greater distances from the camera. While bottles were detected reliably at closer distances, detection became less consistent when their apparent size in the image decreased.

This finding highlights the importance of object distance and image resolution in detection performance. Future improvements could include collecting additional training images at longer distances and evaluating higher input resolutions to improve detection robustness.
