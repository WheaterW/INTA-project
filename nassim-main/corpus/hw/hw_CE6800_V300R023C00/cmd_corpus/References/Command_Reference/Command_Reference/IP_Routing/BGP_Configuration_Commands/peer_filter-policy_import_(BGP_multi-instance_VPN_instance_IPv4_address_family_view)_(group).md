peer filter-policy import (BGP multi-instance VPN instance IPv4 address family view) (group)
============================================================================================

peer filter-policy import (BGP multi-instance VPN instance IPv4 address family view) (group)

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
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **import** | Filters received routes. | - |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 64 case-sensitive characters starting with a letter. It cannot contain spaces. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


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

# Set the filtering policy for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] acl 2001
[*HUAWEI-acl4-basic-2001] rule permit
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] group test
[*HUAWEI-bgp-instance-a-vpna] peer test filter-policy 2001 import

```