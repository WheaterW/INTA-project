l2protocol-tunnel drop-threshold
================================

l2protocol-tunnel drop-threshold

Function
--------



The **l2protocol-tunnel drop-threshold** command configures a drop threshold for Layer 2 protocol data units (PDUs) on an interface enabled with Layer 2 protocol tunneling.

The **undo l2protocol-tunnel drop-threshold** command restores the default drop threshold for Layer 2 PDUs on an interface enabled with Layer 2 protocol tunneling.



By default, the drop threshold is 0, meaning that the drop threshold for Layer 2 protocol data units (PDUs) on an interface enabled with Layer 2 protocol tunneling is not set.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**l2protocol-tunnel drop-threshold** *rate* [ **user-defined-protocol** *protocol-name* | { *protocol* } &<1-16> ]

**undo l2protocol-tunnel drop-threshold** [ { *rate* { { **user-defined-protocol** *protocol-name* } | *protocol* } } | { **user-defined-protocol** *protocol-name* } | { *protocol* } &<1-16> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rate* | Specifies the threshold for dropping Layer 2 PDUs per second on an interface enabled with Layer 2 protocol tunneling. | The value is an integer ranging from 1 to 4096, in pps. |
| **user-defined-protocol** *protocol-name* | Specifies a user-defined Layer 2 protocol of which the drop threshold is configured for Layer 2 PDUs. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| *protocol* | Specifies the Layer 2 protocol of which the drop threshold is configured for Layer 2 PDUs. | The following protocols are supported:   * cdp * dldp * dtp * eoam3ah * gmrp * gvrp * hgmp * lacp * lldp * pagp * pvst+ * stp * udld * vtp   One or more of the preceding protocols can be specified. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an interface enabled with Layer 2 protocol transparent transmission receives a large number of Layer 2 protocol packets, you can run this command to set a drop threshold for Layer 2 PDUs to prevent malicious attacks.If the number of Layer 2 PDUs that pass through an inbound interface (on which Layer 2 protocol tunneling is enabled) within a period (1s) exceeds the configured threshold, the inbound interface discards excess Layer 2 PDUs.

**Prerequisites**

Layer 2 protocol tunneling has been enabled using the l2protocol-tunnel vlan or **l2protocol-tunnel** command.

**Follow-up Procedure**

Run the **display l2protocol-tunnel statistics** command to view statistics about tunneled Layer 2 PDUs on an interface enabled with Layer 2 protocol tunneling and use the statistics as a reference for traffic statistics and fault diagnosis.

**Precautions**

Before using the l2protocol-tunnel drop-threshold command, note the following:

* If no protocol is specified, the configured drop threshold applies to all tunneled Layer 2 protocols on the interface enabled with Layer 2 protocol tunneling.
* If a protocol is specified, the interface drops the excess Layer 2 PDUs of this specified protocol when the configured drop threshold is exceeded.
* If you do not specify any protocol when configuring a drop threshold and then you specify a protocol when configuring a drop threshold, the latest configuration takes effect.

Example
-------

# Set the drop threshold for STP BPDUs on an interface enabled with Layer 2 protocol tunneling to 10.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] l2protocol-tunnel stp enable
[*HUAWEI-100GE1/0/1] l2protocol-tunnel drop-threshold 10 stp

```