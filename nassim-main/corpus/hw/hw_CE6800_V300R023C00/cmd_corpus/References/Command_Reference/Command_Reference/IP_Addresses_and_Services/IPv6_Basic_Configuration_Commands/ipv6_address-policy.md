ipv6 address-policy
===================

ipv6 address-policy

Function
--------



The **ipv6 address-policy** command configures the policies for selecting source and destination addresses.

The **undo ipv6 address-policy** command deletes the policies for selecting source and destination addresses.



By default, only default address selection policy entries are configured. These entries are prefixed with ::1, ::, 2002::, FC00::, and ::ffff:0.0.0.0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 address-policy** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* *prefix-length* *precedence* *label*

**undo ipv6 address-policy** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* *prefix-length*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ipv6-address* | Specifies the IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of an IPv6 address. | It is an integer ranging from 0 to 128. |
| *precedence* | Specifies the priority of an IPv6 address when the address is the destination address. | The value is an integer ranging from 0 to 4294967295. |
| *label* | Specifies the priority of an IPv6 address when the address is the source address. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Source/destination addresses used for sending out can be manipulated by applying policy entries into the policy table. The ipv6 address-policy command allows the user to configure source/destination address selection policy for an address/prefix. The policy table allows the user to give preference to an address/prefix in comparison to other available addresses/prefixes during the source/destination address selection.

**Configuration Impact**

* The label parameter can be used to determine the result of source address selection. The address whose label value is the same as the label value of the destination address is selected preferably as the source address.
* The destination address is selected based on both the label and precedence parameters. If label values of the candidate addresses are the same, the address whose precedence value is the largest is selected preferably as the destination address.

**Precautions**

The default policy entries are those whose prefixes are ::1, ::, 2002::, FC00::, and :ffff:0.0.0.0.Default policy entries cannot be configured by using a command.


Example
-------

# Configure the priorities to be 15 and 20 respectively when the IPv6 address 2001:db8::1/64 is used as a source address and a destination address.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 address-policy 2001:db8::1 64 15 20

```