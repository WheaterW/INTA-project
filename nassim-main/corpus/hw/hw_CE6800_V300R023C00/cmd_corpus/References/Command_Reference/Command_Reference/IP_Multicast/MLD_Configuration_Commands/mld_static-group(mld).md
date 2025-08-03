mld static-group(mld)
=====================

mld static-group(mld)

Function
--------



The **mld static-group** command adds a sub-interface to an IPv6 multicast group statically.

The **undo mld static-group** command deletes the IPv6 multicast group to which an interface is statically added.



By default, an interface is not added to any IPv6 multicast group statically.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld static-group** *ipv6-group-address* [ **inc-step-mask** *ipv6-group-mask-length* **number** *group-number* ] [ **source** *ipv6-source-address* ]

**undo mld static-group** { **all** | *ipv6-group-address* **inc-step-mask** *ipv6-group-mask-length* **number** *group-number* [ **source** *ipv6-source-address* ] }

**undo mld static-group** *ipv6-group-address* [ **source** *ipv6-source-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-group-address* | Specifies the IP address of the IPv6 multicast group to which an interface is statically added. In batch configuration mode, this parameter specifies the initial address of the multicast group range. | The value is in the hexadecimal notation and in the format of FFxA:xxxx:xxxx::xxxx, among which x ranges from 0 to F and A ranges from 3 to F or can be 0. |
| **inc-step-mask** *ipv6-group-mask-length* | Specifies the incremental mask step in batch configuration mode. | The value is an integer ranging from 9 to 128. |
| **number** *group-number* | Specifies the number of IPv6 group addresses in batch configuration mode. | The value is an integer ranging from 2 to 512. |
| **source** *ipv6-source-address* | Specifies the IPv6 address of a multicast source. source-address specifies a multicast source address. | The address is in hexadecimal notation. |
| **all** | Indicates that the interface is statically added to all IPv6 multicast groups. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If user hosts want to receive IPv6 multicast data for a Multicast Listener Discovery (MLD) group stably for a long time or to ensure that MLD group memberships on the user network segment are stable, run the mld static-group command to add the interface connected to user hosts to MLD groups statically. In this manner, the interface can fast respond to users' requests, thereby reducing the channel switch time.If user hosts want to receive IPv6 multicast data for an MLD group from a specific multicast source for a long time, set the source SourceAddr parameter in the mld static-group command to specify the IPv6 multicast source address.The mld static-group command is run on the interface connected to user hosts. The interface can be added to a single IPv6 multicast group or source/group, or be added to multiple IPv6 multicast groups or source/groups in batches.


Example
-------

# Add 100GE1/0/1 to two multicast source-groups in a batch. Set the start multicast group address to FF33::1, the source address to 2001:DB8::101, and the step mask length to 24.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld static-group ff33::1 inc-step-mask 24 number 2 source 2001:DB8::101

```

# Configure 100GE1/0/1 to forward packets from multicast source 2001:DB8::101 to multicast group FF04::202.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld static-group ff04::202 source 2001:DB8::101

```

# Add 100GE1/0/1 to two multicast groups in a batch. Set the start multicast group address to FF25::1 and the step mask length to 24.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld static-group ff25::1 inc-step-mask 24 number 2

```

# Statically add 100GE1/0/1 to group FF03::101.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld static-group ff03::101

```