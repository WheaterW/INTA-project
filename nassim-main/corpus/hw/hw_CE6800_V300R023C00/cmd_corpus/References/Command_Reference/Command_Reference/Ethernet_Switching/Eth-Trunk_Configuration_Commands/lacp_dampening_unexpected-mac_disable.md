lacp dampening unexpected-mac disable
=====================================

lacp dampening unexpected-mac disable

Function
--------



The **lacp dampening unexpected-mac disable** command disables MAC address flapping suppression in Ethernet headers of LACPDUs.

The **undo lacp dampening unexpected-mac disable** command restores the default configuration.



By default, MAC address flapping suppression in Ethernet headers of LACPDUs is enabled.


Format
------

**lacp dampening unexpected-mac disable**

**undo lacp dampening unexpected-mac disable**


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



By default, an Eth-Trunk interface in LACP mode is enabled to suppress invalid MAC addresses in Ethernet headers of received LACPDUs from flapping, in which case the source MAC addresses of the LACPDUs and system ID are checked. To disable the check, run the **lacp dampening unexpected-mac disable** command to disable MAC address flapping suppression in Ethernet headers of LACPDUs.



**Prerequisites**



An Eth-Trunk interface has been configured to work in LACP mode using the mode { lacp-static | lacp-dynamic command.




Example
-------

# Disable the invalid-MAC-based state flapping suppression function on Eth-Trunk 1.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp dampening unexpected-mac disable

```