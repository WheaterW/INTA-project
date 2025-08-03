igmp group-policy
=================

igmp group-policy

Function
--------



The **igmp group-policy** command configures an IGMP group policy on an interface to limit the range of multicast groups that hosts connected to the interface can join.

The **undo igmp group-policy** command restores the default configuration.



By default, no IGMP group policy is configured on an interface, so that hosts connected to this interface can join any multicast groups.


Format
------

**igmp group-policy** { *acl-number* | **acl-name** *acl-name* } { **1** | **2** | **3** }

**igmp group-policy** { *acl-number* | **acl-name** *acl-name* }

**undo igmp group-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL or an advanced ACL. The ACL defines a multicast group range. | The number of a basic ACL is an integer ranging from 2000 to 2999; the number of an advanced ACL is an integer ranging from 3000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **1** | Sets the range of multicast groups that an IGMPv1 host can join. | - |
| **2** | Sets the range of multicast groups that an IGMPv2 host can join. | - |
| **3** | Sets the range of multicast groups that an IGMPv3 host can join. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To restrict the range of multicast groups that user hosts can join, run the **igmp group-policy** command to apply an ACL to the Router interface connected to the user hosts. IGMP security is thus improved.

**Prerequisites**

The **multicast routing-enable** command must be run in the instance to which the interface belongs and the ACL to be referenced must be configured.

**Configuration Impact**

If the **igmp group-policy** command is run more than once, the latest configuration overrides the previous one.After the **igmp group-policy** command is run on an interface:

* The interface filters received Report messages based on the ACL and maintains memberships only for multicast groups permitted by the ACL.
* The interface discards Report messages denied by the ACL. If entries have been already created for multicast groups denied by the ACL, the device deletes these entries after the specified timeout period expires.If an IGMP version is not specified, the ACL applies to IGMPv1, IGMPv2, and IGMPv3 hosts.

**Precautions**

The **igmp group-policy** command and the **acl** command are used together. For numbered ACLs and named ACLs:

* In the basic ACL view, you can set the range of multicast groups that an interface is allowed to join by specifying the source parameter in the **rule** command.
* In the advanced ACL view, you can set the range of multicast sources that an interface is allowed to join by specifying the source parameter in the **rule** command, and set the range of multicast groups that an interface is allowed to join by specifying the destination parameter in the **rule** command.For IGMPv1/v2 and IGMPv3 MODE\_IS\_EXCLUDE/CHANGE\_TO\_EXCLUDE\_MODE Report messages, the source parameter in the **rule** command must match 255.255.255.255.The group-policy command takes effect only for dynamic IGMP join requests. Static IGMP join requests are not controlled by the group-policy command.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Create ACL 2005, and configure a rule for ACL 2005 to allow hosts to receive messages from multicast group 225.1.1.1. Configure a filter on vlanif 1 to allow hosts connected to the interface to join only multicast group 225.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2005
[*HUAWEI-acl4-basic-2005] rule permit source 225.1.1.1 0
[*HUAWEI-acl4-basic-2005] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-Vlan1] quit
[*HUAWEI] interface vlanif 1
[*HUAWEI-Vlanif1] igmp group-policy 2005

```

# Create an ACL named myacl, and configure a rule for the ACL to allow hosts to receive messages from multicast group 225.1.0.0/16. Configure a filter on vlanif 1.
```
<HUAWEI> system-view
[~HUAWEI] acl name myacl
[*HUAWEI-acl4-advance-myacl] rule permit ip destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-myacl] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-Vlan1] quit
[*HUAWEI] interface vlanif 1
[*HUAWEI-Vlanif1] igmp group-policy acl-name myacl

```