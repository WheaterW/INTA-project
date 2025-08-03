configuration file auto-save
============================

configuration file auto-save

Function
--------



The **configuration file auto-save** command configures the function of saving system configurations periodically.

The **undo configuration file auto-save** command cancels the function of saving system configurations periodically.



By default, the system does not enable the function.


Format
------

**configuration file auto-save** [ **interval** *interval* | **delay** *delay-interval* | **cpu-limit** *cpu-usage* ] \*

**configuration file auto-save** { **interval** | **delay** | **cpu-limit** } **default**

**undo configuration file auto-save**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval* | Specifies the interval at which configurations are saved automatically. | The value is an integer ranging from 30 to 43200, in minutes. The default value is 30. |
| **delay** *delay-interval* | Specifies the delay time for backing up a configuration automatically after the configuration is changed. | The value is an integer ranging from 1 to 60, in minutes. The default value is 5. |
| **cpu-limit** *cpu-usage* | Specifies the maximum CPU usage. | The value is an integer ranging from 1 to 100. The default value is 50. |
| **default** | Restores the default values for the parameters of the automatic save function. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the **configuration file auto-save** command is not run, the system does not enable the auto-save function. After the function of periodically saving configurations is enabled, if the configuration or configuration file changes, the system saves the configuration. Otherwise, the system does not save the configuration. If the system is configured to periodically save the configuration file to the server, the configuration file is also uploaded to the server.

* To specify the interval at which configurations are saved, specify interval.
* cpu-limit: specifies the upper limit of the CPU usage when the system automatically saves the configuration. When the auto-save timer is triggered and the CPU usage of the system is higher than the configured value, the system cancels the auto-save operation. By default, the upper limit of the CPU usage is 50%.
* delay: The system automatically saves the configuration after the specified delay.
* If interval and delay are specified, the configuration saving operation is triggered by the parameter whose configuration time arrives first. When the configuration time of the other parameter arrives, the system checks the configuration again. If no change is found, the system does not save the configuration.The **undo configuration file auto-save** command is used to disable the auto-save function.The configuration file auto-save { interval | delay | cpu-limit } default command is used to restore the default values for the parameters of the auto-save function.

**Configuration Impact**



After the autosave function is configured, the system automatically saves configurations to the configuration file used for the next startup when the current running configuration is different from the next startup configuration file and the interval configured in the interval parameter expires, no matter whether the save operation has been manually saved.



**Follow-up Procedure**



Run the **display saved-configuration configuration** command, and view configuration information about the function of saving configurations periodically.



**Precautions**

In the following situations, the system cancels the operation of saving configurations periodically:

* The configuration file is being written.
* The device is restoring configurations.
* The CPU usage exceeds the configured threshold.

When the configuration file for next startup is specified, automatic saving is disabled and the disabling duration is 30 minutes.When the configuration is changed or the configuration file for next startup is specified, the configuration sequence number is changed and the configuration is automatically saved to the configuration file for next startup.When the automatic saving function is disabled, the configuration file auto-save delay default command cannot be used to enable the automatic saving function.



Example
-------

# Configure the autosave function, with the delay time for saving configuration change being 3 minutes, the interval for saving configuration change being 10 hours, and the maximum CPU usage being 60%.
```
<HUAWEI> system-view
[~HUAWEI] configuration file auto-save interval 600 delay 3 cpu-limit 60

```

# Configure the interval at which the system saves new configurations to be 60 minutes.
```
<HUAWEI> system-view
[~HUAWEI] configuration file auto-save interval 60

```