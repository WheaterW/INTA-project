display lldp neighbor brief
===========================

display lldp neighbor brief

Function
--------



The **display lldp neighbor brief** command displays summary information about Link Layer Discovery Protocol (LLDP) neighbors.




Format
------

**display lldp neighbor brief**


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



To quickly obtain summary information about LLDP neighbors, run the display lldp neighbor brief command. The summary information about LLDP neighbors includes the local interface name, neighbor name, neighbor interface name, and neighbor information aging time.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and LLDP has also been enabled on interfaces using the lldp enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the summary information about LLDP neighbors.
```
<HUAWEI> display lldp neighbor brief
Local Interface         Exptime(s) Neighbor Interface      Neighbor Device     
--------------------------------------------------------------------------
100GE1/0/1                 96           10GE1/0/1          HUAWEI 
100GE1/0/1                 19           10GE1/0/1          HUAWEI                           
100GE1/0/2                 19           10GE1/0/2          HUAWEI                           
100GE1/0/3                 19           10GE1/0/3          HUAWEI

```

**Table 1** Description of the **display lldp neighbor brief** command output
| Item | Description |
| --- | --- |
| Local Intf | Local interface. |
| Local Interface | Local interface. |
| Neighbor Dev | Name of an LLDP neighbor. |
| Neighbor Intf | LLDP neighbor interface name. |
| Neighbor Interface | LLDP neighbor interface name. |
| Neighbor Device | Name of an LLDP neighbor. |
| Exptime (sec) | Aging time (in seconds) of the information about an LLDP neighbor. |
| Exptime | Aging time (in seconds) of the information about an LLDP neighbor. |