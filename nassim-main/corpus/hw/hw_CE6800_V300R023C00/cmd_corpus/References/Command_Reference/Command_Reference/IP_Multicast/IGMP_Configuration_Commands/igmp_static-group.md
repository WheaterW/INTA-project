igmp static-group
=================

igmp static-group

Function
--------



The **igmp static-group** command configures an interface to statically join multicast groups.

The **undo igmp static-group** command deletes the multicast groups that an interface statically joins.



By default, an interface does not join any multicast group statically.


Format
------

**igmp static-group** *group-address* [ **inc-step-mask** { *group-mask* | *group-mask-length* } **number** *group-number* ] [ **source** *source-address* ]

**undo igmp static-group** { **all** | *group-address* **inc-step-mask** { *group-mask* | *group-mask-length* } **number** *group-number* [ **source** *source-address* ] }

**undo igmp static-group** *group-address* [ **source** *source-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Specifies the IP address of the multicast group that an interface statically joins. In batch configuration mode, this parameter specifies the initial address of the multicast group range. | The value is in dotted decimal notation and ranges from 224.0.1.0 to 239.255.255.255. |
| **inc-step-mask** | Indicates the step mask of a group address in batch configuration mode. | - |
| *group-mask* | Specifies the step mask of a group address in batch configuration mode, that is, the distance between two group addresses. | The value is in dotted decimal notation and ranges from 0.0.0.1 to 15.255.254.255. |
| *group-mask-length* | Specifies the length of the step mask in batch configuration mode. | The value is an integer ranging from 5 to 32. |
| **number** *group-number* | Specifies the number of group addresses in batch configuration mode. | The value is an integer ranging from 2 to 512. |
| **source** *source-address* | Specifies a multicast source address. | The address is in dotted decimal notation. |
| **all** | Indicates all multicast groups that an interface statically joins. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If users want to receive multicast data for a group for a long time, the **igmp static-group** command can be used to configure the interface connected to user hosts to statically join groups. This allows the interface to rapidly respond to users' requests, thus reducing the channel switching time.If users want to receive multicast data sent by a specific multicast source for a long time, source source-address can be set to specify a multicast source address.The **igmp static-group** command is run on the interface connected to user hosts. The interface can statically join a single or multiple multicast groups at one time, including source-specific multicast groups.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

After the **igmp static-group** command is run on an interface, static IGMP group records on the interface never time out. The device considers that the interface is always connected to group member hosts and continuously forwards qualified multicast packets to the network segment where the interface resides.After the **igmp static-group** command is run for the first time to configure multicast groups in batches, when you configure again, only the value of group-number is changed, and the values of group-address and group-mask | group-mask-length are not changed, the batch multicast static group configuration overwrites the previous batch multicast static group configuration.If inc-step-mask and number group-number are specified in the **igmp static-group** command, an interface is configured to statically join multicast groups in batches.The format of group-mask-length is as follows: group-mask = 1<< (32-group-mask-length), where the symbol << is a left shift operator.That is, all binary bits of an integer are shifted leftwards by a specified number of bits. Extra binary bits moved beyond the left boundary are discarded and 0 is shifted from the right boundary.For example, when group-mask-length is 32, 1<<0 represents 0.0.0.1. When group-mask-length is 31, 1<<1 represents 0.0.0.2. When group-mask-length is 30, 1<<2 represents 0.0.0.4. If group-mask-length is used to configure the incremental masks of group addresses, when you run the **display current-configuration** command to view related configurations, the format of the displayed incremental masks of group addresses is converted to group-mask.

**Follow-up Procedure**

If a user host no longer wants to receive multicast data for a group that the user host statically joins, delete the static group configuration.

**Precautions**



If an interface belongs to an NDR or Assert Loser, the interface will not be added as a real PIM outbound interface. As a result, static traffic diversion fails.When different multicast groups are configured in batches, the same multicast group address may exist. Such configuration overlapping is allowed.After an interface is configured to statically join multicast groups in batches, do not delete the configuration if the system has not completed the batch static group joining.If the igmp-snooping enable command is run in the VLAN view and the command for static join is run on the corresponding VLANIF interface, a multicast routing table can be generated, but traffic cannot be forwarded. To enable a static group to forward traffic, delete the igmp-snooping enable configuration from the VLAN.




Example
-------

# Configure 100GE 1/0/1 to statically join multicast groups in batches, with the initial group address of 225.1.1.1, the step mask length of 32, and the number of group addresses of 2. Specifically, add the interface to the multicast groups 225.1.1.1 and 225.1.1.2.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] igmp static-group 225.1.1.1 inc-step-mask 32 number 2

```

# Configure 100GE 1/0/1 on the Router to forward packets sent by multicast source 192.168.11.1 to multicast group 232.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-GEt0/1/0] undo portswitch
[*HUAWEI-100GE1/0/1] igmp static-group 232.1.1.1 source 192.168.11.1

```

# Configure 100GE 1/0/1 to statically join multicast groups in batches, with the initial group address of 232.1.1.1, the source IP address of 192.168.11.1, the incremental mask length of 32, and the number of group addresses of 2.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] igmp static-group 232.1.1.1 inc-step-mask 32 number 2 source 192.168.11.1

```

# Configure the sub-interface for dot1q VLAN tag termination to statically join multicast groups.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] interface Eth-Trunk 1.1
[*HUAWEI-Eth-Trunk1.1] dot1q termination vid 1
[*HUAWEI-Eth-Trunk1.1] igmp static-group 225.0.0.1 inc-step-mask 0.0.0.1 number 17 dot1q vid 1

```

# Configure 100GE 1/0/1 connected to users to statically join multicast group 224.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] igmp static-group 224.1.1.1

```