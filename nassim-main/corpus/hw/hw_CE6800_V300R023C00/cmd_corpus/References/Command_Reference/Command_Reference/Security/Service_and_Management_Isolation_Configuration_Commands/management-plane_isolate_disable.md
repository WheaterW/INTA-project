management-plane isolate disable
================================

management-plane isolate disable

Function
--------



The **management-plane isolate disable** command disables traffic isolation between the service and management planes.

The **undo management-plane isolate disable** command enables traffic isolation between the service and management planes.



By default, traffic isolation between the service and management planes is enabled.


Format
------

**management-plane isolate disable**

**undo management-plane isolate disable**


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



By default, traffic isolation between the service and management planes is enabled. In this case, IP packets received by a service interface are not forwarded through the interface configured with a management IP address, and IP packets destined for the interface configured with a management IP address cannot access the device.To forward IP packets on the service plane through the management plane, run the **management-plane isolate disable** command to disable the isolation function.



**Precautions**



For devices that do not support management interfaces, traffic isolation between the service plane and management plane does not take effect.




Example
-------

# Disable traffic isolation between the service and management planes.
```
<HUAWEI> system-view
[~HUAWEI] management-plane isolate disable

```