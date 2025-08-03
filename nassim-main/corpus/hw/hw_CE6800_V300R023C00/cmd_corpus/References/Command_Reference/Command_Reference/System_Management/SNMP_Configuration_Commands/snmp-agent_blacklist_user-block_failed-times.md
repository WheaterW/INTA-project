snmp-agent blacklist user-block failed-times
============================================

snmp-agent blacklist user-block failed-times

Function
--------



The **snmp-agent blacklist user-block failed-times** command configures the maximum number of consecutive authentication failures allowed for an SNMPv3 user.

The **undo snmp-agent blacklist user-block failed-times** command restores the default maximum number of consecutive authentication failures allowed.



By default, an SNMPv3 user is locked if the user's five consecutive authentication attempts fail within 5 minutes.


Format
------

**snmp-agent blacklist user-block failed-times** *failed-times* **period** *period-time*

**undo snmp-agent blacklist user-block failed-times**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *failed-times* | Specifies the maximum number of consecutive authentication failures allowed. | The value is an integer ranging from 0 to 10. The default value is 5.  Value 0 indicates that no limitation is set for the number of user consecutive authentication failures. |
| **period** *period-time* | Specifies the period during which consecutive authentication attempts fail. | The value is an integer ranging from 1 to 120, in minutes. The default value is 5. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To defense against a user's attack to crack other users' passwords, run the **snmp-agent blacklist user-block failed-times** command so that when a user's consecutive authentication attempts exceed a specified number of times, the user is put on a blacklist and cannot be authenticated.

**Configuration Impact**

* This command takes effect on subsequent SNMPv3 users, not existing logged-in SNMPv3 users.
* If a malicious user repeatedly enters incorrect passwords, the user will be put on a blacklist and not allowed to log in to a device.

**Follow-up Procedure**

To unlock a user, run the **snmp-agent activate usm-user** command.


Example
-------

# Configure a device to lock a user if the user fails to be authenticated 3 consecutive times within 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent blacklist user-block failed-times 3 period 5

```