Overview of NTP
===============

Overview of NTP

#### Definition

Network Time Protocol (NTP) is an application layer protocol in the TCP/IP protocol suite. It is used to synchronize clocks between a series of distributed time servers and clients.


#### Purpose

NTP is used to synchronize the time of all clock devices on a network. If time is not synchronized on a network, time errors may occur because devices run their own clocks. NTP synchronizes the time on all devices, enabling them to provide various applications based on consistent time.

NTP is mainly used in the following scenarios where the clocks of all network devices must be consistent:

* Network management: Synchronized time is used as a reference when a network management system (NMS) analyzes the logs and debugging information collected from different devices.
* Charging system: Synchronized time is required to ensure the accuracy and trustworthiness of charging information.
* Several systems interworking on the same complex event: The systems must use the same clock for reference to ensure proper sequencing of operations.
* Incremental backup between the backup server and client: Synchronized time ensures integrity of the backup data which can be used for production system recovery.