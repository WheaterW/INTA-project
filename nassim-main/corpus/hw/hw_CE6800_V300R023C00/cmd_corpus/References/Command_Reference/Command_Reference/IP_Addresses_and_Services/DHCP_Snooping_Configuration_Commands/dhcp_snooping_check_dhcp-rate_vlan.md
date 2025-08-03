dhcp snooping check dhcp-rate vlan
==================================

dhcp snooping check dhcp-rate vlan

Function
--------



The **dhcp snooping check dhcp-rate vlan** command enables the device to check the rate of sending DHCP messages from different VLANs to the processing unit.

The **undo dhcp snooping check dhcp-rate vlan** command disables the device from checking the rate of sending DHCP messages from different VLANs to the processing unit in a batch.



By default, the device does not check the rate of sending DHCP messages to the processing unit, and the maximum rate of sending DHCP messages to the processing unit is 5000 pps.


Format
------

**dhcp snooping check dhcp-rate** { **enable** | *rate* } **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo dhcp snooping check dhcp-rate** [ **enable** ] **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Sets enabling status. | - |
| *vlan-id1* | Indicates the number of the first VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Indicates the ID of the last VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **dhcp-rate** *rate* | Specifies the maximum rate of sending DHCP messages to the processing unit. | The value is an integer ranging from 1 to 5000. The default value is 5000. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

This command is used to configure different VLANs in batches. For details about the command functions and configuration restrictions, see the **dhcp snooping check dhcp-rate enable** command in the VLAN view.


Example
-------

# Enable the device to check the rate of sending DHCP messages from VLAN 10 to VLAN 20 to the processing unit in batches in the system view.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan batch 10 to 20
[*HUAWEI] dhcp snooping check dhcp-rate enable vlan 10 to 20

```

# Set the threshold for the rate of sending DHCP messages from VLAN 10 to VLAN 20 to the processing unit to 300 in batches in the system view.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan batch 10 to 20
[*HUAWEI] dhcp snooping check dhcp-rate 300 vlan 10 to 20

```