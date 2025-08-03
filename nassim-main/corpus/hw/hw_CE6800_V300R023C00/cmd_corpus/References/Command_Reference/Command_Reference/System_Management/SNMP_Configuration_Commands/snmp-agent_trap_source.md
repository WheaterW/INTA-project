snmp-agent trap source
======================

snmp-agent trap source

Function
--------



The **snmp-agent trap source** command specifies the source interface for sending traps.

The **undo snmp-agent trap source** command deletes the specified source interface for sending traps.



By default, no source interface is specified for sending traps.


Format
------

**snmp-agent trap source** { *interface-name* | *interface-type* *interface-number* }

**undo snmp-agent trap source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of the source interface that sends trap messages. | - |
| *interface-type* | Specifies the type of the source interface that sends trap messages. | - |
| *interface-number* | Specifies the number of the source interface that sends trap messages. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To specify the type and number of a source interface with a specific IP address used to send SNMP trap messages, run the **snmp-agent trap source** command. The device uses the IPv4 address of the source interface as the source IPv4 address for sending traps.

**Configuration Impact**

Trap messages carry IP addresses of the outbound interfaces, and the receivers can identify the source addresses.

**Precautions**

The source interface that sends trap/Inform messages must have an IP address configured.After a source interface is configured using this command, the source interface is automatically bound to the private VPN to which the source interface belongs.Rules for selecting a VPN for the destination host:

* Rule 1: If the snmp-agent target-host or **snmp-agent target-host inform** command is run and the source interface-type interface-number parameter is specified, use the private VPN bound to the source interface to send trap/inform messages. Otherwise, follow rule 2.
* Rule 2: If the **snmp-agent trap source** command is run to configure a global source interface for sending trap/Inform messages, use the private VPN bound to the source interface to send trap/Inform messages. Otherwise, follow rule 3.
* Rule 3: If the snmp-agent target-host or **snmp-agent target-host inform** command is run and the public-net parameter is specified, use the public network to send trap/inform messages. Otherwise, follow rule 4.
* Rule 4: If the snmp-agent target-host or **snmp-agent target-host inform** command is run and the vpn-instance vpn-instance-name parameter is specified, use the VPN of the host to send trap/inform messages. Otherwise, follow rule 5.
* Rule 5: If the **set net-manager vpn-instance** command is run to configure a global VPN, use the global VPN to send trap/inform messages. Otherwise, follow rule 6.
* Rule 6: Use the public network to send trap/inform messages.

Example
-------

# Configure the IP address of the interface as the source address for trap messages.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap source 100GE 1/0/1

```