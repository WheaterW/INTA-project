display trapbuffer brief
========================

display trapbuffer brief

Function
--------



The **display trapbuffer brief** command is used to display brief information recorded in the trap buffer.




Format
------

**display trapbuffer brief**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Compared with the **display trapbuffer** command, the **display trapbuffer brief** command filters out CID and OID information from each trap.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# The display trapbuffer brief command displays the brief information of recent traps.
```
<HUAWEI> display trapbuffer brief
Trapping buffer configuration and contents : enabled                                                                                
Allowed max buffer size : 1024                                                                                                      
Actual buffer size : 256                                                                                                            
Channel number : 3 , Channel name : trapbuffer                                                                                      
Dropped messages : 0                                                                                                                
Overwritten messages : 0                                                                                                            
Current messages : 2                                                                                                                
Jul  4 2014 17:13:20 HUAWEI : The board partially failed. (EntPhysicalIndex=17104897, EntPhysicalName=MPU slot 1, EntityType=1, EntityTrapFaultID=132167, Reason=The memory size is
 different from the standard configuration.)

```

**Table 1** Description of the **display trapbuffer brief** command output
| Item | Description |
| --- | --- |
| Trapping buffer configuration and contents | Trapping buffer configuration and contents. |
| Allowed max buffer size | Allowed max buffer size. |
| Actual buffer size | Actual buffer size. |
| Channel number | Channel number. |
| Channel name | Channel name. |
| Dropped messages | Dropped messages. |
| Overwritten messages | Overwritten messages. |
| Current messages | Current messages. |