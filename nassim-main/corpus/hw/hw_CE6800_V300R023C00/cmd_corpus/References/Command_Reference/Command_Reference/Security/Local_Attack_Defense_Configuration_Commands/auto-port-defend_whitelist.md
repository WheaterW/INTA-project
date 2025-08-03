auto-port-defend whitelist
==========================

auto-port-defend whitelist

Function
--------



The **auto-port-defend whitelist** command configures a whitelist for port attack defense.

The **undo auto-port-defend whitelist** command deletes a whitelist for port attack defense.



By default, no whitelist is configured for port attack defense.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**auto-port-defend whitelist** *whitelist-id* { **acl** *acl-number* | **interface** { *interface-name* | *interface-type* *interface-number* } }

**undo auto-port-defend whitelist** *whitelist-id*

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**auto-port-defend whitelist** *whitelist-id* { **acl** **ipv6** *ipv6-acl-number* | **interface** { *interface-name* | *interface-type* *interface-number* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *whitelist-id* | Specifies the ID of a whitelist. | The value is an integer ranging from 1 to 32. |
| **acl** *acl-number* | Specifies the number of an ACL referenced by a whitelist. | The value is an integer that ranges from 2000 to 4999.   * 2000 to 2999: basic ACLs * 3000 to 3999: advanced ACLs * 4000 to 4999: Layer 2 ACLs |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface to which the whitelist is applied.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
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

The port attack defense function is enabled by default on the device, so the device calculates protocol packet rates on all interfaces, and traces the source and limits the rate of attack packets. In some services, network-side interfaces need to receive a lot of valid protocol packets. You should add these interfaces or network nodes connecting to these interfaces to the whitelist. The device does not trace the source or limit the rate of protocol packets received by the interfaces in the whitelist. In this manner, the CPU can promptly process the packets from the network-side interfaces.

**Precautions**

To define the whitelist using an ACL, you must create an ACL and configure rules for the ACL.Before configuring an ACL whitelist for some protocols, ensure that the port attack defense function supports these protocols. Use the **auto-port-defend protocol** command to specify the protocols to which port attack defense is applied.


Example
-------

# In the attack defense policy test, configure a whitelist that references an ACL. The ACL permits the packets from the users with IP addresses 10.1.1.1 and 10.1.1.2.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] rule permit source 10.1.1.1 0
[*HUAWEI-acl4-basic-2000] rule permit source 10.1.1.2 0
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend whitelist 1 acl 2000

```

# In the attack defense policy test, add interface 100GE1/0/1 to the whitelist for port attack defense.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend whitelist 1 interface 100GE 1/0/1

```