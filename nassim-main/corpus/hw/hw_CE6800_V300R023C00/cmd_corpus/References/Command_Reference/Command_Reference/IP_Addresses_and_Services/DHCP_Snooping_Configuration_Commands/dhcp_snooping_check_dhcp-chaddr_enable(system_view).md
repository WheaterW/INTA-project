dhcp snooping check dhcp-chaddr enable(system view)
===================================================

dhcp snooping check dhcp-chaddr enable(system view)

Function
--------



The **dhcp snooping check dhcp-chaddr enable** command enables the device to check whether the CHADDR field matches the source MAC address in the header of a DHCP Request message.

The **undo dhcp snooping check dhcp-chaddr enable** command disables the device from checking whether the CHADDR field matches the source MAC address in the header of a DHCP Request message.



By default, the device does not check whether the source MAC address in the header of a DHCP Request message is the same as the CHADDR field value.


Format
------

**dhcp snooping check dhcp-chaddr enable vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo dhcp snooping check dhcp-chaddr enable vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


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

In normal situations, the CHADDR field in a DHCP Request message is the same as the MAC address of the client that sends the message. The DHCP server identifies the client MAC address based on the CHADDR field. If attackers continuously apply for IP addresses by changing the CHADDR field in the DHCP Request message, addresses in the address pool on the DHCP server will be exhausted. As a result, authorized users cannot obtain IP addresses.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

If you run this command in the VLAN view, the command takes effect for the DHCP messages of the specified VLAN on all device interfaces. If you run this command in the interface view, the command takes effect for all the DHCP messages received on the interface.


Example
-------

# Enable the function of checking the CHADDR field in DHCP messages globally.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan batch 20 to 40
[*HUAWEI] dhcp snooping check dhcp-chaddr enable vlan 20 to 40

```