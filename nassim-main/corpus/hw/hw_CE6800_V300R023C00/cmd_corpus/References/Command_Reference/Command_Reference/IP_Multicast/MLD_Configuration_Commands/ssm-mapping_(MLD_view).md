ssm-mapping (MLD view)
======================

ssm-mapping (MLD view)

Function
--------



The **ssm-mapping** command configures static Source-Specific Multicast (SSM) mapping rules.

The **undo ssm-mapping** command deletes the configured static SSM mapping rules.



By default, SSM mapping rules are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ssm-mapping** *ipv6-group-address* *ipv6-group-mask-length* *ipv6-source-address*

**undo ssm-mapping** { *ipv6-group-address* *ipv6-group-mask-length* [ *ipv6-source-address* ] | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-group-address* | Specifies the IPv6 address of a multicast group configured with SSM mapping. | The address ranges from FF00:: to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF, in the hexadecimal format. |
| *ipv6-group-mask-length* | Specifies the mask length of an IPv6 multicast group address. | The value is an integer, which can be 16, 32, 64, or 128. |
| *ipv6-source-address* | Specifies the IPv6 address of a multicast source. | The address is in the hexadecimal format. |
| **all** | Deletes all the configured static SSM mapping rules. | - |



Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Users can run this command to configure static Source-Specific Multicast (SSM) mapping rules.


Example
-------

# Configure a static SSM mapping rule to map multicast group FF35::1/128 to multicast source 2001:DB8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] ssm-mapping ff35::1 128 2001:DB8:1::1

```