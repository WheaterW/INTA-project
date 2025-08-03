display arp learning strict
===========================

display arp learning strict

Function
--------



Using the **display arp learning strict** command, you can view information about strict Address Resolution Protocol (ARP) learning on all interfaces.




Format
------

**display arp learning strict**


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

**Usage Scenario**



To locate or rule out the ARP fails, the user needs to check whether strict ARP entry learning is enabled on an interface. By using the command, the user can view the strict ARP entry learning information of all the interfaces and the global circumstances, and to help users quickly locate the fault.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the strict ARP entry learning of all interfaces.
```
<HUAWEI> display arp learning strict
The global arp learning strict state:enable
------------------------------------------------------------
 Interface                           LearningStrictState
------------------------------------------------------------
 10GE1/0/2                              force-enable
 10GE1/0/1                              force-disable
------------------------------------------------------------
 Total:2     Force-enable:1     Force-disable:1

```

**Table 1** Description of the **display arp learning strict** command output
| Item | Description |
| --- | --- |
| The global arp learning strict state | Global status of strict ARP learning. |
| Interface | Interface name. |
| LearningStrictState | Status of strict ARP learning. |
| Total | Number of the interfaces to which strict ARP learning is applied. |
| Force-enable | Number of the interfaces on which strict ARP learning is enabled. |
| Force-disable | Number of the interfaces on which strict ARP learning is disabled. |