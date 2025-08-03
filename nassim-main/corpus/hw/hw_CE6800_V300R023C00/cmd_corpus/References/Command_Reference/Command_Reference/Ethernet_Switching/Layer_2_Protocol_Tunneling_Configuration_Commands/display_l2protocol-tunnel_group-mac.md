display l2protocol-tunnel group-mac
===================================

display l2protocol-tunnel group-mac

Function
--------



The **display l2protocol-tunnel group-mac** command displays Layer 2 protocol tunneling information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display l2protocol-tunnel group-mac** { **all** | *protocol* | **user-defined-protocol** *protocol-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays Layer 2 protocol tunneling information for all Layer 2 protocols. | - |
| *protocol* | Displays Layer 2 protocol tunneling information for a specified Layer 2 protocol. | The following protocols are supported:   * cdp * dldp * dtp * eoam3ah * gmrp * gvrp * hgmp * lacp * lldp * pagp * stp * udld * vtp * pvst+ |
| **user-defined-protocol** *protocol-name* | Displays Layer 2 protocol tunneling information for a user-defined Layer 2 protocol. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view Layer 2 protocol tunneling information after Layer 2 protocol tunneling is configured, run the display l2protocol-tunnel group-mac command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all Layer 2 protocol tunneling information.
```
<HUAWEI> display l2protocol-tunnel group-mac all
Protocol         EncapeType ProtocolType Protocol-MAC   Group-MAC      Pri
-----------------------------------------------------------------------------
hgmp             ethernetii 0x88a7       0180-c200-000a 0100-0ccd-cdd0 0
stp              llc        dsap 0x42    0180-c200-0000 0100-0ccd-cdd0 0
                            ssap 0x42

```

**Table 1** Description of the **display l2protocol-tunnel group-mac** command output
| Item | Description |
| --- | --- |
| Protocol | Tunneled Layer 2 protocol name. |
| EncapeType | Ethernet encapsulation type (Ethernet II, snap, or LLC) for Layer 2 protocol data units (PDUs). |
| ProtocolType | Tunneled Layer 2 protocol type. |
| Protocol-MAC | Multicast destination MAC address in tunneled Layer 2 PDUs. |
| Group-MAC | Multicast MAC address (group MAC address) specified to replace the multicast destination MAC address in tunneled Layer 2 PDUs. |
| Pri | Priority of tunneled Layer 2 PDUs, which has a fixed value 0. |
| dsap | Destination service access point of transparently transmitted Layer 2 protocol packets. |
| ssap | Source service access point of transparently transmitted Layer 2 protocol packets. |