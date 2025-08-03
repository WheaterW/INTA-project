reset evpn mac-duplication
==========================

reset evpn mac-duplication

Function
--------



The **reset evpn mac-duplication** command clears MAC route suppression status of all EVPN instances.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset evpn mac-duplication**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If you are sure that MAC routes of all EVPN instances will no longer flap and want to restore the MAC routes immediately instead of waiting for the suppression recovery time to expire, run the clear mac-route dampening command to clear the suppression status of MAC routes of all EVPN instances.


Example
-------

# Clear the suppression status of MAC routes in all EVPN instances.
```
<HUAWEI> reset evpn mac-duplication

```