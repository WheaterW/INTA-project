ip source destination(Flow Matrix view)
=======================================

ip source destination(Flow Matrix view)

Function
--------



The **ip source destination** command configures a path planning rule for a specified flow.

The **undo ip source destination** command deletes a path planning rule for a specified flow.



By default, no flow path planning rule is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip source** *source-ip-address* **destination** *destination-ip-address* **flow-rail** { *interface-name* | *interface-type* *interface-number* }

**undo ip source** *source-ip-address* **destination** *destination-ip-address* **flow-rail** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-ip-address* | Indicates the source IP address that matches the rule. | The value is in dotted decimal notation. |
| *destination-ip-address* | Indicates the destination IP address that matches the rule. | The value is in dotted decimal notation. |
| **flow-rail** | Specifies a flow rail. | - |
| *interface-name* | Specifies the name of an outbound interface. | - |
| *interface-type* | Specifies the type of an outbound interface. | - |
| *interface-number* | Specifies the number of an outbound interface. | - |



Views
-----

Flow Matrix view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to configure a path planning rule for a specified flow in Flow Matrix.

**Precautions**

If two of the command configurations have the same source and destination IP addresses, the later configuration overrides the previous one.A maximum of 1024 path planning rules can be created in Flow Matrix.The source and destination IP addresses in a Flow Matrix rule must be different.An interface cannot function as both an Eth-Trunk member interface and a flow rail in a Flow Matrix rule.The Flow Matrix function supports only IPv4 addresses, and the IPv4 addresses cannot be non-class A/B/C or loopback addresses.


Example
-------

# Configure a flow path planning rule for the Flow Matrix.
```
<HUAWEI> system-view
[~HUAWEI] flow-matrix
[*HUAWEI-flow-matrix] ip source 10.1.1.2 destination 10.1.2.2 flow-rail 100GE1/0/1

```