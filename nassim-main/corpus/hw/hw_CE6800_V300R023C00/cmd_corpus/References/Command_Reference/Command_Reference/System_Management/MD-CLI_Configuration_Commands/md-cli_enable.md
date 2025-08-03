md-cli enable
=============

md-cli enable

Function
--------



The **md-cli enable** command enables the MD-CLI service.

The **undo md-cli enable** command disables the MD-CLI service.



By default, the MD-CLI service is disabled.


Format
------

**md-cli enable**

**undo md-cli enable**


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

To run commands in MD-CLI mode, run the **md-cli enable** command to enable the MD-CLI service first. To release resources occupied by the MD-CLI service, run the **undo md-cli enable** command to disable the MD-CLI service.

**Precautions**

When the **undo md-cli enable** command is run to disable the MD-CLI service, all current MD-CLI sessions will be disconnected, and all uncommitted configurations will be lost.


Example
-------

# Enable the MD-CLI service.
```
<HUAWEI> system-view
[~HUAWEI] md-cli enable

```

# Disable the MD-CLI service.
```
<HUAWEI> system-view
[~HUAWEI] undo md-cli enable

```