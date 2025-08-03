display license esn
===================

display license esn

Function
--------



The **display license esn** command displays the equipment serial number (ESN) of a device.




Format
------

**display license esn**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To use a function controlled by a license file, you need to apply for a license file. When applying for a new license file, you need to enter the ESN as the key information. The ESN uniquely identifies a device component. After running the **display license esn** command, you can view the ESN of the device.



**Precautions**

The **display license esn** command outputs on the active and standby boards must be the same.The ESN of the device must be the same as the ESN field in the license file to be activated. Otherwise, the license file cannot be activated or the license file enters the trial state after being activated.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the equipment serial number of a device.
```
<HUAWEI> display license esn
MainBoard:
ESN: 2161ABC10efg01001***

```

**Table 1** Description of the **display license esn** command output
| Item | Description |
| --- | --- |
| ESN | Equipment serial number. |
| MainBoard | Main control board. |