ntp high-precision-time server enable
=====================================

ntp high-precision-time server enable

Function
--------



The **ntp high-precision-time server enable** command enables the high-precision NTP server function.

The **undo ntp high-precision-time server enable** command disables the high-precision server function.



By default, the high-precision NTP server function is disabled.


Format
------

**ntp high-precision-time server enable**

**undo ntp high-precision-time server enable**


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

For a network that requires high reliability and high time precision, you can enable the NTP high-precision server function.


Example
-------

# Enable the high-precision NTP server function.
```
<HUAWEI> system-view
[~HUAWEI] ntp high-precision-time server enable

```