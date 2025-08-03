mac-duplication (EVPN instance view)
====================================

mac-duplication (EVPN instance view)

Function
--------



The **mac-duplication** command displays the EVPN-MAC-duplication view.



By default, the EVPN-MAC-duplication view is not displayed.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-duplication**


Parameters
----------

None

Views
-----

EVPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To modify the configuration of MAC duplication suppression, run the **mac-duplication** command to enter the EVPN-MAC-duplication view first. Then, run the **detect loop-times** command to modify the parameter settings of the function.

**Precautions**

To ensure that MAC duplication suppression works as expected, you are advised to run the mac-address learning disable command on NVE interfaces.


Example
-------

# Enter the EVPN-MAC-duplication view.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 100
[*HUAWEI-bd100] evpn
[*HUAWEI-bd100-evpn] mac-duplication

```