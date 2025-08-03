stp root-protection (Layer 2 interface view)
============================================

stp root-protection (Layer 2 interface view)

Function
--------



The **stp root-protection** command enables root protection on a port.

The **undo stp root-protection** command restores the default setting.



By default, root protection is disabled on all ports.


Format
------

**stp root-protection**

**undo stp root-protection**


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



A root bridge may no longer be the root bridge after receiving Bridge Protocol Data Units (BPDUs) with a higher priority due to incorrect configurations or attacks on the network. Once the network topology is changed, a spanning tree begins to be recalculated, which may cause traffic to be transferred from high-speed links to low-speed links and trigger traffic congestion.A designated port enabled with the root protection function cannot change its port role. If such a port receives BPDUs with a higher priority, the port enters the Discarding state and does not forward packets. If the port does not receive any BPDUs with a higher priority before a period (generally twice longer than Forward Delay) expires, the port automatically enters the Forwarding state.You can run the **stp timer forward-delay** command to set the Forward Delay period.



**Precautions**



The root protection function takes effect only on a designated port. Configuring the root protection function on a port that functions as the designated port in all instances is recommended.If the stp root-protection command is run on a non-designated port, the root protection function does not take effect.




Example
-------

# Enable the root protection function on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp root-protection

```