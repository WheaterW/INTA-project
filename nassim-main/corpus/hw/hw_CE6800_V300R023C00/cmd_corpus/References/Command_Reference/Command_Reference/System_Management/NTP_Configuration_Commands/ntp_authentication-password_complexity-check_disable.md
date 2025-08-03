ntp authentication-password complexity-check disable
====================================================

ntp authentication-password complexity-check disable

Function
--------



The **ntp authentication-password complexity-check disable** command disables password strength check on NTP identity authentication.

The **undo ntp authentication-password complexity-check disable** command enables password strength check on NTP server identity authentication.



By default, password strength check on NTP server identity authentication is enabled.


Format
------

**ntp authentication-password complexity-check disable**

**undo ntp authentication-password complexity-check disable**


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

On a network that requires high security, you are advised to run this command to enable strong password strength check for NTP identity authentication.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the **ntp server disable** or **ntp ipv6 server disable** command in the configuration file to disable the NTP service. To enable the NTP service, run the **undo ntp server disable** or **undo ntp ipv6 server disable** command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the **ntp server disable** or **ntp ipv6 server disable** command from the configuration file.Disabling the key strength check function causes security risks. Therefore, you are advised not to run this command.


Example
-------

# Disable password strength check on NTP server identity authentication.
```
<HUAWEI> system-view
[~HUAWEI] ntp authentication-password complexity-check disable
Warning: Password complexity check on NTP authentication will be disabled. Continue?  [Y/N]:y

```