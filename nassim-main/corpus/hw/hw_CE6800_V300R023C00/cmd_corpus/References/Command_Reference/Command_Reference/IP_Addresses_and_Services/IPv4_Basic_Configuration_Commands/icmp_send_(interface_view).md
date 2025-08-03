icmp send (interface view)
==========================

icmp send (interface view)

Function
--------



The **icmp send enable** command enables an interface to send ICMP packets.

The **undo icmp send enable** command restores the default setting.

The **icmp send disable** command disables an interface from sending ICMP packets.

The **undo icmp send disable** command restores the default setting.



By default, the system sends ICMP packets.

By default, an interface's ICMP packet sending capability is determined by the system's ICMP packet sending capability.


Format
------

**icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** } **send** **disable**

**icmp name reassembly-timeout send disable**

**icmp name reassembly-timeout send enable**

**icmp name port-unreachable send disable**

**icmp name port-unreachable send enable**

**icmp name fragmentneed-dfset send disable**

**icmp name fragmentneed-dfset send enable**

**icmp name source-route-failed send disable**

**icmp name source-route-failed send enable**

**icmp type** *typevalue* **code** *codevalue* **send** **disable**

**icmp type** *typevalue* **code** *codevalue* **send** **enable**

**icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** } **send** **enable**

**undo icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** } **send** { **disable** | **enable** }

**undo icmp name reassembly-timeout send** { **disable** | **enable** }

**undo icmp name port-unreachable send** { **disable** | **enable** }

**undo icmp name fragmentneed-dfset send** { **disable** | **enable** }

**undo icmp name source-route-failed send** { **disable** | **enable** }

**undo icmp type** *typevalue* **code** *codevalue* **send** { **disable** | **enable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **echo** | Enables the device to send ICMP echo request packets. | - |
| **echo-reply** | Enables the device to send ICMP echo reply packets. | - |
| **net-unreachable** | Enables the device to send net-unreachable packets. | - |
| **parameter-problem** | Enables the device to send parameter-problem packets. | - |
| **timestamp-reply** | Enables the device to send Timestamp Reply packets. | - |
| **timestamp-request** | Enables the device to send Timestamp Request packets. | - |
| **ttl-exceeded** | Enables the device to send ICMP TTL Exceeded packets. | - |
| **name** | Enables the device to receive ICMP packets with a specified name. | - |
| **reassembly-timeout** | Enables the device to send reassembly-timeout packets. | - |
| **port-unreachable** | Enables the device to send ICMP port-unreachable packets. | - |
| **fragmentneed-dfset** | Enables the device to send fragmentneed-DFset packets. | - |
| **source-route-failed** | Enables the device to send source-route-failed packets. | - |
| **type** *typevalue* | Enables the system to send ICMP packets with a specified type. | The value is an integer ranging from 0 to 255. |
| **code** *codevalue* | Enables the system to send ICMP packets with a specified code. | The value is an integer ranging from 0 to 255. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In normal situations, the router can correctly send ICMP packets. In the case of heavy network traffic, if hosts or ports are frequently unreachable, the router sends a large number of ICMP packets, which causes heavier traffic burden and performance deterioration. In addition, network attackers often make use of ICMP error packets to probe the internal network structure. To improve network performance and enhance network security, run the **icmp send disable** command to disable an interface from sending ICMP packets to prevent attacks that make use of ICMP packets.If an interface is required to send ICMP packets, run the **icmp send enable** command.To run the **icmp send enable** command in the view of an interface, the interface must be the outbound interface of a route that sends an error response.


Example
-------

# Enable an interface to send Timestamp Request messages.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 100
[*HUAWEI-Vlanif100] icmp name timestamp-request send enable

```