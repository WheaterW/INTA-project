software
========

software

Function
--------



The **software** command configures the image software package used by an application.

The **undo software** command restores the image software package specified in the configuration file during application installation.



By default, the image software package of an application is specified in the configuration file during application installation.


Format
------

**software** *software-name*

**undo software**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *software-name* | Specifies the image software package. | The value is a string of 1 to 127 case-sensitive characters. It cannot contain spaces. |



Views
-----

OAS application view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* Run the **software** command to modify the image software package used by the application. If you do not specify a configuration file or the configuration file does not contain image information during application installation, you need to run this command to specify the image software package of the application. Otherwise, the application fails to be started.
* If the image software package is updated when the application is started, the update takes effect when the application is started next time. You can also manually restart the application for the settings to take effect.

Example
-------

# Restore the image software package specified in the configuration file during application installation.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] application app1
[*HUAWEI-oas-app1] undo software
Warning: Software will be restored to its default settings. Continue? [Y/N]:y

```

# Configure the image software package used by the application.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] application app1
[*HUAWEI-oas-app1] software oasImage.zip

```