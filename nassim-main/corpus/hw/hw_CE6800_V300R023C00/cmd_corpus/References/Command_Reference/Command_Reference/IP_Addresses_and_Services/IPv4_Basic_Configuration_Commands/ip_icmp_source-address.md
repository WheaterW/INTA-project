ip icmp source-address
======================

ip icmp source-address

Function
--------



The **ip icmp source-address** command configures the IP address of the loopback interface as the source IP address of ICMP Port Unreachable or Time Exceeded messages.

The **undo ip icmp source-address** command restores the default configuration.



By default, the source IP address of ICMP Time Exceeded messages is the IP address of the inbound interface in a non-VPN scenario. In a VPN scenario, if the inbound interface of tracert packets is a VPN interface, the source IP address of ICMP Time Exceeded messages is the IP address of the inbound interface. If the inbound interface of tracert packets on a PE is a public network interface, the source IP address of ICMP Time Exceeded messages is the IP address of the outbound interface (VPN interface) on the PE.


Format
------

**ip icmp** { **port-unreachable** | **ttl-exceeded** } **source-address**

**undo ip icmp** { **port-unreachable** | **ttl-exceeded** } **source-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **port-unreachable** | Indicates an ICMP Port Unreachable message. | - |
| **ttl-exceeded** | Indicates an ICMP Time Exceeded message. | - |



Views
-----

Loopback interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To reduce exposure of the IP addresses of device interfaces in order to prevent against detection through ICMP Port Unreachable or Time Exceeded messages, run the **ip icmp source-address** command to specify the source IP address of ICMP Port Unreachable or Time Exceeded messages. After this command is run, if the device needs to give a reply to the messages, the device uses the IP address of the loopback interface as the source IP address of ICMP Port Unreachable or Time Exceeded messages.



**Precautions**



This command can be configured only on one loopback interface in a VPN.




Example
-------

# Configure the IP address of the Loopback2 interface as the source IP address of ICMP Port Unreachable messages.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 2
[*HUAWEI-LoopBack2] ip icmp port-unreachable source-address

```

# Configure the IP address of the Loopback1 interface as the source IP address of ICMP Time Exceeded messages.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn10
[*HUAWEI-vpn-instance-vpn10] quit
[*HUAWEI] interface loopback 1
[*HUAWEI-LoopBack1] ip binding vpn-instance vpn10
[*HUAWEI-LoopBack1] ip icmp ttl-exceeded source-address

```