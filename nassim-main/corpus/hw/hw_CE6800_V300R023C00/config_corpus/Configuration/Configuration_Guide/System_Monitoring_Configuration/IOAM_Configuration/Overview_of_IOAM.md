Overview of IOAM
================

Overview of IOAM

#### Definition

In-band Operations, Administration, and Maintenance (IOAM) is a technology that measures and monitors networks. It enables devices to sample real-time service traffic at a high speed, add IOAM information to the sampled traffic, and proactively send the collected data to an analyzer. This enables real-time awareness and monitoring of the network running status.

![](public_sys-resources/note_3.0-en-us.png) 

The device supports the IOAM function, which is used to monitor the network running status and may involve obtaining personal data such as IP address and MAC address. Huawei will not collect or store users' communication information without prior user approval. Therefore, you must use this function in compliance with the local laws and regulations, and take proper security protection measures to ensure that personal data of users is fully protected. For example, technical support engineers must not use this function to obtain packets unless they have been authorized by customers. Ensure obtained packets are deleted completely and immediately after the fault is located and analyzed. Huawei will not bear any legal responsibility or liabilities for any security events (such as personal data leakage) that are not the result of Huawei's misconduct.



#### Purpose

The continuous growth of users and Internet services is driving networks to become large-scale, high-speed, multi-access, and unpredictable. This raises the requirements on network management and control.

Network measurement is the basic means and data source of network management and control. Common network measurement methods are classified into three types: proactive, passive, and hybrid. Although proactive measurement methods such as ping and traceroute are flexible to use, they increase the bandwidth and processing overhead of the network. Passive measurement methods, including Internet Protocol Flow Information Export (IPFIX), do not generate extra measurement load, but cannot obtain network-wide information, such as the network status and packet loss rate. Hybrid measurement combines the advantages of proactive and passive measurement modes. A typical example of this type of measurement that has emerged in recent years is IOAM technology. This technology enables forwarding nodes to add metadata (MD) into data packets to collect information about the network status. This, in turn, enables the network running status to be monitored in real time, allows faulty nodes to be located quickly and accurately, improves network stability, and reduces network maintenance costs.


#### Benefits

* Routine network maintenance: IOAM information about network nodes is added into the original packets to provide real-time network monitoring capabilities without increasing network bandwidth consumption. This helps monitor the network health status in real time and meets the routine O&M monitoring requirements.
* Fast network troubleshooting and fault locating: Fast and accurate fault locating capabilities help quickly locate network connectivity faults and monitor the connectivity of the entire network, reducing O&M costs.