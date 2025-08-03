reset acl ipv6 counter
======================

reset acl ipv6 counter

Function
--------



The **reset acl ipv6 counter** command clears statistics about a specified or all ACL6s.




Format
------

**reset acl ipv6 counter name** *acl6-name*

**reset acl ipv6 counter all**

**reset acl ipv6 counter** *basic-acl6-number*

**reset acl ipv6 counter** *advance-acl6-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears statistics about all ACL6s. | - |
| *basic-acl6-number* | Specifies the number of an ACL6. | The number of a basic ACL6 ranges from 2000 to 2999. |
| *advance-acl6-number* | Specifies the number of an ACL6. | The number of an advanced ACL6 ranges from 3000 to 3999. |
| **name** *acl6-name* | Specifies the name of an ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To clear statistics about a specified or all ACL6s, run the reset acl ipv6 counter command. Before collecting ACL6 statistics in a specified period, run this command to clear the original statistics.



**Configuration Impact**



No message is displayed when statistics about ACL6s are cleared using the reset acl ipv6 counter command. Exercise caution when running this command.



**Follow-up Procedure**



Run the **display acl ipv6** command to check the current rule information and packet matching statistics about ACL6s.




Example
-------

# Clear statistics about ACL6 2100.
```
<HUAWEI> reset acl ipv6 counter 2100

```