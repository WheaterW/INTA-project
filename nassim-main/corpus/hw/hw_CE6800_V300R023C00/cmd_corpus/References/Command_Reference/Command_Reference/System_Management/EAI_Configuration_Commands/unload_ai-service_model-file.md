unload ai-service model-file
============================

unload ai-service model-file

Function
--------



The **unload ai-service model-file** command uninstalls a model file imported into the embedded AI system.




Format
------

**unload ai-service model-file** *model-file* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **model-file** *model-file* | Specifies the name of a model package file. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **all** | Unload the global model file. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to uninstall the model file imported to the embedded AI system.

**Precautions**

* The embedded AI system verifies the model file to be uninstalled. If the model file fails the verification, the uninstallation fails and the log MODEL\_UNLOAD\_FAILED is recorded.
* The model file that has been subscribed to cannot be uninstalled. If a user attempts to uninstall such a model file, the uninstallation fails, and the log MODEL\_UNLOAD\_FAILED is recorded.
* If a slave main control board exists on the device, the model file on the slave main control board also needs to be uninstalled. If the model file on the slave main control board fails to be uninstalled, the embedded AI system considers that the model file fails to be uninstalled and records the log MODEL\_UNLOAD\_FAILED.

Example
-------

# Uninstall the model package aiecn\_v1.2.zip.
```
<HUAWEI> unload ai-service model-file aiecn_v1.2.zip all

```