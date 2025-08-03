lacp stable-preferred disable
=============================

lacp stable-preferred disable

Function
--------



The **lacp stable-preferred disable** command disables the function to keep the selection status of interfaces stable for an Eth-Trunk interface in static LACP mode.

The **undo lacp stable-preferred disable** command enables the function to keep the selection status of interfaces stable for an Eth-Trunk interface in static LACP mode.



By default, the function to keep the selection status of interfaces stable for an Eth-Trunk interface in static LACP mode is enabled.


Format
------

**lacp stable-preferred disable**

**undo lacp stable-preferred disable**


Parameters
----------

None

Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, after the selection parameters (bandwidth, system priority, system ID, port priority, and port number) of a port in the Eth-Trunk interface on the LACP passive end change and then are restored, the selection status of the selected interfaces in the Eth-Trunk corresponding to the Actor remains stable. After the **lacp stable-preferred disable** command is run, the function to keep the selection status of interfaces stable is disabled.



**Prerequisites**



Run the **mode lacp-static** command in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in LACP mode.



**Precautions**



After the function to keep the selection status of interfaces stable for an Eth-Trunk interface in static LACP mode is disabled, if the port selection parameters (bandwidth, system priority, system ID, port priority, and port number) of a port in an Eth-Trunk interface on the LACP passive end change, the Eth-Trunk link may be unstable.




Example
-------

# Disable the function to keep the selection status of interfaces stable for Eth-Trunk 1 in static LACP mode.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp stable-preferred disable

```