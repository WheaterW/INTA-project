display hwtacacs-server accounting-stop-packet
==============================================

display hwtacacs-server accounting-stop-packet

Function
--------



The **display hwtacacs-server accounting-stop-packet** command displays information about Accounting-Stop packets sent by an HWTACACS server.




Format
------

**display hwtacacs-server accounting-stop-packet** { **all** | *number* | **ip** *ip-address* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays all accounting-stop packets. | - |
| *number* | Specifies the start number of the Accounting-Stop packets to be displayed. | The value is an integer ranging from 1 to 65535. |
| **ip** *ip-address* | Displays information about Accounting-Stop packets sent by the HWTACACS server with a specified IPv4 address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

During HWTACACS troubleshooting, you can run this command to check information about Accounting-Stop packets sent by the HWTACACS server.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all Accounting-Stop packets.
```
<HUAWEI> display hwtacacs-server accounting-stop-packet all
-------------------------------------------------------------
NO. SendTime      IP Address                         Template
1   10            192.168.1.110                      tac
-------------------------------------------------------------
Whole accounting stop packet to resend:1

```

**Table 1** Description of the **display hwtacacs-server accounting-stop-packet** command output
| Item | Description |
| --- | --- |
| NO. | Number of the Accounting-Stop packet. |
| SendTime | Number of times that Accounting-Stop packets are sent. |
| IP Address | IP address of the HWTACACS server. |
| Template | Name of the HWTACACS server template. |
| Whole accounting stop packet to resend | Total number of Accounting-Stop packets sent by a device. |