bandwidth-config enable
=======================

bandwidth-config enable

Function
--------



The **bandwidth-config enable** command enables a device to use the configuration bandwidth of each OSPF interface to calculate the cost for the interface.

The **undo bandwidth-config enable** command disables a device from using the configuration bandwidth of each OSPF interface to calculate the cost for the interface.



By default, the configuration bandwidth of an OSPF interface is not used in cost calculation for the interface.


Format
------

**bandwidth-config enable**

**undo bandwidth-config enable**


Parameters
----------

None

Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

External factors may affect the physical bandwidth of links and change the physical bandwidth of interfaces, which in turn affects network performance. To configure a device to adjust and optimize route selection rules, you can run the **bandwidth** command in the interface view to set configuration bandwidth for the interface, and then run the **bandwidth-config enable** command to enable the device to calculate the cost for the interface based on the configuration bandwidth of the interface.

**Precautions**

* If the **bandwidth** command is not run, the cost is calculated based on the physical bandwidth of each OSPF interface.
* If the **bandwidth-config enable** command is not run, the cost is calculated based on the physical bandwidth of each OSPF interface.

Example
-------

# Enable a device to use the configuration bandwidth of each OSPF interface to calculate the cost for the interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] bandwidth-config enable

```