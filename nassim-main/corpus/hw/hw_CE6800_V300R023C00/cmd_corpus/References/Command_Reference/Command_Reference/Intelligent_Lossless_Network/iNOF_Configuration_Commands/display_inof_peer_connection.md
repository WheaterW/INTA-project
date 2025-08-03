display inof peer connection
============================

display inof peer connection

Function
--------



The **display inof peer connection** command displays information about the iNOF connection established between the local and peer devices after the iNOF reflector and client are configured.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display inof peer connection**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the iNOF reflector and client are configured, you can run this command to check information about the iNOF connection established between the local and peer devices, including the local role, local address, and peer address.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the iNOF connection established between the reflector and peer devices after the iNOF reflector and client are configured.
```
<HUAWEI> display inof peer connection
Role: Reflector
IPv4 Info:
Port: 19516
ServiceAddress: 192.168.110.153
----------------------------------------------------------------------------------
Index  PeerIP                                   ConnectStatus  EstablishTime
----------------------------------------------------------------------------------
    1  192.168.110.151                          Established    2020-07-03 23:31:12
    2  192.168.110.191                          Connect        --
    3  192.168.110.192                          OpenSend       --
    4  192.168.110.193                          OpenConfirm    --
----------------------------------------------------------------------------------
IPv6 Info:
Port: 19516
ServiceAddress: 2001:DB8:110::153
----------------------------------------------------------------------------------
Index  PeerIP                                   ConnectStatus  EstablishTime
----------------------------------------------------------------------------------
    1  2001:DB8:1::1                            Established    2020-07-03 23:31:22
    2  2001:DB8:1::2                            Connect        --
    3  2001:DB8:1::3                            OpenSend       --
    4  2001:DB8:1::4                            OpenConfirm    --  
----------------------------------------------------------------------------------

```

# Display information about the iNOF connection established between the reflect-client and peer devices after the iNOF reflector and client are configured.
```
<HUAWEI> display inof peer connection
Role: Reflect-Client
IPv4 Info:
Port: 19516
ServiceAddress: 192.168.110.153
----------------------------------------------------------------------------------
Index  PeerIP                                   ConnectStatus  EstablishTime
----------------------------------------------------------------------------------
    1  192.168.110.152                          Established    2020-07-03 10:33:37
    2  192.168.110.154                          OpenSend       --
    3  192.168.110.156                          OpenConfirm    --
----------------------------------------------------------------------------------
IPv6 Info:
Port: 19516
ServiceAddress: 2001:DB8:110::153
----------------------------------------------------------------------------------
Index  PeerIP                                   ConnectStatus  EstablishTime
----------------------------------------------------------------------------------
    1  2001:DB8:1::2                            Established    2020-07-03 10:33:47
    2  2001:DB8:1::4                            OpenSend       --
    3  2001:DB8:1::6                            OpenConfirm    --
----------------------------------------------------------------------------------

```

**Table 1** Description of the **display inof peer connection** command output
| Item | Description |
| --- | --- |
| IPv4 Info | IPv4 information. |
| Index | Index. |
| PeerIP | IP address of the peer device. |
| ConnectStatus | Connection status. The options are as follows:   * Established: indicates that the connection is successful. * Connect: indicates that the connection is in progress. * OpenSend: indicates that the local end has sent an Open message and waits for a response from the peer end. If no response is received within the timeout period, the status changes to Connect. * OpenConfirm: indicates that the local end starts to send keepalive packets and waits for a response from the peer end. |
| EstablishTime | Connection establishment time. |
| IPv6 Info | IPv6 information. |
| Role | Device role. |
| Port | Port ID. |
| ServiceAddress | Local service address. |