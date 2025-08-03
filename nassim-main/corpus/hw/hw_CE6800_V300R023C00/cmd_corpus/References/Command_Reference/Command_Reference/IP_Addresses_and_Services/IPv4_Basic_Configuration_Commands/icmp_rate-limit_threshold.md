icmp rate-limit threshold
=========================

icmp rate-limit threshold

Function
--------



The **icmp rate-limit threshold** command sets an ICMP packet rate limit.

The **undo icmp rate-limit threshold** command restores the default ICMP packet rate limit.



By default, the rate threshold for global ICMP packets is 1500 pps.


Format
------

**icmp rate-limit threshold** *threshold-value*

**undo icmp rate-limit threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **threshold** *threshold-value* | Specified an ICMP packet rate limit. | The value is an integer ranging from 0 to 5000, in pps. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In normal situations, the router can correctly receive ICMP packets. In the case of heavy network traffic, if hosts or ports are frequently unreachable, the router receives a large number of ICMP packets, which causes heavier traffic burden and performance deterioration. In addition, network attackers often make use of ICMP error packets to probe the internal network structure.To improve device performance and enhance network security, run the **icmp rate-limit threshold** command to set the ICMP packet rate limit.After the **icmp rate-limit threshold** command is run, when the rate at which ICMP messages are sent over a specified interface exceeds the limit, an ACL is automatically delivered to allow the device to discard ICMP messages destined for the local device and start the ICMP packet rate limit timer.



**Prerequisites**



ICMP packet rate limiting has been enabled using the **undo icmp rate-limit disable** command in the system view.




Example
-------

# Set a rate limit for ICMP messages sent.
```
<HUAWEI> system-view
[~HUAWEI] undo icmp rate-limit disable
[*HUAWEI] icmp rate-limit threshold 900

```