display m-lag unpaired-port reserved
====================================

display m-lag unpaired-port reserved

Function
--------



The **display m-lag unpaired-port reserved** command displays the names of interfaces that are configured not to enter the Error-Down state when the peer-link fails but the DAD status is normal.




Format
------

**display m-lag unpaired-port reserved**


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

You can run the **display m-lag unpaired-port reserved** command to check the names of the interfaces that are configured not to enter the Error-Down state when the peer-link fails but the DAD status is normal.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the names of the interfaces that are configured not to enter the Error-Down state when the peer-link fails but the DAD status is normal.
```
<HUAWEI> display m-lag unpaired-port reserved
*    : errordown
Ports
------------------------------------------------------------------------------
Eth-Trunk2      Eth-Trunk30     100GE1/0/1      100GE1/0/1

```

**Table 1** Description of the **display m-lag unpaired-port reserved** command output
| Item | Description |
| --- | --- |
| \* | Indicates that the interface is configured to enter the Error-Down state.  Indicates that the interface enters the Error-Down state only when the peer-link fails. |
| Ports | Name of an interface. |