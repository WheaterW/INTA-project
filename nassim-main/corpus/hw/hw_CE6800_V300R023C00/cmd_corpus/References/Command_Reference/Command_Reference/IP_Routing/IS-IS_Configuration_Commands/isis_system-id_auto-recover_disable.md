isis system-id auto-recover disable
===================================

isis system-id auto-recover disable

Function
--------



The **isis system-id auto-recover disable** command disables the system from automatically resolving IS-IS system ID conflicts.

The **undo isis system-id auto-recover disable** command enables the system to automatically resolve IS-IS system ID conflicts.



By default, if the system detects an IS-IS system ID conflict, it automatically changes the local system ID to resolve the conflict.


Format
------

**isis system-id auto-recover disable**

**undo isis system-id auto-recover disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A system ID uniquely identifies an IS-IS device. If the same system ID is configured for more than one device on the network, a routing loop may occur. By default, IS-IS is enabled to automatically change its system ID in the case of a system ID conflict. When a system ID conflict occurs, IS-IS automatically changes the local system ID to resolve the conflict.To disable the system from automatically resolving IS-IS system ID conflicts, run the **isis system-id auto-recover disable** command. After the command is run, IS-IS system ID conflicts need to be manually resolved.The first two bytes of the system ID automatically changed by the system are Fs, and the last four bytes are randomly generated.

**Precautions**

If the system IDs of two directly connected devices conflict, the neighbor relationship cannot be established but the entire network is not affected. Therefore, the system IDs of the two directly connected devices are not automatically adjusted. When a system ID conflict occurs between non-directly connected devices, IS-IS can automatically change the local system ID to eliminate the conflict.The automatically generated system ID is not recorded in the configuration file. Therefore, after the device is restarted, the system ID is restored to the first configured value and is regenerated. The newly generated system ID may be different from that before the restart. In addition, if the conflict persists after the system ID is automatically changed for three consecutive times, the system does not adjust the system ID.Changing the system ID will reset the IS-IS process. Therefore, exercise caution when performing this operation.If a system ID conflict of an IS-IS process has been automatically rectified, the system ID of the IS-IS process has been automatically changed to a value starting with ffff, and then the **isis system-id auto-recover disable** command is configured on the device, the system ID starting with ffff is restored to the configured value, triggering the IS-IS process to reset. As a result, the IS-IS neighbor relationship goes Down and is re-established, and a system ID conflict may occur again.


Example
-------

# Disable the system from automatically resolving IS-IS system ID conflicts.
```
<HUAWEI> system-view
[~HUAWEI] isis system-id auto-recover disable

```