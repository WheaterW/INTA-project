source (Tunnel interface view)
==============================

source (Tunnel interface view)

Function
--------



The **source** command configures a source IP address or source interface for a tunnel interface.

The **undo source** command deletes a source IP address or source interface for a tunnel interface.



By default, no source IP address or source interface is configured for a tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**source** *source-ip-address*

**source** { *interface-name* | *interface-type* *interface-number* }

**undo source** [ *source-ip-address* | { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-ip-address* | Specifies the source IP address for a tunnel interface. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of the source interface of a GRE tunnel. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-number* | Specifies the source interface number for a tunnel. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When configuring a tunnel, you must create a tunnel interface and run the **source** command to configure the source address on the tunnel interface. The IP address of the interface that sends packets should be specified as the source address on the tunnel interface.

**Prerequisites**

The tunnel mode has been configured using the **tunnel-protocol** command.

**Configuration Impact**

The same source or destination IP address cannot be configured for two or more tunnel interfaces that use the same encapsulation protocol.


Example
-------

# Configure Tunnel1 and specify the outbound interface encapsulated into packets as Loopback1.
```
<HUAWEI> system-view
[~HUAWEI] interface LoopBack 1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] interface Tunnel 1
[*HUAWEI-Tunnel1] tunnel-protocol gre
[*HUAWEI-Tunnel1] source loopback 1

```