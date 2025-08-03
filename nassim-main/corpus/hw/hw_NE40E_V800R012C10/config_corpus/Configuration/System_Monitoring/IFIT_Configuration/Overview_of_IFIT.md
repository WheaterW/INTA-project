Overview of IFIT
================

Overview of IFIT

#### Definition

In-situ Flow Information Telemetry (IFIT) is an in-band operations, administration and maintenance (OAM) technology that uses service packets to measure performance indicators (such as the packet loss rate and delay) of an IP network.


#### Purpose

In the 5G era, the Enhanced Mobile Broadband (eMBB), ultra-reliable low-latency communication (URLLC), and Massive Machine-Type Communications (mMTC) scenarios pose higher requirements on bearer networks. To meet these requirements in terms of network O&M and performance measurement, 5G networks need the following:

* Effective troubleshooting methods that can improve O&M efficiency, because deterioration of network performance is difficult to diagnose.
* A service flow-based performance measurement mechanism that can accurately reflect actual user traffic in real time. Existing performance measurement mechanisms support only coarse OAM granularities (such as ports, tunnels, and pseudo wires), which is insufficient in the 5G era.
* Functions such as network-wide delay visualization, delay abnormality monitoring, and delay-based routing are needed to improve 5G user experience for delay-sensitive 5G services.

Currently, OAM performance measurement can be classified into out-of-band measurement and in-band measurement by measurement type. Out-of-band measurement includes NQA and TWAMP, and in-band measurement includes IP FPM. These methods have the following advantages and disadvantages:

* NQA can monitor the performance of multiple protocols running on a network. However, it measures the performance using simulated packets (constructed based on the types of measurement instances) rather than real service packets transmitted on the network. As such, the performance indicators collected by NQA may not represent the actual service quality and should be used as reference only.
* TWAMP can insert probe packets into service flows, achieving fast and flexible deployment. However, it sends packets at intervals for measurement, resulting in low-precision measurement results. In addition, TWAMP does not support hop-by-hop measurement.
* IP FPM is also an in-band flow measurement method, but it has high requirements on network devices, applies to limited scenarios, and is complex to deploy.

To address the fact that current OAM detection technologies cannot adequately meet the performance measurement requirements of 5G transport networks, Huawei launches the IFIT in-band flow performance measurement solution with the following highlights:

* Extensibility: IFIT features high measurement precision and easy deployment and can be easily extended in the future.
* Fast fault locating: IFIT provides in-band flow measurement to help measure the delay and packet loss of service flows in real time.
* Visualization: IFIT allows performance data to be presented on a Graphical User Interface (GUI) for quick location of failure points.

#### Benefits

IFIT offers the following benefits:

* Allows customers to monitor the network running status through an NMS and determine whether the network quality complies with Service Level Agreements (SLAs).
* Enables customers to promptly adjust services according to obtained measurement results, thereby ensuring proper transmission of voice and data services and enhancing user experience.