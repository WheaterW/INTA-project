reset l2protocol-tunnel statistics
==================================

reset l2protocol-tunnel statistics

Function
--------



The **reset l2protocol-tunnel statistics** command deletes statistics about tunneled Layer 2 protocol data units (PDUs) on a specified interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset l2protocol-tunnel statistics** { *interface-type* *interface-number* | *interface-name* } [ { **user-defined-protocol** *protocol-name* } | { *protocol* } &<1-19> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the interface type. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies the interface name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **user-defined-protocol** *protocol-name* | Specifies Layer 2 protocol tunneling for a user-defined protocol. | The name is a string of 1 to 31 case-insensitive characters, spaces not supported.  If spaces are used, the string must start and end with double quotation marks ("). |
| *protocol* | Deletes statistics about tunneled Layer 2 PDUs of a specified protocol on an interface. | The following protocols are supported:   * cdp * dldp * dtp * eoam3ah * gmrp * gvrp * hgmp * lacp * lldp * pagp * pvst+ * stp * udld * vtp   One or more of the preceding Layer 2 protocols can be specified. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before collecting statistics about tunneled Layer 2 PDUs on an interface, run the reset l2protocol-tunnel statistics command to delete the existing statistics so that the interface can re-collect the statistics.

**Follow-up Procedure**

Run the **display l2protocol-tunnel statistics** command to check whether statistics are deleted.

**Precautions**

The statistics about tunneled Layer 2 PDUs cannot be restored after they are cleared. Exercise caution when running the reset l2protocol-tunnel statistics command.Before using the reset l2protocol-tunnel statistics command, note the following:

* If no protocol is specified, this command deletes the statistics about all tunneled Layer 2 PDUs on a specified interface.
* If a protocol is specified, this command deletes the statistics about tunneled Layer 2 PDUs of this specified protocol on a specified interface.

Example
-------

# Delete statistics about all tunneled Layer 2 PDUs on 100GE 1/0/1.
```
<HUAWEI> reset l2protocol-tunnel statistics 100GE 1/0/1

```