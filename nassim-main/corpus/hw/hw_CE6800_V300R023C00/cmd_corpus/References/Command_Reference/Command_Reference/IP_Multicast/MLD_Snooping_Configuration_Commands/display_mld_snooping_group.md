display mld snooping group
==========================

display mld snooping group

Function
--------



The **display mld snooping group** command displays multicast group information dynamically learned on a specified interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld snooping group interface** { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* [ [ **source-address** *source-address* ] **group-address** *group-address* ]

**display mld snooping group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Displays dynamically learned multicast group information of a specified interface. | - |
| **vlan** *vlan-id* | Displays dynamically learned multicast group information of a specified VLAN. | The value is an integer ranging from 1 to 4063. |
| **source-address** *source-address* | Displays dynamically learned information about a multicast group to which a specified multicast source sends data. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **group-address** *group-address* | Displays dynamically learned information about a specified multicast group. | The value is a 32-digit hexadecimal number in X:X:X:X:X:X:X:X format. The value ranges from FF00:: to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF. |
| **interface** *interface-type* *interface-number* | Displays dynamically learned multicast group information of a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To display multicast group information of a local interface or a remote peer dynamically learned by a device, run this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display dynamically learned multicast group information with the source address 2001:db8:1::1 and group address FF33::1 in VLAN 2 on 10GE1/0/1.
```
<HUAWEI> display mld snooping group interface 10ge 1/0/1 vlan 2 source-address 2001:db8:1::1 group-address ff33::1
 Group FF33::1 information:
  Uptime: 00h38m36s
  Expire: --
  Group timer: Not exist
  Retran count: 0
  Last member query: No
  Router filter mode: Include
  Compat mode: V2
  V1 host timer: Not exist
  Source last member query: No
  Last member query timer: Not exist
   Source 2001:db8::105 infor:
    Uptime: 00h38m36s
    Expire: 00h02m20s
    Source timer: Exist
    Retran count: 0
    Source last member query: No

```

**Table 1** Description of the **display mld snooping group** command output
| Item | Description |
| --- | --- |
| Group FF33::1 information | Information about the multicast group FF33::1. |
| Group timer | Whether a group timer exists:   * Exist. * Not exist. |
| Retran count | Number of times group-specific query messages are sent. |
| Last member query | Whether the multicast group has a member:   * Yes. * No. |
| Last member query timer | Whether the timer for last member query exists:   * Exist. * Not exist. |
| Router filter mode | Filtering mode of the multicast group:   * include. * exclude. |
| Compat mode | Running MLD version:   * V1: MLDv1. * V2: MLDv2. |
| V1 host timer | Whether an MLDv1 host timer exists:   * Exist. * Not exist. |
| Source last member query | Whether to send MLD Query messages to members of the source-specific group:   * Yes. * No. |
| Source 2001:db8::105 infor | Information about the multicast source 2001:db8::105. |
| Source timer | Whether a multicast source timer exists:   * Exist. * Not exist. |
| Uptime | Time since the multicast group was created. |
| Expire | Time before the multicast group expires. |