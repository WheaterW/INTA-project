peer filter-policy import (BGP view/BGP-IPv4 unicast address family view)(IPv4)
===============================================================================

peer filter-policy import (BGP view/BGP-IPv4 unicast address family view)(IPv4)

Function
--------



The **peer filter-policy import** command configures an ACL-based policy for filtering BGP routes received from a specified peer group.

The **undo peer filter-policy import** command cancels this configuration.



By default, no filtering policy is configured for the routes received from peers.


Format
------

**peer** *ipv4-address* **filter-policy** *acl-number* **import**

**peer** *ipv4-address* **filter-policy** **acl-name** *acl-name* **import**

**undo peer** *ipv4-address* **filter-policy** *acl-number* **import**

**undo peer** *ipv4-address* **filter-policy** **acl-name** *acl-name* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in the dotted decimal format. |
| *acl-number* | Specifies the number of the basic ACL. | The value is an integer ranging from 2000 to 2999. |
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

If you do not want to receive all routes from a peer, you can run the **peer filter-policy import** command to configure an ACL-based filtering policy to filter the routes received from the peer.

**Precautions**

For a named ACL, when the **rule** command is used to configure a filtering rule, only the configurations specified by source and time-range take effect.Select a correct basic ACL based on the address family type of the peer.For a peer, only one route filtering policy can take effect. If the **peer filter-policy** command is run more than once, the latest configuration takes effect.


Example
-------

# Set the filtering policy for peers.
```
<HUAWEI> system-view
[~HUAWEI] acl 2001
[*HUAWEI-acl4-basic-2001] rule permit
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.1 filter-policy 2001 import

```