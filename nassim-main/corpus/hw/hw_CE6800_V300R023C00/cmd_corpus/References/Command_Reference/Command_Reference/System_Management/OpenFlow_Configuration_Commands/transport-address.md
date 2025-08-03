transport-address
=================

transport-address

Function
--------



The **transport-address** command configures the IP address used to establish an OpenFlow connection with the specified controller.

The **undo transport-address** command deletes the IP address used to establish an OpenFlow connection with the specified controller.



By default, no IP address is configured to establish an OpenFlow connection with the specified controller.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**transport-address** *ip-address*

**undo transport-address** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address. | The value is in dotted decimal notation. The IP address of a loopback interface is recommended. |



Views
-----

OpenFlow-forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After you run the **source-ip** command to configure the global IP address used to establish an OpenFlow connection with the controller, the device uses the global IP address to establish an OpenFlow connection with the controller by default. If you do not want to use the global IP address to establish an OpenFlow connection with a controller, run the **transport-address** command to configure the IP address used to establish an OpenFlow connection with the controller.


Example
-------

# Set the IP address used to set up an OpenFlow connection with the specified controller to 10.10.10.10.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] controller-ip 10.1.1.1
[*HUAWEI-sdn-agent-ctrl-10.1.1.1] openflow agent
[*HUAWEI-sdn-agent-ctrl-10.1.1.1-openflow] transport-address 10.10.10.10

```