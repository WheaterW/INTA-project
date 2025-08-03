snmp-agent extend error-code enable (System view)
=================================================

snmp-agent extend error-code enable (System view)

Function
--------



The **snmp-agent extend error-code enable** command enables extended error codes.

The **undo snmp-agent extend error-code enable** command disables extended error codes.



By default, extended error codes are disabled.


Format
------

**snmp-agent extend error-code enable**

**undo snmp-agent extend error-code enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

With the increasing number of features and scenarios supported by a device, the existing types of SNMP standard error codes cannot meet requirements in diversified scenarios. Therefore, the extended error code function is used. The extended error code defines more scenarios for the NMS to correctly analyze NE fault types.

**Precautions**

Huawei devices support the extended error code. An NMS and a managed device made by Huawei can be configured with the SNMP extended error code to extend the standard error code so that users can locate faults quickly.


Example
-------

# Enable the extended error code.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent extend error-code enable

```