display icmp statistics
=======================

display icmp statistics

Function
--------

The **display icmp statistics** command displays ICMP packet statistics.



Format
------

**display icmp statistics**

**display icmp statistics interface** { *interface-name* | *interface-type* *interface-num* }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Displays ICMP packet statistics based on a specified interface name. | - |
| **interface** *interface-type* *interface-num* | Displays ICMP packet statistics based on a specified interface type and number. | - |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

The Internet Control Message Protocol (ICMP) is an error-reporting mechanism and is used by IP or an upper-layer protocol (TCP or UDP). An ICMP packet is encapsulated as a part of an IP datagram and transmitted through the Internet.

When an error occurs during the IP datagram forwarding, ICMP reports the error to the source of the IP datagram, but does not rectify the error or notify the intermediate devices of the error.To check statistics about ICMP packets, including sent and received ICMP error packets, echo request packets, and echo reply packets, run the
**display icmp statistics** command.During the ping or traceroute operations, for example, run the
**display icmp statistics** command on the Router to check whether the number of sent and received packets is correct.

**Precautions**

Network attackers sometimes make use of ICMP packets to obtain network information for attacking the network. If the "destination unreachable", "redirects", "echo reply", and "time exceeded" field values displayed are large, check whether the device is being attacked.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display statistics about ICMP packets.
```
<HUAWEI> display icmp statistics
------------------------ Display ICMP Statistics ----------------------
Received packets:
        bad formats:         0          bad checksum:             0
        echo:                2          destination unreachable:  0
        source quench:       0          redirects:                0
        echo reply:          0          parameter problem:        0
        timestamp request:   0          information request:      0
        mask requests:       0          mask replies:             0
        time exceeded:       0          timestamp reply:          0
        Mping request:       0          Mping reply:              0
Sent packets:
        echo:                0          destination unreachable:  0
        source quench:       0          redirects:                0
        echo reply:          2          parameter problem:        0
        timestamp request:   0          information reply:        0
        mask requests:       0          mask replies:             0
        time exceeded:       0          timestamp reply:          0
        Mping request:       0          Mping reply:              0
-----------------------------------------------------------------------

```


**Table 1** Description of the
**display icmp statistics** command output

| Item | Description |
| --- | --- |
| bad formats | Number of packets with incorrect formats. |
| bad checksum | Number of packets with incorrect checksums. |
| echo | Number of echo request packets. |
| echo reply | Number of echo reply packets. |
| destination unreachable | Number of destination unreachable packets. |
| source quench | Number of source quench packets. |
| redirects | Number of redirect packets. |
| parameter problem | Number of packets with incorrect parameters. |
| timestamp request | Number of timestamp request packets. |
| timestamp reply | Number of timestamp reply packets. |
| information request | Number of information request packets. |
| mask requests | Number of mask request packets. |
| mask replies | Number of mask reply packets. |
| time exceeded | Number of timeout packets. |
| Mping request | Number of multicast ping request packets. |
| Mping reply | Number of multicast ping reply packets. |
| Received packets | Received packet statistics. |
| Sent packets | Sent packet statistics. |