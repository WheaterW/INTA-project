display snmp-agent proxy rule
=============================

display snmp-agent proxy rule

Function
--------



The **display snmp-agent proxy rule** command displays proxy rules for SNMP packets.




Format
------

**display snmp-agent proxy rule** [ *rule-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-name* | Specifies the name of a proxy rule for SNMP packets. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a proxy rule for SNMP packets has been configured using the **snmp-agent proxy rule** command, you can run the display **snmp-agent proxy rule** command to view the proxy rule information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display proxy rules for SNMP packets.
```
<HUAWEI> display snmp-agent proxy rule
Proxy Rule name : proxy_rule_read@ccu
       Type             : read
       Remote engine ID : 01120025602101
       Host name        : 10.1.1.1
       Security name    : %#%#[7SCH}$<HX.vZ8%7YS3L:IsCPA^LbRRK-`/6"i"$%#%#
       Version          : v3
       Level            : Authentication

   Proxy Rule name : proxy_rule_read@ccu1
       Type             : read
       Remote engine ID : 800007DB01192168001100
       Host name        : proxy_host@ccu1
       Security name    : %#%#[7SCH}$<HX.vZ8%7YS3L:IsCPA^LbRRK-`/6"i"$%#%#
       Version          : v2c
       Level            : No authentication and privacy

   Proxy Rule name : proxy_rule_trap@ccu1
       Type             : trap
       Remote engine ID : 800007DB01192168001100
       Host name        : proxy_host@ems
       Security name    : %#%#[7SCH}$<HX.vZ8%7YS3L:IsCPA^LbRRK-`/6"i"$%#%#
       Version          : v2c
       Level            : No authentication and privacy

   Proxy Rule name : proxy_rule_write@ccu1
       Type             : write
       Remote engine ID : 01120025602101
       Host name        : 10.2.2.2
       Security name    : %#%#[7SCH}$<HX.vZ8%7YS3L:IsCPA^LbRRK-`/6"i"$%#%#
       Version          : v1
       Level            : No authentication and privacy

```

**Table 1** Description of the **display snmp-agent proxy rule** command output
| Item | Description |
| --- | --- |
| Proxy Rule name | Name of a proxy rule for SNMP packets. |
| Type | SNMP packet type:   * read: sends GetRequest packets from the NMS to the managed device. * write: sends SetRequest packets from the NMS to the managed device. * trap: sends traps from the managed device to the NMS. * inform: sends informs from the managed device to the NMS. |
| Remote engine ID | Engine ID of a managed device. |
| Host name | Target host name.  The target host may be either an NMS or a managed device. |
| Security name | Security user or community name. |
| Version | SNMP version number. |
| Level | Security level:   * Authentication: authenticates SNMP packets without encrypting them. * Privacy: authenticates and encrypts SNMP packets. * No authentication and privacy: neither authenticates nor encrypts SNMP packets. |