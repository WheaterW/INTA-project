filter-policy export
====================

filter-policy export

Function
--------



The **filter-policy export** command configures IS-IS to filter the imported routes to be advertised.

The **undo filter-policy export** command disables IS-IS from filtering the routes to be advertised.



By default, IS-IS does not filter the routes to be advertised.


Format
------

**filter-policy** { *acl-number* | **acl-name** *acl-name-string* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } { **export** [ **direct** | **static** | **rip** *process-id* | **bgp** | **ospf** *process-id* | **isis** *process-id* ] }

**undo filter-policy** [ *acl-number* | **acl-name** *acl-name-string* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* ] { **export** [ **direct** | **static** | **rip** *process-id* | **bgp** | **ospf** *process-id* | **isis** *process-id* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies a basic ACL number. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name-string* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy to filter routes based on tags and other protocol parameters. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **direct** | Specifies to filter the imported direct routes before route advertisement. | - |
| **static** | Specifies to filter the imported static routes before route advertisement. | - |
| **rip** *process-id* | Specifies to filter the imported RIP routes before route advertisement. | The value is an integer ranging from 1 to 4294967295. |
| **bgp** | Specifies to filter the imported BGP routes before route advertisement. | - |
| **ospf** *process-id* | Specifies to filter the imported OSPF routes before route advertisement. | The value is an integer ranging from 1 to 4294967295. |
| **isis** *process-id* | Specifies to filter the imported IS-IS routes before route advertisement. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When IS-IS and other routing protocols are running on the network, and a boundary router in the IS-IS domain has imported routes of other routing protocols, the boundary router will advertise all the imported routes to its IS-IS neighbors by default.When the routes that meet certain conditions need to be advertised, you can run the filter-policy export command to configure filtering rules. In this manner, only the routes that meet the filtering rules can be advertised.

**Prerequisites**

Routes of other routing protocols have been imported using the **import-route** command.

**Configuration Impact**

The filter-policy export command does not take effect on local routes. After the command is run, only the imported routes that meet the filtering rules can be advertised to IS-IS neighbors.


Example
-------

# Use route-policy policy1 to filter all the imported routes to be advertised.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix prefix-a index 10 permit 172.17.1.0 24
[*HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] if-match ip-prefix prefix-a
[*HUAWEI-route-policy] quit
[*HUAWEI] isis
[*HUAWEI-isis-1] filter-policy route-policy policy1 export

```