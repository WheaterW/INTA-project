pim neighbor-policy
===================

pim neighbor-policy

Function
--------



The **pim neighbor-policy** command configures a policy for filtering PIM neighbors and sets a valid range for PIM neighbor addresses.

The **undo pim neighbor-policy** command restores the default configuration.



By default, no policy is configured for filtering PIM neighbors, and the valid range of PIM neighbor addresses is not limited.


Format
------

**pim neighbor-policy** { *basic-acl-number* | **acl-name** *acl-name* }

**undo pim neighbor-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect a Router against pseudo PIM Hello message attacks, run the pim neighbor-policy command to set a range of valid PIM neighbor addresses. The Router then discards Hello messages received from Routers whose addresses are not in the specified range.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the pim neighbor-policy command is run more than once, the latest configuration overrides the previous one.After the pim neighbor-policy command is configured, an interface sets up neighbor relationships only with the devices whose IP addresses are in the specified range of valid addresses.

* If a Router address is permitted by the ACL, Hello messages sent by this Router are accepted.
* If a Router address is denied by the ACL or no action is configured for this Router address, Hello messages sent by this Router are discarded.
* If the ACL specified in the pim neighbor-policy command does not exist, all Hello messages are discarded.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# In the public network instance, configure an interface to permit only Hello messages sent by Routers on the network segment 10.1.1.0/24.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2001
[*HUAWEI-acl4-basic-2001] rule permit source 10.1.1.0 0.0.0.255
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim neighbor-policy 2001

```