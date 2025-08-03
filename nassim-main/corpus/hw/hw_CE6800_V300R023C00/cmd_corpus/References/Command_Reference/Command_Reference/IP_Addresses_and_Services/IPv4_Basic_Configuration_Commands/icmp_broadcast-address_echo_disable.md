icmp broadcast-address echo disable
===================================

icmp broadcast-address echo disable

Function
--------



The **icmp broadcast-address echo disable** command disables the system from responding to ICMP echo messages whose destination addresses are broadcast addresses.

The **undo icmp broadcast-address echo disable** command enables the system to respond to ICMP echo messages whose destination addresses are broadcast addresses.



By default, the system responds to all ICMP request messages.


Format
------

**icmp broadcast-address echo disable**

**undo icmp broadcast-address echo disable**


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



Network attackers may launch attacks with ICMP messages whose destination addresses are broadcast addresses, increasing the traffic burden and deteriorating device performance. To improve device performance and enhance network security, run the **icmp broadcast-address echo disable** command to disable the system from responding to ICMP echo messages whose destination addresses are broadcast addresses. This configuration helps defend against attacks by such ICMP messages.



**Precautions**



The system cannot discard broadcast ping packets sent by itself.When the network status is normal, run the **undo icmp broadcast-address echo disable** command to enable the system to respond to ICMP echo messages whose destination addresses are broadcast addresses.




Example
-------

# Disable the system from responding to ICMP echo messages whose destination addresses are broadcast addresses.
```
<HUAWEI> system-view
[~HUAWEI] icmp broadcast-address echo disable

```