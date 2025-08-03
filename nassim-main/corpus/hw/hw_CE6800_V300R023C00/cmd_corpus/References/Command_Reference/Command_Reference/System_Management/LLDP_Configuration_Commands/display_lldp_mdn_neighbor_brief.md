display lldp mdn neighbor brief
===============================

display lldp mdn neighbor brief

Function
--------



The **display lldp mdn neighbor brief** command displays summary information about MAC address discovery neighbor (MDN).




Format
------

**display lldp mdn neighbor brief**


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



To quickly check summary information about MDN neighbors, run the display lldp mdn neighbor brief command.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and MDN has been enabled on interfaces using the lldp mdn enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the summary information about MDN neighbors.
```
<HUAWEI> display lldp mdn neighbor brief
Local Intf                     Neighbor Mac Address     Neighbor Intf        Exptime (sec)        Neighbor Dev         
--------------------------------------------------------------------------------------------------------------
10GE1/0/1                      00e0-fc12-3456           FastEthernet1/0/14   162                  C3750_V8R5               
10GE1/0/1                      00e0-fc12-3456           FastEthernet1/0/14   161                  C3750_V8R5               
10GE1/0/2                      00e0-fc12-3456           FastEthernet1/0/14   162                  C3750_V8R5               
10GE1/0/3                      00e0-fc12-3456           FastEthernet1/0/14   162                  C3750_V8R5               
10GE1/0/4                      00e0-fc12-3456           FastEthernet1/0/14   162                  C3750_V8R5               
10GE1/0/5                      00e0-fc12-3456           FastEthernet1/0/14   162                  C3750_V8R5

```

**Table 1** Description of the **display lldp mdn neighbor brief** command output
| Item | Description |
| --- | --- |
| Local Intf | Local interfaces. |
| Neighbor Dev | Name of an MDN neighbor. |
| Neighbor Intf | Interface name of an MDN neighbor. |
| Neighbor Mac Address | MAC address of an MDN neighbor. |
| Exptime (sec) | Aging time (in seconds) of information about an MDN neighbor. |