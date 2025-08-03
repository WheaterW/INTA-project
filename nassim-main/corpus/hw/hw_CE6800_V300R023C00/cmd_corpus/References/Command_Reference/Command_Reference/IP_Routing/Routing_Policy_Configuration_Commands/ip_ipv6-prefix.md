ip ipv6-prefix
==============

ip ipv6-prefix

Function
--------



The **ip ipv6-prefix** command configures an IPv6 prefix list or one entry in the IPv6 prefix list.

The **undo ip ipv6-prefix** command deletes an IPv6 prefix list or one entry in the IPv6 prefix list.



By default, no IPv6 prefix list is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip ipv6-prefix** *ipv6-prefix-name* [ **index** *index-number* ] *matchMode* *ipv6-address* *masklen* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]

**undo ip ipv6-prefix** *ipv6-prefix-name* [ **index** *index-number* ]

**undo ip ipv6-prefix** *ipv6-prefix-name* *ipv6-address* *masklen* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-prefix-name* | Specifies the name of an IP prefix list. | The value is a string of 1 to 169 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **index** *index-number* | Specifies the sequence number of the entry in the IPv6 prefix list. By default, the sequence number increases with a step of 10 according to the configuration order, and the first number is 10. | The value is an integer ranging from 1 to 4294967295. |
| *matchMode* | Specifies the matching mode of the IP prefix list. | The value is of the enumerated type.   * permit: indicates that the matching mode of IP prefix entries is permit. In permit mode, if the IPv6 address to be filtered is in the defined prefix range, the IPv6 address matches the route-policy and stops matching against the next entry. Otherwise, the IPv6 address continues to match against the next entry. * deny: indicates that the matching mode of the IP prefix list entry is deny. In deny mode, if the IPv6 address to be filtered is in the defined prefix range, the IPv6 address fails to match the route-policy and cannot match against the next entry. Otherwise, the IPv6 address continues to match against the next entry. |
| *ipv6-address* | Specifies the IPv6 prefix range in the form of an IPv6 address. If :: is specified, the address 0::0 is matched. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *masklen* | Specifies the IPv6 prefix range using the mask length. If ::0 less-equal 128 is used, all the IPv6 addresses are matched. | The value is an integer that ranges from 0 to 128. |
| **match-network** | Matches network addresses. The match-network parameter is used to match routes to a specified network address and can be configured only when ipv6-address is set to::. For example, ip ipv6-prefix prefix1 permit :: 96 matches all the routes with the prefix length of 96, and ip ipv6-prefix prefix1 permit :: 96 match-network matches all the routes in the range from ::1 to ::FFFF:FFFF. | - |
| **greater-equal** *greater-equal-value* | A mask length range can be set to match the routes with the same prefix but different masks. That is, the mask length range specified in [ greater-equal greater-equal-value ] [ less-equal less-equal-value ] can be used to match such routes. greater-equal means "greater than or equal to", and less-equal means "less than or equal to". | The mask range must be specified according to the following relationship: masklen<=greater-equal-value<=less-equal-value<=128.   * If only greater-equal is set, the mask length ranges from greater-equal-value to 128. * If only less-equal is specified, the mask length ranges from masklen to less-equal-value. * If both greater-equal and less-equal are specified, the mask length ranges from greater-equal-value to less-equal-value. |
| **less-equal** *less-equal-value* | A mask length range can be set to match the routes with the same prefix but different masks. That is, the mask length range specified in [ greater-equal greater-equal-value ] [ less-equal less-equal-value ] can be used to match such routes. greater-equal means "greater than or equal to", and less-equal means "less than or equal to". | The mask length range needs to be specified as maskLen <= greater-equal-value <= less-equal-value <= 128.   * If only greater-equal is set, the mask length range is from greater-equal-value to 128. * If only less-equal is set, the mask length range is from masklen to less-equal-value. * If greater-equal and less-equal are specified, the mask length range is from greater-equal-value to less-equal-value. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **ip ipv6-prefix** command is used to configure an IPv6 prefix list. An IPv6 prefix can be used as a filter by various protocols or used with a route-policy.

* The **ip ipv6-prefix** command can be used with the following commands to filter routes to be advertised globally with an IPv6 prefix list as a filtering condition:
* filter-policy export(OSPFv3)
* ipv6 filter-policy export(IS-IS)
* filter-policy export(BGP)
* The **ip ipv6-prefix** command can be used with the following commands to filter routes to be accepted globally with an IPv6 prefix list as a filtering condition:
* filter-policy import(OSPFv3)
* ipv6 filter-policy import(IS-IS)
* filter-policy import(BGP)
* The **ip ipv6-prefix** command can be used with the following commands to configure a route-policy based on an IPv6 prefix list for a specific peer:
* peer ip-prefix (BGP)
* The ipv6 import-route isis level-1 into level-2 filter-policy ipv6-prefix command is used to control the route leaking from a Level-1 area to a Level-2 area.
* The ipv6 import-route isis level-2 into level-1 filter-policy ipv6-prefix command is used to control route leaking from an IS-IS Level-2 area to an IS-IS Level-1 area.
* The **ip ipv6-prefix** command and the **if-match ipv6** command can be used to test received or sent routes based on an IPv6 prefix list.An IPv6 prefix list can contain several entries, and each entry specifies an IPv6 prefix range. The relationship between the nodes is "OR". That is, if a route matches one entry, the route matches the IPv6 prefix list; if a route does not match any entry, the route fails to match the IPv6 prefix list.An IPv6 prefix range is determined by prefix-length and greater-equal-value, less-equal-value. If mask-length and greater-equal-value, less-equal-value are specified, an IPv6 address must match the prefix range.

**Precautions**

The IPv6 prefix lists in use cannot be deleted.After a configuration is delivered, the device checks the validity of the parameters in the configuration and processes these parameters. After the processing, the generated configuration is the result of the AND calculation between the specified ipv6-address and prefix-length. For example, if the specified ipv6-address and prefix-length are 2001:db8::1 and 64, respectively, the generated configuration is 2001:db8:: 64.If the ipv6-address in the generated configuration is ::, the configuration matches all IPv6 addresses.


Example
-------

# Permit the routes with the mask length ranging from 32 to 64 bits.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix abc permit :: 0 greater-equal 32 less-equal 64

```

# Deny the routes with the IP prefix 2001:db8:D00::/32 and with the prefix longer than 32 bits.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix abc deny 2001:db8:D00:: 32 less-equal 128

```