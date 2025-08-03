dhcp snooping check dhcp-giaddr enable(system view)
===================================================

dhcp snooping check dhcp-giaddr enable(system view)

Function
--------



The **dhcp snooping check dhcp-giaddr enable** command enables the device to check whether the GIADDR field in a DHCP Request message is 0.

The **undo dhcp snooping check dhcp-giaddr enable** command disables the device from checking whether the GIADDR field in a DHCP Request message is 0.



By default, the device does not check whether the GIADDR field in a DHCP Request message is 0.


Format
------

**dhcp snooping check dhcp-giaddr enable vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo dhcp snooping check dhcp-giaddr enable vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


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

To ensure that the device can obtain user parameters such as MAC addresses when generating DHCP snooping binding entries, DHCP snooping needs to be applied to the access device or the first DHCP relay agent on the Layer 2 network. Therefore, the GIADDR field in the DHCP messages received by the DHCP snooping-enabled device must be 0. If the GIADDR field is not 0, the DHCP messages are invalid and need to be discarded. This function is recommended when DHCP snooping is enabled on the DHCP relay agent. Generally, the GIADDR field in DHCP messages sent by a PC is 0. In some cases, the GIADDR field in DHCP messages sent by a PC is not 0, which may cause the DHCP server to allocate an incorrect IP address. To prevent PC users from forging DHCP messages with non-0 GIADDR field to apply for IP addresses, you are advised to configure this function.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

If you run this command in the VLAN view, the command takes effect only for the DHCP messages in the VLAN. If you run this command in the interface view, the command takes effect for all DHCP messages on the interface.


Example
-------

# Enable the device to check whether the GIADDR field in DHCP messages is 0.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] quit
[*HUAWEI] dhcp snooping check dhcp-giaddr enable vlan 10

```