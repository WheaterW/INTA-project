display vrrp6 statistics
========================

display vrrp6 statistics

Function
--------



The **display vrrp6 statistics** command displays statistics about Virtual Router Redundancy Protocol for IPv6 (VRRP6) Advertisement packets sent and received by a VRRP6 backup group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vrrp6** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and ID of an interface. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface on which a VRRP6 backup group is configured. | - |
| *virtual-router-id* | Specifies the ID of a VRRP6 backup group. | The value is an integer ranging from 1 to 255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After you configure a VRRP6 backup group, run the **display vrrp6 statistics** command to view statistics about VRRP6 Advertisement packets sent and received by the VRRP6 backup group.

**Precautions**

To view statistics about packets sent and received by a VRRP6 backup group within a certain period, run the **reset vrrp6 statistics** command to clear the original statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about VRRP6 Advertisement packets sent and received by all VRRP6 backup groups.
```
<HUAWEI> display vrrp6 statistics
100GE1/0/1 statistics information :
      IP protocol number errors : 0
  Destination IP address errors : 0
                Checksum errors : 0
                 Version errors : 0
                    Vrid errors : 0

100GE1/0/1 | Virtual Router 1
                            Transited to master : 1
                            Sent advertisements : 8
                        Received advertisements : 0
                  Advertisement interval errors : 0
                 Failed to authentication check : 0
                         Received IP TTL errors : 0
            Received packets with priority zero : 0
                Sent packets with priority zero : 0
                  Received invalid type packets : 0
        Received unmatched address list packets : 0
            Unknown authentication type packets : 0
                 Mismatched authentication type : 0
                           Packet length errors : 0
         Received packets vrrp master self sent : 0
                        Received attack packets : 0
         Failed to learn advertisement interval : 0

```

**Table 1** Description of the **display vrrp6 statistics** command output
| Item | Description |
| --- | --- |
| IP protocol number errors | Number of packets with an incorrect IP protocol number. |
| Destination IP address errors | Number of packets with an incorrect destination IP address. |
| Checksum errors | Number of packets with an incorrect checksum. |
| Version errors | Number of packets with an incorrect version number. |
| Vrid errors | Number of packets with an incorrect VRRP6 backup group ID. |
| Transited to master | Number of times that the VRRP6 backup group switches to the Master state. |
| Sent advertisements | Number of sent Advertisement packets. |
| Sent packets with priority zero | Number of sent VRRP6 packets with a priority of 0. |
| Received advertisements | Number of received Advertisement packets. |
| Received IP TTL errors | Number of TTL errors. |
| Received packets with priority zero | Number of received VRRP6 packets with a priority of 0. |
| Received invalid type packets | Number of received VRRP6 packets with an invalid type. |
| Received unmatched address list packets | Number of received packets with an incorrect virtual IP address list. |
| Received packets vrrp master self sent | Number of received packets that the master device sends by itself. |
| Received attack packets | Received attack packets: number of received attack packets. |
| Advertisement interval errors | Number of broadcast interval errors. |
| Failed to authentication check | Number of authentication errors. |
| Failed to learn advertisement interval | Failed to learn advertisement interval: number of failures to learn the interval at which packets are sent. |
| Unknown authentication type packets | Number of packets with an unknown authentication type. |
| Mismatched authentication type | Number of packets with an invalid authentication type. |
| Packet length errors | Number of packet length errors. |
| 100GE1/0/1 | Statistics on the interface on which the VRRP6 backup group is configured. |
| 100GE1/0/1 | Virtual Router 1 | Interface on which the VRRP6 backup group is configured and ID of the VRRP6 backup group. |