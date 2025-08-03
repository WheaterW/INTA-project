dhcp snooping enable no-user-binding(system view)
=================================================

dhcp snooping enable no-user-binding(system view)

Function
--------



The **dhcp snooping enable no-user-binding** command disables an interface from generating DHCP snooping binding entries after DHCP snooping is enabled.

The **undo dhcp snooping enable no-user-binding** command restores the default setting.



By default, an interface generates DHCP snooping binding entries after DHCP snooping is enabled.


Format
------

**dhcp snooping enable no-user-binding vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo dhcp snooping enable no-user-binding vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id2* | Specifies the ID of the last VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **vlan** *vlan-id1* | Represents the number of the first VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DHCP snooping is enabled on a device, the device generates DHCPv4 and DHCPv6 snooping binding entries for users by default. If the number of binding entries on the device reaches the upper limit, new users cannot go online. On a trusted DHCP network, if you do not want to limit the number of online users but want to record user location information, run the **dhcp snooping enable no-user-bind** command to disable the device from generating DHCP snooping binding entries.If the command is run in the interface view, the command takes effect for all DHCP users connected to the interface. If the command is run in the VLAN view, the command takes effect for DHCP users connected to all interfaces that belong to the VLAN. The configuration in the system view is similar to that in the VLAN view. The difference is that the configuration in the system view takes effect for multiple VLANs.

**Prerequisites**

DHCP snooping has been enabled using the dhcp snooping enable command.

**Precautions**

After this command is executed, the device deletes the binding entries of the corresponding VLAN or interface.If the DHCP snooping binding table-dependent function, such as IPSG or DAI, is configured on the device, the corresponding function does not take effect after this command is run.This command cannot be used together with the dhcp snooping check dhcp-request enable command. Otherwise, online users cannot go offline.


Example
-------

# In the system view, disable the interfaces in VLAN 10 and VLAN 20 from generating DHCP snooping binding entries.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan batch 10 20
[*HUAWEI] dhcp snooping enable vlan 10 20
[*HUAWEI] dhcp snooping enable no-user-binding vlan 10 20

```