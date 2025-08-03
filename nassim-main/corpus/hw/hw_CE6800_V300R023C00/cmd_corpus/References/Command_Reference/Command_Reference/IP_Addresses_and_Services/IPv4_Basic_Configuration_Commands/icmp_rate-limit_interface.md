icmp rate-limit interface
=========================

icmp rate-limit interface

Function
--------



The **icmp rate-limit interface** command sets an ICMP packet rate limit.

The **undo icmp rate-limit interface** command restores the default ICMP packet rate limit.



By default, no ICMP packet rate limit is configured on an interface, and the global ICMP packet rate limit (1500 pps) is used as the ICMP packet rate limit on the interface.


Format
------

**icmp rate-limit interface** { *interface-name* | *interface-type* *interface-number1* } [ **to** *interface-number2* ] **threshold** *threshold-value*

**undo icmp rate-limit interface** { *interface-name* | *interface-type* *interface-number1* } [ **to** *interface-number2* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *interface-number2* | Specified the number of an interface for which ICMP messages are destined. | - |
| **threshold** *threshold-value* | Specified an ICMP packet rate limit. | The value is an integer ranging from 0 to 5000, in pps. |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number1* | Specifies the type and number of an interface. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In normal situations, the router can correctly receive ICMP packets. In the case of heavy network traffic, if hosts or ports are frequently unreachable, the router receives a large number of ICMP packets, which causes heavier traffic burden and performance deterioration. In addition, network attackers often make use of ICMP error packets to probe the internal network structure.To improve device performance and enhance network security, run the **icmp rate-limit interface** command to set the ICMP packet rate limit.After the **icmp rate-limit interface** command is run, when the rate at which ICMP messages are sent over a specified interface exceeds the limit, an ACL is automatically delivered to allow the device to discard ICMP messages destined for the local device and start the ICMP packet rate limit timer.



**Prerequisites**



ICMP packet rate limiting has been enabled using the **undo icmp rate-limit disable** command in the system view.



**Configuration Impact**



If the **icmp rate-limit interface** command is run more than once, all configurations take effect.



**Precautions**



If the **icmp rate-limit interface** command is run on an interface, the rate at which ICMP packets are sent on the interface does not exceed the configured rate limit. If the **icmp rate-limit interface** command is run on multiple interfaces, the sum of the rates at which ICMP packets are sent on these interfaces does not exceed the global ICMP packet rate limit.




Example
-------

# Set a rate limit for ICMP messages sent from 1/0/1 interface to 1/0/2.
```
<HUAWEI> system-view
[~HUAWEI] undo icmp rate-limit disable
[*HUAWEI] icmp rate-limit interface 100GE 1/0/1 to 1/0/2 threshold 900

```