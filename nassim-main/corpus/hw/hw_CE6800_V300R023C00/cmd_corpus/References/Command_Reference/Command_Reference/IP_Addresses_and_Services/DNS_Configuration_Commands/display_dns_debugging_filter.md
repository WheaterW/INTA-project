display dns debugging filter
============================

display dns debugging filter

Function
--------



The **display dns debugging filter** command displays debugging information allowed to be sent by the DNS module.




Format
------

**display dns debugging filter**


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

Debugging affects device performance. To obtain the debugging information allowed to be sent by the DNS module, run this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DNS debugging information.
```
<HUAWEI> display dns debugging filter
Domain condition : huawei.com 
                   www.baidu.com
IP condition     : 1.1.1.1 
                   2.2.2.2
IPv6 condition   : 2001:db8:1::1/64 
                   2001:db8:1::2/64

```

**Table 1** Description of the **display dns debugging filter** command output
| Item | Description |
| --- | --- |
| Domain condition | Domain name matching item. |
| IP condition | IPv4 address matching item. |
| IPv6 condition | IPv6 address matching item. |