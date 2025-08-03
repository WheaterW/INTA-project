display isis brief
==================

display isis brief

Function
--------



The **display isis brief** command displays brief information about IS-IS processes.




Format
------

**display isis brief** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**display isis** *process-id* **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays brief information about IS-IS processes in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view brief information about IS-IS processes, run the display isis brief command. If process-id is not specified, the command displays brief information about all IS-IS processes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all IS-IS processes of the public network instance.
```
<HUAWEI> display isis brief


ISIS Protocol Information for ISIS( 1 )
--------------------------------------------------

SystemId: cccc.cccc.cccc         System Level: L12
L1 Lsp Over Flow: false
L2 Lsp Over Flow: false
Level-1 Avoid Redistribute Loop Capability: true
Level-2 Avoid Redistribute Loop Capability: true
Ipv6 is not enabled
Systemid has been auto-recovered              : System-id conflict/Sequence number overflow
Some virtual Systemid has been auto-recovered : Sequence number overflow

```

**Table 1** Description of the **display isis brief** command output
| Item | Description |
| --- | --- |
| System Level | Level of a router:   * L1. * L2. * L12. |
| L1 Lsp Over Flow | Whether all Level-1 LSP fragments are used to encapsulate link information:   * true: yes. * false: no. |
| L2 Lsp Over Flow | Whether all Level-2 LSP fragments are used to encapsulate link information:   * true: yes. * false: no. |
| Level-1 Avoid Redistribute Loop Capability | Status of the Level-1 routing loop detection capability. |
| Level-2 Avoid Redistribute Loop Capability | Status of the Level-2 routing loop detection capability. |
| Ipv6 is not enabled | IPv6 is not enabled in an IS-IS process. If IPv6 is enabled in an IS-IS process, Ipv6 is enabled is displayed. |
| Systemid has been auto-recovered | Automatic IS-IS system ID recovery is triggered in the physical system because of a system ID conflict or sequence number reversal. |
| Some virtual Systemid has been auto-recovered | Automatic IS-IS system ID recovery is triggered in some virtual systems because of a sequence number reversal. |
| SystemId | Host system ID of the local IS-IS device. |