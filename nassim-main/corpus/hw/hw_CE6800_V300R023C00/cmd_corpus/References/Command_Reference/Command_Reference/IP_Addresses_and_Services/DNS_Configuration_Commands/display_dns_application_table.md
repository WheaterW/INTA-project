display dns application table
=============================

display dns application table

Function
--------



The **display dns application table** command displays the requests of application domain name resolution.




Format
------

**display dns application table**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display dns application table** command to display the requests of application domain resolution.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the requests of application domain name resolution.
```
<HUAWEI> display dns application table
 Host                                     Type   ModuleId                                               
 www.huaweiikepeer100_1.com               A         0X3                                                    
 www.huaweiikepeer100_10.com              AAAA      0X3
 Total : 2

```

**Table 1** Description of the **display dns application table** command output
| Item | Description |
| --- | --- |
| Host | Full name of a host. |
| Type | Type of resolution. The options are as follows:  A: indicates the resolution from a domain name to an IP address.  AAAA: indicates the resolution from a domain name to an IPv6 address. |
| ModuleId | Module ID (UNKNOWN = 0; data\_agent = 1; pki = 2; ipsec = 3; aaa = 4; ldapd = 5; hc = 6; sip = 7; nqa = 8; ddns = 9). |
| Total | Total number of application domain name resolution request entries. |