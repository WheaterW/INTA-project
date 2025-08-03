arp limit vlan
==============

arp limit vlan

Function
--------



The **arp limit** command limits the maximum number of dynamic Address Resolution Protocol (ARP) entries that an interface can learn.

The **undo arp limit** command restores the default number of dynamic ARP entries that an interface can learn.



For the default maximum number of dynamic ARP entries that an interface can learn, see "Parameters."


Format
------

**arp limit vlan** *vlan-id1* [ **to** *vlan-id2* ] *maximum*

**undo arp limit vlan** *vlan-id1* [ **to** *vlan-id2* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies the ID of the VLAN for which ARP entry learning is restricted. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. This parameter can be set only in the Layer 2 interface view and QinQ sub-interface view. If you set this parameter in the QinQ sub-interface view, vlan-id specifies the outer VLAN ID of the QinQ sub-interface. The value of <vlan-id2> must be greater than that of <vlan-id1>.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *vlan-id2* | Specifies the ID of the VLAN for which ARP entry learning is restricted. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. This parameter can be set only in the Layer 2 interface view and QinQ sub-interface view. If you set this parameter in the QinQ sub-interface view, vlan-id specifies the outer VLAN ID of the QinQ sub-interface. The value of <vlan-id2> must be greater than that of <vlan-id1>.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **limit** *maximum* | Specifies the maximum number of the ARP entries that the interface can learn. | For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 131072. The default value is 131072.  For the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer ranging from 1 to 261120. The default value is 261120. |



Views
-----

Layer 2 100GE interface view,100ge sub-interface view,Layer 2 10GE interface view,10GE sub-interface view,1200ge sub-interface view,Layer 2 200GE interface view,200GE sub-interface view,25GE-L2 view,25GE sub-interface view,400GE-L2 view,400GE sub-interface view,Layer 2 50GE interface view,50GE sub-interface view,Layer 2 Eth-Trunk interface view,Eth-Trunk sub-interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an unauthorized user sends a large number of ARP messages to a device, the device learns a large number of ARP entries in a short period of time, causing the ARP buffer to overflow. As a result, normal operation of the network is affected. To address such a problem, you can set the maximum number of ARP entries that each interface can learn.

**Configuration Impact**

If the number of ARP entries that an interface can learn changes, and the number of the learned ARP entries exceeds the changed value, the interface cannot learn additional ARP entries. You can delete the excess ARP entries based on the system prompt.If this command is run more than once, all configurations take effect.

**Precautions**



Ethernet, GE, and Eth-Trunk interfaces can function as Layer 3 or Layer 2 interfaces. When they function as Layer 3 interfaces, vlan-id cannot be configured. When they function as Layer 2 interfaces, vlan-id must be configured.Ethernet, GE, and Eth-Trunk sub-interfaces can function as common sub-interfaces or QinQ sub-interfaces. When they function as common sub-interfaces, vlan-id cannot be configured. When they function as QinQ sub-interfaces, vlan-id must be configured. vlan-id specifies the outer VLAN ID of a QinQ sub-interface.




Example
-------

# Configure the maximum number of dynamic ARP entries that a Layer 2 interface of VLAN 10 can learn to 20.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] arp limit vlan 10 20

```