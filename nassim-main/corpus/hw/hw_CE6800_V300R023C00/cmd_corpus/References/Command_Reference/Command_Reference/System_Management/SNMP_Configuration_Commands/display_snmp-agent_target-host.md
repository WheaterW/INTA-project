display snmp-agent target-host
==============================

display snmp-agent target-host

Function
--------



The **display snmp-agent target-host** command displays information about all target hosts, including the IP address of each target host, VPN instance names, modes of sending trap messages, security names used to send trap messages, protocol versions, and security levels.




Format
------

**display snmp-agent target-host**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To view the configuration information about all target hosts, run the display snmp-agent target-host command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configurations of all target hosts on a device.
```
<HUAWEI> display snmp-agent target-host
Target host NO. 1
---------------------------------------------------------------------------
  Host name                        : 1
  IP address                       : 10.1.1.1
  Source interface                 : -
  VPN instance                     : -
  Security name                    : %^%#lJp'ERl$KB`=e14z2bk~~Og'MIBwaL@$cBF*cRzY%^%#
  Alarm Port                       : 162
  Event Port                       : 162
  Type                             : inform
  Version                          : v2c
  Level                            : No authentication and privacy
  NMS type                         : NMS
  With ext vb                      : No
  Notification filter profile name : -  
  Heart beat required              : No
---------------------------------------------------------------------------

```

**Table 1** Description of the **display snmp-agent target-host** command output
| Item | Description |
| --- | --- |
| Target-host NO | Index of a target host. |
| Host-name | Name of a target host. |
| IP-address | IP address of a target host. |
| Source interface | Source IP address of a target host. |
| VPN instance | VPN instance name. |
| Security name | Security user name in ciphertext for SNMPv1 and SNMPv2c and simple text for SNMPv3. |
| Alarm Port | Alarm port number. |
| Port | Number of a UDP port through which SNMP Request messages are sent.  The default port number is 162. |
| Event Port | Event port ID. |
| Type | Type of SNMP notification:   * Trap: SNMP notifications are sent in the form of trap messages. * Inform: SNMP notifications are sent in the form of Inform messages. |
| Version | SNMP version:   * v1. * v2c. * v3. |
| Level | Security level defined in a security mechanism:   * Authentication: Messages are authenticated, not encrypted. * Privacy: Messages are authenticated and encrypted. * No authentication and privacy: Messages are neither authenticated nor encrypted. |
| NMS type | Type of host NM:   * NMS. * HW NMS. |
| With ext-vb | Whether an SNMP trap sent to a destination host carries extended VB information:   * No: No extended private VB information is carried. * Yes: Extended private VB information is carried. |
| Notification filter profile name | Filter profile name. |
| Heart beat required | Whether to report heartbeat messages. |