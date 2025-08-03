igmp access-limit
=================

igmp access-limit

Function
--------



The **igmp access-limit** command sets the maximum number of IGMP group memberships that can be created on an interface.

The **undo igmp access-limit** command cancels the setting.



By default, the maximum number of IGMP group memberships on an interface is not configured.


Format
------

**igmp access-limit** *number* **except** { *acl-number* | **acl-name** *acl-name* }

**igmp access-limit** *number*

**undo igmp access-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of IGMP entries that can be created on an interface. | The value is an integer ranging from 1 to 16384. |
| **except** | Specifies an unrestricted ACL rule. | - |
| *acl-number* | Specifies the number of a basic or an advanced ACL. | The value is an integer.   * The value ranging from 2000 to 2999 specifies a basic ACL. A basic ACL filters group addresses, without distinguishing between (\*, G) and (S, G) entries. * The value ranging from 3000 to 3999 specifies an advanced ACL. An advanced ACL filters only (S, G) entries on an interface. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a large number of multicast users request multiple programs simultaneously, excessive bandwidth resources will be exhausted, and the Router's performance will be degraded, deteriorating the multicast service quality. To prevent this issue, run the **igmp access-limit** command on a Router interface to limit the number of IGMP entries. When receiving an IGMP Join message from a user, the Router interface first checks whether the configured maximum number of IGMP entries is reached. If the maximum number is reached, the Router interface discards the IGMP Join message and rejects the user. If the maximum number is not reached, the Router interface sets up an IGMP membership and forwards data flows of the requested multicast group to the user. This mechanism enables users who have successfully joined multicast groups to enjoy smoother multicast services.The principles of counting the number of IGMP entries are as follows:

* Each (\*, G) entry is counted as one entry on an interface, and each (S, G) is counted as one entry on an interface.
* SSM-mapping (\*, G) entries are not counted as entries on an interface, and each (S, G) entry mapped using the SSM-mapping mechanism is counted as one entry on an interface.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command.

**Precautions**

If except is not specified, the maximum number is effective for all multicast groups, including source-specific groups. If except is specified, the interface uses the ACL to filter received IGMP Join messages. The entries matching the ACL are not restricted by the maximum number of IGMP entries.<br />
The **igmp access-limit** command is used together with the acl (basic ACL) or acl (advanced ACL) command.

* In the basic ACL view, you can set the address range of multicast groups that are not limited by the number parameter by specifying the source parameter in the **rule** command.
* In the advanced ACL view, you can set the source address range of multicast data packets by specifying the source parameter in the **rule** command, and set the multicast group address range of multicast data packets by specifying the destination parameter in the **rule** command.If this command is run more than once, the latest configuration overrides the previous one.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Set the maximum number of IGMP entries that can be created on VLANIF 1 to 1024.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp access-limit 1024

```

# Create a named ACL myacl, and configure a rule for the named ACL to allow hosts to receive messages sent by multicast source 1.1.1.1 to multicast group 232.0.0.0/16. The maximum number of IGMP entries that can be created on VLANIF 1 is 1024, and the multicast group 232.0.0.0/16 is not limited.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] acl name myacl
[*HUAWEI-acl4-advance-myacl] rule permit ip source 1.1.1.1 0 destination 232.0.0.0 0.0.255.255
[*HUAWEI-acl4-advance-myacl] quit
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp access-limit 1024 except acl-name myacl

```