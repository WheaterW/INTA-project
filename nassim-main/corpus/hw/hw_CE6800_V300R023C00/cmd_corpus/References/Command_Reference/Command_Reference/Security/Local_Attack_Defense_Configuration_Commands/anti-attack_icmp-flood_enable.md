anti-attack icmp-flood enable
=============================

anti-attack icmp-flood enable

Function
--------



The **anti-attack icmp-flood enable** command enables defense against ICMP flood attacks.

The **anti-attack icmp-flood disable** command disables defense against ICMP flood attacks.

The **undo anti-attack icmp-flood enable** command disables defense against ICMP flood attacks.



By default, defense against ICMP flood attacks is enabled.


Format
------

**anti-attack icmp-flood enable**

**anti-attack icmp-flood disable**

**undo anti-attack icmp-flood enable**


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

If an attacker sends a large number of ICMP request packets to the target host in a short time, the target host is busy with these ICMP request packets. As a result, the target host is overloaded and cannot process normal services. To prevent ICMP flood attacks, run the anti-attack icmp-flood enable command to enable defense against ICMP flood attacks.The device detects ICMP flood attack packets after defense against ICMP flood attacks is enabled. If the device detects ICMP flood attack packets, the device limits the rate of these ICMP flood attack packets to ensure that the device CPU works properly.


Example
-------

# Enable defense against ICMP flood.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack icmp-flood enable

```