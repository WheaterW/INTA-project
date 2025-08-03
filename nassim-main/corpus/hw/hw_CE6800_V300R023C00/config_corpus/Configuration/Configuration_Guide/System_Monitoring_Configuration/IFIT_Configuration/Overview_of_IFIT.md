Overview of IFIT
================

Overview of IFIT

#### Definition

In-situ Flow Information Telemetry (IFIT) is an in-band Operations, Administration, and Maintenance (OAM) measurement technology that uses service packets to measure real performance indicators of an IP network, such as the packet loss rate and delay. IFIT can significantly improve the timeliness and effectiveness of network O&M, thereby promoting the development of intelligent O&M.


#### Purpose

In the cloud era, the services and architecture of IP networks have changed greatly. For one thing, the development has given rise to new services, such as HD video, virtual reality (VR), and Internet of Vehicles (IoV). For another, cloudification of network devices and services has become a common choice for facilitating unified management and reducing O&M costs. New services and architectures pose many challenges to bearer networks, including ultra-bandwidth, hyperconnectivity, low delay, and high reliability. Traditional network O&M methods cannot meet high reliability requirements of new services and architectures. Currently, most OAM technologies are out-of-band measurement technologies that indirectly simulate service data packets and periodically send packets to implement performance measurement for end-to-end paths. A typical out-of-band OAM technology is Network Quality Analysis (NQA), which measures the performance of constructed simulated service packets but provides inaccurate performance indicators.

Under such circumstances, Huawei proposed IFIT to meet the increasingly stringent Service Level Agreement (SLA) requirements of network services and address the challenges facing network O&M in the cloud era. IFIT â an Internet Engineering Task Force (IETF) standardized protocol â is the industry's first complete in-band quality awareness and fault locating solution. IFIT is an in-band measurement technology. It marks characteristics of real service packets or adds measurement information to real service packets to implement performance measurement for real service flows. IFIT has the following advantages:

* Fast fault locating: IFIT provides in-band measurement capabilities to monitor indicators such as the delay and packet loss rate of service flows in real time.
* Visualization: IFIT provides visualized O&M capabilities to centrally manage and control networks and graphically display performance data.
* Scalability: IFIT has high measurement precision and is easy to deploy. It helps construct an intelligent O&M system and has future-oriented scalability.

#### Benefits

* You can use the NMS to monitor the network running status and check whether the network quality complies with the SLA signed with users.
* You can adjust services in a timely manner based on the measurement result to ensure normal transmission of high-demand services such as voice and video services, improving user experience.