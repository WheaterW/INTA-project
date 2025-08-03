display udp ipv6 status
=======================

display udp ipv6 status

Function
--------



The **display udp ipv6 status** command displays information about IPv6 UDP connections.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display udp ipv6 status** [ **local-ip** *l6address* | **local-port** *lport* | **remote-ip** *f6address* | **remote-port** *fport* ] \* [ **cid** *taskid* ] [ **socket-id** *soFd* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local-ip** *l6address* | Displays the IPv6 TCP connection with a specified local IP address. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **local-port** *lport* | Displays the IPv6 TCP connection with a specified local port number. | The value ranges from 0 to 65535. |
| **remote-ip** *f6address* | Displays the IPv6 TCP connection with a specified remote IP address. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **remote-port** *fport* | Displays the IPv6 TCP connection with a specified remote port number. | The value ranges from 0 to 65535. |
| **cid** *taskid* | Displays information about IPv6 UDP connections based on a specified CID of the APP component. | The value is an integer that ranges from 0 to FFFFFFFF in hexadecimal notation. |
| **socket-id** *soFd* | Displays the IPv6 TCP connection with a specified socket ID. | The value is an integer that ranges from 0 to 2147418111. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display udp ipv6 status** command is used to view a list of all valid IPv6 UDP control blocks and gives the following information for each valid IPv6 UDP control block:

* IPv6 UDP Socket ID
* APP Cid
* Local IPv6 address and port
* Remote IPv6 address and port
* FeNode Id

**Precautions**

No information is displayed if there is no IPv6 UDP connection on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of IPv6 UDP connections.
```
<HUAWEI> display udp ipv6 status
---------------------------------------------------------------------------------
  SockId        Cid Local Address             Foreign Address          FeNode
---------------------------------------------------------------------------------
       1 0x80742726 ::->3784                  ::->0                    0          
       5 0x80D5271A ::->161                   ::->0                    0          
---------------------------------------------------------------------------------

```

**Table 1** Description of the **display udp ipv6 status** command output
| Item | Description |
| --- | --- |
| SockId | IPv6 UDP socket ID. |
| Cid | Cid of the APP component. |
| Local Address | Local IPv6 address and port number of a UDP connection. |
| Foreign Address | Remote IPv6 address and port number of a UDP connection. |
| FeNode | Node ID of a board. |