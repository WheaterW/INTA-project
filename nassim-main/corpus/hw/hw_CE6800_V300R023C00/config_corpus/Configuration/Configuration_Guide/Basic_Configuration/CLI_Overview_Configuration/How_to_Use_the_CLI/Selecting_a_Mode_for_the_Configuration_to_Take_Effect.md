Selecting a Mode for the Configuration to Take Effect
=====================================================

To ensure the reliability of user configurations, the system allows configurations to take effect immediately or after two stages. The two-stage mode is used by default.

Before configuring a service, enter the system view. After the system view is displayed, the system initiates the corresponding configuration process based on the configured mode.

* The immediate mode is the traditional mode.
  
  In immediate mode, after you enter a command line and press **Enter**, the system performs a syntax check. The configuration takes effect as soon as it passes the syntax check.
* The two-stage mode divides the system configuration process into two stages.
  
  + In the first stage, a user enters command lines and the system performs syntax and semantics checks in the candidate database. If syntax or semantics errors are found in the command lines, the system displays a message on the terminal to inform the user of the error and the cause.
  + In the second stage, the user commits the configuration, and the system enters the configuration commitment stage. The system delivers configurations in the candidate database to a service. If these service configurations take effect, the system adds them to the running database of the current system. During the configuration commitment stage, the system checks the validity of configurations and displays a message when the same configurations exist in the candidate database and running database.

**Table 1** Advantages and disadvantages of the immediate mode and two-stage mode
| Mode | Advantage | Disadvantage |
| --- | --- | --- |
| Immediate mode | The system can immediately detect configuration impacts on services. | Any configuration errors will immediately impact services. In addition, you cannot delete service configurations all at once, and must delete commands individually. |
| Two-stage mode | * All committed configurations take effect at the same time. * Users can preview configurations in the candidate database. * A configuration that does not take effect can be deleted immediately if an error occurs, or in cases of unexpected results. * The impacts of configurations on existing services are minimized. | Configurations take effect only after the [**commit**](cmdqueryname=commit) command is run. |


In two-stage mode, you must run the [**commit**](cmdqueryname=commit) command for configurations to take effect, except in the following cases:

* Query commands (such as [**display interface**](cmdqueryname=display+interface)) are run.
* Maintenance commands (such as [**reset saved-configuration**](cmdqueryname=reset+saved-configuration) and [**reset keepalive packets count**](cmdqueryname=reset+keepalive+packets+count)) are run.
* Commands such as [**interface**](cmdqueryname=interface) **100GE****1/0/1** are run to enter the existing views (such as the physical interface view) on a physical device.
* Commands are run without changing the existing configurations.

#### Immediate Mode

Enable the immediate mode.
```
[system-view](cmdqueryname=system-view) immediately
```

In immediate mode, the command line prompt is as follows:

```
<HUAWEI> system-view immediately
Enter system view, return user view with return command.
[HUAWEI]
```

#### Two-Stage Mode

1. Enable the two-stage mode.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Display all uncommitted configurations.
   ```
   [display configuration candidate](cmdqueryname=display+configuration+candidate) [ merge | changes ]
   ```
   
   If you do not specify the **merge** and **changes** keywords, the command displays uncommitted configurations only. If you specify the **merge** keyword, the command displays both uncommitted and committed configurations. The **changes** keyword is specified to display the differences between the uncommitted configurations and current running configurations.
   
   You can edit uncommitted configurations.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the system displays a message indicating that the current running configurations are changed when you run the [**display configuration candidate**](cmdqueryname=display+configuration+candidate) **changes** command, run the [**refresh configuration candidate**](cmdqueryname=refresh+configuration+candidate) command to resolve the configuration conflict so that you can continue to view the configuration differences.
3. (Optional) Delete all uncommitted configurations.
   ```
   [clear configuration candidate](cmdqueryname=clear+configuration+candidate)
   ```
4. (Optional) Enable a trial run of system configurations.
   ```
   [commit](cmdqueryname=commit) trial [ time ] [ persist persistId ]
   ```
   
   This command enables a trial run of new functions and services without interrupting those running on the live network, which improves network reliability. When the trial running period elapses, the configurations in trial running state are automatically rolled back. If the **persist** parameter is not specified, the configuration trial run takes effect only in the current session. If the **persist** parameter is specified, the configuration trial run does not stop when the session ends.
   
   To disable the trial run of configurations before the trial run times out, run the [**abort trial**](cmdqueryname=abort+trial) command to roll the system configurations back to those used before the trial run. To view the trial run status of system configurations, run the [**display configuration trial status**](cmdqueryname=display+configuration+trial+status) command.
5. Commit configurations.
   ```
   [commit](cmdqueryname=commit) [ persist persistId ]
   ```
   
   Before the persistent trial run is rolled back due to timeout, you can specify the **persist** keyword in any session to commit the configurations in trial run.

In two-stage mode, if the user modifies but not commits configurations, the system prompt **~** is changed to **\***, notifying the user that the configurations are not committed. After the user runs the [**commit**](cmdqueryname=commit) command to commit the configurations, the system prompt **\*** is restored to **~**.

For example:

```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] sysname HUAWEIA
[*HUAWEI] commit
[~HUAWEIA]
```

![](public_sys-resources/note_3.0-en-us.png) 

* In both the immediate and two-stage modes, the system can lock the configuration of a service as soon as the service process starts, in order to prevent a service from being affected. In this situation, users can query configurations but cannot edit or commit them. If configurations fail to be committed, you are advised to wait for 30 seconds before retrying. If configurations still fail to be committed, the configurations are locked by a user.
* You can run the [**configuration exclusive**](cmdqueryname=configuration+exclusive) command to lock a configuration. If a configuration is locked by another user, you will need to ask the user to unlock it.
* In two-stage mode, when multiple users perform the same configuration, only the first committed configuration takes effect. Other users will receive a configuration conflict prompt.