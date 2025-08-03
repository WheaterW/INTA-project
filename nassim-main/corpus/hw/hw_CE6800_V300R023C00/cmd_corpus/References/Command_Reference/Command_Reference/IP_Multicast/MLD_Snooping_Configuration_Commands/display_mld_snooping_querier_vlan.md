display mld snooping querier vlan
=================================

display mld snooping querier vlan

Function
--------



The **display mld snooping querier vlan** command displays querier configurations.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld snooping querier vlan** [ *vlan-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays querier configurations in a specified VLAN. If vlan-id is not specified, MLD querier configurations in all VLANs are displayed. | The value is an integer ranging from 1 to 4094. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If MLD messages sent from an upstream Layer 3 device fail to reach a downstream Layer 2 device or the upstream device is not configured to learn multicast forwarding entries dynamically, queriers can be configured on the Layer 2 device to send MLD Query messages on behalf of the Layer 3 device. This reduces the burden of the upstream device. To check querier configurations, run the display mld snooping querier command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display querier configurations in all VLANs.
```
<HUAWEI> display mld snooping querier vlan
VLAN                            Querier-state Querier
---------------------------------------------------------------
1                               Disable       --
2                               Disable       --
---------------------------------------------------------------
 total entry 2

```

**Table 1** Description of the **display mld snooping querier vlan** command output
| Item | Description |
| --- | --- |
| VLAN | VLAN ID. |
| Querier-state | Querier status:   * Disable: The querier has not been started. * Enable: The querier has been started. |
| Querier | IP address of a querier. |
| total entry 2 | Total two pieces of querier information. |