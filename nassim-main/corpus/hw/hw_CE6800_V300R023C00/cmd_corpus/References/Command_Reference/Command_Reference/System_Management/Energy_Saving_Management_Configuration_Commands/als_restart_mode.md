als restart mode
================

als restart mode

Function
--------



The **als restart mode** command sets a restart mode for the laser of an optical module.

The **undo als restart mode** command restores the default restart mode of a laser.



By default, a laser works in automatic restart mode.


Format
------

**als restart mode manual**

**als restart mode automatic**

**undo als restart mode** [ **manual** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **automatic** | Sets the mode of restarting the laser of the optical module to automatic. | - |
| **manual** | Sets the mode of restarting the laser of the optical module to manual. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Laser restart modes include automatic restart and manual restart.

* In automatic restart mode, the laser sends probe light pulses at the interval set using the **als restart pulse interval** command to detect whether the link recovers. The pulse width is set using the **als restart pulse width** command.
* In manual restart mode, you must run the **als restart** command to manually start the laser so that the laser sends a probe light pulse. The pulse width is specified by pulse-width in the **als restart pulse width** command.If the fiber link recovery can be detected in a timely manner, you can use the manual restart mode to enable the laser to immediately emit light. In this manner, data communication can be quickly restored.The constraints of the ALS function are as follows:
* ALS is supported only when an optical module is pre-configured, an optical interface has an optical module installed, or a combo interface works in optical mode. Electrical interfaces do not support ALS.
* When an optical port is used for unidirectional communication, the ALS function is not supported.
* Breakout interfaces do not support ALS.

Example
-------

# Configure lasers on 100GE1/0/1 to work in manual restart mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] als restart mode manual

```