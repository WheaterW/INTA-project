controller-ip
=============

controller-ip

Function
--------



The **controller-ip** command configures the controller IP address used to establish an OpenFlow connection with the device and displays the controller-IP view.

The **undo controller-ip** command deletes the controller IP address used to establish an OpenFlow connection with the device.



By default, the controller IP address used to establish an OpenFlow connection with the device is not specified.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**controller-ip** [ **vpn-instance** *vpn-instance-name* ] *ipv4-address*

**undo controller-ip** [ **vpn-instance** *vpn-instance-name* ] *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance that the controller belongs to. | The value must be the name of an existing VPN instance. |
| *ipv4-address* | Specifies the controller IP address. | The value is in the dotted decimal format. |



Views
-----

SDN forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The device communicates with the controller through an OpenFlow connection. You need to run the **controller-ip** command to configure the controller IP address used to establish an OpenFlow connection with the device. After the **controller-ip** command is run, the controller-IP view is displayed.A device can establish a single OpenFlow connection with a single controller or multiple controllers. The reliability of a single OpenFlow connection is low. If the controller or OpenFlow connection fails, you need to reconfigure the controller IP address for the OpenFlow connection and re-establish the OpenFlow connection. This process takes a long time. OpenFlow multi-connection features high reliability and load balancing. If a controller fails or an OpenFlow connection fails, the device can still maintain OpenFlow connections with other controllers.


Example
-------

# Set the controller IP address used to establish an OpenFlow connection with the device to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] controller-ip 10.1.1.1

```