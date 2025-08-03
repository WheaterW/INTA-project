Configuring Model Files for the EAI System
==========================================

Configuring Model Files for the EAI System

#### Prerequisites

Before configuring model files for EAI, you have uploaded the model files to flash:/ on the device.


#### Context

The EAI system provides a complete universal framework for AI functions and performs inference on a massive volume of data related to an AI function based on the model to which the AI function subscribes. The AI function analyzes the inference result, generates specific configurations, and delivers the configurations to the device.

By default, a device has a default model file. After an AI function is enabled, the AI function automatically subscribes to the applicable model in the model file. After a new model file is loaded to the EAI system, the EAI system automatically uses the model of the latest version.

To update a model file, perform the following operations:


#### Procedure

1. Load a model file stored in a specified path for the EAI system.
   
   
   ```
   [load ai-service](cmdqueryname=load+ai-service) model-file model-file all
   ```
   
   Each device has a default model file, which cannot be uninstalled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * A maximum of 20 model files can be loaded to a device.
   * You can run the [**unload ai-service**](cmdqueryname=unload+ai-service) **model-file** *model-file* **all** command to uninstall an imported model file. If a model in the model file has been subscribed to, the model file cannot be uninstalled. After the AI service is disabled, the subscription is canceled.
   * The EAI system verifies the model files to be loaded. If a model file fails the verification, it cannot be loaded and a MODEL\_LOAD\_FAILED log is generated. Therefore, do not modify the name or content of downloaded model files.