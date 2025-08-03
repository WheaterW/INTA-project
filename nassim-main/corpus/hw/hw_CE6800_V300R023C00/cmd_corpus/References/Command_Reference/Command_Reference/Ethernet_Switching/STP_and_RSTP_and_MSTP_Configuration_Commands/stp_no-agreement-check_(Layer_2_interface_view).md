stp no-agreement-check (Layer 2 interface view)
===============================================

stp no-agreement-check (Layer 2 interface view)

Function
--------



The **stp no-agreement-check** command configures the common fast transition mechanism on an interface.

The **undo stp no-agreement-check** command restores the default fast transition mechanism on an interface.



By default, the enhanced fast transition mechanism is configured on an interface.


Format
------

**stp no-agreement-check**

**undo stp no-agreement-check**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If Huawei and non-Huawei data communication devices are deployed on a network running STP, the Huawei and non-Huawei devices may fail to communicate with each other, because they have different Proposal/Agreement mechanisms. To address this problem, run the stp no-agreement-check or undo **stp no-agreement-check** command to set a common or enhanced fast transition mechanism based on the Proposal/Agreement mechanism of the non-Huawei device.



**Precautions**

For two directly connected devices in a spanning tree, the device closer to the root bridge is the upstream device of the other device. The port fast transition mechanism is also called the Proposal/Agreement mechanism. The device currently supports the following modes:

* Enhanced mode: The current port participates in root port calculation when calculating the synchronization flag bit.
  1. An upstream device sends a Proposal message to a downstream device, requesting fast transition. After receiving the message, the downstream device sets the port connected to the upstream device as a root port and blocks all non-edge ports.
  2. The upstream device then sends an Agreement message to the downstream device. After the downstream device receives the message, the root port transitions to the Forwarding state.
  3. The downstream device responds to the Proposal message with an Agreement message. After receiving the message, the upstream device sets the port connected to the downstream device as a designated port, and the designated port transitions to the Forwarding state.
* Common mode: The current port does not participate in root port calculation when calculating the synchronization flag bit.
  1. An upstream device sends a Proposal message to a downstream device, requesting fast transition. After receiving the message, the downstream device sets the port connected to the upstream device as a root port and blocks all non-edge ports. The root port then transitions to the Forwarding state.
  2. The downstream device responds to the Proposal message with an Agreement message. After receiving the message, the upstream device sets the port connected to the downstream device as a designated port, and the designated port transitions to the Forwarding state.


Example
-------

# Configure the common fast transition mechanism for 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp no-agreement-check

```