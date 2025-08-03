anti-attack tcp-syn enable
==========================

anti-attack tcp-syn enable

Function
--------



The **anti-attack tcp-syn enable** command enables defense against TCP SYN flood attacks.

The **anti-attack tcp-syn disable** command disables defense against TCP SYN flood attacks.

The **undo anti-attack tcp-syn enable** command disables defense against TCP SYN flood attacks.



By default, defense against TCP SYN flood attacks is enabled.


Format
------

**anti-attack tcp-syn enable**

**anti-attack tcp-syn disable**

**undo anti-attack tcp-syn enable**


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

An attacker sends a SYN packet to a target host to initiate a TCP connection but does not respond to the SYN-ACK sent from the target host. If the target host receives no ACK packet from the attacker, it keeps waiting for the ACK packet. A half-open connection is formed. The attacker keeps sending SYN packets, so many half-open connections are set up on the target host. This wastes a large number of resources. To prevent TCP SYN flood attacks, run the anti-attack tcp-syn enable command to enable defense against TCP SYN flood attacks.The device detects TCP SYN flood attack packets after defense against TCP SYN flood attacks is enabled. If the device detects TCP SYN flood attack packets, the device limits the rate of these TCP SYN flood attack packets to ensure that the device CPU works properly.


Example
-------

# Enable defense against TCP SYN flood attacks.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack tcp-syn enable

```