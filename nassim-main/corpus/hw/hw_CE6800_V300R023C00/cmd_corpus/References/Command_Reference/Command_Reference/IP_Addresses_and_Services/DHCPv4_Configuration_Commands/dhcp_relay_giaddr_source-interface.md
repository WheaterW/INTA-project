dhcp relay giaddr source-interface
==================================

dhcp relay giaddr source-interface

Function
--------



The **dhcp relay giaddr source-interface** command configures the source interface of DHCP relayed packets and enters the primary IP address of the interface into the giaddr field.

The **undo dhcp relay giaddr source-interface** command restores the default settings.



By default, the source interface of DHCP relayed packets is not configured and the IP address of the DHCP relay agent is entered into the giaddr field.


Format
------

**dhcp relay giaddr source-interface** { *interface-type* *interface-num* | *interface-name* }

**undo dhcp relay giaddr source-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the interface type. | - |
| *interface-num* | Specifies an interface number. | - |
| *interface-name* | Specifies an interface name. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* In a distributed gateway scenario, configure the DHCP relay function on the gateway interface of each distributed gateway. The DHCP relay agent fills the giaddr field with the IP address of the gateway interface in the request packet sent to the DHCP server. Based on the giaddr field, the DHCP server sets the destination IP address of the response packet to the IP address of the gateway interface. However, because the gateway interfaces of distributed gateways have the same IP address, the response packet from the DHCP server may be sent back to other distributed gateways (not the device that sends the request packet). As a result, users cannot obtain IP addresses. To solve the preceding problems, you can configure a source interface for DHCP relay packets on each distributed gateway. Then, the DHCP relay agent uses the primary IP address of the interface to fill in the giaddr field to communicate with the DHCP server. The IP address of the source interface can communicate with the DHCP server, and the IP address is unique on all distributed gateways. Therefore, the response packets from the DHCP server can be sent to the correct distributed gateways.
* When a user and a DHCP server are located in different VPNs, if the DHCP relay agent still uses the IP address of the relay interface as the relay agent address, the DHCP server cannot communicate with the DHCP relay agent through this address, and DHCP reply packets are unreachable. To solve this problem, run the **dhcp relay giaddr source-interface** command to configure the IP address of the source interface as the relay agent address so that the DHCP reply packets from the DHCP server can be forwarded to the DHCP relay agent.

**Prerequisites**

DHCP relay has been enabled by running the **dhcp select relay** command in the interface view.

**Follow-up Procedure**

By default, the DHCP server selects an IP address pool based on the giaddr field. After this command is configured, the primary IP address of the source interface is entered into the giaddr field. Because the primary IP address of the source interface and the IP address of the DHCP relay-enabled interface are on different network segments, if the DHCP server still selects an IP address pool based on the giaddr field, DHCP clients cannot properly communicate even if they have obtained IP addresses. The DHCP relay-enabled interface functions as the gateway for connected DHCP clients. Therefore, you need to run the **dhcp option82 link-selection insert enable** command to configure the function of inserting the Link-selection suboption of the Option82 field into DHCP relayed DHCP request packets. The IP address of the DHCP relay-enabled interface is entered into the Link-selection suboption. The DHCP server then selects an IP address pool based on the Link-selection suboption after receiving a request packet.

**Precautions**

* Ensure that the IP address of the source interface and the DHCP server can communicate with each other.
* The source interface and the DHCP relay-enabled interface can be bound to different VPNs.
* The DHCP server must be capable of parsing the Link-selection suboption.

Example
-------

# On interface 100GE1/0/1, set the source interface of DHCP relayed packets to LoopBack1.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 1
[*HUAWEI-LoopBack1] ip address 10.1.1.1 24
[*HUAWEI-LoopBack1] quit
[*HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp select relay
[*HUAWEI-100GE1/0/1] dhcp relay giaddr source-interface loopback 1

```