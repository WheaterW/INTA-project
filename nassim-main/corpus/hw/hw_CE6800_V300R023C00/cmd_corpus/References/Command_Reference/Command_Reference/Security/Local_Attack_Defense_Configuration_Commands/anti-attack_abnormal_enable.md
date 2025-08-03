anti-attack abnormal enable
===========================

anti-attack abnormal enable

Function
--------



The **anti-attack abnormal enable** command enables defense against malformed packet attacks.

The **anti-attack abnormal disable** command disables defense against malformed packet attacks.

The **undo anti-attack abnormal enable** command disables defense against malformed packet attacks.



By default, defense against malformed packets is enabled.


Format
------

**anti-attack abnormal enable**

**anti-attack abnormal disable**

**undo anti-attack abnormal enable**


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

The malformed packet attack is to send malformed IP packets to the system. If such an attack occurs, the system may break down when processing the malformed IP packets. To ensure network services work normally, run the anti-attack abnormal enable command to enable defense against malformed packets.The device directly discards packets of the following types:

* Flooding without IP payload
* IGMP null packet
* LAND attack
* Smurf attack
* TCP flag bit invalid attack

Example
-------

# Enable defense against malformed packet attacks.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack abnormal enable

```