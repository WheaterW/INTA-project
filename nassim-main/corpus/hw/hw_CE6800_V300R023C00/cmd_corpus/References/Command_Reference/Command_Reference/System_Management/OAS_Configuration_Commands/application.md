application
===========

application

Function
--------



The **application** command installs an application in the open application system and displays the application view, or directly displays an existing application view.

The **undo application** command uninstalls an application from the open application system.



By default, no application is installed in the open application system.


Format
------

**application** *application-name* [ **config-file** *config-file-name* ]

**undo application** *application-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *application-name* | Specifies the name of an application. | The value is a string of 2 to 63 case-sensitive characters without spaces. |
| **config-file** *config-file-name* | Specifies the name of a configuration file. | The value is a string of 1 to 127 case-sensitive characters without space. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During application installation, you can configure applications in either of the following ways:

* Specify the configuration file to generate the default configuration. You need to install the verification public key on the device to verify the signature of the configuration file.
* The default configuration file is not provided during application installation. After the application is installed, run the **run-options** command to configure the default configuration file.

**Precautions**

Before uninstalling an application, you need to stop the application.


Example
-------

# Install an application in the open application system.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] application app1

```