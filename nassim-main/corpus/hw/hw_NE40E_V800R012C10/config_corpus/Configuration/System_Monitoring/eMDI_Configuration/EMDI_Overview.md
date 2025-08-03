EMDI Overview
=============

Enhanced Media Delivery Index (eMDI) is an end-to-end method for detecting specified multicast video service packets on each node of an IP network. This enables you to obtain performance indicators such as the packet loss rate, disorder rate, and jitter. eMDI is easy to deploy, applies to all NEs, and provides high statistical precision.

#### Background

As multicast video services, such as IPTV, become more commonplace on carrier networks and become an important source of revenue for carriers, monitoring the quality of videos becomes more and more important. Packet loss, jitter, and disorder are major factors that affect video quality. A packet loss rate and disorder rate of less than 0.01% may result in artifacts, pixelation, and similar problems occurring on a terminal, and jitter may cause the terminal to display a black screen. These problems negatively affect the quality of experience (QoE) of services, and in turn affect carriers' revenue and reputation. Carriers therefore urgently need a video quality monitoring and fault locating solution that monitors and maintains service quality in real time and quickly demarcates faults and clarifies responsibilities.

The eMDI solution is a quality monitoring and fault locating solution designed for multicast video streams such as IPTV. It can monitor quality indicators such as the packet loss rate, packet disorder rate, and jitter of real service packets in real time and provides precise statistics and reliable data. The solution can be deployed on each network node from the edge device to the core device. The detection results of multiple nodes can be used to quickly locate faulty network segments.


#### Detection Principles

The eMDI detection solution is a distributed board detection solution. It supports distributed detection for video streams of a specified multicast channel on a specified board.

This solution supports detection only of UDP-based RTP video streams. The NP of the board to be detected performs a validity check and an RTP check on the IP header, UDP header, and RTP header of RTP packets and calculates the packet loss rate and packet disorder rate based on the sequence number in the RTP header. The NP then calculates jitter based on the timestamp in the RTP header. This makes it possible to monitor video quality in real time.

The implementation process of eMDI detection is as follows:

1. The NMS delivers eMDI monitoring instructions to a device.
2. The device monitors eMDI indicators in real time.
3. The device periodically reports the monitored eMDI indicators and alarms to the NMS.
4. The NMS displays eMDI indicators on its GUI and supports segment-based fault demarcation and analysis.

**Figure 1** eMDI detection solution deployment
  
![](images/fig_dc_ne_feature_emdi_000301.png "Click to enlarge")  



#### Indicator Collection

eMDI can obtain monitoring data from a device on a regular basis and periodically send the data to the NMS using various methods, such as telemetry. After analysis is performed on the NMS, the monitoring data can be displayed in various forms, such as a trend chart.

eMDI also supports reporting of alarms to the NMS. The alarm thresholds and the number of times that alarms are suppressed can be configured as required.


#### Indicators

The detection indicators supported by eMDI include the packet loss rate (RTP-LR), packet out-of-order rate (RTP-SER), and jitter. The packet loss rate and packet out-of-order rate are calculated based on the sequence number in an RTP packet header. The jitter is calculated based on the timestamp in an RTP packet header. For details, see [[**eMDI Detection Indicators**](cmdqueryname=eMDI+Detection+Indicators)](dc_ne_feature_emdi_0004.html).