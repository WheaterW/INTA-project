dhcp snooping alarm dhcp-rate vlan
==================================

dhcp snooping alarm dhcp-rate vlan

Function
--------



The **dhcp snooping alarm dhcp-rate vlan** command enables the alarm function for discarded DHCP messages and sets the alarm threshold for the number of discarded DHCP messages in different VLANs in batches.

The **undo dhcp snooping alarm dhcp-rate vlan** command disables the alarm function for discarded DHCP messages and cancels the alarm threshold for the number of discarded DHCP messages in different VLANs in batches.



By default, the device does not generate an alarm when the number of discarded DHCP messages reaches the alarm threshold. The alarm threshold for the number of discarded DHCP messages is 100.


Format
------

**dhcp snooping alarm dhcp-rate** { **enable** | **threshold** *threshold* } **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo dhcp snooping alarm dhcp-rate** { **enable** | **threshold** } **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Sets enabling status. | - |
| **threshold** *threshold* | Specifies the alarm threshold. When the number of discarded DHCP messages reaches the threshold, an alarm is generated. | The value is an integer ranging from 1 to 1000. The default value is 100. |
| *vlan-id1* | Indicates the number of the first VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Indicates the ID of the last VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command is used to enable the alarm function for discarded DHCP messages in different VLANs in batches. For details about the command functions and configuration restrictions, see the description of the **dhcp snooping alarm dhcp-rate enable** command in the VLAN view.


Example
-------

# Enable the alarm function for discarded DHCP messages in VLANs 10 to 20 in the system view.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan batch 10 to 20
[*HUAWEI] dhcp snooping alarm dhcp-rate enable vlan 10 to 20

```

# Set the alarm threshold for the number of discarded DHCP messages in VLANs 10 to 20 to 50 in the system view.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan batch 10 to 20
[*HUAWEI] dhcp snooping alarm dhcp-rate threshold 50 vlan 10 to 20

```