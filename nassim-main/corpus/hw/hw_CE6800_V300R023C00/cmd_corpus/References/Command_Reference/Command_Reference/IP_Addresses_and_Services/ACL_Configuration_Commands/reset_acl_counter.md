reset acl counter
=================

reset acl counter

Function
--------



The **reset acl counter** command clears statistics about a specified or all ACLs.




Format
------

**reset acl counter all**

**reset acl counter name** *acl-name*

**reset acl counter** *basic-acl-number*

**reset acl counter** *user-acl-number*

**reset acl counter** *advance-acl-number*

**reset acl counter** *arp-acl-number*

**reset acl counter** *numberLink*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *acl-name* | Specifies the name of an ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| *basic-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 2000 to 2999, the number of a basic ACL ranges from 2000 to 2999. |
| *user-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 5000 to 5999, the number of a user ACL ranges from 5000 to 5999. |
| *advance-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 3000 to 3999, the number of an advanced ACL ranges from 3000 to 3999. |
| *arp-acl-number* | Specifies the number of an ACL. | The value is an integer ranging from 23000 to 23999, the number of an ARP-based ACL ranges from 23000 to 23999. |
| *numberLink* | Specifies the number of an ACL. | The value is an integer ranging from 4000 to 4999, the number of a Layer 2 ACL ranges from 4000 to 4999. |
| **all** | Clears statistics about all ACLs. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To clear statistics about a specified or all ACLs, run the reset acl counter command. Before collecting ACL statistics in a specified period, run this command to clear the original statistics.



**Configuration Impact**



No message is displayed when statistics about ACLs are cleared using the reset acl counter command. Exercise caution when running this command.



**Follow-up Procedure**



Run the **display acl** command to check the current rule information and packet matching statistics about ACLs.




Example
-------

# Clear statistics about ACL 2001.
```
<HUAWEI> reset acl counter 2001

```