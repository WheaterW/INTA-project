display vxlan troubleshooting
=============================

display vxlan troubleshooting

Function
--------



The **display vxlan troubleshooting** command displays causes for VXLAN tunnel Down events and dynamic VXLAN tunnel establishment failures.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vxlan troubleshooting**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If a VXLAN tunnel goes Down or fails to be dynamically created, run the **display vxlan troubleshooting** command to check causes for fault locating.This command can display causes for the recent five VXLAN tunnel Down events and dynamic VXLAN tunnel establishment failures at most.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display causes for the VXLAN tunnel Down events and dynamic VXLAN tunnel establishment failures.
```
<HUAWEI> display vxlan troubleshooting
Total counts: 2
--------------------------------------------------------------------------------
Sequence   Time                       Event Description                         
--------------------------------------------------------------------------------
1          2016-02-26 01:40:22        The VXLAN tunnel is down because the route
                                       to the source or destination address is u
                                      nreachable (SourceIpAddress=1.1.1.1, Desti
                                      nationIpAddress=2.2.2.2).                 
2          2016-02-26 01:40:22        The number of VXLAN tunnel exceeded the thr
                                      eshold (Threshold=16384). 
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display vxlan troubleshooting** command output
| Item | Description |
| --- | --- |
| Total counts | Number of VXLAN tunnel Down events and dynamic VXLAN tunnel establishment failures. |
| Sequence | Sequence number. |
| Time | Time when a VXLAN tunnel went Down or failed to be dynamically created. |
| Event Description | Cause for a VXLAN tunnel Down event or dynamic VXLAN tunnel establishment failure. |