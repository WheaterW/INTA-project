Overview of iNOF
================

Overview of iNOF

#### Definition

Intelligent Lossless NVMe Over Fabrics (iNOF) technology allows a device to quickly manage and control hosts, and applies intelligent lossless network technology to storage systems to implement the convergence of computing and storage networks.


#### Purpose

Forwarding devices on a network transmit various types of traffic that have different network requirements. In the traditional network architecture, three independent networks are deployed to transmit different types of traffic. Typically, a TCP/IP-based Ethernet network transmits user-to-user application traffic that is tolerant of packet loss, delay, and throughput. A low-delay and high-throughput InfiniBand (IB) network transmits computing traffic that requires an extremely low delay. A lossless and high-throughput Fibre Channel (FC) network transmits storage traffic that requires zero packet loss. The deployment and maintenance of the three types of networks are independent of each other.

As more enterprises around the world undergo digital transformation, efficient processing of massive amount of data promotes the rapid development of storage systems. Storage media has evolved from hard disk drives (HDDs) to Non-Volatile Memory express (NVMe) drives, improving the access performance 10,000-fold and greatly reducing the internal latency of storage media, satisfying the requirements of large-scale storage services.

A storage system consists of compute and storage nodes, and requires a network with zero packet loss, low delay, and high throughput. If the traditional network architecture with three independent networks is still used, deployment and maintenance costs are high, and the traditional TCP/IP-based Ethernet network cannot meet the performance requirement of the storage system.

Based on the RDMA over Converged Ethernet version 2 (RoCEv2) protocol, intelligent lossless network technology uses an Intelligent Lossless (iLossless) algorithm that integrates Priority-based Flow Control (PFC) and Artificial Intelligence Explicit Congestion Notification (AI ECN) technologies to implement lossless, low-delay, and high-throughput traffic transmission on an Ethernet network, meeting the requirements of storage systems and implementing the convergence of computing and storage networks.

A storage system that stores large amounts of data usually needs to manage a large number of hosts, and a growing number of new hosts are connected to network devices in the system. To enable intelligent lossless network technology to better serve the storage system, iNOF technology is introduced to quickly manage and control hosts connected to the network. An iNOF-enabled device can detect a new host immediately after it connects to the network, and intelligently adjusts configurations of the intelligent lossless network. Additionally, the device can notify the storage system of host information, and help the storage system manage hosts.