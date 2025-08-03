dns debugging filter
====================

dns debugging filter

Function
--------



The **dns debugging filter** command enables the debugging of DNS filter criteria.

The **undo dns debugging filter** command disables the debugging of DNS filter criteria.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**dns debugging filter** { **domain** *domain-name* | **client-ip** *ip-address* | **client-ipv6** *ipv6-address* }

**undo dns debugging filter** { **domain** [ *domain-name* ] | **client-ip** [ *ip-address* ] | **client-ipv6** [ *ipv6-address* ] }

For CE6885-LL (low latency mode):

**dns debugging filter** { **domain** *domain-name* | **client-ip** *ip-address* }

**undo dns debugging filter** { **domain** [ *domain-name* ] | **client-ip** [ *ip-address* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **domain** *domain-name* | Specifies a domain name as a filter criterion for DNS debugging. | The value is a string of 1 to 255 case-sensitive characters. |
| **client-ip** *ip-address* | Specifies an IPv4 client address as a filter criterion for DNS debugging. | The value is in dotted decimal notation. |
| **client-ipv6** *ipv6-address* | Specifies an IPv6 client address as a filter criterion for DNS debugging.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If refined DNS debugging is required, run this command to configure filter criteria. This facilitates maintenance.


Example
-------

# Enable DNS debugging and set the filter criterion to the domain name huawei.com.
```
<HUAWEI> dns debugging filter domain huawei.com

```