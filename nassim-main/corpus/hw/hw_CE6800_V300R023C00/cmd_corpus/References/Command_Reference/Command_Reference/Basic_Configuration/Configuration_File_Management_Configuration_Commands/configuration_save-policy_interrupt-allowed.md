configuration save-policy interrupt-allowed
===========================================

configuration save-policy interrupt-allowed

Function
--------



The **configuration save-policy interrupt-allowed** command enables configuration saving interruption upon configuration committing and triggers the system to automatically save configurations.

The **undo configuration save-policy interrupt-allowed** command disables configuration saving interruption upon configuration committing and triggers the system to automatically save configurations.



By default, configuration committing will interrupt configuration saving, and the system is disabled from automatically saving configurations.


Format
------

**configuration save-policy interrupt-allowed**

**undo configuration save-policy interrupt-allowed**


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

After the **configuration save-policy interrupt-allowed** command is configured, if a user delivers configurations during configuration saving, configuration saving will be interrupted and fail, and configuration delivery will succeed. The system automatically saves the configurations five minutes later.After the **undo configuration save-policy interrupt-allowed** command is configured, if a user delivers configurations during configuration saving, configuration saving will not be affected, and configuration delivery will fail.

**Precautions**

* After the configuration saving is interrupted due to configuration committing, the system automatically saves the configurations 5 minutes later. If automatic or manual configuration saving is triggered within 5 minutes, the system does not automatically save the configurations 5 minutes after the interruption of configuration saving.
* The system may fail to save the configurations automatically. If the system restarts, the configurations added after the configurations are saved last time will be lost. Before restarting the device, manually save the configurations to ensure that the configurations are saved successfully.
* When the system automatically saves the configurations, if a user delivers configurations, the configuration saving will be interrupted again. After 5 minutes, the system saves the configurations again.
* The system may fail to automatically save configurations because the system is saving configurations or the disk space is insufficient.
* If you run the **startup** command to reset the configuration file for the next startup within 5 minutes after the configuration saving is interrupted due to configuration committing, the system does not automatically save the configurations 5 minutes later.

Example
-------

# Set the saving policy to the type that allows interruption.
```
<HUAWEI> system-view
[~HUAWEI] configuration save-policy interrupt-allowed

```

# Cancel the configuration of the saving policy as the type that allows interruption.
```
<HUAWEI> system-view
[~HUAWEI] undo configuration save-policy interrupt-allowed

```