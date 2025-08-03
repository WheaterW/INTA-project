Maintaining an Application
==========================

Maintaining an Application

#### Procedure

The OAS allows users to stop, restart, and delete applications, and access the backend operating system of applications to perform O&M operations. [Table 1](#EN-US_TASK_0000001512846250__table3102145012364) lists the specific operations.

**Table 1** Operations related to application maintenance
| Operation | Command | Description |
| --- | --- | --- |
| Back up application data. | **[**backup application**](cmdqueryname=backup+application)** **application-name** | - |
| Expand the application storage space. | [**expand application**](cmdqueryname=+expand+application+volume+size) *application-name* **volume size** *expand-size* | When an application is running, you can run this command to expand the storage space. After this command is executed, the application automatically restarts for the capacity expansion to take effect. |
| Stop and delete an application instance. | **undo [**start**](cmdqueryname=start) position** { **slot** *slot-id* | **type** *board-type* } | - |
| Restart an application. | [**reset application**](cmdqueryname=reset+application) *application-name* **slot** *slot-id* | After an application is started, if you adjust the image software package and running options of the application, you need to restart the application for the modification to take effect. |
| Uninstall an application. | **undo** [**application**](cmdqueryname=application) *application-name* | Before uninstalling an application, stop the application and exit the OAS application view. |
| Log in to the backend operating system of the application. | [**login application**](cmdqueryname=login+application) *application-name* **slot** *slot-id* | Perform O&M operations and view information such as processes and application logs. |