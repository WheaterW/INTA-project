display netconfc session
========================

display netconfc session

Function
--------



The **display netconfc session** command displays information about all or specific NETCONF Client session.




Format
------

**display netconfc session** [ **peer-id** *peerid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer-id** *peerid* | Specifies the ID of a peer device. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command displays information about a specified session or all sessions.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the NETCONF Client session.
```
<HUAWEI> display netconfc session
--------------------------------------------------------------
Peer ID             : 2147483648
NETCONFC Session ID : 2
Dest IP             : 127.0.0.1
Dest Port           : 830
Connection Name     : MyTest-1
User Name           :
Session Type        : CFG
Session State       : READY
Up Time             : 2021-12-01 03:28:48
PID                 : 26674213

Peer ID             : 2147483649
NETCONFC Session ID : 2
Dest IP             : 127.0.0.1
Dest Port           : 831
Connection Name     : MyTest-8006
User Name           :
Session Type        : CFG
Session State       : READY
Up Time             : 2021-12-01 03:28:47
PID                 : 26674213

Peer ID             : 2147483650
NETCONFC Session ID : 2
Dest IP             : 127.0.0.1
Dest Port           : 832
Connection Name     : MyTest2-11
User Name           :
Session Type        : CFG
Session State       : READY
Up Time             : 2021-12-01 03:28:47
PID                 : 26674213

Peer ID             : 2147483651
NETCONFC Session ID : 2
Dest IP             : 127.0.0.1
Dest Port           : 833
Connection Name     : MyTest2-21
User Name           :
Session Type        : CFG
Session State       : READY
Up Time             : 2021-12-01 03:28:57
PID                 : 26674213
--------------------------------------------------------------

```

# Display session information about a NETCONF client with peer-id 2147483648.
```
<HUAWEI> display netconfc session peer-id 2147483648
--------------------------------------------------------------
Peer ID             : 2147483648
NETCONFC Session ID : 2
Dest IP             : 127.0.0.1
Dest Port           : 830
Connection Name     : MyTest-1
User Name           :
Session Type        : CFG
Session State       : READY
Up Time             : 2021-12-01 03:28:48
PID                 : 26674213
--------------------------------------------------------------

```

**Table 1** Description of the **display netconfc session** command output
| Item | Description |
| --- | --- |
| Peer ID | ID of a peer device. |
| NETCONFC Session ID | ID of a NETCONFC session. |
| Session Type | Session type.   * NCC: transparent transmission channel. * NONE: idle channel. * CFG: configuration channel. * QUERY: query channel. * ACT: maintenance channel. |
| Session State | Session status.   * INIT: The session is in initialization state. * LOCKING: The NETCONF client is locking peer device configurations. * READY: The session is idle. * BLOCK: The session is blocked and backpressure is required for CMF messages. |
| Dest IP | Peer IP address of a session. |
| Dest Port | Peer port number of a session. |
| Connection Name | Name of a BFD session. |
| User Name | User name for session establishment. |
| Up Time | Time when the session is successfully established. |
| PID | PID of the component on which the session exists. |