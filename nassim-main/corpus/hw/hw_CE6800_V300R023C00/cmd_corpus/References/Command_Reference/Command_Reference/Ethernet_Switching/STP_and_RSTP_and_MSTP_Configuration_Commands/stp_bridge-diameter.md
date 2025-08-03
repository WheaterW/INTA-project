stp bridge-diameter
===================

stp bridge-diameter

Function
--------



The **stp bridge-diameter** command configures a network diameter for a spanning tree.

The **undo stp bridge-diameter** command restores the default network diameter.



By default, the network diameter of a spanning tree is 7.


Format
------

**stp bridge-diameter** *diameter*

**undo stp bridge-diameter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *diameter* | Specifies a network diameter. | The value is an integer ranging from 2 to 7. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* On a network running STP, the network diameter is the maximum number of devices between two devices. An improper network diameter may slow down network convergence and affect user communication.
* You can run the **stp bridge-diameter** command to set a proper network diameter based on the network scale. This helps accelerate network convergence.
* The following time parameters are related to the network scale:
* Hello Time
* Forward Delay
* Max Age

**Configuration Impact**



The device will automatically set proper values for Hello Time, Forward Delay, and Max Age based on the configured network diameter.



**Precautions**



After a network diameter is configured, Forward Delay and Max Age values are recorded in the configuration file, but the bridge-diameter value is not recorded in the configuration file. For an MSTP network, the network diameter configured using this command takes effect only for the CIST.




Example
-------

# Set the network diameter to 5.
```
<HUAWEI> system-view
[~HUAWEI] stp bridge-diameter 5

```