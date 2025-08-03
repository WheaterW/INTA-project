ipv6 nd ra preference
=====================

ipv6 nd ra preference

Function
--------



The **ipv6 nd ra preference** command configures the default router preference value in the RA packets.

The **undo ipv6 nd ra preference** command restores the default router preference value in RA packets to be the default value.



By default, the router preference of RA packets is medium.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra preference** { **high** | **medium** | **low** }

**undo ipv6 nd ra preference**

**undo ipv6 nd ra preference** { **high** | **medium** | **low** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **high** | Specifies the default router preference to be high. | - |
| **medium** | Specifies the default router preference to be medium. | - |
| **low** | Specifies the default router preference to be low. | - |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If there are multiple Routing devices on the links connected to a host, the host needs to select suitable Routing devices based on different destination addresses of the packets to be forwarded. Each Routing device advertises its default router priority and specific route information to the host so that the host can enhance its own capability of selecting suitable forwarding Routing devices based on different IP addresses of the packets to be forwarded.After receiving an RA message that contains routing information, the host updates its own routing table. Before sending packets to other devices, the host can search the updated route information to select a suitable routing device to forward the packets.After receiving an RA message that contains the default router priority, the host updates its own default router list. If the host does not have any routing devices to select when sending packets to other devices, the host will search the updated router list for the Routing devices with the highest priority. If the Routing device with the highest priority becomes faulty, the host selects another Routing device in descending order of priority.To set a default router priority in RA messages, run the **ipv6 nd ra preference** command. This setting allows the Router with the highest priority to function as the gateway for hosts.

**Prerequisites**

Before running this command, run the **ipv6 enable** command on the interface view to enable the IPv6 function.By default, the Routing device does not advertise RA packets. Therefore, to allow the default router preference to be advertised to the host, you need to run the **ipv6 nd ra halt disable** command to enable the function of advertising RA packets for the device.

**Precautions**



If the system is deleting the binding relationship between an interface and an IPv6 address family VPN instance, you are prompted not to run the **ipv6 nd ra preference** command.




Example
-------

# Configure the default router preference value in RA packets on 100GE1/0/1 to be high.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra halt disable
[*HUAWEI-100GE1/0/1] ipv6 nd ra preference high

```