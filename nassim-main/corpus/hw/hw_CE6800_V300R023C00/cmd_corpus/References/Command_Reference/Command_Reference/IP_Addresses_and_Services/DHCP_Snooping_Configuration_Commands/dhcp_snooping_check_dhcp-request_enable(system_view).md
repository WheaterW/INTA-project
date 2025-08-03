dhcp snooping check dhcp-request enable(system view)
====================================================

dhcp snooping check dhcp-request enable(system view)

Function
--------



The **dhcp snooping check dhcp-request enable** enables the device to check DHCP messages against the DHCP snooping binding table.

The **undo dhcp snooping check dhcp-request enable** disables the device from checking DHCP messages against the DHCP snooping binding table.



By default, the device does not check DHCP messages against the DHCP snooping binding table.


Format
------

**dhcp snooping check dhcp-request enable vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo dhcp snooping check dhcp-request enable vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


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

After a binding table is generated, the device checks DHCPv4 Request or Release messages against the binding table. The device forwards only the messages that match the binding table. Otherwise, the device discards the messages. This effectively prevents unauthorized users from sending bogus DHCP packets to pretend to be authorized users to renew or release IP addresses. The device checks DHCPv4 Request or Release messages against binding entries based on the following rules:· For DHCPv4 Request messages:

1. The device checks whether the CIADDR field in the DHCPv4 Request message is 0. If the CIADDR field is 0, the DHCPv4 Request message is sent for the first login and is directly forwarded. If the CIADDR field in the DHCPv4 Request message is not 0, the DHCPv4 Request message is sent for lease renewal and is checked against the binding table.
2. The device checks whether the CHADDR field in the message matches an entry in the binding table. If not, the device considers that the user goes online for the first time and forwards the message. If yes, the device checks whether the VLAN ID, client IP address, and interface information in the message match the binding table. If yes, the device forwards the message. If no, the device discards the message.· After receiving a DHCPv4 Release/Inform/Decline message, the device checks whether the CHADDR field in the message matches an entry in the binding table. If not, the device forwards the message. If a binding entry is matched, the device checks whether the VLAN ID, client IP address, and interface information in the message match the binding table. If yes, the device forwards the message. If no, the device discards the message.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.


Example
-------

# Enable the function of checking DHCP messages against the DHCP snooping binding table in VLAN 10 in the system view.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] quit
[*HUAWEI] dhcp snooping check dhcp-request enable vlan 10

```