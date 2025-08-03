display ipv6 security interface
===============================

display ipv6 security interface

Function
--------



The **display ipv6 security interface** command displays the IPv6 SEND configuration.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 security interface** { *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* *interface-num* | Specifies the type and number of an interface. The IPv6 SEND configuration on the specified interface is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display ipv6 security interface command to view the IPv6 SEND configuration on the specified interface, including the CGA IPv6 address, RSA key pair bound to the interface, timestamp configuration, and whether the strict security mode is enabled on the interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the IPv6 SEND configuration on 100GE 1/0/1.
```
<HUAWEI> display ipv6 security interface 100ge 1/0/1
(L) : Link local address
 SEND: Security ND
 SEND information for the interface : 100GE1/0/1
----------------------------------------------------------------------------
 IPv6 address                                   PrefixLength Collision Count
----------------------------------------------------------------------------
 2001:db8:1::1                                  64              0
----------------------------------------------------------------------------
 SEND sec value                     : 1
 SEND security modifier value       : 2001:db8:1::1
 SEND RSA key label bound           : huawei
 SEND ND minimum key length value   : 512
 SEND ND maximum key length value   : 2048
 SEND ND Timestamp delta value      : 300
 SEND ND Timestamp fuzz value       : 1
 SEND ND Timestamp drift value      : 1
 SEND ND fully secured mode         : enable

```

**Table 1** Description of the **display ipv6 security interface** command output
| Item | Description |
| --- | --- |
| SEND information for the interface | IPv6 SEND configuration on the interface. |
| SEND sec value | Security level of the CGA address. |
| SEND security modifier value | Modifier value of the CGA address. |
| SEND RSA key label bound | Name of the RSA key pair that is bound to the interface. |
| SEND ND minimum key length value | Minimum key length allowed on the interface. |
| SEND ND maximum key length value | Maximum key length allowed on the interface. |
| SEND ND Timestamp delta value | delta value of the timestamp in the ND message. |
| SEND ND Timestamp fuzz value | fuzz-factor value of the timestamp in the ND message. |
| SEND ND Timestamp drift value | drift value of the timestamp in the ND message. |
| SEND ND fully secured mode | Whether the strict security mode is enabled on the interface. |
| SEND | Security ND. |
| IPv6 address | CGA IPv6 address. |
| PrefixLength | Prefix length of the CGA IPv6 address. |
| Collision Count | Number of CGA IPv6 addresses conflicts. |