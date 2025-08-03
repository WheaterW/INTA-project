auto-defend whitelist
=====================

auto-defend whitelist

Function
--------



The **auto-defend whitelist** command configures a whitelist for attack source tracing. The device does not check the source of users in the whitelist.

The **undo auto-defend whitelist** command deletes a whitelist for attack source tracing.



By default, no whitelist is configured.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**auto-defend whitelist** *whitelist-id* { **acl** *acl-number* | **interface** { *interface-name* | *interface-type* *interface-number* } }

**undo auto-defend whitelist** *whitelist-id*

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**auto-defend whitelist** *whitelist-id* { **acl** **ipv6** *ipv6-acl-number* | **interface** { *interface-name* | *interface-type* *interface-number* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *whitelist-id* | Specifies the ID of a whitelist. | The value is an integer ranging from 1 to 32. |
| **acl** *acl-number* | Specifies the number of an ACL referenced by a whitelist. | The value is an integer that ranges from 2000 to 4999.   * 2000 to 2999: basic ACLs * 3000 to 3999: advanced ACLs * 4000 to 4999: Layer 2 ACLs |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface to which the whitelist is applied.   * interface-type specifies the interface type. * interface-number specifies the interface number. | The value must be set according to the device configuration. |
| **ipv6** *ipv6-acl-number* | Specifies the number of an ACL6 referenced by a whitelist.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 2000 to 3999.   * 2000 to 2999: basic ACL6s * 3000 to 3999: advanced ACL6s |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Attack source tracing helps locate and punish sources of denial of service (DoS) attacks. If some users do not need to be traced regardless of whether an attack occurs, run the auto-defend whitelist command to configure a whitelist for users.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command.

**Precautions**

Before referencing an ACL in a whitelist, create the ACL and configure rules.If the ACL referenced by the whitelist specifies some protocols, ensure that packets of these protocols can be traced. If a specified protocol is not supported by attack source tracing, you can run the **auto-defend protocol** command to configure attack source tracing to support the protocol.


Example
-------

# Add source IP addresses 10.1.1.1 and 10.1.1.2 to the whitelist for attack source tracing.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] rule permit source 10.1.1.1 0
[*HUAWEI-acl4-basic-2000] rule permit source 10.1.1.2 0
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] auto-defend whitelist 1 acl 2000

```