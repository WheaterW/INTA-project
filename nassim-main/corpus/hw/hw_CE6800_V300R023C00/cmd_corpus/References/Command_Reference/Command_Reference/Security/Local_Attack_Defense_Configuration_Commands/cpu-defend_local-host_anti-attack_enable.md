cpu-defend local-host anti-attack enable
========================================

cpu-defend local-host anti-attack enable

Function
--------



The **cpu-defend local-host anti-attack enable** command enables host attack defense.

The **undo cpu-defend local-host anti-attack enable** command disables host attack defense.



By default, host attack defense is disabled.


Format
------

**cpu-defend local-host anti-attack enable**

**undo cpu-defend local-host anti-attack enable**


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

After the **ssh server acl**, **telnet server acl** command is configured, a switch forwards SSH or Telnet packets to the CPU and matches these packets against software ACLs. When host attack defense is enabled, the switch matches these packets against hardware ACLs. If packets match an ACL with a deny action, the switch directly discards the packets and will no longer forward such packets to the CPU.


Example
-------

# Enable host attack defense.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend local-host anti-attack enable

```