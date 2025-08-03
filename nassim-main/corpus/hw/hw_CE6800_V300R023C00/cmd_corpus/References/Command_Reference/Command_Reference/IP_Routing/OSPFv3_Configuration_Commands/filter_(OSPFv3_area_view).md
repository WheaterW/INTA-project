filter (OSPFv3 area view)
=========================

filter (OSPFv3 area view)

Function
--------



The **filter export** command filters outgoing Type-3 LSAs (Inter-Area-Prefix-LSAs) of the local area.

The **undo filter export** command restores the default setting.

The **filter import** command filters the incoming Type-3 LSAs (Inter-Area-Prefix-LSAs) of the local area.

The **undo filter import** command restores the default setting.



By default, outgoing Type-3 LSAs of the local area are not filtered.

By default, the incoming Type-3 LSAs are not filtered.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**filter** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* } **export**

**filter** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* } **import**

**filter** *acl6-number* **export**

**filter** *acl6-number* **import**

**undo filter** [ **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* | *acl6-number* ] **export**

**undo filter** [ **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* | *acl6-number* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **acl6-name** *acl6-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *acl6-number* | Specifies a basic ACL6 number. | The value is an integer ranging from 2000 to 2999. |



Views
-----

OSPFv3 area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **filter export** command can be used to filter out the LSAs that do not need to be sent to neighbors to reduce the size of the LSDB and speed up network convergence.The **filter import** command can be used to filter out the unneeded LSAs learned from neighbors to reduce the size of the LSDB and speed up network convergence.

**Configuration Impact**



After filtering conditions are set for the outgoing Type-3 LSAs to be advertised using the **filter export** command, only the outgoing Type-3 LSAs that match the filtering conditions can be advertised.After filtering conditions are set for the incoming Type-3 LSAs using the **filter import** command, only the incoming Type-3 LSAs that match the filtering conditions can be accepted.



**Precautions**

* The command can be configured only on an ABR.
* For a named ACL, configure a filtering rule, the filtering rule takes effective only when the source address range is specified in source and the time period is specified in time-range.
* To set filtering conditions for the incoming Type-3 LSAs, run the **filter import** command.
* To set filtering conditions for the outgoing Type-3 LSAs to be advertised, run the **filter export** command.


Example
-------

# Configure OSPFv3 to filter the outgoing Type-3 LSAs.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] area 1
[*HUAWEI-ospfv3-100-area-0.0.0.1] filter 2000 export

```

# Filter incoming Type-3 LSAs within the local area.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix my-prefix deny 2001:db8::1 64
[*HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] area 1
[*HUAWEI-ospfv3-100-area-0.0.0.1] filter ipv6-prefix my-prefix import

```