display evpn vpn-instance
=========================

display evpn vpn-instance

Function
--------



The **display evpn vpn-instance** command displays EVPN instance information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display evpn vpn-instance** [ **name** *vpn-instance-name* ]

**display evpn vpn-instance** [ **name** *vpn-instance-name* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *vpn-instance-name* | Specifies the name of an EVPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **verbose** | Displays detailed information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check EVPN instance information, run the **display evpn vpn-instance** command.If vpn-instance-name is not specified, the **display evpn vpn-instance** command displays a summary of all configured EVPN instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about BD-EVPN instance 1.
```
<HUAWEI> display evpn vpn-instance name 1 verbose
 VPN-Instance Name and ID : 1, 5120
  Address family evpn
  Route Distinguisher :
  Label Policy        : label per instance
  Per-Instance Label  : NULL(unicast),NULL(bum),NULL(bypass)

```

**Table 1** Description of the **display evpn vpn-instance** command output
| Item | Description |
| --- | --- |
| VPN-Instance Name and ID | Name and ID of the EVPN instance. The ID is allocated by the system for indexing. |
| Address family evpn | EVPN instance address family. |
| Route Distinguisher | EVPN instance RD. |
| Label Policy | Label policy of the EVPN instance:   * label per bridge-domain. * label per vpn-instance. |
| Per-Instance Label | Label shared by all private network routes in the EVPN instance. |