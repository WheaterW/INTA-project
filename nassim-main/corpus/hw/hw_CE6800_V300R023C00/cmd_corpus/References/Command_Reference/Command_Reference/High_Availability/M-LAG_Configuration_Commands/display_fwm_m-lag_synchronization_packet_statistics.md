display fwm m-lag synchronization packet statistics
===================================================

display fwm m-lag synchronization packet statistics

Function
--------



The **display fwm m-lag synchronization packet statistics** command displays statistics about synchronization packets between the devices paired into a DFS group.




Format
------

**display fwm m-lag synchronization packet statistics** [ **slot** *slotid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotid* | Specifies the slot ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |
| **fwm** | Specifies forwarding control. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display fwm m-lag synchronization packet statistics** command displays statistics about synchronization packets between the devices paired into a DFS group, including the numbers of packets that are successfully received and sent or fail to be received and sent. The command output facilitates maintenance and location of the data packet synchronization mechanism.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about synchronization packets between the devices paired into a DFS group on the FWM side (for the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, and CE6820S).
```
<HUAWEI> display fwm m-lag synchronization packet statistics
Last send success type    : -
Last receive success type : -
Last send fail type       : -
Last receive fail type    : -
Last send fail reason     : -
Last receive fail reason  : -
Last send success time    : 0000-00-00 00:00:00
Last receive success time : 0000-00-00 00:00:00
Last send fail time       : 0000-00-00 00:00:00
Last receive fail time    : 0000-00-00 00:00:00
------------------------------------------------------------------------------------
Slot    Type            Send success    Send fail    Receive success    Receive fail
------------------------------------------------------------------------------------
1       MLAG            0               0            0                  0           
1       MAC             0               0            0                  0           
1       STP             0               0            0                  0           
1       VRRP            0               0            0                  0           
1       BFD             0               0            0                  0           
1       ICMP            0               0            0                  0           
1       PIM             0               0            0                  0           
1       IGMP            0               0            0                  0           
1       CONNECTIVITY    0               0            0                  0           
1       PORTGROUP       0               0            0                  0           
1       ARP             0               0            0                  0           
1       MLAGMBSTATE     0               0            0                  0           
1       ND              0               0            0                  0           
1       DHCP            0               0            0                  0           
1       MLD             0               0            0                  0           
1       PIMV6           0               0            0                  0           
1       VBST            0               0            0                  0           
------------------------------------------------------------------------------------

```

# Display statistics about synchronization packets between the devices paired into a DFS group on the FWM side (for the CE8855, CE8851-32CQ4BQ, CE6863E-48S8CQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL in standard forwarding mode, and CE6885-T).
```
<HUAWEI> display fwm m-lag synchronization packet statistics
Last send success type    : -
Last receive success type : -
Last send fail type       : -
Last receive fail type    : -
Last send fail reason     : -
Last receive fail reason  : -
Last send success time    : 0000-00-00 00:00:00
Last receive success time : 0000-00-00 00:00:00
Last send fail time       : 0000-00-00 00:00:00
Last receive fail time    : 0000-00-00 00:00:00
------------------------------------------------------------------------------------
Slot    Type            Send success    Send fail    Receive success    Receive fail
------------------------------------------------------------------------------------
1       MLAG            0               0            0                  0           
1       MAC             0               0            0                  0           
1       STP             0               0            0                  0           
1       VRRP            0               0            0                  0           
1       BFD             0               0            0                  0           
1       ICMP            0               0            0                  0           
1       PIM             0               0            0                  0           
1       IGMP            0               0            0                  0           
1       CONNECTIVITY    0               0            0                  0           
1       ARP             0               0            0                  0           
1       MLAGMBSTATE     0               0            0                  0           
1       ND              0               0            0                  0           
1       DHCP            0               0            0                  0           
1       MLD             0               0            0                  0           
1       PIMV6           0               0            0                  0           
1       VBST            0               0            0                  0           
------------------------------------------------------------------------------------

```

# Display statistics about synchronization packets between the devices paired into a DFS group on the FWM side (for the CE6885-LL in low latency mode).
```
<HUAWEI> display fwm m-lag synchronization packet statistics
Last send success type    : CONNECTIVITY
Last receive success type : MAC
Last send fail type       : -
Last receive fail type    : -
Last send fail reason     : -
Last receive fail reason  : -
Last send success time    : 2022-10-29 11:29:55
Last receive success time : 2022-10-29 11:30:05
Last send fail time       : 0000-00-00 00:00:00
Last receive fail time    : 0000-00-00 00:00:00
------------------------------------------------------------------------------------
Slot    Type            Send success    Send fail    Receive success    Receive fail
------------------------------------------------------------------------------------
1       MLAG            0               0            0                  0           
1       MAC             0               0            0                  0           
1       STP             0               0            0                  0           
1       VRRP            0               0            0                  0           
1       BFD             0               0            0                  0           
1       ICMP            0               0            0                  0           
1       PIM             0               0            0                  0           
1       IGMP            0               0            0                  0           
1       CONNECTIVITY    0               0            0                  0            
1       ARP             0               0            0                  0           
1       MLAGMBSTATE     0               0            0                  0           
1       DHCP            0               0            0                  0           
1       VBST            0               0            0                  0           
------------------------------------------------------------------------------------

```

**Table 1** Description of the **display fwm m-lag synchronization packet statistics** command output
| Item | Description |
| --- | --- |
| Last send success type | Type of packets that are successfully sent last time. |
| Last receive success type | Type of packets that are successfully received last time. |
| Last send fail type | Type of packets that fail to be sent last time. |
| Last receive fail type | Type of packets that fail to be received last time. |
| Last send fail reason | Reason why the last packet fails to be sent.  [1] GET PEERLINK FAILED: Failed to obtain peer-link information.  [2] FILL HEADER FAILED: Failed to fill the packet header.  [3] FILL DIGEST FAILED: Failed to fill in digest information.  [4] HPP SEND FAILED: Failed to send the HPP. |
| Last receive fail reason | Reason why the last packet fails to be received.  [1] ADD PKT HEAD FAILED: Failed to add the packet header.  [2] CUT MLAG HEAD FAILED: The packet header fails to be pruned.  [3] COPY ADDR FAILED: Packet content fails to be copied.  [4] ZERO THREADID: The HPP channel parameter is invalid.  [5] INVALID CHANNEL: The HPP channel is invalid.  [6] HPP SEND FAILED: HPP packets fail to be sent to the CPU.  [7] MLAG INFO ERROR: Failed to obtain MLAG information.  [8] TRUNK MEMBER ERROR: Failed to obtain LAG member interfaces.  [9] VERSION MISMATCH: The version does not match.  [10] VSID ERROR: The VSID is inconsistent.  [11] DFS PAIR FAILED: DFS pairing failed.  [12] RECEIVE LIMIT: The number of received packets reaches the upper limit.  [13] INTEGRITY CHECK FAILED: Digest verification fails.  [14] SERIALNUM CHECK FAILED: The serial number verification fails.  [15] PEERLINK IFINDEX ERROR: Failed to obtain the index of the peer-link interface. |
| Last send success time | Time when the last packet is successfully sent. If no packet is successfully sent, 0000-00-00 00:00:00 is displayed. |
| Last receive success time | Time when the last packet is successfully received. If no packet is successfully received, 0000-00-00 00:00:00 is displayed. |
| Last send fail time | Time when the last packet fails to be sent. If no packet fails to be sent, 0000-00-00 00:00:00 is displayed. |
| Last receive fail time | Time when the last packet fails to be received. If no packet fails to be received, 0000-00-00 00:00:00 is displayed. |
| Slot | Slot number. |
| Type | Packet type. |
| Send success | Statistics on packets that are successfully sent. |
| Send fail | Statistics on packets that fail to be sent. |
| Receive success | Statistics on packets that are successfully received. |
| Receive fail | Statistics on packets that fail to be received. |