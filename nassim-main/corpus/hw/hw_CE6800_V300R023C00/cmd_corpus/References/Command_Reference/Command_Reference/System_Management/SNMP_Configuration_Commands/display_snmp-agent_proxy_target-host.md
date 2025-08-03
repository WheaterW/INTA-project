display snmp-agent proxy target-host
====================================

display snmp-agent proxy target-host

Function
--------



The **display snmp-agent proxy target-host** command displays target host information on an SNMP proxy.




Format
------

**display snmp-agent proxy target-host** [ *target-host-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *target-host-name* | Specifies a target host name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view default or configured target host information on an SNMP proxy, run the **display snmp-agent proxy target-host** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configured target host information on an SNMP proxy.
```
<HUAWEI> display snmp-agent proxy target-host
Proxy target-host NO. 1
-----------------------------------------------------------
  Host-name        : proxy_host@ccu1
  IP-address       : 192.168.1.100
  Port             : 161
  Timeout          : 15
  Source interface : -
  VPN instance     : -
  Security name    : %#%#j!IJ)6sI%#%#j!IJ6^(sI<z~CMH5@^@zj(&.G^ylO4#{n4sXq&-A*;iAW(:-!@0&rY'5x\6%#%#
  Version          : v2c
  Level            : No authentication and privacy
-----------------------------------------------------------

Proxy target-host NO. 2
-----------------------------------------------------------
  Host-name        : proxy_host@ccu2
  IP-address       : 10.1.1.1
  Port             : 161
  Timeout          : 15
  Source interface : -
  VPN instance     : -
  Security name    : %#%#[7SCH}$<HX.vZ8%7YS3L:IsCPA^LbRRK-`/6"i"$%#%#
  Version          : v3
  Level            : Authentication
-----------------------------------------------------------

```

**Table 1** Description of the **display snmp-agent proxy target-host** command output
| Item | Description |
| --- | --- |
| Proxy target-host NO. | Number of a target host for an SNMP proxy. |
| Host-name | Name of the target host for an SNMP proxy. |
| IP-address | IP address of the target host for an SNMP proxy. |
| Port | Number of a UDP port used by a target host to send SNMP messages. |
| Timeout | Timeout period for a target host to send a response to an SNMP agent after receiving an inform from the SNMP agent. |
| Source interface | Source interface of the target host configured on the SNMP proxy. |
| VPN instance | Name of a VPN instance to which a target host belongs. |
| Security name | Security user or community name. |
| Version | SNMP version number. |
| Level | Security level:   * Authentication: authenticates SNMP packets without encrypting them. * Privacy: authenticates and encrypts SNMP packets. * No authentication and privacy: neither authenticates nor encrypts SNMP packets. |