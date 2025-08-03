snmp-agent protocol server disable
==================================

snmp-agent protocol server disable

Function
--------



The **snmp-agent protocol server disable** command disables the SNMP IPv4 or IPv6 listening port.

The **undo snmp-agent protocol server disable** command enables the SNMP IPv4 or IPv6 listening port.



By default, the SNMP IPv4 or IPv6 listening port is enabled.


Format
------

**snmp-agent protocol server disable**

**snmp-agent protocol server ipv4 disable**

**snmp-agent protocol server ipv6 disable**

**undo snmp-agent protocol server disable**

**undo snmp-agent protocol server ipv4 disable**

**undo snmp-agent protocol server ipv6 disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Disables the SNMP IPv4 listening port. | - |
| **ipv6** | Disables the SNMP IPv6 listening port. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Enabling alarm sending to the NMS without performing the Get/Set operation does not require SNMP port listening. To disable the SNMP IPv4 and IPv6 listening ports, run the **snmp-agent protocol server disable** command.If ipv4 or ipv6 is not selected, both SNMP IPv4 and IPv6 listening ports are disabled.

**Precautions**

After you disable the SNMP IPv4 or IPv6 listening port using the **snmp-agent protocol server disable** command, SNMP no longer processes SNMP packets. Exercise caution when you disable the SNMP IPv4 or IPv6 listening port.


Example
-------

# Disable the SNMP IPv4 listening port.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent
[*HUAWEI] snmp-agent protocol server ipv4 disable

```