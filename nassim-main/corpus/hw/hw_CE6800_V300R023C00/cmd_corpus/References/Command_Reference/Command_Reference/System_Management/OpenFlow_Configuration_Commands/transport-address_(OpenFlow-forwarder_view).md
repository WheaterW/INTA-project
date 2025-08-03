transport-address (OpenFlow-forwarder view)
===========================================

transport-address (OpenFlow-forwarder view)

Function
--------



The **transport-address** command configures the IPv6 address used to establish an OpenFlow connection with the specified controller.

The **undo transport-address** command deletes the IPv6 address used to establish an OpenFlow connection with the specified controller.



By default, no IPv6 address is configured to establish an OpenFlow connection with the specified controller.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**transport-address** *ipv6-address*

**undo transport-address** [ *ipv6-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

OpenFlow-forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After you run the **source-ipv6** command to configure the global IPv6 address used to establish an OpenFlow connection with the controller, the device uses the global IPv6 address to establish an OpenFlow connection with the controller by default. If you do not want to use the global IPv6 address to establish an OpenFlow connection with a controller, run the **transport-address** command to configure an IPv6 address for the controller.


Example
-------

# Set the IPv6 address used to set up an OpenFlow connection with the specified controller to 2001:db8:1::2.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] controller-ipv6 2001:db8:1::1
[*HUAWEI-sdn-agent-ctrl-2001:db8:1::1] openflow agent
[*HUAWEI-sdn-agent-ctrl-2001:db8:1::1-openflow] transport-address 2001:db8:1::2

```