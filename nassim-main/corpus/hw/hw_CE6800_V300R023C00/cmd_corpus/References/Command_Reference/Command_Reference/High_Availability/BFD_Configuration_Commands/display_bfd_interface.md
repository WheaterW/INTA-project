display bfd interface
=====================

display bfd interface

Function
--------



The **display bfd interface** command displays information about BFD interfaces.




Format
------

**display bfd interface** [ { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface that is enabled with BFD. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To obtain the interfaces to which BFD sessions are bound or view the status of BFD sessions bound to a specified interface, run the **display bfd interface** command.Only BFD session for IP binding to an interface is supported.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BFD interfaces.
```
<HUAWEI> display bfd interface
--------------------------------------------------------------------------------
Interface Name                                 Sess-Count      BFD-State
--------------------------------------------------------------------------------
100GE1/0/1                                       1               up
--------------------------------------------------------------------------------
     Total Interface Number : 1

```

**Table 1** Description of the **display bfd interface** command output
| Item | Description |
| --- | --- |
| Interface Name | Name of the BFD interface. |
| Sess-Count | Number of sessions bound to the interface. |
| BFD-State | If PIS is enabled for a BFD session bound to the interface, the BFD session status is displayed. Otherwise, the interface status is displayed. |
| Total Interface Number | Total interface number. |