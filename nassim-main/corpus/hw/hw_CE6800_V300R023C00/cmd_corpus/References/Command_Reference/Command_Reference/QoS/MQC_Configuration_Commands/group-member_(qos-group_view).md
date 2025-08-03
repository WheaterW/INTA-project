group-member (qos-group view)
=============================

group-member (qos-group view)

Function
--------



The **group-member** command adds a member to a QoS group.



By default, no member is added to a QoS group.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**group-member interface** { *interface-type* *interface-num* | *interface-name* [ **to** *interface-type* *interface-num* | *interface-name* ] } &<1-8>

**group-member vlan** { *vlanid* [ **to** *vlanid* ] } &<1-8>

**undo group-member interface** { *interface-type* *interface-num* | *interface-name* [ **to** *interface-type* *interface-num* | *interface-name* ] } &<1-8>

**undo group-member vlan** { *vlanid* [ **to** *vlanid* ] } &<1-8>

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**group-member ip source** *ip-address* { *ip-address-wildcard* | *ip-address-netmask* }

**undo group-member ip source** *ip-address* { *ip-address-wildcard* | *ip-address-netmask* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** { *vlanid* [ **to** *vlanid* ] } | Specifies VLANs added to a QoS group.  The keyword to specifies a VLAN range that includes all VLANs between the start and end VLANs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **interface** { *interface-type* *interface-num* | *interface-name* [ **to** *interface-type* *interface-num* | *interface-name* ] } | Specifies interfaces added to a QoS group.  The keyword to specifies an interface range that includes all interfaces between the start and end interfaces. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **ip** **source** *ip-address* | Specifies the source IP address added to the QoS group.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is in dotted decimal notation. |
| *ip-address-wildcard* | Indicates the mask of an IP address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is in dotted decimal notation. |
| *ip-address-netmask* | Indicates the mask length of the IP address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer in the range from 1 to 32. |



Views
-----

qos-group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* After creating a QoS group, you can add all VLANs to which the same traffic policy is applied to the QoS group.
* After creating a QoS group, you can add all interfaces to which the same traffic policy is applied to the QoS group.


Example
-------

# Add VLAN 10 to the QoS group qosgroup1.
```
<HUAWEI> system-view
[~HUAWEI] qos group qosgroup1
[*HUAWEI-qos-group-qosgroup1] group-member vlan 10

```