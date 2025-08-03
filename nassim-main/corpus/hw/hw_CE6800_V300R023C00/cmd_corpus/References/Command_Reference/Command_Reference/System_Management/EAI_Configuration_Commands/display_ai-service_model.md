display ai-service model
========================

display ai-service model

Function
--------



The **display ai-service model** command displays information about the model file imported to the embedded AI system.




Format
------

**display ai-service model** [ **model-file** *model-file* | **model-name** *model-name* [ **model-version** *model-version* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **model-file** *model-file* | Specifies the name of a model package file. | The value is a string of 1 to 63 case-sensitive characters without spaces. |
| **model-name** *model-name* | Specifies a model name. | The value is a string of 1 to 16 case-sensitive characters without spaces. |
| **model-version** *model-version* | Specifies a model version. | The value is a string of 1 to 16 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After the embedded AI system loads the model file, the enabled AI service automatically reads the model file and performs inference on a large amount of data in the model based on the intelligent algorithm to obtain the optimal configuration value and implement the AI service function.You can run this command to view information about the current and loaded model files in the embedded AI system, including the model file name, version, and AI services that subscribe to the model file.

**Precautions**

* If no model package is imported to the embedded AI system, the query result of this command is empty.
* If no model information is filtered by command parameters, the query result of this command is empty.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all models.
```
<HUAWEI> display ai-service model
--------------------------------------------------------------------------------
File Name
          Model Name        Model Version     Model Type        Service
--------------------------------------------------------------------------------
AI_ECN-1.0.0-1.0.0.zip
          AI_ECN            1.0.0             Default           --
AI_ECN-1.0.0-1.0.2.zip
          AI_ECN            1.0.2             User Define       --
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ai-service model** command output
| Item | Description |
| --- | --- |
| File Name | Name of a model package. |
| Model Name | Model name. |
| Model Version | Model version. |
| Model Type | Model type. Valid options are Default, User Define, and PATCH, which indicates the default model package, user-defined model package file, and model patch package, respectively. |
| Service | Service name. |