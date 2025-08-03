mld static-group
================

mld static-group

Function
--------

The **mld static-group** command adds a sub-interface to an IPv6 multicast group statically.

The **undo mld static-group** command deletes the IPv6 multicast group to which an interface is statically added.

By default, an interface is not added to any IPv6 multicast group statically.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**mld static-group** *ipv6-group-address* [ **inc-step-mask** *ipv6-group-mask-length* **number** *group-number* ] [ **source** *ipv6-source-address* ] **dot1q** **vid** *low-pe-vid*

**undo mld static-group all**

**undo mld static-group** *ipv6-group-address* [ **inc-step-mask** *ipv6-group-mask-length* **number** *group-number* ] [ **source** *ipv6-source-address* ] **dot1q** **vid** *low-pe-vid*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-group-address* | Specifies the IP address of the IPv6 multicast group to which an interface is statically added. In batch configuration mode, this parameter specifies the initial address of the multicast group range. | The value is in hexadecimal notation and in the format FFxA:xxxx:xxxx::xxxx, in which x ranges from 0 to F and A is 0 or ranges from 3 to F. |
| **inc-step-mask** *ipv6-group-mask-length* | Specifies the incremental mask step in batch configuration mode. | The value is an integer that ranges from 9 to 128. |
| **number** *group-number* | Specifies the number of IPv6 group addresses in batch configuration mode. | The value is an integer that ranges from 2 to 512. |
| **source** *ipv6-source-address* | Specifies the IPv6 address of a multicast source. source-address specifies a multicast source address. | The address is in hexadecimal notation. |
| **vid** *low-pe-vid* | Specifies the lower limit of PE-VLAN ID (outer VLAN tag). | The value is an integer in the range from 1 to 4094. |




Views
-----

100ge sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

If user hosts want to receive IPv6 multicast data for a Multicast Listener Discovery (MLD) group stably for a long time or to ensure that MLD group memberships on the user network segment are stable, run the **mld static-group** command to add the interface connected to user hosts to MLD groups statically. In this manner, the interface can fast respond to users' requests, thereby reducing the channel switch time.

If user hosts want to receive IPv6 multicast data for an MLD group from a specific multicast source for a long time, set the source ipv6-source-address parameter in the
**mld static-group** command to specify the IPv6 multicast source address.The
**mld static-group** command is run on the interface connected to user hosts. The interface can be added to a single IPv6 multicast group or source/group, or be added to multiple IPv6 multicast groups or source/groups in batches.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

After the **mld static-group** command is run, the records about the MLD groups that the interface is added statically never time out. The router considers that this interface is always connected to IPv6 member hosts, and continues to forward qualified IPv6 multicast packets to the network segment where the interface resides.

If IPv6 multicast groups have been configured in batches and you modify only the value of group-number but not the value of ipv6-group-address or ipv6-group-mask-length to configure batch multicast groups again, the new batch configurations overwrite the previous batch configurations.

**Follow-up Procedure**

If user hosts no longer want to receive IPv6 multicast data for a group, manually delete the configurations of static MLD groups from the interface connected with user hosts.

**Precautions**

When different IPv6 multicast groups are configured in batches, the same IPv6 multicast group address may exist. Such configuration overlapping is allowed.

After an interface is configured to statically join IPv6 groups in batches, do not delete the configuration if the system has not completed the batch static IPv6 group joining.

Example
-------

# Statically add
100GE
1/0/1 to group FF03::101.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld static-group ff03::101

```

# Configure
100GE
1/0/1 to forward packets from multicast source 2001:DB8::101 to multicast group FF04::202.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld static-group ff04::202 source 2001:DB8::101

```