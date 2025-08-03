commit (All views except the user view)
=======================================

commit (All views except the user view)

Function
--------



The **commit** command commits a configuration.




Format
------

**commit** [ **trial** [ *time* ] [ **label** *label* ] ] [ **persist** *persistId* ] [ **description** *description* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **trial** *time* | Specifies the timeout period for the trial running of a configuration. | The value is an integer ranging from 60 to 65535, in seconds. The default value is 600 seconds. |
| **label** *label* | Specifies a user label for a configuration rollback point. | The value is a string of 1 to 256 case-sensitive characters. It can be any visible ASCII character except for the space. However, the string can contain spaces if it is enclosed with double quotation marks (" "). The string cannot start with a digit or be a hyphen (-). |
| **persist** *persistId* | Specifies a persistence ID for a configuration trial run. | The value is a string of 1 to 256 case-sensitive characters. It can be any visible ASCII characters excluding spaces. If double quotation marks are used around the tag name, spaces are allowed in the tag name. |
| **description** *description* | Specifies information about a configuration rollback point. | The value is a string of 1 to 60 case-sensitive ASCII characters, spaces supported. |



Views
-----

All views except the user view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* To add a description for the committed configuration to provide guidance and help for subsequent configuration rollback, run the commit description command in two-phase validation mode. You can run the **display configuration commit list verbose** command to view the generated description.
* You can use the trial keyword to configure the trial run function. This function enables a trial run of new functions and services on the live network to improve network reliability. The time parameter specifies the timeout period of the trial run. During the trial run, you can run the **commit** command to make the configuration in trial running state take effect. When the trial run time exceeds the specified timeout period, the system automatically rolls back the configuration in the trial running state and restores the system to the status before the configuration. If you want the configuration in the trial run state to take effect, reconfigure the configuration and commit it. During the trial run, you can run the **commit trial** command to refresh the trial run time.
* If you are not sure about the configuration impact or want to observe the configuration effect after the configuration, you are advised to run the **commit trial** command. After confirming that the configuration has achieved the expected effect, reconfigure and commit the configuration to ensure operation security on the live network.
* If persistId is specified during the configuration trial run, the persistent trial run does not terminate when the session ends. You can run the commit persist \ command to confirm the configuration of persistent trial running.
* In two-phase validation mode, if a user has uncommitted configurations, the configurations are marked with asterisks (\*) in the corresponding view. If all configurations have been committed, ~ is displayed in the corresponding view except the user view.

**Prerequisites**



The system view for the two-phase configuration validation mode has been displayed using the system-view command, and the configuration has been modified.



**Configuration Impact**



After the **commit** command is run, the changes in system configurations take effect. The changes include only configuration changes committed after the two-phase configuration validation mode is configured.



**Precautions**

The **commit trial** command applies to the two-phase configuration validation mode only.When multiple users commit configurations at the same time, the configurations of some users may fail to be committed due to configuration locking.


Example
-------

# Enable the trial running of a configuration and set the timeout period for the trial running to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] sysname ROLLBACK
[*HUAWEI] commit trial 120
Info: The system enters the trial configuration mode.
The system will revert to previous configuration if the trial configuration is not confirmed in 120 seconds.
[~ROLLBACK]

```

# Enable persistent configuration trial run.
```
<HUAWEI> system-view
[~HUAWEI] sysname DeviceA
[*HUAWEI] commit trial persist abcid
Info: The system enters the trial configuration mode.
The system will revert to previous configuration if the trial configuration is not confirmed in 600 seconds.
[~DeviceA]

```

# Add description for the configuration rollback point.
```
<HUAWEI> system-view
[~HUAWEI] sysname ROLLBACK
[*HUAWEI] commit description This is a new name
[~ROLLBACK] display configuration commit list verbose
1) CommitId: 1000000114
        Label: -
        User: Huawei
        User-Intf: VTY 0
        Type: CLI
        TimeStamp: 2012-07-03 20:20:40
        Description: This is a new name

2) CommitId: 1000000113
        Label: -
        User: root
        User-Intf: VTY 0
        Type: CLI
        TimeStamp: 2012-06-30 15:17:09
        Description: 

3) CommitId: 1000000112
        Label: -
        User: SNMP_User
        User-Intf: 
        Type: SNMP
        TimeStamp: 2012-06-30 15:16:56
        Description:

```

# Modify a configuration and commit the modified configuration.
```
<HUAWEI> system-view
[~HUAWEI] sysname HUAWEIA
[*HUAWEI] commit label a123
[~HUAWEI]

```