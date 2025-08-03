configuration check local-user disable
======================================

configuration check local-user disable

Function
--------



The **configuration check local-user disable** command disables local user configuration check.

The **undo configuration check local-user disable** command enables local user configuration check.



By default, local user configuration check is enabled.


Format
------

**configuration check local-user disable**

**undo configuration check local-user disable**


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

* When you run the **startup** command to configure the configuration file for next startup, if the configuration file does not contain the **configuration check local-user disable** command, the system checks whether the configuration file contains local user configurations (such as the local login user name and password).
* If the specified configuration file does not contain local user configurations, the **startup** command fails to be delivered, and the configuration file for next startup fails to be configured.
* If the specified configuration file contains local user configurations, the **startup** command is successfully delivered, and the configuration file for next startup is successfully configured.
* When you run the **startup** command to configure the configuration file for next startup, if the configuration file contains the **configuration check local-user disable** command, the system does not check whether the configuration file contains local user configurations.

Example
-------

# Disable local user configuration check.
```
<HUAWEI> system-view
[~HUAWEI] configuration check local-user disable

```

# Enable local user configuration check.
```
<HUAWEI> system-view
[~HUAWEI] undo configuration check local-user disable

```