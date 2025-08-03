multicast deny-vlan
===================

multicast deny-vlan

Function
--------

The **multicast deny-vlan** command enables the function of filtering out multicast data packets in a VLAN on an interface.

The **undo multicast deny-vlan** command disables an interface from filtering out multicast data packets in a VLAN.

By default, an interface forwards received multicast data packets.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.





Format
------

**multicast deny-vlan** { *start-vlan-id* [ **to** *end-vlan-id* ] } &<1-10>

**undo multicast deny-vlan** { *start-vlan-id* [ **to** *end-vlan-id* ] } &<1-10>



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-vlan-id* | Specifies the start VLAN ID. | The value is an integer that ranges from 1 to 4094. |
| **to** *end-vlan-id* | Indicates the end VLAN ID. | The value is an integer. The value ranges from 1 to 4094.  By default, the value is null. |




Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

After the **multicast deny-vlan** command is run on an interface, the interface discards the received multicast packets from the specified VLANs. This function may be used in the following scenarios:

The user-side interface receives multicast packets, but the switch does not need to receive multicast data packets from the user-side interface. After this command is run on a user-side interface, the interface discards multicast data packets received by the interface. This prevents user hosts from forging multicast sources to send multicast data packets.Multiple multicast sources in different VLANs are connected to the switch at Layer 2. The switch only needs to receive data from some of the multicast sources.In some special cases, for example, when the multicast service of a user on an interface expires and needs to be suspended, the network administrator can run this command to reject multicast data packets of the corresponding VLAN.

**Precautions**

If the command is run more than once, all configurations take effect.

The VLAN specified in the
**multicast deny-vlan** command must be the VLAN to which the interface has been added. Otherwise, the configuration is meaningless.You can run this command to filter only the multicast data packets that meet the following conditions:

* The destination MAC address of the packet is an IP multicast MAC address, that is, an IPv4 multicast MAC address starting with 0x01-00-5e or an IPv6 multicast MAC address starting with 0x33-33.
* The protocol type encapsulated in the packet is UDP.


Example
-------

# Enable multicast data filtering for VLANs from VLAN 100 to VLAN 105 on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] multicast deny-vlan 100 to 105

```