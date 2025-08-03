display current-configuration (All views)
=========================================

display current-configuration (All views)

Function
--------

The **display current-configuration** command displays the set parameters that take effect on the device.



Format
------

**display current-configuration** [ **configuration** [ *configuration-type* [ *configuration-instance* ] | *config-type-no-inst* ] | **all** | **inactive** ] [ **include-default** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **configuration** | Displays the configuration of some specified level-2 features. | The value must be set according to the device configuration. |
| *configuration-type* | Specifies the configuration type. | The value must be set according to the device configuration. |
| *configuration-instance* | Specifies the configuration instance. | The instance is a string of 1 to 200 characters. |
| *config-type-no-inst* | Specifies the configuration module. | The value must be set according to the device configuration. |
| **all** | Specifies all the configuration information. | - |
| **inactive** | Specifies all configurations of the board in the offline state. | - |
| **include-default** | Displays both the configurations that users have performed and default configurations. | - |




Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

* After completing a set of configurations, you can run the **display current-configuration** command to check the parameters that take effect. If a function does not take effect, the parameters corresponding to the function are not displayed. This command does not display parameters that use default settings.
* When you run the **display current-configuration** command:
* If include-default is not specified, only user configurations are displayed.
* If include-default is specified, the command displays both user configurations and default device configurations.

**Configuration Impact**

You can filter the output using regular expressions in the case of a large amount of configuration information. For usage of regular expressions, see "CLI Overview" in Configuration Guide > Basic Configurations.

**Precautions**

The following configurations are not displayed in the command output.

* Configurations that are the same as default ones
* Configurations that have not been committedIn different view, this command displays the configurations associated with the view.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display both the configurations that include user, including default configurations. (The command output is not all listed.)
```
<HUAWEI> display current-configuration include-default | include user
local-user aaa password irreversible-cipher $1d$wrcoG+up@($z((,He+)x<\Wbv1K"paL#$~(NcTY~J|8kj)=7k:H$          
 user-password min-len 6   
 undo user-password complexity-check  
 user-password expire 0 prompt 0  
 undo user-password change   
 user-block failed-times 5 period 5
 user-block reactive 5

```

# Display the configuration that includes the default configuration.
```
<HUAWEI> display current-configuration include-default
!Software Version V300R023C00
!Last configuration was updated at 2020-06-01 07:13:54+00:00
#
~language character-set UTF-8
#
sysname HUAWEI
#
~info-center channel 0 name console
~info-center channel 1 name monitor
~info-center channel 2 name loghost
~info-center channel 3 name trapbuffer

```

# Display all the configurations that begin with user.
```
<HUAWEI> display current-configuration | begin user
user-interface con 0
 set authentication password cipher $1d$k4:o79a_DJ$dkxW!,\@7Cjr*k+Q}gb'{g{x)#wS1GjQST'EZ]/F$
 history-command max-size 30
#
return

```

# Display all the configurations that include user.
```
<HUAWEI> display current-configuration | include user
local-user aaa password irreversible-cipher $1d$wrcoG+up@($z((,He+)x<\Wbv1K"paL#$~(NcTY~J|8kj)=7k:H$

```

# Display the configuration parameters that take effect in the system.
```
<HUAWEI> display current-configuration
#
sysname HUAWEI
#
interface 10GE1/0/1
#
interface 10GE1/0/2
#
user-interface con 0
 set authentication password cipher $1d$k4:o79a_DJ$dkxW!,\@7Cjr*k+Q}gb'{g{x)#wS1GjQST'EZ]/F$
 history-command max-size 30
#

```


**Table 1** Description of the
**display current-configuration (All views)** command output

| Item | Description |
| --- | --- |
| # | The # command can be used to return to the system view from the current view stack. |