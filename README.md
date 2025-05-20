# YOLOGESTURE - 智能手势识别系统

## 项目摘要

手势识别作为人类与机器交互的核心技术之一，它在无人安全技术、助力无障碍交互等多端的应用价值不断提高。而针对现有方法存在的实时性不足、难以检测小目标乃至多重小目标、交互功能单一等问题，本文设计并实现了一种融合深度学习与可视化交互的智能手势识别系统。

在算法架构层面，本文提出一分为三的改进：

1. 基于YOLOV11的路径聚合特征金字塔网络（PAFPN）进行结构优化，实现多尺度细节强化架构Multi-Scale Minutiae Amplification Architecture(MSMA)的构建。通过SPDConv模块处理P2特征层提取细粒度特征，并与P3层进行跨尺度融合，同时将跨阶段局部网络思想（CSP）与AAAI2024提出的全维度卷积核（OmniKernel）相结合以改进得到的CSP-OmniKernel进行特征整合，以实现小目标检测任务检测准度的提高。

2. 采用CVPR2025最新提出的OverLock模块（三分支纯卷积结构）中的BackBone重构骨干网络来动态扩大感受野，增强上下信息获取能力，在保持精准度的同时进一步增强对小目标及多重小目标的检测能力。

3. 并使用改进的轻量化检测头LSCD，通过组合GN与无归一化策略并引入scale因子将计算复杂度降低，同时保持较高的检测精度。

而系统方面则实现了以下功能：

1. 多元流实时分析：支持本地/网络摄像头（RTSP/HTTP协议）多源输入，具备置信度/IoU阈值动态调节、热力图可视化及双模型性能对比功能。

2. 智能批处理模块：可批量解析图像/视频流数据，生成手势类别占比图，数量统计图。

3. 可扩展控制平台：集成可调检测框线宽、模型热插拔、结果保存功能，通过pysqlcipher3加密SQLite数据库实现用户权限管理及个性化配置存储。

4. AI辅助决策：搭载Deepseek专业问答引擎，提供实时技术决策支持。

**关键词**：YOLOV11；多尺度细节强化架构；OverLock-Backbone；改进轻量化检测头；python实时交互系统

## 英文翻译 (English Translation)

Gesture recognition, as one of the core technologies for human-machine interaction, continues to increase in value across multiple applications such as unmanned security technology and accessibility interaction. Addressing the limitations of existing methods—insufficient real-time performance, difficulty in detecting small and multiple small targets, and limited interaction functionality—this paper designs and implements an intelligent gesture recognition system that integrates deep learning with visual interaction.

At the algorithmic architecture level, this paper proposes three improvements:

1. Based on YOLOV11's Path Aggregation Feature Pyramid Network (PAFPN), the structure is optimized to build a Multi-Scale Minutiae Amplification Architecture (MSMA). By processing the P2 feature layer with the SPDConv module to extract fine-grained features and performing cross-scale fusion with the P3 layer, while combining the Cross-Stage Partial Network (CSP) concept with the OmniKernel proposed at AAAI2024 to develop CSP-OmniKernel for feature integration, the system achieves improved detection accuracy for small target detection tasks.

2. Using the OverLock module (a three-branch pure convolutional structure) newly proposed at CVPR2025, the backbone network is reconstructed to dynamically expand the receptive field and enhance the ability to capture contextual information, further improving the detection capabilities for small and multiple small targets while maintaining precision.

3. Using an improved lightweight detection head LSCD, which reduces computational complexity by combining Group Normalization (GN) with a non-normalization strategy and introducing scale factors, while maintaining high detection accuracy.

The system implements the following functions:

1. Multi-source real-time analysis: Supports multiple input sources including local/network cameras (RTSP/HTTP protocols), features dynamic adjustment of confidence/IoU thresholds, heatmap visualization, and dual-model performance comparison.

2. Intelligent batch processing module: Capable of batch analyzing image/video stream data, generating gesture category proportion charts and quantity statistics charts.

3. Extensible control platform: Integrates adjustable detection box line width, hot-swappable models, result saving functionality, and user permission management and personalized configuration storage through pysqlcipher3-encrypted SQLite database.

4. AI-assisted decision making: Equipped with the Deepseek professional Q&A engine to provide real-time technical decision support.

**Keywords**: YOLOV11; Multi-Scale Minutiae Amplification Architecture; OverLock-Backbone; Improved Lightweight Detection Head; Python Real-time Interactive System

## 系统功能

待完善...

## 安装与使用

待完善...

## 项目结构

待完善...

## 开发团队

待完善...

## 许可证

待完善... 