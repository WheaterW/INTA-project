Configuring the Immediate Validation Mode
=========================================

To immediately validate configurations, configure the immediate validation mode.

#### Context

Before configuring a service, you must enter the system view. After the system view is displayed, the system initiates the corresponding configuration transaction based on the configured validation mode. In immediate validation mode, after you enter a command and press **Enter**, the system performs a syntax check. If the check is successful, the configuration immediately takes effect.


#### Procedure

1. (Optional) Run [**configuration exclusive**](cmdqueryname=configuration+exclusive)
   
   
   
   Configurations are locked in the user view.
   
   
   
   To use the running database exclusively, lock configurations on the router to prevent other users from configuring services or committing configurations. Other users can configure services in the running database only after you unlock configurations.
   
   To view information about the user who locked the configuration database, run the [**display configuration-occupied user**](cmdqueryname=display+configuration-occupied+user) command.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After locking configurations, you can edit and commit configurations. Other users can view and edit configurations but cannot commit configurations.
   
   Other users can configure services in the running database only after you unlock configurations.
2. Run [**system-view**](cmdqueryname=system-view) **immediately**
   
   
   
   The immediate validation mode is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent a service from being affected, you can lock the configuration of the service as soon as the service process is initiated. When the configuration is being locked, configurations cannot be committed. The configuration of the service remains locked until the service process successfully starts. During this period, the configuration cannot be modified but can be viewed.
   
   If the configuration fails to be committed, wait 30 seconds and commit the configuration again. If the configuration fails to be committed again, a user has locked the configuration.
   
   In immediate validation mode, the command prompt is as follows:
   
   ```
   <HUAWEI> system-view immediately
   ```
   ```
   [HUAWEI] 
   ```
3. (Optional) If the configuration has been locked, run the [**quit**](cmdqueryname=quit) command to return to the user view. Then, run the [**undo configuration exclusive**](cmdqueryname=undo+configuration+exclusive) command to unlock the configuration.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After locking the configuration, you must unlock it after completing the configuration. Otherwise, configurations of other users cannot take effect.
4. Run [**configuration-occupied timeout**](cmdqueryname=configuration-occupied+timeout) *timeout-value*
   
   
   
   A period after which the configuration database is unlocked automatically is configured.