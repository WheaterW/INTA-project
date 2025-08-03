icmp receive (interface view)
=============================

icmp receive (interface view)

Function
--------



The **icmp receive enable** command enables an interface to receive ICMP packets.

The **undo icmp receive enable** command restores the default setting.

The **icmp receive disable** command disables an interface from receiving ICMP packets.

The **undo icmp receive disable** command restores the default setting.



By default, the system is enabled to receive ICMP packets.

By default, an interface's ICMP packet receiving capability is determined by the system's ICMP packet receiving capability.


Format
------

**icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** | **information-reply** | **information-request** | **net-redirect** | **source-quench** } **receive** **disable**

**icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** | **information-reply** | **information-request** | **net-redirect** | **source-quench** } **receive** **enable**

**icmp name** { **reassembly-timeout** | **host-unreachable** | **host-redirect** } **receive** **disable**

**icmp name** { **reassembly-timeout** | **host-unreachable** | **host-redirect** } **receive** **enable**

**icmp name** { **net-tos-redirect** | **protocol-unreachable** } **receive** **disable**

**icmp name** { **net-tos-redirect** | **protocol-unreachable** } **receive** **enable**

**icmp name** { **port-unreachable** | **host-tos-redirect** } **receive** **disable**

**icmp name** { **port-unreachable** | **host-tos-redirect** } **receive** **enable**

**icmp name fragmentneed-dfset receive disable**

**icmp name fragmentneed-dfset receive enable**

**icmp name source-route-failed receive disable**

**icmp name source-route-failed receive enable**

**icmp name redirect receive enable**

**icmp type** *typevalue* **code** *codevalue* **receive** **disable**

**icmp type** *typevalue* **code** *codevalue* **receive** **enable**

**icmp name redirect receive disable**

**undo icmp name** { **echo** | **echo-reply** | **net-unreachable** | **parameter-problem** | **timestamp-reply** | **timestamp-request** | **ttl-exceeded** | **information-reply** | **information-request** | **net-redirect** | **source-quench** } **receive** { **disable** | **enable** }

**undo icmp name** { **reassembly-timeout** | **host-unreachable** | **host-redirect** } **receive** { **disable** | **enable** }

**undo icmp name** { **net-tos-redirect** | **protocol-unreachable** } **receive** { **disable** | **enable** }

**undo icmp name** { **port-unreachable** | **host-tos-redirect** } **receive** { **disable** | **enable** }

**undo icmp name fragmentneed-dfset receive** { **disable** | **enable** }

**undo icmp name source-route-failed receive** { **disable** | **enable** }

**undo icmp name redirect receive** { **disable** | **enable** }

**undo icmp type** *typevalue* **code** *codevalue* **receive** { **disable** | **enable** }


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
| **name** | Enables the device to receive ICMP packets with a specified name. | - |
| **reassembly-timeout** | Enables the device to receive Time Exceeded packets (type 11; code 1: fragment reassembly time exceeded). | - |
| **host-unreachable** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 1: host unreachable). | - |
| **host-redirect** | Enables the device to receive Redirect packets (type 5; code 1: Redirect datagrams for the Host). | - |
| **net-tos-redirect** | Enables the device to receive Redirect packets (type 5; code 2: Redirect datagrams for the Type of Service and Network). | - |
| **protocol-unreachable** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 2: protocol unreachable). | - |
| **port-unreachable** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 3: port unreachable). | - |
| **host-tos-redirect** | Enables the device to receive Redirect packets (type 5; code 3: Redirect datagrams for the Type of Service and Host). | - |
| **fragmentneed-dfset** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 4: fragmentation needed and DF set). | - |
| **source-route-failed** | Enables the device to receive ICMP Destination Unreachable packets (type 3; code 5: source route failed). | - |
| **redirect** | Enables the device to receive Redirect packets (type 5; code 0: Redirect datagrams for the Network; code 1: Redirect datagrams for the Host; code 2: Redirect datagrams for the Type of Service and Network; code 3: Redirect datagrams for the Type of Service and Host). | - |
| **type** *typevalue* | Enables the system to receive ICMP packets of a specified type. | The value is an integer ranging from 0 to 255. |
| **code** *codevalue* | Enables the system to receive ICMP packets with a specified message code. | The value is an integer ranging from 0 to 255. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the network is normal, ICMP packets can be correctly received. However, when network traffic is heavy, if hosts or ports are frequently unreachable, routing devices receive a large number of ICMP packets, which burdens the network and degrades the performance of routing devices. In addition, network attackers often use ICMP error packets to probe the internal structure of the network. To improve network performance and security, run the **icmp receive disable** command to disable the system from receiving ICMP packets.To re-enable an interface to receive ICMP packets, run the **icmp receive enable** command.Before running the **icmp receive enable** command in the interface view, you need to configure the inbound interface of original packets.


Example
-------

# Enable an interface to receive Host Unreachable messages.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 100
[*HUAWEI-Vlanif100] icmp name host-unreachable receive enable

```