display logbuffer brief
=======================

display logbuffer brief

Function
--------



The **display logbuffer brief** command is used to display brief information recorded in the log buffer.




Format
------

**display logbuffer brief**


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

Compared with the **display logbuffer** command, the **display logbuffer brief** command filters out CID and OID information from each log.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the summary of information in the log buffer.
```
<HUAWEI> display logbuffer brief
Logging buffer configuration and contents : enabled                                                                                 
Allowed max buffer size : 10240                                                                                                     
Actual buffer size : 512                                                                                                            
Channel number : 4 , Channel name : logbuffer                                                                                       
Dropped messages : 0                                                                                                                
Overwritten messages : 581                                                                                                            
Current messages : 512                                                                                                               
Dec 29 2020 11:55:31-07:00 : Callhome function maintenance information is collected. (Details =Socket creation failure response, local ip = 0.0.0.0, peer ip = 2.2.2.2, ret = 100011.)

```

**Table 1** Description of the **display logbuffer brief** command output
| Item | Description |
| --- | --- |
| Logging buffer configuration and contents | Logging buffer configuration and contents. |
| Allowed max buffer size | Allowed max buffer size. |
| Actual buffer size | Actual buffer size. |
| Channel number | Channel number. |
| Channel name | Channel name. |
| Dropped messages | Dropped messages. |
| Overwritten messages | Overwritten messages. |
| Current messages | Current messages. |