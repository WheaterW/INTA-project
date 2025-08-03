fips-mode enable(System view)
=============================

fips-mode enable(System view)

Function
--------



The **fips-mode enable** command enables the FIPS mode.

The **undo fips-mode enable** command disables the FIPS mode.



By default, the FIPS mode is disabled.


Format
------

**fips-mode enable**

**undo fips-mode enable**


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

You can run the **fips-mode enable** command to enable the FIPS mode. In this mode, the algorithms used by cryptographic modules must comply with FIPS to ensure that cryptographic modules are running properly.

**Configuration Impact**

If the FIPS mode is changed, the configuration file for next startup is cleared and the device is restarted immediately. Therefore, exercise caution when changing the FIPS mode.


Example
-------

# Enable the FIPS mode.
```
<HUAWEI> system-view
[~HUAWEI] fips-mode enable
Warning: Changing the FIPS mode will clear the configuration file used for next startup and restart the device. Continue? [Y/N]:y

```