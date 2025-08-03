filter-policy import (OSPF view)
================================

filter-policy import (OSPF view)

Function
--------



The **filter-policy import** command configures the device to filter the routes calculated by OSPF according to a filtering policy. Only the routes that pass the filtering can be added to the RIB.

The **undo filter-policy import** command disables OSPF from filtering received routes.



By default, OSPF does not filter received routes.


Format
------

**filter-policy** *acl-number* **import**

**filter-policy** { **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | { **route-policy** *route-policy-name* } [ **secondary** ] } **import**

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | { **route-policy** *route-policy-name* } [ **secondary** ] ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the basic ACL number. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **secondary** | Indicates the suboptimal route. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **filter-policy import** command to set a filtering policy for the received routes. Only the routes that pass the filtering are added to the RIB. OSPF is a link-state dynamic routing protocol, with routing information carried in the link-state database (LSDB). Therefore, the **filter-policy import** command cannot be used to filter the advertised or received LSAs. Actually, this command is used to filter the routes calculated by OSPF.

**Precautions**

For a named ACL, only the source address range specified by the source parameter and the time period specified by the time-range parameter are valid for the configured filtering rule.


Example
-------

# Configure OSPF to filter the received routes.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix1 permit 1.1.1.1 24
[*HUAWEI] ospf 100
[*HUAWEI-ospf-100] filter-policy ip-prefix prefix1 import

```