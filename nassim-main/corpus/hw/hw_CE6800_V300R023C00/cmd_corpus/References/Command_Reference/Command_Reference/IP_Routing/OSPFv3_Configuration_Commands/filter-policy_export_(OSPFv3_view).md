filter-policy export (OSPFv3 view)
==================================

filter-policy export (OSPFv3 view)

Function
--------



The **filter-policy export** command filters imported routes to be advertised based on a filtering policy.

The **undo filter-policy export** command restores the default setting.



By default, the imported routes to be advertised are not filtered.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } **export** **direct**

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } **export** **bgp**

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } **export** **static**

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } **export** **ripng** *protocolID*

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } **export** **isis** *protocolID*

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } **export** **ospfv3** *protocolID*

**filter-policy** *acl-number* **export** **direct**

**filter-policy** *acl-number* **export** **bgp**

**filter-policy** *acl-number* **export** **static**

**filter-policy** *acl-number* **export** **ripng** *protocolID*

**filter-policy** *acl-number* **export** **isis** *protocolID*

**filter-policy** *acl-number* **export** **ospfv3** *protocolID*

**filter-policy** *acl-number* **export**

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* } **export**

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* ] **export** **direct**

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* ] **export** **bgp**

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* ] **export** **static**

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* ] **export** **ripng** *protocolID*

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* ] **export** **isis** *protocolID*

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* ] **export** **ospfv3** *protocolID*

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* ] **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **acl6-name** *acl6-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **direct** | Specifies to filter imported direct routes to be advertised based on a filtering policy. | - |
| **bgp** | Specifies to filter imported BGP routes to be advertised based on a filtering policy. | - |
| **static** | Specifies to filter imported static routes to be advertised based on a filtering policy. | - |
| **ripng** | Specifies to filter imported RIPng routes to be advertised based on a filtering policy. | - |
| *protocolID* | Displays information about the ABR or ASBR of an OSPF route in a specified OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **isis** | Specifies to filter imported IS-IS routes to be advertised based on a filtering policy. | - |
| **ospfv3** | Specifies to filter imported OSPFv3 routes from other OSPFv3 processes to be advertised based on a filtering policy. | - |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **filter-policy export** command is only valid for the routes that are imported using the import-route (OSPFv3) command.If no external routes are imported using the import-route (OSPFv3) command, the **filter-policy export** command does not take effect. The external routes include the OSPFv3 routes of other processes.When the rule (basic ACL6 view) command is used to configure a filtering rule for an IPv6 named ACL, only the source address range that is specified in source and the time period that is specified in time-range take effect on the filtering rule.


Example
-------

# Filter the imported routes based on the rule defined by ACL6 2002.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2002
[*HUAWEI-acl6-basic-2002] rule deny source 2001:db8::1 64
[*HUAWEI-acl6-basic-2002] quit
[*HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] filter-policy 2002 export

```