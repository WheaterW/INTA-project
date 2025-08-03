display udp status
==================

display udp status

Function
--------



The **display udp status** command displays information about IPv4 UDP connections.




Format
------

**display udp status** [ **local-ip** *laddress* | **local-port** *lport* | **remote-ip** *faddress* | **remote-port** *fport* ] \* [ **cid** *taskid* ] [ **socket-id** *soFd* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local-ip** *laddress* | Displays the IPv4 UDP connection with a specified local IP address. | The address is a 4-digit decimal number, in the format of X.X.X.X. |
| **local-port** *lport* | Displays the IPv4 UDP connection with a specified local port number. | The value ranges from 0 to 65535. |
| **remote-ip** *faddress* | Displays the IPv4 UDP connection with a specified remote IP address. | The address is a 4-digit decimal number, in the format of X.X.X.X. |
| **remote-port** *fport* | Displays the IPv4 UDP connection with a specified remote port number. | The value ranges from 0 to 65535. |
| **cid** *taskid* | Displays information about the IPv4 UDP connection with a specified APP CID. | The value is a hexadecimal integer ranging from 0 to ffffffff. |
| **socket-id** *soFd* | Displays the IPv4 UDP connection with a specified socket ID. | The value is an integer that ranges from 0 to 2147418111. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

UDP is a communications protocol used for packet switching on the Internet. It uses the simplest transmission model to send messages from one user application to another. To monitor the UDP connection status, run the display udp status command to check the following information:

* APP Cid
* IPv4 UDP Socket ID
* Local IPv4 address and port number
* Remote IPv4 address and port number
* FeNode ID


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of IPv4 UDP connections.
```
<HUAWEI> display udp status
----------------------------------------------------------------------
Cid        SocketId Local Addr:Port       Foreign Addr:Port     FeNode
----------------------------------------------------------------------
0x8069048F        3 0.0.0.0:3503          0.0.0.0:0                  0
0x80532737       10 0.0.0.0:68            0.0.0.0:0                257
----------------------------------------------------------------------

```

**Table 1** Description of the **display udp status**  command output
| Item | Description |
| --- | --- |
| Cid | Cid of the APP component. |
| SocketId | IPv4 UDP socket ID. |
| Local Addr:Port | Local IPv4 address and number of a UDP connection. |
| Foreign Addr:Port | Remote IPv4 address and number of a UDP connection. |
| FeNode | Node ID of a board. |