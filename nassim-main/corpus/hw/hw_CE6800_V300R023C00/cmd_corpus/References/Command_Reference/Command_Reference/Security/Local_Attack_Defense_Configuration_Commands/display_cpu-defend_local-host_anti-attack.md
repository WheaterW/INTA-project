display cpu-defend local-host anti-attack
=========================================

display cpu-defend local-host anti-attack

Function
--------



The **display cpu-defend local-host anti-attack** command displays statistics about packets matching the hardware ACL and the number and status of the ACL bound to the corresponding protocol after host attack defense is configured.




Format
------

**display cpu-defend local-host anti-attack** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After host attack defense is configured, you can run this command to view statistics about packets matching the hardware ACL and the number and status of the ACL bound to the corresponding protocol.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about packets matching the hardware ACL and the number and status of the ACL bound to the corresponding protocol after host attack defense is configured.
```
<HUAWEI> display cpu-defend local-host anti-attack
ACL resource on slot 1                                                                                                            
----------------------------------------------                                                                                      
Protocol       State           ACL                                                                                                  
----------------------------------------------                                                                                      
SSH            Successful     3000                                                                                                  
----------------------------------------------                                                                                      
                                                                                                                                    
SSH Statistics on slot 1                                                                                                          
--------------------------------------------------------------------------------                                                    
  rule 10 deny tcp                                                                                                                  
  Dropped Packets                     0, Dropped Bytes                         0                                                    
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend local-host anti-attack** command output
| Item | Description |
| --- | --- |
| ACL resource on slot 1 | ACL resources in a specified slot. |
| ACL | Type of an ACL. |
| Protocol | Packet type. |
| State | ACL delivery state:  Failed(n): An ACL fails to be delivered.  Successful: An ACL is delivered successfully. |
| SSH Statistics on slot 1 | Statistics about a specified type of packets in a slot. |
| rule 10 deny tcp | ACL rule. |
| Dropped Packets | Number of packets that are discarded. |
| Dropped Bytes | Number of discarded bytes. |