display rip bfd session
=======================

display rip bfd session

Function
--------



The **display rip bfd session** command displays information about BFD sessions.




Format
------

**display rip** *process-id* **bfd** **session** { **all** | **interface** { *interface-name* | *interface-type* *interface-number* } | *neighbor-address4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays information about BFD sessions in a specified RIP process. | The value is an integer that ranges from 1 to 4294967295. |
| **all** | Displays all information about BFD sessions in a specified RIP process. | - |
| **interface** *interface-type* *interface-number* | Displays information about BFD sessions on the specified interface. | - |
| *neighbor-address4* | Displays information about BFD sessions on a neighbor with a specified ID. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about BFD sessions, including the local and remote IP addresses, BFD status, and BFD parameters, run the **display rip bfd session** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all information about BFD sessions in RIP process 1.
```
<HUAWEI> display rip 1 bfd session all
 Interface :100GE1/0/1
   LocalIp       :192.168.1.2     RemoteIp  :192.168.1.1     BFDState  :Up

```

**Table 1** Description of the **display rip bfd session** command output
| Item | Description |
| --- | --- |
| Interface | Interface from which a local device advertises BFD sessions. |
| LocalIp | Local IP address. |
| RemoteIp | Peer IP address. |
| BFDState | BFD session status:   * Up. * Down. |