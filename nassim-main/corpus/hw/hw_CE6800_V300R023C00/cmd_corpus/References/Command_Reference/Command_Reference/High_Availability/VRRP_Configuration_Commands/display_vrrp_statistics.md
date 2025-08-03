display vrrp statistics
=======================

display vrrp statistics

Function
--------



The **display vrrp statistics** command displays the current VRRP status, configured parameters, and statistics about the sent and received VRRP Advertisement packets.




Format
------

**display vrrp** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and number of an interface. | - |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After a VRRP group is configured, run the **display vrrp statistics** command to view statistics about sent and received VRRP Advertisement packets.

* If interface-type, interface-number, interface-name, or virtual-router-id is not specified, the status of all VRRP groups on the device is displayed.
* If only interface-number, interface-type, or interface-name is specified, the status of all VRRP groups on the specified interface is displayed.
* If interface-number, interface-type, or interface-name and virtual-router-id are specified, the status of the specified VRRP group on the specified interface is displayed.

**Precautions**

It is recommended that you run the **reset vrrp statistics** command to clear statistics about the received and sent VRRP Advertisement packets before you collect statistics within a specified period.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about all VRRP Advertisement packets.
```
<HUAWEI> display vrrp statistics
100GE1/0/1 statistics information :
      IP protocol number errors : 0
  Destination IP address errors : 0
                Checksum errors : 0
                 Version errors : 0
                    Vrid errors : 0

  100GE1/0/1 | virtual router 1
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

**Table 1** Description of the **display vrrp statistics** command output
| Item | Description |
| --- | --- |
| statistics information | Statistics about the VRRP group on the interface. |
| IP protocol number errors | Number of packets with an incorrect IP protocol number. |
| Destination IP address errors | Number of packets with an incorrect destination IP address. |
| Checksum errors | Number of packets with an incorrect checksum. |
| Version errors | Number of packets with an incorrect version number. |
| Vrid errors | Number of packets with an incorrect VRRP group ID. |
| virtual router 1 | Interface on which the VRRP group is configured and ID of the VRRP group. |
| Transited to master | Number of times that the device switches to the Master state. |
| Sent advertisements | Number of sent VRRP Advertisement packets. |
| Sent packets with priority zero | Number of sent VRRP Advertisement packets with a priority of 0. |
| Received advertisements | Number of received VRRP Advertisement packets. |
| Received IP TTL errors | Number of packets with an incorrect TTL. |
| Received packets with priority zero | Number of received VRRP Advertisement packets with a priority of 0. |
| Received invalid type packets | Number of received invalid VRRP Advertisement packets. |
| Received unmatched address list packets | Number of packets with an incorrect virtual IP address list. |
| Received packets vrrp master self sent | Number of received packets that the master device sends by itself. |
| Received attack packets | Received attack packets: number of received attack packets. |
| Advertisement interval errors | Number of VRRP Advertisement packets sent at an incorrect interval. |
| Failed to authentication check | Number of authentication errors. |
| Failed to learn advertisement interval | Failed to learn advertisement interval: number of failures to learn the interval at which packets are sent. |
| Unknown authentication type packets | Number of packets with an unknown authentication type. |
| Mismatched authentication type | Number of packets with an invalid authentication type. |
| Packet length errors | Number of packets with an incorrect length. |