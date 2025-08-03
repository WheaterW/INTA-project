snmp-agent blacklist user-block disable
=======================================

snmp-agent blacklist user-block disable

Function
--------



The **snmp-agent blacklist user-block disable** command disables the blacklist function for an SNMPv3 user.

The **undo snmp-agent blacklist user-block disable** command enables the blacklist function for an SNMPv3 user.



By default, the blacklist function for an SNMPv3 user is enabled.


Format
------

**snmp-agent blacklist user-block disable**

**undo snmp-agent blacklist user-block disable**


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

To improve security, run the undo snmp-agent blacklist user-block disable command to enable the blacklist function for an SNMPv3 user so that the user will be locked for several minutes if the user's authentication attempts exceed a specified number of times.

**Follow-up Procedure**

Run the **snmp-agent blacklist user-block failed-times** command to set the number of consecutive authentication failures allowed for an SNMPv3 user.Run the **snmp-agent blacklist user-block reactive** command to configure a locking period for an SNMPv3 user who fails to be authenticated for a specified number of consecutive times. After the period of time elapses, the user is automatically unlocked and can continue to be authenticated.

**Precautions**

By default, an SNMPv3 user is not allowed to log in if the user's authentication attempts fail five times within 5 minutes.


Example
-------

# Disable the blacklist function for an SNMPv3 user.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent blacklist user-block disable

```