single-fiber rx
===============

single-fiber rx

Function
--------



The **single-fiber rx** command enables the single-fiber receiving function on an optical interface.

The **undo single-fiber rx** command disables the single-fiber receiving function on an optical interface.



By default, the single-fiber receiving function is disabled on an optical interface.


Format
------

**single-fiber rx**

**undo single-fiber rx**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The single-fiber receiving function allows you to connect the RX end of a local optical module to a remote optical module using a single optical fiber so that the local interface can only receive packets but cannot send packets. You can configure this function on an optical interface when an optical module (not a single-fiber bidirectional optical module) is installed or the transmission medium is pre-configured on the interface. The local interface goes Up only when both the local and remote optical modules are installed and can properly receive optical signals. With this function, the device can only receive packets but cannot send packets. This function ensures data security on the device and allows you to obtain the real physical status of the interface.

**Precautions**

* If an MPO optical module is installed on an unsplit optical interface or an LC optical module is installed on a split optical interface, the interface enters the Down(Transceiver type mismatch) state after this command is run. Replace the optical module with another type of optical module.
* If this command has been run on an interface and a single-fiber bidirectional optical module or high-speed cable is installed on the interface, the interface goes Down and the single-fiber receiving function cannot be used.
* After you run the **single-fiber rx** command on the local interface, the local interface can only receive packets through a single fiber. The local interface must be connected to the TX end of the remote optical module, and the remote optical module cannot have the same configuration.
* The interfaces on the local and remote devices must work in non-auto-negotiation mode and have the same rate configured.
* The single-fiber rx and loopback commands cannot be used together.
* If you run the single-fiber rx and single-fiber enable commands in sequence, the command that you run last takes effect.

Example
-------

# Enable the single-fiber receiving function on an optical interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] single-fiber rx

```