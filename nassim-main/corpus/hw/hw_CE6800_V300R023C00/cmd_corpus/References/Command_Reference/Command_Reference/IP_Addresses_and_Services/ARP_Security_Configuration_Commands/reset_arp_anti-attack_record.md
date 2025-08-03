reset arp anti-attack record
============================

reset arp anti-attack record

Function
--------



The **reset arp anti-attack record** command clears information about discarded Address Resolution Protocol (ARP) packets whose rate exceeds the limit.

The **reset arp miss anti-attack record** command clears information about discarded Address Resolution Protocol (ARP) Miss messages whose rate exceeds the limit.




Format
------

**reset arp anti-attack record**

**reset arp miss anti-attack record**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After ARP packet rate limit is configured, the device counts the number of received ARP packets. If the number of ARP packets received in a specified period exceeds the upper limit, the device discards the excess ARP packets. To facilitate fault location, the device records information about discarded ARP packets whose rate exceeds the limit. To clear information about discarded ARP packets whose rate exceeds the limit, run the reset arp anti-attack record command.After ARP Miss message rate limit is configured, the device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds the upper limit, the device discards the excess ARP Miss messages. To facilitate fault location, the device records information about discarded ARP Miss messages whose rate exceeds the limit. To clear information about discarded ARP Miss messages whose rate exceeds the limit, run the reset arp miss anti-attack record command.




Example
-------

# Clear information about discarded ARP packets whose rate exceeds the limit.
```
<HUAWEI> reset arp anti-attack record

```

# Clear information about discarded ARP Miss message whose rate exceeds the limit.
```
<HUAWEI> reset arp miss anti-attack record

```