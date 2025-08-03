c-rp priority (VPN instance PIM view/PIM view of a public network instance)
===========================================================================

c-rp priority (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **c-rp priority** command globally sets a priority value for candidate-rendezvous points (C-RPs).

The **undo c-rp priority** command restores the setting.



By default, the global priority value of C-RPs is 0.


Format
------

**c-rp priority** *priority*

**undo c-rp priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a global priority value for C-RPs. A larger value indicates a lower priority. | The value is an integer ranging from 0 to 255. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An RP is elected from C-RPs based on the following rules:

* The C-RP wins if it serves the group address that has the longest mask.
* If group addresses that all C-RPs serve have the same mask length, the C-RP with the highest priority wins (a larger priority value indicates a lower priority).
* If the C-RPs have the same priority, the hash function is started. The C-RP with the greatest calculated value wins.
* If none of the above criteria can determine a winner, the C-RP with the largest address wins.
* To have a C-RP be elected as the RP, run the c-rp priority command to set a lower priority value for the C-RP than those of the other C-RPs.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the c-rp priority command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 5 as the global priority value for C-RPs.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-rp priority 5

```