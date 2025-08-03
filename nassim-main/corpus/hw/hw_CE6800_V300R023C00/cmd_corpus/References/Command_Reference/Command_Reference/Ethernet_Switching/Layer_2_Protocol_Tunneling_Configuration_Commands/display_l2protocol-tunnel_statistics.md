display l2protocol-tunnel statistics
====================================

display l2protocol-tunnel statistics

Function
--------



The **display l2protocol-tunnel statistics** command displays statistics about tunneled Layer 2 protocol data units (PDUs) on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display l2protocol-tunnel statistics** { *interface-type* *interface-number* | *interface-name* } [ { *protocol* } &<1-19> | **user-defined-protocol** *protocol-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies the interface name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *protocol* | Displays statistics about tunneled Layer 2 PDUs of a specified protocol on an interface. | The following protocols are supported:   * cdp * dldp * dtp * eoam3ah * gmrp * gvrp * hgmp * lacp * lldp * pagp * pvst+ * stp * udld * vtp   One or more of the preceding Layer 2 protocols can be specified. |
| **user-defined-protocol** *protocol-name* | Displays statistics about tunneled Layer 2 PDUs of a user-defined Layer 2 protocol on an interface. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After you configure Layer 2 protocol tunneling, run the display l2protocol-tunnel statistics command to view statistics about tunneled Layer 2 PDUs on an interface. The statistics include:

* Number of incoming Layer 2 PDUs
* Number of outgoing Layer 2 PDUs
* Number of dropped Layer 2 PDUs that exceed the configured drop thresholdThe proceeding statistics serve as a reference for traffic statistics and fault diagnosis.

**Precautions**

When tunneling is enabled on an interface for more than one Layer 2 protocol, specifying protocol or user-defined-protocol in this command is recommended. Otherwise, the following problems may occur due to excessive output information:

* The output information is repeatedly refreshed, and therefore it is difficult to locate your desired information.
* The system fails to respond to other requests because it is busy searching information.Before using the display l2protocol-tunnel statistics command, note the following:
* If protocol is specified, this command displays the statistics about tunneled Layer 2 PDUs of a specified protocol on a specified interface.
* If user-defined-protocol is specified, this command displays the statistics about tunneled Layer 2 PDUs of a user-defined Layer 2 protocol on a specified interface.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about tunneled STP BPDUs.
```
<HUAWEI> display l2protocol-tunnel statistics 10GE 1/0/1 stp
-----------------------------------------------------------------------------                                                       
Port            Protocol             Drop      Input     Output    Drop                                                             
                                     Threshold Packets   Packets   Packets                                                          
-----------------------------------------------------------------------------                                                       
10GE1/0/1       stp                  0         0         0         0

```

**Table 1** Description of the **display l2protocol-tunnel statistics** command output
| Item | Description |
| --- | --- |
| Port | Name of the interface enabled with Layer 2 protocol tunneling. |
| Protocol | Tunneled Layer 2 protocol name. |
| Drop Packets | Number of dropped Layer 2 PDUs that exceed the configured drop threshold on the inbound interface. |
| Drop Threshold | Drop threshold for Layer 2 PDUs on an interface enabled with Layer 2 protocol tunneling.  The drop threshold is configured using the l2protocol-tunnel drop-threshold command, expressed in packets per second.  The interface drops excess Layer 2 PDUs when the number of Layer 2 PDUs received in 1s exceeds the configured drop threshold. |
| Input Packets | Number of incoming Layer 2 PDUs on an interface enabled with Layer 2 protocol tunneling. |
| Output Packets | Number of outgoing Layer 2 PDUs on an interface enabled with Layer 2 protocol tunneling. |