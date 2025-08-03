source-ip
=========

source-ip

Function
--------



The **source-ip** command configures the global IP address used to establish an OpenFlow connection with the controller.

The **undo source-ip** command deletes the global IP address used to establish an OpenFlow connection with the controller.



By default, the global IP address used to establish an OpenFlow connection with the controller is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**source-ip** *ipv4-address*

**undo source-ip** [ *ipv4-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies a global IP address. | The value is in dotted decimal notation. |



Views
-----

SDN forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

An OpenFlow-compatible device communicates with the controller through an OpenFlow connection. You can run the source-ip command to configure a global IP address used to establish an OpenFlow connection with the controller. By default, this IP address is used to establish OpenFlow connections with all controller IP addresses specified using the controller-ip command.


Example
-------

# Set the global IP address used to establish an OpenFlow connection with the controller to 10.10.10.10.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] source-ip 10.10.10.10

```