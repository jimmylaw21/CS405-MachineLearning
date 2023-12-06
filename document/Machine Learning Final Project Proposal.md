# Machine Learning Final Project Proposal - 2023

### Project Proposal Outline: Object Detection and Tracking in SUSTech Campus

### 0. Team Members

- 罗皓予
- 李昱纬
- 莫羡瑜
- 李田

## 1. Background

### Significance of the Project:

Autonomous driving is at the forefront of technological advancements, aiming to revolutionize transportation by minimizing human intervention. Object detection and tracking serve as the eyes of intelligent vehicles, enabling them to perceive and respond to their surroundings. In the context of South University of Science and Technology (SUSTech) campus, the implementation of robust object detection is essential for navigating the unique challenges posed by campus traffic scenarios.

The SUSTech campus, characterized by diverse pedestrian movement, various vehicle types, and intricate road structures, demands a tailored approach to object detection. Traditional models may struggle to adapt to the nuances of campus environments, making it imperative to explore and enhance existing algorithms for more accurate and efficient detection.

### Technological Framework:

Our project is anchored in the utilization of YOLOv8, a cutting-edge algorithm renowned for its real-time object detection capabilities. YOLOv8 stands out due to its ability to process images in a single forward pass, making it highly suitable for applications where low latency is crucial, such as autonomous vehicles. By building upon the YOLOv8 architecture, we aim to customize and optimize the model to excel in the specific challenges presented by SUSTech's dynamic campus setting.

The choice of YOLOv8 is motivated by its versatility and proven success in various computer vision tasks. Leveraging this technology, we seek to contribute to the advancement of autonomous driving within the unique context of a university campus, addressing the need for precise object detection and tracking in dynamic and densely populated environments.

In summary, our project addresses the gap in object detection for autonomous vehicles on the SUSTech campus, leveraging the power of YOLOv8 to provide a solution tailored to the distinctive challenges presented by campus traffic scenarios. This endeavor not only enhances the safety and efficiency of autonomous vehicles within the campus but also contributes valuable insights to the broader field of computer vision and autonomous driving technology.

## 2. Motivations

### Problems to be Solved:

#### 1. **Enhancing Detection Accuracy and Efficiency:**

- Current object detection models may struggle to achieve optimal accuracy in the diverse and dynamic traffic scenarios of the SUSTech campus.
- Improving accuracy is crucial for ensuring the safety of autonomous vehicles, pedestrians, and cyclists navigating the campus.

#### 2. **Addressing Specific Challenges of Campus Traffic Scenarios:**

- SUSTech's campus presents unique challenges, including varying lighting conditions, frequent pedestrian crossings, and a mix of slow-moving and fast-moving vehicles.
- Existing object detection models may not be adequately tuned to handle these specific challenges, necessitating customization for optimal performance.

#### 3. **Applicability of YOLOv8 in Campus Environments:**

- While YOLOv8 has demonstrated success in various scenarios, its performance on university campuses, with a multitude of diverse objects in motion, remains to be thoroughly explored.
- Assessing the adaptability of YOLOv8 to campus-specific challenges is essential for validating its practical utility in these environments.

### Overall Project Motivations:

The motivation behind this project stems from a commitment to advancing the capabilities of autonomous vehicles within the unique context of SUSTech's campus. By addressing the specific challenges outlined above, our project aims to:

- **Improve Safety:** Enhancing detection accuracy ensures the safe interaction of autonomous vehicles with pedestrians, cyclists, and other vehicles on campus, contributing to overall road safety.
- **Optimize Efficiency:** A more efficient object detection model contributes to the real-time decision-making process of autonomous vehicles, leading to smoother traffic flow and reduced response times.
- **Pioneer Campus-Specific Solutions:** Customizing YOLOv8 for SUSTech's campus sets a precedent for tailoring object detection models to the unique characteristics of university environments, potentially influencing similar projects at other institutions.

In essence, the motivations driving this project are rooted in the desire to make autonomous vehicles safer and more effective in navigating complex campus traffic scenarios, while also contributing valuable insights to the broader field of autonomous driving technology.

