Configuring the Two-Phase Validation Mode
=========================================

To validate configurations after they are complete, configure the two-phase validation mode.

#### Context

The two-phase validation mode enhances configuration security and reliability and minimizes the impact of configurations on services. If the configuration of a service that has taken effect does not meet your expectation, roll the system back to the status before the configuration is committed.


#### Procedure

1. (Optional) Run [**configuration exclusive**](cmdqueryname=configuration+exclusive)
   
   
   
   Configurations are locked in the user view.
   
   
   
   To use the running database exclusively, lock configurations on the router.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After locking configurations, you can edit and commit configurations. Other users can view and edit configurations but cannot commit configurations.
   
   Other users can configure services in the running database only after you unlock configurations.
2. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The two-phase validation mode is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In two-phase validation mode, the command prompt is as follows:
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] 
   ```
3. (Optional) Run [**display configuration candidate merge**](cmdqueryname=display+configuration+candidate+merge)
   
   
   
   Configurations in the candidate database are previewed, including uncommitted and committed ones.
   
   
   
   You can run the [**clear configuration candidate**](cmdqueryname=clear+configuration+candidate) command to delete all uncommitted configurations.
4. (Optional) Run [**commit**](cmdqueryname=commit) **trial** [ *time* ] [ **persist***persistId* ]
   
   
   
   The trial running of a system configuration is enabled.
   
   
   
   * To disable the trial running function before the trial running times out, run the [**abort trial**](cmdqueryname=abort+trial) [ { **session** *session-id* | **persist** *persistId* } ] command to roll the configuration back to the status before the trial running.
   * To view the trial running status of a system configuration, run the [**display configuration trial status**](cmdqueryname=display+configuration+trial+status) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent a service from being affected, you can lock the configuration of the service as soon as the service process is initiated. When the configuration is being locked, configurations cannot be committed. The configuration of the service remains locked until the service process successfully starts. During this period, the configuration cannot be committed but can be viewed.
   
   If the configuration fails to be committed, wait 30 seconds and commit the configuration again. If the configuration fails to be committed again, a user has locked the configuration.
6. (Optional) If the configuration has been locked, run the [**quit**](cmdqueryname=quit) command to return to the user view. Then, run the [**undo configuration exclusive**](cmdqueryname=undo+configuration+exclusive) command to unlock the configuration.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After locking the configuration, you must unlock it after completing the configuration. Otherwise, configurations of other users cannot take effect.