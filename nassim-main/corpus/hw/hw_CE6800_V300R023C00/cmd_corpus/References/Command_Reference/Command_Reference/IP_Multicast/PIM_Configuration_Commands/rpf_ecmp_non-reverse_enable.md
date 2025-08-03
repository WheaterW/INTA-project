rpf ecmp non-reverse enable
===========================

rpf ecmp non-reverse enable

Function
--------



The **rpf ecmp non-reverse enable** command is used to disable the ECMP switchback function for PIM.

The **undo rpf ecmp non-reverse enable** command restores the default configuration.



By default, the multicast traffic is switched back to higher priority primary link, when the primary link recovers.


Format
------

**rpf ecmp non-reverse enable**

**undo rpf ecmp non-reverse enable**


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

**Usage Scenario**

In an ECMP scenario, when the primary link which takes over multicast traffic is down, the multicast traffic is switched over to a secondary ECMP link. After the primary link recovers, the multicast traffic is switched to the primary link. During a switchover, the multicast packets may be discarded or repeatedly sent. To address this issue, run the rpf ecmp non-reverse enable command, the traffic is not switched back to the primary link even if the primary link recovers.After the rpf ecmp non-reverse enable command is configured, traffic is not switched back to the primary link even if the recovered primary link has higher priority. Traffic will be switched back to the primary link only when the secondary link fails.

**Precautions**

The rpf ecmp non-reverse enable command can be configured only in IPv4 PIM-SM.If the rpf ecmp non-reverse enable command is mutually exclusive with load balance configurations.


Example
-------

# Disable the ECMP switchback function in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] pim
[*HUAWEI-pim] rpf ecmp non-reverse enable

```