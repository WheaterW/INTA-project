anti-attack udp-flood enable
============================

anti-attack udp-flood enable

Function
--------



The **anti-attack udp-flood enable** command enables defense against UDP flood attacks.

The **anti-attack udp-flood disable** command disables defense against UDP flood attacks.

The **undo anti-attack udp-flood enable** command disables defense against UDP flood attacks.



By default, defense against UDP flood attacks is enabled.


Format
------

**anti-attack udp-flood enable**

**anti-attack udp-flood disable**

**undo anti-attack udp-flood enable**


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

If an attacker sends a large number of UDP packets to the target host in a short time, the target host is busy with these UDP packets. As a result, the target host is overloaded and cannot process normal services. To prevent UDP flood attacks, run the anti-attack udp-flood enable command to enable defense against UDP flood attacks.The device detects UDP flood attack packets after defense against UDP flood attacks is enabled. The device directly discards UDP flood attack packets.


Example
-------

# Enable defense against UDP flood attacks.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack udp-flood enable

```