lacp timeout
============

lacp timeout

Function
--------



The **lacp timeout** command configures a timeout period for an Eth-Trunk interface in static Link Aggregation Control Protocol (LACP) mode to receive LACPDUs.

The **undo lacp timeout** command restores the default timeout period.



The default timeout period for an Eth-Trunk interface to receive LACPDUs is slow mode, 90 seconds.


Format
------

**lacp timeout fast** [ **user-defined** *user-defined* ]

**lacp timeout slow**

**undo lacp timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **user-defined** *user-defined* | Indicates a timeout period for an Eth-Trunk interface to receive LACPDUs when fast is specified. | The value is an integer ranging from 3 to 90, in seconds. |
| **slow** | Indicates that the timeout period of Eth-Trunk interfaces in static LACP mode to receive packets is 90 seconds.  If slow is configured, the peer sends an LACP packet every 30 seconds. In this case, the device responds to the LACPDUs from the peer slowly but consumes fewer system resources compared with the situation that fast is configured.  The timeout periods set for the two ends can be different. To facilitate maintenance, setting the same timeout period for both ends is recommended. | - |
| **fast** | Indicates that the timeout period of Eth-Trunk interfaces in static LACP mode to receive packets is 3 seconds.  If fast is configured, the peer sends an LACP packet every 1 second. In this case, the device can quickly respond to the LACPDUs from the peer but consume more system resources compared with the situation that slow is configured. | - |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



For an Eth-Trunk interface with many member Ethernet interfaces, if one of the member interfaces has not received packets for indicated period then it will be turned down. To make sure the reliability of the network, and other member interfaces will forward the data. By default, the timeout period is slow mode, 90 seconds, and the fast mode can quickly respond to the LACPDUs from the peer but consume more system resources compared with the situation that slow is configured.



**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static LACP mode.



**Configuration Impact**

After this command is executed successfully:

* If fast is specified, the timeout period for the Eth-Trunk interface to receive LACPDUs is 3 seconds, and the interval for the peer end to send LACPDUs is 1 second.
* If slow is configured, the timeout period for the Eth-Trunk interface to receive LACPDUs is 90 seconds, and the interval for the peer end to send LACPDUs is 30 seconds.

The timeout period configured on an Eth-Trunk interface takes effect on all its member interfaces.



Example
-------

# Set the timeout period for Eth-Trunk 1 to receive LACPDUs to 90 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp timeout slow

```