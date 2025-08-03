peer filter-policy import (BGP view/BGP-IPv4 unicast address family view) (group)
=================================================================================

peer filter-policy import (BGP view/BGP-IPv4 unicast address family view) (group)

Function
--------



The **peer filter-policy import** command configures an ACL-based policy for filtering BGP routes received from a specified peer group.

The **undo peer filter-policy import** command cancels this configuration.



By default, no filtering policy is configured for the routes to be received from a peer group.


Format
------

**peer** *group-name* **filter-policy** *acl-number* **import**

**peer** *group-name* **filter-policy** **acl-name** *acl-name* **import**

**undo peer** *group-name* **filter-policy** *acl-number* **import**

**undo peer** *group-name* **filter-policy** **acl-name** *acl-name* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **import** | Filters received routes. | - |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters starting with a letter. It cannot contain spaces. |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you do not want to accept all the routes from a peer group, run the **peer filter-policy import** command to configure an ACL-based filtering policy to filter the routes received from the peer group.

**Precautions**

For a named ACL, when the **rule** command is used to configure a filtering rule, only the configurations specified by source and time-range take effect.Select a correct basic ACL based on the address family type of the peer group.For a peer group, only one route filtering policy can take effect. If the **peer filter-policy** command is run more than once, the latest configuration takes effect.


Example
-------

# Set the filtering policy for peer group.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] rule permit
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test filter-policy 2000 import

```