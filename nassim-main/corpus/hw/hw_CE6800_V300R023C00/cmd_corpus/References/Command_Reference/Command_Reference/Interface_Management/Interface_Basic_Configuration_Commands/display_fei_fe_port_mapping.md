display fei fe port mapping
===========================

display fei fe port mapping

Function
--------



The **display fei fe port mapping** command displays interface index and chip number information of interfaces on a device panel.




Format
------

**display fei fe port mapping slot** *slotid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotid* | Displays interface index and chip number information of all interfaces in a specified slot on a device panel. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about the interface index and chip number information of interfaces on a device panel, run the **display fei fe port mapping** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display interface index and chip number information of all interfaces in the specified slot on the device panel.
```
<HUAWEI> display fei fe port mapping slot 1
------------------------------------------------------------------------
Interface           IfIndex       TB       TP     Chip     Port     Core
------------------------------------------------------------------------
10GE1/0/1               262        0       44        0       44        0
10GE1/0/1               263        0       40        0       40        0
10GE1/0/2               264        0       36        0       36        0
10GE1/0/3               265        0       32        0       32        0
10GE1/0/4               266        0        0        0        0        0

```

**Table 1** Description of the **display fei fe port mapping** command output
| Item | Description |
| --- | --- |
| Interface | Name of an interface on the panel. |
| IfIndex | Interface index. |
| TB | Module ID. |
| TP | Local port number on the TB module. |
| Chip | Chip ID. |
| Port | Local port number on the chip. |
| Core | Channel where the interface resides. |