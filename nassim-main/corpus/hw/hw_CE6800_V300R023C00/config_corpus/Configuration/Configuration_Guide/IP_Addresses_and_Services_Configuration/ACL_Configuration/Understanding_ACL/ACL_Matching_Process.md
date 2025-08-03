ACL Matching Process
====================

ACL Matching Process

#### ACL Step

An ACL step is the difference between two adjacent ACL rule IDs that are automatically allocated. For example, if the ACL step is set to 5, the rule IDs are multiples of 5, such as 5, 10, 15, and 20.

* If an ACL step is changed, rules in the ACL are automatically renumbered according to the new step, with the start rule ID being the step value. For example, if the ACL step is changed from 5 to 2, the original rule IDs 5, 10, 15, and 20 will be renumbered as 2, 4, 6 and 8.
* If the default step of 5 is restored for an ACL, the system immediately renumbers the rules in the ACL based on the default step. For example, the step of ACL 3001 is 2, and rules in ACL 3001 are numbered 0, 2, 4, and 6. In this case, if the default step 5 is restored, the rules will be renumbered as 5, 10, 15, and 20.

An ACL step can be used to maintain ACL rules, making it convenient to add new ones. For example, if you have created four rules numbered 0, 5, 10, and 15 in an ACL, you can add rules between any two rules, such as rule 1 between rules 0 and 5.


#### ACL Rule ID

* All rules in an ACL are identified by rule IDs and arranged in ascending order of ID. Rule IDs can be manually configured or automatically generated based on the ACL step.
* If rule IDs are automatically generated, they are incremented in predefined steps. For example, if the ACL step is set to 5, the difference between rule IDs will be 5. In this case, the first rule ID is 5, and subsequent IDs will increase by increments of 5. This facilitates ACL management, enabling you to add new rules between existing ones.
* In the configuration file, the rules are displayed in ascending order of ID, not in the order of configuration.

#### ACL Matching Mechanism

A device stops matching packets against ACL rules once the packets match a rule.

After a packet is filtered by an ACL, the packet may be matched or unmatched:

* Matched: The packet matches a rule in the ACL.
* Unmatched: The packet does not match any rule in the ACL, the ACL is unavailable, or the ACL does not contain rules.

Whether packets are permitted or denied is determined by actions specified in matched rules of an ACL and the service module that has this ACL applied. Different service modules may process the packets that are filtered by ACL rules in different ways.


#### ACL Matching Order

The system matches packets against ACL rules in ascending order of rule IDs. That is, the rule with the smallest ID takes effect first.

* If a smaller rule ID is manually specified for a rule, the rule takes effect earlier than those with larger rule IDs.
* If no ID is manually specified for a rule, the system allocates one. This rule ID is the largest in the ACL and has the minimum multiple of the step. Therefore, this rule is the last one that functions.