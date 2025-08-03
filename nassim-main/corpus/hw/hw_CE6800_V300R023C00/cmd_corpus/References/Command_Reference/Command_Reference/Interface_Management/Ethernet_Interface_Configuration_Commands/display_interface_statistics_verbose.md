display interface statistics verbose
====================================

display interface statistics verbose

Function
--------



The **display interface statistics verbose** command displays statistics on packets with different lengths sent and received on a specified interface.




Format
------

**display interface statistics** { *interface-type* *interface-number* | *interface-name* } **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | The value must be set according to the device configuration. |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When locating an interface fault, you can run the command to view statistics about sent and received packets with different lengths on a specified interface. The command output helps you locate and rectify the fault.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on packets with different lengths sent and received on 10GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] display interface statistics 10ge 1/0/1 verbose
        PacketLength(Bytes)      Send(packets)       Receive(packets)
        1~64                     0                   0
        65~127                   0                   0
        128~255                  0                   0
        256~511                  0                   0
        512~1023                 0                   0
        1024~1518                0                   0
        1519~9216                0                   0

```

**Table 1** Description of the **display interface statistics verbose** command output
| Item | Description |
| --- | --- |
| PacketLength(Bytes) | Range of packet length. |
| Send(packets) | Number of transmitted packets. |
| Receive(packets) | Number of received packets. |