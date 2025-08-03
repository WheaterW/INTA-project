igmp static-group (dot1q)
=========================

igmp static-group (dot1q)

Function
--------

The **igmp static-group** command configures an interface to statically join multicast groups.

The **undo igmp static-group** command deletes the multicast groups that an interface statically joins.

By default, an interface does not join any multicast group statically.



Format
------

**igmp static-group** *StaticGrp* [ **inc-step-mask** { *IncStepGrpMask* | *IncStepGrpMaskLen* } **number** *TotalNum* ] [ **source** *SourceAddr* ] **dot1q** **vid** *lowVidValue*

**undo igmp static-group all**

**undo igmp static-group** *StaticGrp* [ **inc-step-mask** { *IncStepGrpMask* | *IncStepGrpMaskLen* } **number** *TotalNum* ] [ **source** *SourceAddr* ] **dot1q** **vid** *lowVidValue*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *StaticGrp* | Specifies a static group address. | The value is in dotted decimal notation. |
| **inc-step-mask** | Indicates the step mask of a group address in batch configuration mode. | - |
| *IncStepGrpMask* | Specifies the step mask of a group address in batch configuration mode, that is, the distance between two group addresses. | The value is in the wildcard mask format, and ranges from 0.0.0.1 to 15.255.254.255, in dotted decimal notation. |
| *IncStepGrpMaskLen* | Specifies the length of the step mask in batch configuration mode. | The value is an integer that ranges from 5 to 32. |
| **number** *TotalNum* | Specifies the number of group addresses in batch configuration mode. | The value is an integer ranging from 2 to 512. |
| **source** *SourceAddr* | Specifies a multicast source address. | The value is in dotted decimal notation. |
| **dot1q** | Statically adds a sub-interface for dot1q VLAN tag termination to a multicast group. | - |
| **vid** | Specifies a VLAN ID. | - |
| *lowVidValue* | Specifies the lower limit of the VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **all** | Indicates all multicast groups that an interface statically joins. | - |




Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

If a user needs to receive data of a multicast group for a long time, that is, there are stable multicast group members on the user network segment, you can configure an interface to statically join the multicast group. In this manner, the interface can quickly respond to user requests and shorten the channel switching time.

If users need to receive data sent from a multicast source to a specified multicast group for a long time, specify source SourceAddr in the command to specify a multicast source address.This command is configured on the interface connected to the user host. An interface can be statically added to a single multicast group or source-specific multicast groups, or statically added to multicast groups or source-specific multicast groups in batches.If users on a sub-interface for dot1q VLAN tag termination need to join one or more multicast groups for a long time, you can run the
**igmp static-group** command to configure the sub-interface to statically join multicast groups.

**Configuration Impact**

After the **igmp static-group** command is run on an interface, static IGMP group records on the interface never time out. The device considers that the interface is always connected to group member hosts and continuously forwards eligible multicast packets to the network segment where the interface resides.

If dot1q is not specified in the
**igmp static-group** command and multicast groups are configured in batches for the first time, you only need to change the value of TotalNum and do not change the values of StaticGrp and IncStepGrpMask | IncStepGrpMaskLen when configuring multicast groups in batches again. The new configuration overrides the previous one.You can run the
**igmp static-group StaticGrp inc-step-mask number TotalNum** command to configure an interface to statically join multicast groups in batches. The format of the IncStepGrpMaskLen parameter converted to IncStepGrpMask is IncStepGrpMask = 1<< (32-IncStepGrpMaskLen). The symbol << is a left shift operator, that is, all binary bits of an integer are moved leftwards by a specified number of bits. Extra binary bits that are moved beyond the left boundary are discarded and 0s are moved from the right boundary. For example, 1<<0 indicates 0.0.0.1, 1<<1 indicates 0.0.0.2, and 1<<3 indicates 0.0.0.4. If IncStepGrpMaskLen is used to configure the incremental masks of group addresses, the format of the displayed incremental masks of group addresses is converted to IncStepGrpMask when you run the
**display current-configuration** command to view related configurations.If dot1q is specified in the
**igmp static-group** command and multicast groups are configured in batches for the first time, if you change the value of group-number when configuring multicast groups in batches for the second time, the values of StaticGrp and IncStepGrpMask | IncStepGrpMaskLen remain unchanged. If the tag information configured in the command is different from that configured in the first time, the two configurations are independent of each other. The second configuration does not overwrite the previous batch multicast static group configuration. If the tag information configured in the second configuration is the same as that configured in the first configuration, the previous batch multicast static group configuration is overwritten.When configuring a sub-interface for dot1q VLAN tag termination to statically join a multicast group, pay attention to the following points:

* Tagged static multicast groups can be configured only on sub-interfaces for dot1q VLAN tag termination.
* The dot1q keyword can be specified only on the sub-interface for dot1q VLAN tag termination.
* The dot1q keyword must be specified for the interface.
* The specified VLAN ID range must be the same as that specified in the dot1q termination vid command. If they are inconsistent, the configuration of the non-intersection part is invalid.


Example
-------

# Configuring sub-interface for Dot1Q termination to statically join multicast groups.
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