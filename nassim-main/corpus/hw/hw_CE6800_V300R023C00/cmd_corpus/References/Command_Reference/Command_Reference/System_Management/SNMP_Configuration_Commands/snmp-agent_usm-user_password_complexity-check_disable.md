snmp-agent usm-user password complexity-check disable
=====================================================

snmp-agent usm-user password complexity-check disable

Function
--------



The **snmp-agent usm-user password complexity-check disable** command disables the complexity check on user authentication or encryption passwords.

The **undo snmp-agent usm-user password complexity-check disable** command enables the complexity check on user authentication or encryption passwords.



By default, the complexity check on user authentication or encryption passwords is enabled.


Format
------

**snmp-agent usm-user password complexity-check disable**

**undo snmp-agent usm-user password complexity-check disable**


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

The HUAWEI has the following requirements for user authentication or encryption passwords complexity:

* The default minimum length of a community name is eight characters.
* The community name includes at least two types of characters: uppercase letters, lowercase letters, digits, and special characters that exclude question marks (?) and spaces.On secure networks, to disable the complexity check on user authentication or encryption passwords, run the **snmp-agent usm-user password complexity-check disable** command.

**Precautions**

To improve security, enabling the complexity check on user authentication or encryption passwords is recommended.


Example
-------

# Disable the complexity check on user authentication or encryption passwords.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent usm-user password complexity-check disable

```