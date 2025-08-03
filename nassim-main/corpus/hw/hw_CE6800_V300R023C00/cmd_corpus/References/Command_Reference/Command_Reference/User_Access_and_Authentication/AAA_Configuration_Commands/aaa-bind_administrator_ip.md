aaa-bind administrator ip
=========================

aaa-bind administrator ip

Function
--------



The **aaa-bind administrator ip** command configures the IP address of the trusted host.

The **undo aaa-bind administrator ip** command cancels the setting of the IP address of the trusted host.



By default, the IP address of a trusted host is not configured.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**aaa-bind administrator ip** { *ipv4-address* | *ipv6-address* } &<1-8>

**undo aaa-bind administrator ip** [ *ipv4-address* | *ipv6-address* ]

For CE6885-LL (low latency mode):

**aaa-bind administrator ip** { *ipv4-address* } &<1-8>

**undo aaa-bind administrator ip** [ *ipv4-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | IPv4 address. | The value is in dotted decimal notation. |
| *ipv6-address* | IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

AAA view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If the IP addresses of the connected administrators are different, the login is not allowed and the console port is not affected. A maximum of eight IP addresses can be configured on the device.


Example
-------

# Configure an IP address for a trusted host.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] aaa-bind administrator ip 192.168.92.148

```