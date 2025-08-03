display igmp snooping querier
=============================

display igmp snooping querier

Function
--------



The **display igmp snooping querier** command displays querier configurations.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display igmp snooping querier vlan** [ *vlanid* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping querier bridge-domain** [ *bdid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bridge-domain** *bdid* | Displays querier configurations in a specified BD. If bd-id is not specified, IGMP querier configurations in all BDs will be displayed.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The bd-id value is an integer ranging from 1 to 16777215. |
| **vlan** *vlanid* | Displays querier configurations in a specified VLAN. If vlan-id is not specified, IGMP querier configurations in all VLANs will be displayed. | The value is an integer that ranges from 1 to 4094. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If IGMP messages sent from an upstream router may not reach a downstream Layer 2 device due to specific causes (for example, IGMP is not enabled on the upstream router) or the upstream router does not need to learn multicast forwarding entries dynamically because static entries are configured, the Layer 2 device can be configured as a querier to replace the upstream router to send IGMP Query messages. This reduces the burden of the upstream device. The display igmp-snooping querier command can be used to view querier configurations.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display querier configurations in all VLANs.
```
<HUAWEI> display igmp snooping querier vlan
VLAN                            Querier-state     Querier
------------------------------------------------------------
1                                Enable           192.168.0.1
2                                Disable          --
3                                Disable          --
-----------------------------------------------------------
total entry 3

```

**Table 1** Description of the **display igmp snooping querier** command output
| Item | Description |
| --- | --- |
| VLAN | VLAN ID. |
| Querier-state | Querier status:   * Disable: indicates that the querier has not been started. * Enable: indicates that the querier has been started. |
| Querier | IP address of a querier. |
| total entry 3 | Total three pieces of querier information. |