source-ipv6
===========

source-ipv6

Function
--------



The **source-ipv6** command configures a global IPv6 address used to establish an OpenFlow connection with the controller.

The **undo source-ipv6** command deletes the global IPv6 address used to establish an OpenFlow connection with the controller.



By default, the global IPv6 address used to establish an OpenFlow connection with the controller is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**source-ipv6** *ipv6-address*

**undo source-ipv6** [ *ipv6-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies a global IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

SDN forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

An OpenFlow-compatible device communicates with the controller through an OpenFlow connection. You can run the source-ipv6 command to configure a global IPv6 address used to establish an OpenFlow connection with the controller. By default, the IPv6 address is used to establish OpenFlow connections with all controller IPv6 addresses specified using the controller-ipv6 command.


Example
-------

# Set the global IPv6 address used to establish an OpenFlow connection with the controller to 2001:db8:1::2.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] source-ipv6 2001:db8:1::2

```