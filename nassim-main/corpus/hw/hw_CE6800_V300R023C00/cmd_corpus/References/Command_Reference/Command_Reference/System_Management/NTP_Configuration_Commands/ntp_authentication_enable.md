ntp authentication enable
=========================

ntp authentication enable

Function
--------



The **ntp authentication enable** command enables identity authentication for NTP.

The **undo ntp authentication enable** command disables identity authentication.



By default, identity authentication is disabled.


Format
------

**ntp authentication enable**

**undo ntp authentication enable**


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

NTP authentication can be used on networks that require high security.

**Precautions**



If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function. To enable the NTP server function, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.




Example
-------

# Enable identity authentication for NTP.
```
<HUAWEI> system-view
[~HUAWEI] ntp authentication enable

```