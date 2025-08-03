display route-policy
====================

display route-policy

Function
--------

The **display route-policy** command displays the configured route-policy.



Format
------

**display route-policy** [ *route-policy-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-policy-name* | Specifies the name of the route-policy to be displayed. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string.  The value must be unique. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To view detailed information about the configured route-policy, run the **display route-policy** command.

**Configuration Impact**

If the route-policy name is not specified, the **display route-policy** command displays detailed information about all configured route-policies.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the route-policy named policy1.
```
<HUAWEI> display route-policy policy1
Route-policy : policy1
permit : 10 (matched counts: 0)
Match clauses :
if-match acl 2000
Apply clauses :
apply cost 100
apply tag 100

```


**Table 1** Description of the
**display route-policy** command output

| Item | Description |
| --- | --- |
| Route-policy | Name of the route-policy. |
| permit | Matching mode and node index of the route-policy. |
| Match clauses | List of if-match clauses. |
| Apply clauses | Apply clause list. |
| matched counts | Number of times that routes are successfully matched. The value increases by 1 as long as routes are successfully matched. |