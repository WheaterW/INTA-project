if-match acl
============

if-match acl

Function
--------



The **if-match acl** command sets an ACL-based filtering rule.

The **undo if-match acl** command cancels the configuration.



By default, no ACL-based filtering rule is set.


Format
------

**if-match acl** { *acl-number* | *acl-name* }

**undo if-match acl** { *acl-number* | *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set an ACL-based filtering rule, run the **if-match acl** command.

* Run the **route-policy** command to enter the Route-policy view.
* A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the route matches the route-policy, and the system no longer matches it against other nodes.
* Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.

**Prerequisites**



An acl has been created using the acl command and a route-policy has been configured using the **route-policy** command.



**Precautions**



The if-match acl and if-match ip-prefix commands are mutually exclusive. That is, the if-match ip-prefix command configured later overrides the **if-match acl** command configured earlier.For a named ACL, when the **rule** command is used to configure a filtering rule, only the source address range specified by the source parameter is valid.Generally, the **if-match acl** command is used to match traffic. Matching routes is not recommended. To implement accurate route matching using a route-policy, you are advised to define matching rules using an IP prefix list in the route-policy.




Example
-------

# Set a filtering rule that is based on ACL 2000.
```
<HUAWEI> system-view
[~HUAWEI] acl number 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match acl 2000

```