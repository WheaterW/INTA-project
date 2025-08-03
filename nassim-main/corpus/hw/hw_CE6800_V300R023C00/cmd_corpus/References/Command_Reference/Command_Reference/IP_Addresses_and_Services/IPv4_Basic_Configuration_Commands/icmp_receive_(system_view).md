icmp receive (system view)
==========================

icmp receive (system view)

Function
--------



The **icmp receive disable** command disables a device from receiving ICMP packets of a specified type.

The **undo icmp receive disable** command enables a device to receive ICMP packets of a specified type.

The **clear icmp receive** command clears the configurations of the icmp receive disable and undo icmp receive disable commands.



By default, a device is enabled to receive ICMP packets.


Format
------

**icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** | **information-reply** | **information-request** | **net-redirect** | **source-quench** } **receive** **disable**

**icmp name** { **reassembly-timeout** | **host-unreachable** | **host-redirect** } **receive** **disable**

**icmp name** { **net-tos-redirect** | **protocol-unreachable** } **receive** **disable**

**icmp name** { **port-unreachable** | **host-tos-redirect** } **receive** **disable**

**icmp name fragmentneed-dfset receive disable**

**icmp name source-route-failed receive disable**

**icmp name unreachable receive disable**

**icmp type** *typevalue* **code** *codevalue* **receive** **disable**

**clear icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** | **information-reply** | **information-request** | **net-redirect** | **source-quench** } **receive**

**clear icmp name** { **reassembly-timeout** | **host-unreachable** | **host-redirect** } **receive**

**clear icmp name** { **net-tos-redirect** | **protocol-unreachable** } **receive**

**clear icmp name** { **port-unreachable** | **host-tos-redirect** } **receive**

**clear icmp name fragmentneed-dfset receive**

**clear icmp name source-route-failed receive**

**clear icmp name unreachable receive**

**clear icmp type** *typevalue* **code** *codevalue* **receive**

**undo icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** | **information-reply** | **information-request** | **net-redirect** | **source-quench** } **receive** **disable**

**undo icmp name** { **reassembly-timeout** | **host-unreachable** | **host-redirect** } **receive** **disable**

**undo icmp name** { **net-tos-redirect** | **protocol-unreachable** } **receive** **disable**

**undo icmp name** { **port-unreachable** | **host-tos-redirect** } **receive** **disable**

**undo icmp name fragmentneed-dfset receive disable**

**undo icmp name source-route-failed receive disable**

**undo icmp name unreachable receive disable**

**undo icmp type** *typevalue* **code** *codevalue* **receive** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **echo** | Enables the device to receive ICMP Echo packets (type 8; code 0: echo). An ICMP echo packet is sent to the destination host during a ping operation. The destination host responds with an echo reply packet, indicating that the destination is reachable. | - |
| **echo-reply** | Enables the device to receive ICMP Echo Reply packets (type 0; code 0: echo reply). | - |
| **net-unreachable** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 0: net unreachable). | - |
| **parameter-problem** | Enables the device to receive Parameter Problem packets (type 12; code 0: pointer indicates the error). | - |
| **timestamp-reply** | Enables the device to receive Timestamp Reply packets (type 14; code 0: timestamp reply). | - |
| **timestamp-request** | Enables the device to receive Timestamp packets (type 13; code 0: timestamp). | - |
| **ttl-exceeded** | Enables the device to receive ICMP Time Exceeded packets (type 11; code 0: time to live exceeded in transit). | - |
| **information-reply** | Enables the device to receive Information Reply packets (type 16; code 0: information reply). | - |
| **information-request** | Enables the device to receive Information Request packets (type 15; code 0: information request). | - |
| **net-redirect** | Enables the device to receive Redirect packets (type 5; code 0: Redirect datagrams for the Network). | - |
| **source-quench** | Enables the device to receive Source Quench packets (type 4; code 0: source quench). | - |
| **name** | Enables the system to receive ICMP packets with a specified name. | - |
| **reassembly-timeout** | Enables the device to receive Time Exceeded packets (type 11; code 1: fragment reassembly time exceeded). | - |
| **host-unreachable** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 1: host unreachable). | - |
| **host-redirect** | Enables the device to receive Redirect packets (type 5; code 1: Redirect datagrams for the Host). | - |
| **net-tos-redirect** | Enables the device to receive Redirect packets (type 5; code 2: Redirect datagrams for the Type of Service and Network). | - |
| **protocol-unreachable** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 2: protocol unreachable). | - |
| **port-unreachable** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 3: port unreachable). | - |
| **host-tos-redirect** | Enables the device to receive Redirect packets (type 5; code 3: Redirect datagrams for the Type of Service and Host). | - |
| **fragmentneed-dfset** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 4: fragmentation needed and DF set). | - |
| **source-route-failed** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 5: source route failed). | - |
| **unreachable** | Enables the device to receive protocol unreachable packets. | - |
| **type** *typevalue* | Enables the system to receive ICMP packets of a specified type. | The value is an integer that ranges from 0 to 255. You can run the icmp name? command in the system view or interface view to view the mapping between the ICMP packet name and the values of type and code. |
| **code** *codevalue* | Enables the system to receive ICMP packets with a specified message code. | The value is an integer that ranges from 0 to 255. You can run the icmp name? command in the system view or interface view to view the mapping between the ICMP packet name and the values of type and code. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In normal situations, a device can properly receive ICMP packets. In case of heavy network traffic, if hosts or ports are frequently unreachable, routers receive a large number of ICMP packets, which causes heavy traffic burden and performance deterioration. In addition, network attackers often use ICMP error packets to spy on the internal structure of the network.To improve network performance and security, run the **icmp receive disable** command to disable the system from receiving ICMP packets of a specified type.If you want to restore the default configuration and the **display this** command output does not contain the icmp receive or **undo icmp receive** command configuration, run the **clear icmp receive** command.



**Configuration Impact**



After the system is disabled from receiving ICMP packets, the system collects only statistics about discarded packets.



**Precautions**



If the network status is normal and the system is required to receive ICMP packets, run the **undo icmp receive disable** command.The device does not support the processing of information-request and information-reply packets and directly discards them.The **icmp receive** command run in the system view takes effect on all interfaces, whereas the **icmp receive** command run in the interface view takes effect only on the current interface. If the configuration is performed in both the interface view and system view, the configuration in the interface view has a higher priority.




Example
-------

# Restore the function to receive net-unreachable packets.
```
<HUAWEI> system-view
[~HUAWEI] undo icmp name net-unreachable receive disable

```