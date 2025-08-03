display ip interface
====================

display ip interface

Function
--------



The **display ip interface** command displays the IP-related configuration of and statistics on an interface, including the packets, bytes, and multicast packets sent and received by the interface, and broadcast packets sent, received, forwarded, and discarded by the interface. If no interface type is specified, the system displays IP configurations of and statistics on all interfaces.




Format
------

**display ip interface** [ *interface-name* | *interface-type* *interface-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies an interface type and number. | The value is of the enumerated type. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



Before you monitor the status of an interface or check the sending and receiving of some types of packets on the interface, run the display ip interface command to view the interface status and collect statistics on the interface. The obtained information helps you check whether the network is under attack and possible attack sources.



**Implementation Procedure**

* Run the **display interface description** command to view the description of the interface.
* Run the **display interface** command to view detailed information about the operation and statistics of the interface.

**Precautions**



If an interface is used for services exclude IP services, no information about the interface is displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display specific information about 100GE 1/0/1.
```
<HUAWEI> display ip interface 100GE 1/0/1
100GE1/0/1 current state : UP
Line protocol current state : UP
The Maximum Transmit Unit : 1500 bytes
input packets : 0, bytes : 0, multicasts : 0
output packets : 0, bytes : 0, multicasts : 0
Directed-broadcast packets:
 received packets:            0, sent packets:              0
 forwarded packets:           0, dropped packets:           0
ARP packet input number:           0
  Request packet:                  0
  Reply packet:                    0
  Unknown packet:                  0
Internet Address is 10.1.1.1/16
Broadcast address : 10.1.255.255
TTL being 1 packet number:         0
TTL invalid packet number:         0
ICMP packet input number:          0
  Echo reply:                      0
  Unreachable:                     0
  Source quench:                   0
  Routing redirect:                0
  Echo request:                    0
  Router advert:                   0
  Router solicit:                  0
  Time exceed:                     0
  IP header bad:                   0
  Timestamp request:               0
  Timestamp reply:                 0
  Information request:             0
  Information reply:               0
  Netmask request:                 0
  Netmask reply:                   0
  Unknown type:                    0

```

**Table 1** Description of the **display ip interface** command output
| Item | Description |
| --- | --- |
| current state | Physical status of an interface. The possible physical states are as follows:   * UP: The physical layer of the interface is Up. * DOWN: The physical layer of the interface is Down. * Administratively DOWN: If the administrator runs the shutdown command on the interface, the interface status is Administratively DOWN. * UP(DF backup down): The interface goes Down due to EVPN DF election.   The actual supported physical status depends on the actual device. |
| Line protocol current state | Link layer protocol status of the interface:   * UP. * DOWN: The link layer protocol status of the interface is Down, or no IP address is assigned to the interface. For example, if no IP address is assigned to an IP service-capable interface,its protocol status is Down. * DOWN (dampening suppressed):The interface is being suppressed by the protocol module. * Administratively down: The administrator runs the shutdown network-layer command on the interface. |
| input packets | Total number of packets, bytes, and multicast packets received by the interface. |
| output packets | Total number of packets, bytes, and multicast packets sent by the interface. |
| Directed-broadcast packets | Number of packets broadcast on the interface directly. |
| received packets | Total number of packets received by the interface. |
| forwarded packets | Total number of packets forward by the interface. |
| ARP packet input number | Total number of ARP packets received by the interface. |
| Request packet | Number of request packets. |
| Reply packet | Number of response packets. |
| Unknown packet | Number of unknown packets. |
| Unknown type | Number of packets of the unknown type. |
| Internet Address | IP address of the interface. |
| Internet Address is unnumbered | Unnumbered IP Address of Interface. |
| Broadcast address | Broadcast address of the interface. |
| TTL being 1 packet number | Number of packets with time to live (TTL) of 1. |
| TTL invalid packet number | Number of packets with invalid TTL values. |
| ICMP packet input number | Number of received Internet Control Message Protocol (ICMP) packets. |
| Echo reply | Number of echo-reply packets. |
| Echo request | Number of echo-request packets. |
| Source quench | Number of source suppress packets. |
| Routing redirect | Number of redirected packets. |
| Router advert | Number of router-advertising packets. |
| Router solicit | Number of router-soliciting packets. |
| Time exceed | Number of timeout packets. |
| IP header bad | Number of packets with the corrupted IP header. |
| Timestamp request | Number of timestamp-requiring packets. |
| Timestamp reply | Number of timestamp-replying packets. |
| Information request | Number of information-requiring packets. |
| Information reply | Number of information-replying packets. |
| Netmask request | Number of mask-requiring packets. |
| Netmask reply | Number of mask-replying packets. |
| Unreachable | Number of packets with unreachable destination. |
| the maximum transmit unit | Maximum transmission unit. |