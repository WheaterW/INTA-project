igmp prompt-leave
=================

igmp prompt-leave

Function
--------



The **igmp prompt-leave** command enables the prompt leave function on an interface.

The **undo igmp prompt-leave** command restores the deImmLeaveAclNumValuefault setting.



By default, an IGMP interface sends a last-member query message after receiving a Leave message for a specific multicast group from a host.


Format
------

**igmp prompt-leave**

**igmp prompt-leave group-policy** { *acl-number* | **acl-name** *acl-name* }

**undo igmp prompt-leave**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of an ACL. This ACL defines the range of multicast groups. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enable the device to delete the records of a multicast group immediately after receiving a Leave message of the multicast group on an interface without sending a Last Member Query message.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the **igmp prompt-leave** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The **igmp prompt-leave** command and the **acl** command are used together.

* For a numbered ACL, in the ACL view, you can set the address range of multicast groups that the host is to leave by specifying the source parameter in the **rule** command.
* For a named ACL, when the **rule** command is used in the ACL view to configure a filtering rule, only the configurations specified in the destination and time-range parameters take effect.

When both Layer 2 and Layer 3 services are running, the multicast function in a VLAN inherits the Layer 3 multicast function. Therefore, to use the prompt leave function, ensure that the **igmp prompt-leave** command is run on the Layer 3 interface.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Create an ACL named myacl and configure a rule that allows hosts to promptly leave multicast groups in the range of 225.1.0.0/16. Configure VLANIF 1 to delete records about a multicast group immediately after receiving an IGMP Leave message for the group.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] acl name myacl
[*HUAWEI-acl4-advance-myacl] rule permit ip destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-myacl] quit
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp prompt-leave group-policy acl-name myacl

```

# Create ACL 2005 and configure a rule that allows hosts to promptly leave multicast groups in the range of 225.1.0.0/16. Configure VLANIF 1 to delete records about a multicast group immediately after receiving an IGMP Leave message for the group.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] acl number 2005
[*HUAWEI-acl4-basic-2005] rule permit source 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-basic-2005] quit
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp prompt-leave group-policy 2005

```