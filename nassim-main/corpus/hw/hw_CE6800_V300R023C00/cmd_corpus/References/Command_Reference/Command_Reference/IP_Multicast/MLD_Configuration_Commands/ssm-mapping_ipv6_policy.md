ssm-mapping ipv6 policy
=======================

ssm-mapping ipv6 policy

Function
--------



The **ssm-mapping ipv6 policy** command configures an IPv6 SSM mapping policy.

The **undo ssm-mapping ipv6 policy** command deletes an IPv6 SSM mapping policy.



By default, no IPv6 SSM mapping policy is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ssm-mapping ipv6 policy** *policy-name*

**undo ssm-mapping ipv6 policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Sets an SSM mapping policy name. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported. The string can contain spaces if it is enclosed in double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If users connected different interfaces need to receive multicast service flows from different sources, run the **ssm-mapping ipv6 policy** command to configure an SSM mapping policy. Then, under the policy, configure mapping policies for different interfaces, so that MLD messages can map to different multicast sources.When an IPv6 SSM mapping policy is deleted, all configurations of the policy will be deleted.


Example
-------

# Create an SSM mapping policy named ssmmap1 in the system view.
```
<HUAWEI> system-view
[~HUAWEI] ssm-mapping ipv6 policy ssmmap1
[*HUAWEI-ssm-map6-ssmmap1]

```