## 3. Related Work

### Existing Solutions:

#### 1. **Overview of Camera-based 2D Object Detection Methods:**

- **Faster R-CNN:** Faster R-CNN has been a pioneering approach in camera-based 2D object detection. Its use of region proposal networks (RPNs) for generating region proposals has set a benchmark for accuracy.
- **YOLO (You Only Look Once):** YOLO is another widely adopted method, particularly known for its real-time object detection capabilities. Its single forward pass design makes it suitable for applications with low-latency requirements.

#### 2. **Discussion on YOLOv8 and Its Applications:**

- **YOLOv8:** YOLOv8 is an evolution of the YOLO architecture, incorporating improvements in terms of accuracy and speed. Its focus on real-time processing aligns with the requirements of autonomous vehicles.
- **Applications in Similar Contexts:** YOLOv8 has demonstrated success in various contexts, including traffic surveillance and pedestrian detection. However, its performance in university campus scenarios, characterized by diverse and dynamic movements, requires further investigation.

### Room for Improvements:

#### 1. **Limitations in Current Solutions:**

- **Generic Models:** Existing models may not be fine-tuned to the specific challenges posed by university campuses, leading to suboptimal performance.
- **Adaptability to Campus Environments:** Limited exploration of object detection models in campus scenarios may result in overlooked challenges unique to these environments.

#### 2. **Potential for Enhancing Object Detection and Tracking:**

- **Customization for Campus Scenarios:** Adapting existing models, especially YOLOv8, to the nuances of campus traffic scenarios can lead to significant improvements.
- **Incorporating Campus-specific Features:** There is an opportunity to enhance object detection by considering factors such as pedestrian crossings, varying lighting conditions, and the presence of diverse objects in motion on a university campus.

In summary, while Faster R-CNN and YOLO have laid the foundation for camera-based 2D object detection, the specific challenges presented by university campuses, including SUSTech, warrant a more customized approach. Our project aims to build upon these existing solutions, particularly YOLOv8, to create a model optimized for the distinctive characteristics of SUSTech's campus environment.

## 4. Novelty of This Work

### Improvements Over Existing Approaches:

#### 1. **Tailoring YOLOv8 to Campus Traffic Scenarios:**

- *Contextual Adaptations:* Our project involves making nuanced modifications to the YOLOv8 architecture to better align with the specific challenges posed by the SUSTech campus.
- *Optimizing for Diversity:* By understanding and incorporating the unique characteristics of campus traffic, including pedestrian-dense areas and varied lighting conditions, we aim to achieve improved detection accuracy.

#### 2. **Enhancements in Detection Precision and Recall:**

- *Fine-grained Tuning:* We will conduct fine-grained parameter tuning, leveraging insights from the analysis of campus-specific challenges, to enhance both precision and recall in object detection.
- *Mitigating False Positives:* Addressing scenarios such as pedestrian crossings and diverse object interactions to minimize false positives and improve the overall reliability of the detection system.

#### 3. **Real-world Applicability Testing:**

- *Campus-specific Validation:* While YOLOv8 has demonstrated success in various contexts, its performance in campus environments is relatively unexplored. Our project aims to fill this gap by rigorously testing and validating the model within the SUSTech campus setting.
- *Generalization to University Campuses:* The lessons learned from our modifications and experiments can potentially contribute to the development of campus-specific solutions applicable to other university environments.

### Expected Outcomes:

#### 1. **Improved Detection Accuracy:**

- *Quantifiable Metrics:* We anticipate a measurable increase in precision, recall, and overall accuracy compared to the baseline YOLOv8 model.
- *Enhanced Robustness:* The customized model should demonstrate robust performance under varying campus conditions, contributing to the overall reliability of autonomous vehicles.

#### 2. **Efficient Handling of Campus-specific Challenges:**

- *Adaptability:* The model should showcase improved adaptability to scenarios such as crowded pedestrian areas, diverse traffic patterns, and changing lighting conditions.
- *Minimized False Positives:* We aim to reduce false positives associated with specific campus challenges, enhancing the model's practical utility.

