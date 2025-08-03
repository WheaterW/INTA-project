aaa-quiet administrator except-list
===================================

aaa-quiet administrator except-list

Function
--------



The **aaa-quiet administrator except-list** command configures a user to access the network using a specified IP address when the user account is locked.

The **undo aaa-quiet administrator except-list** command restores the default setting.



By default, a user cannot access the network when the account is locked.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**aaa-quiet administrator except-list** { *ipv4-address* | *ipv6-address* } &<1-32>

**undo aaa-quiet administrator except-list** [ *ipv4-address* | *ipv6-address* ]

For CE6885-LL (low latency mode):

**aaa-quiet administrator except-list** { *ipv4-address* } &<1-32>

**undo aaa-quiet administrator except-list** { *ipv4-address* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 address. A user can access the network using this IPv4 address when the user account is locked. | The value is a valid unicast address in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 address. A user can access the network using this IPv6 address when the user account is locked.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

AAA view,Vsys aaa view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In the AAA view, after the account locking function is configured for AAA local authentication users or AAA remote authentication users, if a user enters incorrect passwords for a specified number of consecutive times, the user account is locked. During the locking period, the user cannot access the network. To facilitate maintenance and management, you can run the **aaa-quiet administrator except-list** command to allow a user to use a specified IP address to access the network when the user account is locked.

**Precautions**

This function takes effect only for the administrators.


Example
-------

# Configure a user to access the network using the specified IP address 10.1.1.1 when the user account is locked.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] aaa-quiet administrator except-list 10.1.1.1

```