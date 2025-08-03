display ospf bfd session
========================

display ospf bfd session

Function
--------



The **display ospf bfd session** command displays information about a BFD-enabled neighbor.




Format
------

**display ospf** [ *process-id* ] **bfd** **session** { **all** | *interfaceName* | *interfaceType* *interfaceNum* | *NbrRouterId* }

**display ospf** [ *process-id* ] **bfd** **session** { *interfaceName* | *interfaceType* *interfaceNum* } *NbrRouterId*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Displays all the interfaces that are enabled with BFD in the OSPF process. | - |
| *interfaceName* | Specifies the name of an interface. | - |
| *interfaceType* | Specifies the type of an interface. | - |
| *interfaceNum* | Specifies the interface number. | - |
| *NbrRouterId* | Specifies the router ID of a neighbor. | Dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

In BFD for OSPF, a BFD session is associated with OSPF. The BFD session fast detects a link fault and then notifies OSPF of the fault, which enables OSPF to fast respond to the change of the network topology.The **display ospf bfd session** command displays information about a BFD-enabled neighbor.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BFD-enabled neighbors.
```
<HUAWEI> display ospf bfd session all
OSPF Process 1 with Router ID 3.3.3.3
  Area 0.0.0.0 interface 10.2.2.1 ( 100GE1/0/1 )'s BFD Sessions

 NeighborId:10.2.2.2          AreaId:0.0.0.0           Interface:100GE1/0/1          
 BFDState:up                  rx    :50                tx       :50               
 Multiplier:3                 BFD Local Dis:16385      LocalIpAdd:10.2.2.1        
 RemoteIpAdd:10.2.2.2         Diagnostic Info:No diagnostic information

   Total UP/DOWN/UNKNOWN BFD Session Number : 1 / 0 / 0

```

**Table 1** Description of the **display ospf bfd session** command output
| Item | Description |
| --- | --- |
| Router ID | Local router ID. |
| BFD Local Dis | Local discriminator of the BFD session. |
| rx | Interval at which BFD packets are received. |
| tx | Interval at which BFD packets are sent. |
| Diagnostic Info | Diagnosis information:   * No diagnostic information: No diagnostic information is displayed. * Control Detection Time Expired: The detection time expires. * Echo Function Failed: indicates that the echo function fails. * Neighbor is down: The neighbor session is Down. * Forwarding Plane Reset: The forwarding plane is reset. * Path Down: indicates that the path is Down. * Concatenated Path Down: The cascading path is Down. * Administator down: indicates AdminDown. * Reverse Concatenated Path Down: The reverse concatenated path is Down. * administrator down event received: indicates that an administrator down event is received. * Global BFD is not enabled: BFD is disabled globally. * BFD session number reaches the max: The number of BFD sessions reaches the maximum value. |
| Total UP/DOWN/UNKNOWN BFD Session Number | Total number of BFD sessions in the Up, Down, or Unknown state. |
| NeighborId | Router ID of the neighbor. |
| BFDState | BFD status:   * up. * down. * unknown. |
| LocalIpAdd | Local IP address. |
| RemoteIpAdd | Remote IP address. |
| AreaId | Region ID. |
| Interface | Interface used to set up the BFD session. |
| Multiplier | Remote detection multiplier. |