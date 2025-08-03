icmp rate-limit disable
=======================

icmp rate-limit disable

Function
--------



The **icmp rate-limit disable** command disables ICMP packet rate limiting.

The **undo icmp rate-limit disable** command enables ICMP packet rate limiting.



By default, ICMP packet rate limiting is enabled.


Format
------

**icmp rate-limit disable**

**undo icmp rate-limit disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In normal situations, the router can correctly receive ICMP packets. In the case of heavy network traffic, if hosts or ports are frequently unreachable, the router receives a large number of ICMP packets, which causes heavier traffic burden and performance deterioration. In addition, network attackers often make use of ICMP error packets to probe the internal network structure.To improve device performance and enhance network security, run the **undo icmp rate-limit disable** command to enable ICMP packet rate limiting.



**Follow-up Procedure**



Run the **icmp rate-limit interface** command to set an ICMP packet rate limit.



**Precautions**



When the network status is normal, run the **undo icmp rate-limit disable** command to disable ICMP packet rate limiting.




Example
-------

# Enable ICMP packet rate limiting.
```
<HUAWEI> system-view
[~HUAWEI] undo icmp rate-limit disable

```