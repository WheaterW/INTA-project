icmp send (system view)
=======================

icmp send (system view)

Function
--------



The **icmp send disable** command disables a device from sending ICMP packets.

The **undo icmp send disable** command enables a device to send ICMP packets.

The **clear icmp send** command clears the configurations of the icmp send disable and undo icmp send disable commands.



By default, the function of sending timestamp-reply packets, parameter-problem packets, reassembly-timeout packets, and source-route-failed packets is disabled, and the function of sending other types of ICMP packets is enabled.


Format
------

**icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** } **send** **disable**

**icmp name reassembly-timeout send disable**

**icmp name port-unreachable send disable**

**icmp name fragmentneed-dfset send disable**

**icmp name source-route-failed send disable**

**icmp type** *typevalue* **code** *codevalue* **send** **disable**

**clear icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** } **send**

**clear icmp name reassembly-timeout send**

**clear icmp name port-unreachable send**

**clear icmp name fragmentneed-dfset send**

**clear icmp name source-route-failed send**

**clear icmp type** *typevalue* **code** *codevalue* **send**

**undo icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** } **send** **disable**

**undo icmp name reassembly-timeout send disable**

**undo icmp name port-unreachable send disable**

**undo icmp name fragmentneed-dfset send disable**

**undo icmp name source-route-failed send disable**

**undo icmp type** *typevalue* **code** *codevalue* **send** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **echo** | Enables the device to send ICMP Echo packets. An ICMP Echo packet is sent to the destination host during a ping operation. The destination host responds with an ICMP Echo Reply packet, indicating that the destination is reachable. | - |
| **echo-reply** | Enables the device to send ICMP Echo Reply packets. | - |
| **net-unreachable** | Enables the device to send net-unreachable packets. | - |
| **parameter-problem** | Enables the device to send parameter-problem packets. | - |
| **timestamp-reply** | Enables the device to send Timestamp Reply packets. | - |
| **timestamp-request** | Enables the device to send Timestamp Request packets. | - |
| **ttl-exceeded** | Enables the device to send ICMP TTL Exceeded packets. | - |
| **name** | Enables the system to send ICMP packets with a name. | - |
| **reassembly-timeout** | Enables the system to send reassembly-timeout packets. | - |
| **port-unreachable** | Enables the device to send ICMP port-unreachable packets. | - |
| **fragmentneed-dfset** | Enables the device to send fragmentneed-DFset packets. | - |
| **source-route-failed** | Enables the device to send source-route-failed packets. | - |
| **type** *typevalue* | Enables the system to send ICMP packets with a specified type. | type: The value is an integer ranging from 0 to 255. You can run the icmp name ? command in the system view or interface view to view the mappings between the ICMP packet name, type, and code. |
| **code** *codevalue* | Enables the system to send ICMP packets with a specified code. | code: The value is an integer ranging from 0 to 255. You can run the icmp name ? command in the system view or interface view to view the mappings between the ICMP packet name, type, and code. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In normal situations, a device can properly send ICMP packets. In case of heavy network traffic, if hosts or ports are frequently unreachable, devices send a large number of ICMP packets, which causes heavy traffic burden and performance deterioration. In addition, network attackers often use ICMP error packets to spy on the internal structure of the network.To improve network performance and security, run the **icmp send disable** command to disable the system from sending ICMP packets of a specified type.If you want to restore the default configuration and the **display this** command output does not contain the icmp send disable or **undo icmp send disable** command configuration, run the **clear icmp send** command.



**Configuration Impact**



After the system is disabled from sending ICMP packets, the system collects only statistics about discarded packets.



**Precautions**



If the network status is normal and the system is required to send ICMP packets, run the **undo icmp send disable** command.In the case of network unreachable and host unreachable, the standard protocol does not require that the routing device must reply with a host unreachable packet. Currently, the device can reply with a network unreachable packet when it receives a packet and fails to query the routing table.In FIB Miss scenarios, the device does not respond to network unreachable packets by default. In ARP Miss scenarios, the device cannot respond to network unreachable packets and triggers ARP learning.




Example
-------

# Enable a device to send ICMP Echo packets.
```
<HUAWEI> system-view
[~HUAWEI] undo icmp name echo send disable

```