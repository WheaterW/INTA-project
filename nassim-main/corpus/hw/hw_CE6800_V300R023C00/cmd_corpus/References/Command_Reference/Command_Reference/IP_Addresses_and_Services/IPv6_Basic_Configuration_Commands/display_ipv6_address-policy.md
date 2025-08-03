display ipv6 address-policy
===========================

display ipv6 address-policy

Function
--------



The **display ipv6 address-policy** command displays information about address selection policy entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 address-policy** [ **vpn-instance** *vpn-instance-name* ] { **all** | *ipv6-address* *prefix-length* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. After this parameter is specified, the address selection policy entries of the specified VPN instance can be displayed. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all** | Displays all the address selection policy entries. | - |
| *ipv6-address* | Specifies the prefix of an IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of an IPv6 address. | It is an integer ranging from 0 to 128. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When this command is run:

* If the parameter is specified to be vpn-instance vpn-instance-name, the address selection policy entry of the VPN is displayed.
* If the parameter is specified to be all, all policy entries (including default policy entries) are displayed.
* If the parameter is specified to be ipv6-address prefix-length, the policy entry with the specified prefix is displayed.

**Precautions**

If no address selection policy entry is configured, the default address selection policy entries, that is the entries with prefixes being ::1, ::, 2002::, FC00::, and ::ffff:0.0.0.0 are displayed when this command is run.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View the address selection policy entries of the VPN instance R1\_VPN6.
```
<HUAWEI> display ipv6 address-policy vpn-instance R1_VPN6 all
 Policy Table :
             Total: 5
-------------------------------------------------------------------------------
 Prefix     : ::                                      PrefixLength  : 0
 Precedence : 40                                      Label         : 1
 Default    : Yes

 Prefix     : ::1                                     PrefixLength  : 128
 Precedence : 50                                      Label         : 0
 Default    : Yes

 Prefix     : ::FFFF:0.0.0.0                          PrefixLength  : 96
 Precedence : 10                                      Label         : 4
 Default    : Yes

 Prefix     : 2002::                                  PrefixLength  : 16
 Precedence : 30                                      Label         : 2
 Default    : Yes

 Prefix     : FC00::                                  PrefixLength  : 7
 Precedence : 20                                      Label         : 3
 Default    : Yes

-------------------------------------------------------------------------------

```

**Table 1** Description of the **display ipv6 address-policy** command output
| Item | Description |
| --- | --- |
| Policy Table | Information of address selection policy entries. |
| Prefix | IPv6 address prefix. |
| PrefixLength | Prefix length of an IPv6 address. |
| Precedence | Indicates the precedence of a policy entry when a destination address is selected. |
| Label | Indicates the label used to match available policy entries when a source address is selected. |
| Default | Whether this is a default policy entry.   * YES. * NO. |
| Total | Number of address selection policy entries. |