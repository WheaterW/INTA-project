snmp-agent blacklist user-block reactive
========================================

snmp-agent blacklist user-block reactive

Function
--------



The **snmp-agent blacklist user-block reactive** command configures a locking period for an SNMPv3 user who fails to be authenticated for a specified number of consecutive times.

The **undo snmp-agent blacklist user-block reactive** command restores the default locking period.



By default, the locking period is 5 minutes.


Format
------

**snmp-agent blacklist user-block reactive** *reactive-time*

**undo snmp-agent blacklist user-block reactive**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *reactive-time* | Specifies the user locking period. | The value is an integer ranging from 0 to 1000, in minutes. The default value is 5. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To improve security, run the snmp-agent blacklist user-block reactive command to configure a locking period for an SNMPv3 user who fails to be authenticated for a specified number of consecutive times. After the period of time elapses, the user is automatically unlocked and can continue to be authenticated.


Example
-------

# Configure a device to lock an SNMPv3 users for 12 minutes.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent blacklist user-block reactive 12

```