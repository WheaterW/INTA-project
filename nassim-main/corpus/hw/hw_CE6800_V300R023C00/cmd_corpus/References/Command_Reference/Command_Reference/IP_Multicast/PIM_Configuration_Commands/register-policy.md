register-policy
===============

register-policy

Function
--------



The **register-policy** command configures a policy used by a rendezvous point (RP) to filter Register messages.

The **undo register-policy** command restores the default configuration.



By default, no Register message filter policy is configured.


Format
------

**register-policy** { *advanced-acl-number* | **acl-name** *acl-name* }

**undo register-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *advanced-acl-number* | Specifies the number of an advanced ACL. | The value is an integer ranging from 3000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named advanced ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent Register message attacks, run the **register-policy** command to enable a Router to permit or deny specific Register messages.The **register-policy** command takes effect only for subsequently received Register messages. That is, the multicast entries that have been registered successfully are not deleted and can still be used for multicast data forwarding.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the **register-policy** command is run more than once, the latest configuration overrides the previous one.If the (S, G) information contained in a Register message is denied by ACL rules or if no ACL action is configured for the (S, G) information, the RP discards the Register message and does not register the multicast source indicated by the (S, G) information.The RP accepts only Register messages permitted by ACL rules. If a specified ACL does not exist, the RP discards all Register messages and does not register any multicast sources.


Example
-------

# In the public network instance, configure the RP to receive Register packets sent by the source on network segment 10.10.0.0/16 to the multicast group 225.1.0.0/16.
```
<HUAWEI> system-view
[~HUAWEI] acl number 3000
[*HUAWEI-acl4-advance-3000] rule permit ip source 10.10.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255
[*HUAWEI-acl4-advance-3000] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] register-policy 3000

```