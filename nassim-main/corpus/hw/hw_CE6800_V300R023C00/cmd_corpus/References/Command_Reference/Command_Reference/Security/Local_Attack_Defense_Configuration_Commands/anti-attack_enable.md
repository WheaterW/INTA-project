anti-attack enable
==================

anti-attack enable

Function
--------



The **anti-attack enable** command enables defense against all attack packets.

The **anti-attack disable** command disables defense against all attack packets.

The **undo anti-attack enable** command disables defense against all attack packets.



By default, defense against all attack packets is enabled.


Format
------

**anti-attack enable**

**anti-attack disable**

**undo anti-attack enable**


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

Different types of attacks on a network cause high device usage or even system breakdown, affecting network services. To prevent the system from breaking down and to ensure normal network services, run the **anti-attack enable** command to enable defense against all attack packets.Running the **anti-attack enable** command is equivalent to running all of the following commands: **anti-attack abnormal enable**, **anti-attack fragment enable**, **anti-attack tcp-syn enable**, **anti-attack udp-flood enable**, and **anti-attack icmp-flood enable**.


Example
-------

# Enable defense against all attack packets.
```
<HUAWEI> system-view
[~HUAWEI] anti-attack enable

```