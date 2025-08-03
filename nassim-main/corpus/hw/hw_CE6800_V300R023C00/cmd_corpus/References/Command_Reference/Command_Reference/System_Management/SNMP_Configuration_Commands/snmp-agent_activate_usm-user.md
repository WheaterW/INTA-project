snmp-agent activate usm-user
============================

snmp-agent activate usm-user

Function
--------



The **snmp-agent activate usm-user** command activates locked users.



By default, a user account is in active state after being created.


Format
------

**snmp-agent activate usm-user** *user-name* [ **remote-engineid** *remote-engineid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies a user name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **remote-engineid** *remote-engineid* | Binds an SNMP proxy rule to the engine ID of a managed device. | The value is a string of 10 to 64 case-insensitive characters without spaces.  The value is a hexadecimal integer ranging from 0 to F. All 0s or all Fs are invalid. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To defend against attacks to crack user passwords, run the **snmp-agent blacklist user-block failed-times** command to configure the maximum number of consecutive authentication failures for users. If a user fails to be authenticated for a specified number of consecutive times, the user is locked and added to a blacklist and will not be authenticated again. To activate locked users, run the **snmp-agent activate usm-user** command.


Example
-------

# Activate a locked user named John.
```
<HUAWEI> snmp-agent activate usm-user John remote-engineid 800007DB0338BA1F8CCC02

```