load ai-service model-file
==========================

load ai-service model-file

Function
--------



The **load ai-service model-file** command imports the model file of an embedded AI system.




Format
------

**load ai-service model-file** *model-file* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **model-file** *model-file* | Specifies the full path and name of the model package file. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **all** | Load the global model file. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The embedded AI system provides common model management, data obtaining, and preprocessing functions for AI services that are inferred based on intelligent algorithms on devices. The processed data can be integrated into devices through model loading.After the model file is loaded using this command, the enabled AI service automatically reads the model file and performs inference on a large amount of data in the model based on the intelligent algorithm to obtain the optimal configuration value to implement the AI service function.

**Prerequisites**

The model file has been uploaded to the path flash:/ on the device.

**Precautions**

* A maximum of 20 model files can be loaded to a device.
* The embedded AI system verifies the loaded model file. If the verification fails, the loading fails and the MODEL\_LOAD\_FAILED log is recorded. Therefore, do not change the file name or content after the model file is downloaded.
* If the device has a standby main control board, the model file needs to be synchronized to the standby main control board. Otherwise, the embedded AI system considers that the file fails to be loaded and records the MODEL\_LOAD\_FAILED log.

Example
-------

# Load the model file flash:/aiecn\_v1.2.zip.
```
<HUAWEI> load ai-service model-file aiecn_v1.2.zip all

```