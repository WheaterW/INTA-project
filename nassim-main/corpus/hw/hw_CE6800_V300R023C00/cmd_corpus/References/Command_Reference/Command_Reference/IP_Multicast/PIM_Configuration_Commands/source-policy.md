source-policy
=============

source-policy

Function
--------



The **source-policy** command configures a policy for filtering multicast data packets based on source addresses or based on source and group addresses.

The **undo source-policy** command restores the default configuration.



By default, the Router does not filter received multicast data packets based on source addresses or based on source and group addresses.


Format
------

**source-policy** { *acl-number* | **acl-name** *acl-name* }

**undo source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic or an advanced ACL. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To implement data flow control and limit information that downstream receivers can obtain, run the **source-policy** command to configure a policy using which the Router filters received multicast data packets based on source addresses or based on source and group addresses. The Router forwards a received multicast data packet only if it is permitted by an ACL rule defined in the filter policy, thus improving system security.The **source-policy** command configuration also applies to multicast data packets encapsulated in Register messages.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the **source-policy** command is run more than once, the latest configuration overrides the previous one.

* If a basic ACL is configured, the Router forwards only multicast data packets whose source addresses are permitted by rules of the ACL.
* If an advance ACL is configured, the Router forwards only multicast data packets whose source and group addresses are both permitted by rules of the ACL.
* If the specified ACL does not exist, the Router discards all multicast data packets.

**Precautions**

The **source-policy** command and the **pim dm** command are mutually exclusive.


Example
-------

# In the public network instance, configure the Router to permit multicast data packets with the source address 10.10.1.2 and to discard those with the source address 10.10.1.1.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2001
[*HUAWEI-acl4-basic-2001] rule permit source 10.10.1.2 0
[*HUAWEI-acl4-basic-2001] rule deny source 10.10.1.1 0
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] source-policy 2001

```