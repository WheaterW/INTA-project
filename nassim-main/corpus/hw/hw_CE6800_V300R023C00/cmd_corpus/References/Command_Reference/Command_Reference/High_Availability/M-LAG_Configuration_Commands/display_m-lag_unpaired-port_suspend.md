display m-lag unpaired-port suspend
===================================

display m-lag unpaired-port suspend

Function
--------



The **display m-lag unpaired-port suspend** command displays the names of interfaces that are configured to automatically enter the Error-Down state.




Format
------

**display m-lag unpaired-port suspend**


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

You can run the **display m-lag unpaired-port suspend** command to view the name of the interface where the **m-lag unpaired-port suspend** command is configured.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the name of the interface that is configured to enter the Error-Down state.
```
<HUAWEI> display m-lag unpaired-port suspend
*    : errordown
Ports
------------------------------------------------------------------------------
Eth-Trunk2      Eth-Trunk30     100GE1/0/1      100GE1/0/1

```

**Table 1** Description of the **display m-lag unpaired-port suspend** command output
| Item | Description |
| --- | --- |
| \* | The interface is configured to enter the Error-Down state.  The interface enters the Error-Down state only when the peer-link is faulty. |
| Ports | Name of an interface. |