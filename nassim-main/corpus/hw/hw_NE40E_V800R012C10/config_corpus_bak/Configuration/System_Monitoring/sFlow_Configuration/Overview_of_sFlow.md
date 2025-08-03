Overview of sFlow
=================

Overview_of_sFlow

#### Definition

Sampled Flow (sFlow) is a traffic monitoring technology that collects and analyzes traffic statistics based on packet sampling.


#### Purpose

Enterprise networks are generally smaller and more flexible than carrier networks. However, they are often prone to attacks and service exceptions. To help ensure network stability, enterprises require a traffic monitoring technique that can promptly identify traffic anomalies and the source of attack traffic, allowing them to quickly rectify faults.

sFlow is developed to meet the preceding requirement. sFlow is an interface-based traffic analysis technique that collects packets on an interface based on the sampling rate. In flow sampling, an sFlow agent analyzes the packets including the packet content and forwarding rule, and encapsulates the original packets and parsing result into sFlow packets. The sFlow agent then sends the sFlow packets to an sFlow collector. In counter sampling, an sFlow agent periodically collects traffic statistics on an interface, CPU usage, and memory usage.

sFlow focuses on traffic on an interface, traffic forwarding, and device running. Therefore, sFlow can be used to monitor and diagnose network exceptions. The sFlow collector displays traffic statistics in a report, facilitating preventive maintenance on enterprise networks, especially for enterprises that do not have specialized network administrators.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, devices support only flow sampling.



#### Benefits

sFlow is comparable to NetStream. In NetStream, network devices collect and analyze traffic statistics. The devices save these statistics to a buffer and export them when they expire or when the buffer overflows. sFlow does not require a flow table. In sFlow, network devices only sample packets, and a remote collector collects and analyzes traffic statistics.

sFlow has the following advantages over NetStream:

* Fewer resources and lower costs. sFlow requires no flow table and uses only a small number of network devices, lowering costs.
* Flexible collector deployment. The collector can be deployed flexibly, enabling traffic statistics to be collected and analyzed according to various traffic characteristics.