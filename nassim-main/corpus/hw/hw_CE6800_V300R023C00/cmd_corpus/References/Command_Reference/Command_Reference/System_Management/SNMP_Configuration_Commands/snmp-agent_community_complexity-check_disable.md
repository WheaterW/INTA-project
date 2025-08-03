snmp-agent community complexity-check disable
=============================================

snmp-agent community complexity-check disable

Function
--------



The **snmp-agent community complexity-check disable** command disables a device from checking the complexity of community names.

The **undo snmp-agent community complexity-check disable** command enables a device to check the complexity of community names.



By default, a device is enabled to check the complexity of community names.


Format
------

**snmp-agent community complexity-check disable**

**undo snmp-agent community complexity-check disable**


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

The HUAWEI has the following requirements on community name complexity:

* The default minimum length of a community name is eight characters.
* The community name includes at least two types of characters: uppercase letters, lowercase letters, digits, and special characters (excluding ? and spaces.)

**Configuration Impact**



After the complexity check is enabled, a configured community name must meet complexity requirements. After complexity check is disabled, a device does not check the complexity of community names.



**Precautions**

If the configured community name fails to meet complexity requirements, the community name may be easily attacked and cracked down by unauthorized users, affecting device security. Therefore, enabling the complexity check on a community name is recommended.


Example
-------

# Disable the complexity check for community names.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent community complexity-check disable

```