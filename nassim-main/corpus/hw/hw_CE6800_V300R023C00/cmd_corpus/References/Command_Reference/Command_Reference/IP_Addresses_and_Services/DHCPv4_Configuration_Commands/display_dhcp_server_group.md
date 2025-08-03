display dhcp server group
=========================

display dhcp server group

Function
--------



The **display dhcp server group** command displays the configuration of a DHCP server group.




Format
------

**display dhcp server group** [ *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Displays the configuration of a specified DHCP server group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, and can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot use "-" and "--" as names. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP relay agents. The **display dhcp server group** command displays information about all the DHCP server groups of a DHCP relay agent and the number of DHCP servers in the DHCP server groups. If group-name is specified, the **display dhcp server group group-name** command displays DHCP server addresses and the number of DHCP servers in a specified DHCP server group.

**Prerequisites**

A DHCP server group has been created using the **dhcp relay server group** command on the DHCP relay agent.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the DHCP server group myServers.
```
<HUAWEI> display dhcp server group myServers
  Group-name          : myServers
    (0)  Server-IP    : 10.1.1.1
    Gateway           : 10.10.10.1
    VPN instance      : vpn1

```

**Table 1** Description of the **display dhcp server group** command output
| Item | Description |
| --- | --- |
| Group-name | Name of a DHCP server group.  To specify the parameter, run the dhcp relay server group command. |
| Gateway | Gateway address of the DHCP server in the DHCP server group.  To specify the parameter, run the gateway(dhcp-server-group) command. |
| VPN instance | VPN-instance of the DHCP server in the DHCP server group.  To specify the parameter, run the vpn-instance(dhcp-server-group) command. |
| (x) Server-IP | IP addresses of DHCP servers in a DHCP server group. x is the index of the IP addresses and ranges from 0 to 19.  To specify the parameter, run the server command. |