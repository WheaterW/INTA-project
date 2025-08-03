display icmp fast-reply statistics
==================================

display icmp fast-reply statistics

Function
--------



The **display icmp fast-reply statistics** command displays ICMP fast reply statistics.




Format
------

**display icmp fast-reply statistics slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays ICMP fast reply statistics in the specified slot. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

It is used to display ICMP fast reply statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ICMP fast reply statistics.
```
<HUAWEI> display icmp fast-reply statistics slot 1
------------------------ Display ICMP Statistics -------------------------------                                                    
Received packets:                                                                                                                   
     request packets:                             9                                                                                 
     invalid request packets:                     0                                                                                 
     failed to get vrf:                           0                                                                                 
     destination is not host ip:                  0                                                                                 
     failed to get ctrl word:                     0                                                                                 
Send packets:                                                                                                                       
     successful reply packets:                    9                                                                                 
     failed reply packets:                        0                                                                                 
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display icmp fast-reply statistics** command output
| Item | Description |
| --- | --- |
| Received packets | The number of all received packets. |
| request packets | The number of request packets. |
| invalid request packets | The number of invalid request packets. |
| failed to get vrf | The number of packets failed to get vrf. |
| failed to get ctrl word | The number of packets failed to get ctrl word. |
| failed reply packets | The number of failed reply packets. |
| destination is not host ip | The number of packets which destination is not host ip. |
| Send packets | The number of all sent packets. |
| successful reply packets | The number of successful reply packets. |