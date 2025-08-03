Overview of 1588v2
==================

Overview of 1588v2

#### Definition

IEEE 1588, also called Precision Time Protocol (PTP), is the IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems.

Two versions of the IEEE 1588 standard exist: 1588v1, which provides clock accuracy in the sub-millisecond range, and 1588v2, which achieves clock accuracy in the sub-microsecond range. 1588v2 is defined as a time synchronization protocol that supports both high-precision time synchronization and frequency synchronization.

As 1588v1 has been basically replaced by 1588v2, PTP in this document refers to 1588v2 unless otherwise specified.


#### Purpose

As networks continue to develop, network devices require more accurate time to meet customers' high-precision time requirements in services such as network delay measurement, O&M problem analysis, and distributed computing.

A number of methods, such as the global positioning system (GPS), Network Time Protocol (NTP), and synchronous Ethernet (SyncE), can be used to implement time and frequency synchronization for network devices. However, GPS requires antenna installation on each device, increasing the construction and maintenance costs; NTP achieves only sub-second-level time synchronization precision, which does not meet the precision requirements of devices; SyncE supports only frequency synchronization.

1588v2 can achieve time synchronization accuracy in the sub-microsecond range by means of hardware-assisted processing, while also offering a lower cost and less dependency on GPS.