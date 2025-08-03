rule (certificate-attribute-based access control policy view)
=============================================================

rule (certificate-attribute-based access control policy view)

Function
--------



The **rule** command configures certificate attribute-based control rules.

The **undo rule** command cancels the configuration.



By default, the certificate attribute-based control rules are not configured.


Format
------

**rule** *id* { **permit** | **deny** } *group-name*

**undo rule** { *id* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *id* | Specifies the ID of a certificate attribute-based access control rule. | The value is an integer that ranges from 1 to 256. |
| **permit** | Indicates that the certificates matching the attributes defined in the attribute group are considered valid and permitted. | - |
| **deny** | Indicates that the certificates matching the attributes defined in the attribute group are considered invalid and denied. | - |
| *group-name* | Specifies the name of an attribute group. | The value must be the name of an existing attribute group. |
| **all** | Indicates all certificate attribute-based access control rules. | - |



Views
-----

Certificate-attribute-based access control policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After configuring certificate attribute rules in the attribute group, run this command to configure certificate attribute-based access control rules. As a result, certificates that meet specific conditions pass or fail the authentication.If a certificate attribute-based access control policy has multiple control rules, the rules are ORed. If a certificate matches a control rule, the device takes the action defined in the rule on the certificate, and the rest of rules are skipped.

**Prerequisites**

The certificate attribute group has been created using the **pki certificate attribute-group** command.


Example
-------

# Create certificate attribute-based access control rule mygroup and permit the certificates that match the rule.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate attribute-group mygroup
[*HUAWEI-pki-attribute-mygroup] commit
[~HUAWEI-pki-attribute-mygroup] quit
[~HUAWEI] pki certificate access-control-policy name policy1
[*HUAWEI-pki-access-policy1] rule 1 permit mygroup

```