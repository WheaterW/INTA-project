igmp ip-source-policy
=====================

igmp ip-source-policy

Function
--------



The **igmp ip-source-policy** command configures a policy for filtering Internet Group Management Protocol (IGMP) Report or Leave messages based on source addresses.

The **undo igmp ip-source-policy** command restores the default configuration.



By default, no policy is configured for filtering IGMP Report or Leave messages based on source addresses.


Format
------

**igmp ip-source-policy**

**igmp ip-source-policy** { *basic-acl-number* | **acl-name** *acl-name* }

**undo igmp ip-source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl-number* | Specifies the number of a basic ACL, which defines the range of source addresses. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect a multicast device against attacks from user hosts, source address-based IGMP message filtering enables a multicast device's interface to filter IGMP messages. To ensure the precision in multicast traffic sending, run the **igmp ip-source-policy** command on the multicast device's interface connecting to a user host to enable the multicast device to filter out IGMP messages whose source addresses do not match the permit action in a specified ACL rule.If you have not specified an ACL rule, the rules for filtering IGMP messages based on source addresses are as follows:

* IGMP Report or Leave message are processed if the source addresses in the IP headers are 0.0.0.0 or are on the same network segment as the addresses of the inbound interfaces of the IGMP Report messages.
* IGMP Report or Leave messages are discarded if the source addresses in the IP headers are on different network segments than the addresses of the inbound interfaces of the IGMP Report messages.If you have specified an ACL rule, the interface filters out the IGMP Report, Leave, and Query messages whose source addresses do not match the ACL rule.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command.

**Configuration Impact**

If the **igmp ip-source-policy** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The **igmp ip-source-policy** command requires an ACL configured using the **acl** command. In the basic ACL view, specify the source parameter in the **rule** command to configure an ACL rule.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# In the public network instance, create ACL 2001; configure VLANIF 1 to permit IGMP Report or Leave messages with the source address 10.10.1.2, but to discard IGMP Report or Leave messages with the source address 10.10.1.1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] acl number 2001
[*HUAWEI-acl4-basic-2001] rule permit source 10.10.1.2 0
[*HUAWEI-acl4-basic-2001] rule deny source 10.10.1.1 0
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp ip-source-policy 2001

```

# In the public network instance, create an ACL named myacl; configure VLANIF 1 to permit IGMP Report or Leave messages with the source address 10.10.1.2, but to discard IGMP Report or Leave messages with the source address 10.10.1.1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] acl name myacl basic
[*HUAWEI-acl4-basic-myacl] rule permit source 10.10.1.2 0
[*HUAWEI-acl4-basic-myacl] rule deny source 10.10.1.1 0
[*HUAWEI-acl4-basic-myacl] quit
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp ip-source-policy acl-name myacl

```

# In the public network instance, configure a policy for filtering IGMP Report or Leave messages based on source addresses.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp ip-source-policy

```