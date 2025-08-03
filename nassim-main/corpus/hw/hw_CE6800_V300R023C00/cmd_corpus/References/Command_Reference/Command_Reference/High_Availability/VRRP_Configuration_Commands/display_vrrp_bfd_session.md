display vrrp bfd session
========================

display vrrp bfd session

Function
--------



The **display vrrp bfd session** command displays information about VRID-based dynamic BFD sessions.




Format
------

**display vrrp bfd session** { **all** | **interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays information about all VRID-based dynamic BFD sessions. | - |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Displays information about a VRID-based dynamic BFD session on a specified interface. | - |
| **vrid** *virtual-router-id* | Displays information about a dynamic BFD session based on a specified VRID. | The value is an integer ranging from 1 to 255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After creating VRID-based dynamic BFD sessions, you can run the display vrrp bfd session command to view information about these sessions.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all VRID-based dynamic BFD sessions.
```
<HUAWEI> display vrrp bfd session all
Total BFD session(s) for VRRP: 1
----------------------------------------------------------------
Interface : Vlanif100
TXInterval(milliseconds) : 1000 / 5066 (Config / Running)
RXInterval(milliseconds) : 1000 / 5066 (Config / Running)
DetectMultiplier : 3 / - (Config / Running)
LocalIP : 10.1.1.5
PeerIP : 10.1.1.1
BFD State : UP

```

**Table 1** Description of the **display vrrp bfd session** command output
| Item | Description |
| --- | --- |
| Total BFD session(s) for VRRP | Total number of VRID-based dynamic BFD sessions. |
| BFD State | Status of the VRID-based dynamic BFD session:   * UP: Status of the VRID-based dynamic BFD session is UP. * DOWN: Status of the VRID-based dynamic BFD session is DOWN. |
| Interface | Interface name. |
| TXInterval(milliseconds) | Minimum interval at which the local device sends BFD control packets:   * Config: Configured minimum interval at which the local device sends BFD control packets. * Running: Running minimum interval at which the local device sends BFD control packets. |
| RXInterval(milliseconds) | Minimum interval at which the local device receives BFD control packets:   * Config: Configured minimum interval at which the local device receives BFD control packets. * Running: Running minimum interval at which the local device receives BFD control packets. |
| DetectMultiplier | Local detection multiplier:   * Config: Configured local detection multiplier. * Running: Running local detection multiplier. |
| LocalIP | Local IP address of the VRID-based dynamic BFD session. |
| PeerIP | Peer IP address of the VRID-based dynamic BFD session. |