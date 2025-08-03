Overview of Packet Capture
==========================

Overview of Packet Capture

#### Definition

The packet capture function enables a device to obtain received packets and save or display the packets in a specific format, enabling maintenance personnel to efficiently locate network faults.

![](public_sys-resources/note_3.0-en-us.png) 

The device supports the packet capture function, which is used to detect transmission faults and errors. Huawei is unable to collect or store user communication information without permission. You are responsible for complying with applicable laws and regulations when enabling related functions used to collect or store user communication information. During user communication information collection and storage, proper measures must be taken to protect user communication information.



#### Purpose

Troubleshooting on a network is complex and increases in difficulty if the network carries a variety of services. Maintenance personnel often need to obtain packets to analyze the root causes of faults. The packet capture function provides an efficient approach for locating faults on a network without the need to deploy packet analysis devices and network monitoring devices, greatly improving maintenance efficiency and reducing maintenance costs.

After the packet capture function is enabled, the device obtains packets that match the specified filter rules. The obtained packet content can be displayed in hexadecimal format on a terminal or saved to a .cap file on the device. Maintenance personnel can download the file to a local PC and use tools such as Wireshark to view the packet information.

Currently, the device can obtain the following types of packets:

* Forwarded packets: If the device fails to forward traffic correctly (for example, the forwarded traffic does not match the traffic model), you can configure the device to obtain forwarded packets for analysis.
* Protocol packets sent to the CPU: If the CPU on a device is not running as normal (for example, encountering a high CPU usage), you can configure the device to obtain protocol packets sent to the CPU for analysis.