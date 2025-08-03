mac-address flapping trigger error-down
=======================================

mac-address flapping trigger error-down

Function
--------



The **mac-address flapping trigger error-down** command configures an action on an interface where MAC address flapping occurs.

The **undo mac-address flapping trigger error-down** command deletes the action configured on an interface where MAC address flapping occurs.



By default, no action is configured on an interface where MAC address flapping occurs.


Format
------

**mac-address flapping trigger error-down**

**undo mac-address flapping trigger error-down**


Parameters
----------

None

Views
-----

100GE Layer 2 sub-interface view,Layer 2 100GE interface view,Layer 2 10GE interface view,200GE Layer 2 sub-interface view,Layer 2 200GE interface view,25GE-L2 view,400GE Layer 2 sub-interface view,400GE-L2 view,50GE Layer 2 sub-interface view,Layer 2 50GE interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Layer 2 sub-interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If MAC address flapping occurs on a user network due to a ring network and the network does not support loop prevention protocols, you can configure an action to be taken on the corresponding interface to prevent loops. After an action is configured on an interface, the system shuts down the interface when detecting MAC address flapping on the interface.

**Follow-up Procedure**

By default, an interface does not recover after being shut down. Network management personnel can run the **shutdown** command and then the **undo shutdown** command to recover the interface, or run the **restart** command in the interface view to restart the interface.

**Precautions**

* Only one interface can be shut down within an aging period of flapping MAC addresses.
* You are advised not to run the **mac-address flapping trigger error-down** command on the uplink interface.
* MAC address flapping detection can only detect single-point loops and cannot obtain the topology of the entire network. If the network supports loop prevention protocols, you are advised to use loop prevention protocols to eliminate loops.

Example
-------

# Configure a switching device to shut down the 100GE 1/0/1 interface after detecting MAC address flapping.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] mac-address flapping trigger error-down

```