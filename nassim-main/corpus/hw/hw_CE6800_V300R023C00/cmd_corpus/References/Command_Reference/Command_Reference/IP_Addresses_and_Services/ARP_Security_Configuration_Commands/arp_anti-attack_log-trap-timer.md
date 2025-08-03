arp anti-attack log-trap-timer
==============================

arp anti-attack log-trap-timer

Function
--------



The **arp anti-attack log-trap-timer** command sets the interval for recording logs and generating alarms about potential attacks.

The **undo arp anti-attack log-trap-timer** command restores the default configuration.

The default value is 0. If the default value is used, the device does not record logs or generate alarms about potential attacks.



The default value is 0. If the default value is used, the device does not record logs or generate alarms about potential attacks.


Format
------

**arp anti-attack log-trap-timer** *timer*

**undo arp anti-attack log-trap-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timer* | Specifies the interval for recording logs and generating alarms about potential attacks. | The value is an integer ranging from 0 to 1200, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After Address Resolution Protocol (ARP) Miss message rate limit is configured, the device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds a specified limit, the device discards additional ARP Miss messages. The device considers this problem as a potential attack. The device records logs and generates alarms about potential attacks.If a large number of potential attacks occur, the device may record a large number of logs and generate a large number of alarms. To resolve this problem, run the arp anti-attack log-trap-timer command to configure the interval for recording logs and generating alarms about potential attacks to reduce the number of logs and alarms.



**Configuration Impact**



After the interval for recording logs and generating alarms about potential attacks is configured, the device discards the logs and alarms generated within this interval. As a result, the device will not notify you of any faults that occur within this interval.




Example
-------

# Set the interval for recording logs and generating alarms about potential attacks to 20s.
```
<HUAWEI> system-view
[~HUAWEI] arp anti-attack log-trap-timer 20

```