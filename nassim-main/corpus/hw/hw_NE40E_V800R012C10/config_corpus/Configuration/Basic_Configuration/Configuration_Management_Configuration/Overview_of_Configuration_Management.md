Overview of Configuration Management
====================================

The system supports two configuration validation modes: immediate validation and two-phase validation. By default, the two-phase validation mode takes effect. The system also supports offline configuration, which means that you can change interface configurations after a board is removed.

#### Configuration Validation Modes

The two configuration validation modes are described as follows:

* The immediate validation mode is a traditional configuration validation mode.
  
  In this mode, the [**system-view**](cmdqueryname=system-view) **immediately** command is used to enter the system view. After you enter a command and press **Enter**, the system performs a syntax check. If the check is successful, the configuration immediately takes effect.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configuration rollback is not supported in immediate validation mode.
* In two-phase validation mode, the system configuration process is divided into two phases:
  
  In this mode, the [**system-view**](cmdqueryname=system-view) command is used to enter the system view. In the first phase, after you enter a configuration command, the system performs syntax and semantics checks on the candidate database. If an incorrect clause is found, the system displays a message on the command line terminal, indicating the fault and cause. After entering a series of commands to complete a configuration, you can run the [**commit**](cmdqueryname=commit) command to commit the configuration. The system then enters the second phase, that is, configuration commitment phase. In the second phase, the system delivers the configuration in the candidate database to the corresponding service module. If the configuration takes effect, the system adds it to the running database. If the same configuration is added, the system displays a message.

The following table describes the advantages and disadvantages of the immediate and two-phase validation modes.

**Table 1** Advantages and disadvantages of the immediate and two-phase validation modes
| Validation Mode | Advantage | Disadvantage |
| --- | --- | --- |
| Immediate validation mode | The configuration impact on services can be detected immediately. | Incorrect configurations immediately affect services. You must delete incorrect configurations one by one because deleting services as a whole is not allowed. |
| Two-phase validation mode | * All configurations take effect at the same time. * Configurations in the candidate database can be previewed. * When you find that a configuration in the candidate database is incorrect or does not meet your expectation, you can immediately clear the configurations that have not taken effect. * The impacts of service configurations on the existing services can be minimized. | The [**commit**](cmdqueryname=commit) command must be run to validate configurations. NOTE:  In two-phase validation mode, if a configuration has not been committed, the symbol "\*" is displayed in the corresponding view (except the user view). If all configurations have been configured, the symbol "~" is displayed in the corresponding view (except the user view). |



#### Offline Configuration

The system supports offline configuration. Specifically, after you configure interfaces on a board and then remove the board, the configurations are not affected and you can continue to configure the interfaces.

If you install another board in the slot, the impacts on the previous configurations are as follows:

* The new board has the same type as the previous board.
  
  The system automatically restores the configurations of all interfaces on the new board. Then, you can view interface configurations and configure the interfaces on the new board.
* The new board has interfaces of a different type than the previous board.
  
  The system deletes the configurations of all interfaces on the previous board. The deleted configurations cannot be restored.
  
  For example, board A has interfaces of type P and configuration information.
  1. Remove board A and install board C with interfaces of type E.
  2. Remove board C without configuring its interfaces. If you run the [**display this**](cmdqueryname=display+this) command in the interface view on board C, the command output does not contain original configurations on board A.
  3. Install board A or another board with interfaces of type P. If you run the [**display
     this**](cmdqueryname=display+this) command in the interface view of board A or the board with interfaces of type P, the command does not contain original configurations on board A, either.
* The new board has a different number of interfaces of the same type as those on the previous board.
  
  + If the new board has more interfaces than the previous board does, the system performs the following operations:
    
    - Restores the configuration information on the interfaces that are the same as those on the previous board.
    - Keeps default configuration information on the other interfaces of the new board.
  + If the new board has fewer interfaces than the previous board, the system performs the following operations:
    
    - Restores the configuration information on the interfaces that are the same as those on the previous board.
    - Deletes the other interfaces of the previous board and their configuration information.

You can run the [**display current-configuration inactive**](cmdqueryname=display+current-configuration+inactive) or [**display current-configuration all**](cmdqueryname=display+current-configuration+all) command to view offline configuration on a device.