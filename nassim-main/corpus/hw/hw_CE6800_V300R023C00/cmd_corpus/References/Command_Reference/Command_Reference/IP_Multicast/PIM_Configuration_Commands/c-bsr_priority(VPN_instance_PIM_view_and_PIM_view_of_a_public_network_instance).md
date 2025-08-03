c-bsr priority(VPN instance PIM view/PIM view of a public network instance)
===========================================================================

c-bsr priority(VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **c-bsr priority** command globally sets a priority value for candidate-bootstrap routers (C-BSRs).

The **undo c-bsr priority** command restores the setting.



By default, the global priority value of C-BSRs is 0.


Format
------

**c-bsr priority** *priority*

**undo c-bsr priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a global priority value for C-BSRs. A larger value indicates a higher C-BSR priority. | The value is an integer ranging from 0 to 255. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple C-BSRs are deployed in a PIM-SM domain, a BSR is elected based on the following rules:

* The C-BSR with the highest priority wins.
* If the C-BSRs have the same priority, the C-BSR with the largest IP address wins.To have a C-BSR be elected as the BSR, run the c-bsr priority command to set a larger priority value for the C-BSR than those of the other C-BSRs.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the c-bsr priority command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 5 as the global priority value for C-BSRs.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-bsr priority 5

```