checkzero (RIPng view)
======================

checkzero (RIPng view)

Function
--------



The **checkzero** command enables the check on the Must-Be-Zero (MBZ) field in RIPng packets.

The **undo checkzero** command disables the check on the MBZ field in RIPng packets.



By default, the check on the MBZ field in RIPng packets is enabled.


Format
------

**checkzero**

**undo checkzero**


Parameters
----------

None

Views
-----

RIPng view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, devices discard all RIPng packets with a non-zero MBZ field.To allow a Huawei device to communicate with a non-Huawei device that can send RIPng packets with a non-zero MBZ field, run the **undo checkzero** command on the Huawei device.If all neighbors are trustworthy, run the **undo checkzero** command to disable the check on the MBZ field to save CPU resources.

**Precautions**

If the device does not need to receive RIPng packets with the MBZ field carrying non-zero values, running the **undo checkzero** command is not recommended because it is insecure.


Example
-------

# Enable the device to check the MBZ field.
```
<HUAWEI> system-view
[~HUAWEI] ripng 1
[*HUAWEI-ripng-1] checkzero

```