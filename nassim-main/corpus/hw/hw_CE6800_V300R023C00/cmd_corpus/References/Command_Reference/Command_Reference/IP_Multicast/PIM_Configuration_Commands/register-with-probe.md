register-with-probe
===================

register-with-probe

Function
--------



The **register-with-probe** command disables the source's DR from sending Register messages. When the DR receives multicast traffic, only Probe messages are sent to RP.

The **undo register-with-probe** command restores the default configuration.



By default, when the DR receives multicast traffic, it sends Register messages to the RP.


Format
------

**register-with-probe**

**undo register-with-probe**


Parameters
----------

None

Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the source's DR receives multicast data, it sends Register messages to the RP, and add registered egress interface. If too many redundant Register messages are sent to RP, the performance is affected. Run the register-with-probe command to disable Register messages sending function on the source's DR, the DR sends Probe messages instead of Register messages, so that the performance is not affected.


Example
-------

# In the public network instance, configure the source DP to send Probe messages but not Register messages to the RP.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] register-with-probe

```