#### 3. **Contributions to Campus-Specific Object Detection:**

- *Knowledge Transfer:* Insights gained from this project can serve as a foundation for future projects aiming to enhance object detection on university campuses.
- *Generalizable Lessons:* The methodologies developed and lessons learned can potentially be applied to other university settings with similar challenges.

In conclusion, our work introduces tailored enhancements to the YOLOv8 model, addressing the specific challenges of object detection within the SUSTech campus. The anticipated outcomes include improved accuracy, adaptability, and valuable contributions to the broader field of campus-specific object detection.

## 5. Proposed Method

### System Diagram:

![Proposed System Diagram](https://chat.openai.com/c/URL_TO_YOUR_IMAGE)

#### Key Components:

1. **YOLOv8 Base Model:**
   - Utilizing the YOLOv8 architecture as the foundation for our customizations.
   - Extracting features and predictions in a single forward pass for real-time processing.
2. **Campus-Specific Feature Integration:**
   - Modifying the model to incorporate features relevant to the SUSTech campus environment.
   - Considering pedestrian crossings, campus road structures, and varying lighting conditions.
3. **Fine-grained Parameter Tuning:**
   - Iteratively adjusting model parameters to optimize detection accuracy.
   - Focusing on parameters influencing object recognition thresholds, anchor box sizes, and non-maximum suppression.

## 6. Resources and Experiment Platform

### Data Collection:

#### 1. **Image Source:**

- Utilizing a diverse set of traffic images captured within the SUSTech campus.
- Ensuring images cover various scenarios, including crowded pedestrian areas, vehicle interactions, and different lighting conditions.

#### 2. **Annotation Process:**

- Manually annotating images to create a labeled dataset for training and evaluation.
- Emphasizing precise labeling for objects such as pedestrians, vehicles, and cyclists.

#### 3. **Dataset Augmentation:**

- Introducing variations in scale, rotation, and lighting to enhance model generalization.
- Augmenting the dataset to simulate diverse campus scenarios not captured in the original images.

### Experiment Platform:

#### 1. **Hardware Infrastructure:**

- **GPU Resources:** Employing high-performance GPUs (e.g., NVIDIA Tesla V100) to expedite training and inference processes.
- **Storage:** Utilizing sufficient storage capacity for storing large datasets and model checkpoints.

#### 2. **Software Dependencies:**

- **Deep Learning Framework:** Leveraging PyTorch as the primary deep learning framework for model development and training.
- **YOLOv8 Codebase:** Utilizing the YOLOv8 open-source implementation as the baseline for modifications.
- **Python Libraries:** Employing essential libraries for image processing, data augmentation, and performance evaluation.

#### 3. **Collaboration Tools:**

- Using collaborative platforms such as GitHub for version control and team collaboration.
- Implementing communication channels for real-time collaboration and issue tracking.

### Experimentation Workflow:

#### 1. **Training Phase:**

- Iteratively training the modified YOLOv8 model on the annotated dataset.
- Fine-tuning parameters based on performance analysis and feedback.

#### 2. **Testing and Validation:**

- Conducting extensive testing in simulated and real-world campus scenarios.
- Validating the model's performance against predefined metrics and scenario-based criteria.

#### 3. **Feedback and Iteration:**

- Gathering feedback from testing results and user interactions.
- Iteratively refining the model based on identified areas of improvement.

### Ethical Considerations:

#### 1. **Privacy and Consent:**

- Ensuring ethical data collection practices, obtaining necessary consents, and protecting the privacy of individuals captured in the images.

#### 2. **Bias Mitigation:**

- Regularly evaluating the model for biases and taking steps to mitigate any disparities in object detection accuracy across different demographic groups.

### Risk Assessment:

#### 1. **Model Robustness:**

- Addressing potential challenges related to model robustness in varying weather conditions and unexpected scenarios.
- Implementing safeguards to handle rare or anomalous situations.

#### 2. **Data Quality:**

- Regularly monitoring and maintaining the quality of annotated data to avoid biases and inaccuracies during training.

### Timeline:

#### 1. **Data Collection and Preparation:**

- Duration: 2 weeks
- Tasks: Image collection, manual annotation, dataset augmentation.

#### 2. **Model Development and Training:**

- Duration: 4 weeks
- Tasks: Modifying YOLOv8, fine-tuning parameters, training the model.

#### 3. **Testing and Validation:**

- Duration: 3 weeks
- Tasks: Scenario-based testing, validation against performance metrics.

#### 4. **Feedback and Iterative Refinement:**

- Duration: Ongoing
- Tasks: Continuous feedback collection, model refinement based on results.

### Budgetary Considerations:

#### 1. **Hardware and Cloud Services:**

- Allocating resources for GPU usage and cloud services, if necessary.

#### 2. **Data Annotation:**

- Budgeting for any external resources required for data annotation.

In summary, the outlined resources and experiment platform provide the necessary infrastructure for the successful execution of the project, ensuring ethical practices, risk mitigation, and a well-structured timeline for development, testing, and refinement.

## 7. Goals and Objectives

### Specific Metrics:

#### 1. **Performance Metrics:**

- **Precision:** Achieve a precision rate of at least 90%, minimizing false positives in object detection.
- **Recall:** Attain a recall rate of at least 85%, ensuring comprehensive coverage of true positives.
- **F1 Score:** Target an F1 score exceeding 0.85, balancing precision and recall metrics.

#### 2. **Scenario-based Evaluation:**

- **Pedestrian Crossings:** Aim for 95% accuracy in detecting pedestrians at designated crossings.
- **Low-light Conditions:** Achieve a minimum of 80% accuracy in object detection during low-light scenarios.

### Evaluation Criteria:

#### 1. **Comparative Analysis:**

- Compare the performance of the customized YOLOv8 model against the baseline YOLOv8 in campus-specific scenarios.
- Assess improvements in accuracy, efficiency, and adaptability to diverse campus environments.

#### 2. **User Feedback:**

- Solicit feedback from stakeholders, including potential end-users, to gauge the model's usability and practicality.
- Prioritize user experience and address any identified pain points through iterative refinement.

### Success Criteria:

#### 1. **Model Accuracy:**

- Consider the project a success if the customized YOLOv8 model achieves a minimum 10% improvement in accuracy over the baseline in campus-specific scenarios.

#### 2. **Real-world Applicability:**

- Validate the success of the project by demonstrating the model's robust performance in real-world campus traffic situations.
- Ensure the model generalizes well to diverse conditions, showcasing its applicability beyond controlled testing scenarios.

### Milestones:

#### 1. **Model Development:**

- Milestone 1: Complete modification and fine-tuning of YOLOv8 architecture.
- Milestone 2: Achieve satisfactory performance on the validation set.

#### 2. **Testing and Validation:**

- Milestone 3: Successfully complete scenario-based testing on the SUSTech campus.
- Milestone 4: Attain positive feedback from initial user testing.

#### 3. **Refinement and Iteration:**

- Milestone 5: Implement necessary model refinements based on user feedback and identified issues.
- Milestone 6: Achieve a stable and optimized model ready for deployment.

### Acceptance Criteria:

#### 1. **Model Accuracy:**

- Accept the model if it meets or exceeds the defined precision, recall, and F1 score metrics.

#### 2. **User Feedback:**

- Accept the project if user feedback indicates satisfactory usability and reliability in real-world campus scenarios.

### Project Significance:

#### 1. **Contribution to Autonomous Vehicles:**

- Establish the significance of the project by highlighting its potential impact on enhancing object detection for autonomous vehicles within campus environments.

#### 2. **Academic and Research Contribution:**

- Emphasize the project's contribution to the academic community by potentially setting a precedent for campus-specific object detection methodologies.

### Risk Mitigation Strategy:

#### 1. **Continuous Monitoring:**

- Regularly monitor project progress and identify potential risks during each phase.
- Implement corrective measures promptly to avoid significant setbacks.

#### 2. **User Feedback Integration:**

- Actively seek and integrate user feedback throughout the development process to identify issues early and ensure user satisfaction.

In conclusion, the goals and objectives are structured around specific metrics, evaluation criteria, success criteria, milestones, and acceptance criteria. The project's significance is emphasized in its potential impact on autonomous vehicles and contributions to academic research. A proactive risk mitigation strategy is outlined to ensure the project's successful execution.

## 8. Task Assignments and Project Schedule

### Team Roles:

#### 1. **Project Manager (PM):**

- Responsibilities:
  - Oversee the overall project timeline and progress.
  - Coordinate communication and collaboration within the team.
  - Ensure tasks are completed on schedule.

#### 2. **Machine Learning Engineer (MLE):**

- Responsibilities:
  - Lead the modification and fine-tuning of the YOLOv8 architecture.
  - Conduct training and testing of the model on the SUSTech campus dataset.
  - Iterate on the model based on performance analysis.

#### 3. **Data Scientist (DS):**

- Responsibilities:
  - Manage the data collection process, ensuring diverse and representative images from the SUSTech campus.
  - Perform manual annotation of images and oversee dataset augmentation.
  - Collaborate with MLE to ensure the dataset meets model requirements.

#### 4. **User Experience (UX) Specialist:**

- Responsibilities:
  - Gather user feedback during testing and validation phases.
  - Collaborate with MLE to understand user pain points and areas for improvement.
  - Assist in refining the model based on user-centric insights.

### Project Schedule:

#### Week 1-2: Preparation and Setup

1. **PM:**
   - Set up project management tools and communication channels.
   - Establish a clear communication plan and schedule regular team meetings.
2. **DS:**
   - Initiate data collection from the SUSTech campus.
   - Begin manual annotation of collected images.

#### Week 3-4: Model Development and Training

1. **MLE:**
   - Modify and fine-tune the YOLOv8 architecture for campus-specific scenarios.
   - Begin training the model on the annotated dataset.
2. **DS:**
   - Continue data annotation and augmentation to ensure a comprehensive dataset.

#### Week 5-6: Testing and Validation

1. **MLE:**
   - Conduct scenario-based testing on the SUSTech campus.
   - Evaluate the model's performance against defined metrics.
2. **UX Specialist:**
   - Gather user feedback during testing.
   - Document user interactions and pain points for further analysis.

#### Week 7-8: Iterative Refinement

1. **MLE and UX Specialist:**
   - Collaborate on refining the model based on testing feedback.
   - Implement necessary adjustments to improve user satisfaction.
2. **PM:**
   - Monitor progress and address any challenges or roadblocks.
   - Ensure the project stays on schedule.

#### Week 9-10: Final Testing and Optimization

1. **MLE:**
   - Perform final testing on the optimized model.
   - Optimize parameters for efficiency and accuracy.
2. **UX Specialist:**

- Conduct a final round of user testing to validate model improvements.

#### Week 11-12: Project Finalization

1. **PM:**

- Compile project documentation and results.
- Ensure all project objectives and metrics are met.

1. **All Team Members:**

- Prepare a final presentation and report on the project.
- Share insights and lessons learned.

### Task Dependencies:

- **Continuous Collaboration:**
  - All team members collaborate throughout the project to address any dependencies or issues promptly.
- **Feedback Loop:**
  - MLE and UX Specialist work closely to ensure iterative refinement based on user feedback.
- **Data Availability:**
  - MLE's progress depends on the availability and quality of annotated data provided by the DS.

### Contingency Plan:

- **Flexibility in Schedule:**
  - Allocate extra time in the schedule for unforeseen challenges or additional refinement iterations.
- **Task Redistribution:**
  - If one team member faces unexpected challenges, redistribute tasks among the team to maintain progress.
- **Communication Protocol:**
  - Establish clear communication channels for quick issue resolution and decision-making.

In summary, the project schedule outlines a month-long plan with specific tasks assigned to each team member. Regular communication, collaboration, and flexibility in the schedule contribute to the successful execution of the project.