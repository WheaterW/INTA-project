display erps interface
======================

display erps interface

Function
--------



The **display erps interface** command displays ERPS information about a port that has been added to an ERPS ring.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display erps interface** { { *interface-name* | *interface-type* *interface-number* } [ **ring** *ring-id* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of the port. | - |
| *interface-type* | Specifies the type of the port. | - |
| *interface-number* | Specifies the number of the port. | - |
| **ring** *ring-id* | Specifies the ID of the ERPS ring to which the port has been added. | The value is an integer ranging from 1 to 255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the running status of ports that have been added to an ERPS ring, run the **display erps interface** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the ERPS configuration of port 100GE1/0/1.
```
<HUAWEI> display erps interface 100GE 1/0/1
Interface State                    : Up
- -------------------------------------------------------------------------------
Ring ID                            : 1                                          
Flush Logic                                                                     
    Remote Node ID                 : 0000-0000-0000                             
    Remote BPR                     : 0                                          
Track Link Detect Protocol         : 1AG

```

**Table 1** Description of the **display erps interface** command output
| Item | Description |
| --- | --- |
| Interface State | Physical status of the port. |
| Ring ID | ID of the ERPS ring to which the port has been added. |
| Flush Logic | Filtering database (FDB) flush status. |
| Remote Node ID | ID of the remote node. |
| Remote BPR | Blocked port reference of the remote node. |
| Track Link Detect Protocol | Protocol associated with ERPS on the port. "-": No protocol is associated with ERPS on the port. |