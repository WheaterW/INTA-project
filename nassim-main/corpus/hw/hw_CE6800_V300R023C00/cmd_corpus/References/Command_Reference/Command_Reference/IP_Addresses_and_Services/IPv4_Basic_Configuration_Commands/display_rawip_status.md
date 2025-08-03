display rawip status
====================

display rawip status

Function
--------



The **display rawip status** command displays information about IPv4 RawIP connections.




Format
------

**display rawip status** [ **cid** *taskid* ] [ **socket-id** *soFd* ] [ **local-ip** *laddress* ] [ **remote-ip** *faddress* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cid** *taskid* | Displays information about the RawIP connection with a specified APP CID. | The value is a hexadecimal integer ranging from 0 to ffffffff. |
| **socket-id** *soFd* | Displays information about the RawIP connection with a specified socket ID. | The value is an integer ranging from 0 to 2147418111. |
| **local-ip** *laddress* | Displays information about the RawIP connection with a specified local IP address. | The value is in dotted decimal notation. |
| **remote-ip** *faddress* | Displays information about the RawIP connection with a specified remote IP address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Run the display rawip status command to check the following information about each valid IPv4 RawIP connection on a device:

* IPv4 TCP socket ID
* APP CID
* Local IPv4 address
* Remote IPv4 address


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IPv4 RawIP connections.
```
<HUAWEI> display rawip status
---------------------------------------------------
Cid        SocketId Local Addr      Foreign Addr   
---------------------------------------------------
0x80692723        1 0.0.0.0         0.0.0.0        
---------------------------------------------------

```

**Table 1** Description of the **display rawip status**  command output
| Item | Description |
| --- | --- |
| Cid | APP CID. |
| SocketId | IPv4 RawIP socket ID. |
| Local Addr | Local IP address. |
| Foreign Addr | Remote IP address. |