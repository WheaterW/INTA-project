display sdn openflow statistics slave
=====================================

display sdn openflow statistics slave

Function
--------



The **display sdn openflow statistics slave** command displays statistics about the OpenFlow connection packets.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display sdn openflow statistics slave**


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

If the OpenFlow connection fails, you can check the OpenFlow packet statistics to determine whether an error occurs in OpenFlow packet sending and receiving.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View statistics about OpenFlow connection packets.
```
<HUAWEI> display sdn openflow statistics slave
Controller: 192.168.78.118, VPN-instance: _public_
--------------------------------------------------------------------------------
Message type          Received        Sent     Invalid    Send failed
--------------------------------------------------------------------------------
HELLO                        1           1           0              0
ECHO_REQUEST                 0       15665           0              0
ECHO_REPLY               15665           0           0              0
EXPERIMENTER                 0          16           0              1
FEATURES_REQUEST             1           0           0              0
FEATURES_REPLY               0           1           0              0
PORT_STATUS                  0           1           0              0
FLOW_MOD                     0           0           0              0
MULTIPART_REQUEST            1           0           1              0
MULTIPART_REPLY              0           0           0              0
ROLE_REQUEST                 1           0           0              0
ROLE_REPLY                   0           1           0              0
PACKET_IN                    0           0           0              0
PACKET_OUT                   1           0           0              0
MULTI_PATH_DETECT            0           0           0              0
L2_PATH_DETECT               0           0           0              0
L3_PATH_DETECT               0           0           0              0
UNKNOWN                      1           0           0              0
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display sdn openflow statistics slave** command output
| Item | Description |
| --- | --- |
| Message type | Type of the message sent or received by the switch. |
| Received | Number of packets received by the switch. |
| Sent | Number of packets sent by the switch. |
| Invalid | Number of invalid packets received by the switch. |
| Send failed | Number of packets that failed to be sent by the switch. |
| Controller | Controller's IP address used to set up an OpenFlow connection. |
| VPN-instance | VPN instance name. |