snmp-agent trap source ipv6
===========================

snmp-agent trap source ipv6

Function
--------



The **snmp-agent trap source ipv6** ipv6-address command is used to configure the SNMP trap IPv6 source address.

The **undo snmp-agent trap source ipv6** command is used to clear the SNMP trap IPv6 source address.



By default, no source IPv6 address is configured to target IPv6 host for SNMP Trap.


Format
------

**snmp-agent trap source ipv6** *ipv6-address* [ **vpn-instance** *vpn-instance-name* ]

**undo snmp-agent trap source ipv6**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specify source IPv6 address of snmp traps packet. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string.  On a VPN network, use the VPN instance specified using vpn-instance, IP address, and security name together to identify a target host. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a device sends SNMP trap packets to an IPv6 destination host, you can run the **snmp-agent trap source ipv6** command to specify the source IPv6 address for sending SNMP trap packets.

**Precautions**

To specify the source IPv4 address for the device to send trap messages to the IPv4 target host, run the **snmp-agent trap source** command to specify the source interface for sending trap messages. The device uses the IPv4 address of the source interface as the source IPv4 address for sending trap messages to the IPv4 target host.Rules for selecting a VPN for the destination host:

* Rule 1: If the snmp-agent target-host or **snmp-agent target-host inform** command is run and the source interface-type interface-number parameter is specified, use the private VPN bound to the source interface to send trap/inform messages. Otherwise, follow rule 2.
* Rule 2: If the **snmp-agent trap source ipv6** command is run to configure the global source address and VPN for sending trap/inform messages, use the private VPN bound to the source interface to send trap/inform messages. Otherwise, follow rule 3. This rule does not apply to proxy hosts.
* Rule 3: If the snmp-agent target-host or **snmp-agent target-host inform** command is run and the public-net parameter is specified, use the public network to send trap/inform messages. Otherwise, follow rule 4.
* Rule 4: If the snmp-agent target-host or **snmp-agent target-host inform** command is run and the vpn-instance vpn-instance-name parameter is specified, use the VPN of the host to send trap/inform messages. Otherwise, follow rule 5.
* Rule 5: If the **set net-manager vpn-instance** command is run to configure a global VPN, use the global VPN to send trap/inform messages. Otherwise, follow rule 6. This rule does not apply to proxy hosts.
* Rule 6: Use the public network to send trap/inform messages.


Example
-------

# Specify the source IPv6 address 2001:db8:1::1 for sending SNMP trap packets.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap source ipv6 2001:db8:1::1

```