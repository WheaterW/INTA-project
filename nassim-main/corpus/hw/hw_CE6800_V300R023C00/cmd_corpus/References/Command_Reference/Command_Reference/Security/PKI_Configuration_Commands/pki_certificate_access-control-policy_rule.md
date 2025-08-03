pki certificate access-control-policy rule
==========================================

pki certificate access-control-policy rule

Function
--------



The **pki certificate access-control-policy rule** command arranges rules in a certificate access policy.




Format
------

**pki certificate access-control-policy** [ **policy-name** *policy-name* ] **rule** **move** *rule-id1* { **after** | **before** } *rule-id2*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **policy-name** *policy-name* | Specifies the name of a certificate access policy. If the policy-name parameter is not specified, the default certificate access policy uses the name default-0. | The value must be an existing certificate access policy name. |
| **move** *rule-id1* | Changes the sequence of rule-id1 and rule-id2. | The values must be existing certificate access policy numbers. |
| **after** | Moves rule-id1 behind rule-id2. | - |
| **before** | Moves rule-id1 before rule-id2. | - |
| *rule-id2* | Changes the sequence of rule-id1 and rule-id2. | The values must be existing certificate access policy numbers. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple control rules are configured in an access control policy based on certificate attributes, the relationship between the rules is "Or". This means that the action defined in the access control policy is implemented as long as the certificate to be authenticated matches one rule. The remaining control rules are not used. You can run this command to adjust rule sequence so that the rule you prefer can take effect first.

**Prerequisites**

A certificate access policy has been created using the **pki certificate access-control-policy name** command.

The certificate access control rules have been configured using the rule (certificate access policy view) command.

**Precautions**

When you change the sequence of some rules, the sequence of rule IDs is unchanged, but the rule contents are swapped. For example:The certificate access policy a has the following rules:pki certificate access-control-policy name arule 5 permit test1rule 20 permit test2After the pki certificate access-control-policy policy-name a rule move 20 before 5 is executed, the rules are changed to:

pki certificate access-control-policy name arule 5 permit test2rule 20 permit test1


Example
-------

# In the certificate access policy a, move rule 20 before rule 5.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate attribute-group test1
[*HUAWEI-pki-attribute-test1] quit
[~HUAWEI] pki certificate attribute-group test2
[*HUAWEI-pki-attribute-test2] quit
[~HUAWEI] pki certificate access-control-policy name a
[*HUAWEI-pki-access-a] rule 5 permit test1
[*HUAWEI-pki-access-a] rule 20 permit test2
[*HUAWEI-pki-access-a] quit
[~HUAWEI] pki certificate access-control-policy policy-name a rule move 20 before 5

```