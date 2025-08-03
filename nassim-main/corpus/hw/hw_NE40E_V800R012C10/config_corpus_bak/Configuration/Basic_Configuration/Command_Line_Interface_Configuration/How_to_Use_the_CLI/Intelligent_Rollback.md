Intelligent Rollback
====================

The CLI supports the intelligent rollback function. That is, in the current view, you can run commands in other views.

#### Context

Intelligent rollback enables the system to automatically return to the previous view if a command fails to be run in the current view. The system performs view return attempts until the applicable view of the command is displayed.

When configuring services, you need to enter the view of the command to be configured to complete the configuration. In this case, you need to run the **quit** command repeatedly to exit the current view and enter the required view. The intelligent rollback function allows you to run commands of other views in the current view to reduce repeated quit operations.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If command matching fails because an ambiguous command is entered in the current view, no intelligent rollback can be performed.

Intelligent rollback is not performed when a command fails to be matched.

The undo commands do not support intelligent rollback.



#### Example

1. Run the [**terminal command forward matched upper-view**](cmdqueryname=terminal+command+forward+matched+upper-view) command to enable the intelligent rollback function.
2. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
3. Run the [**interface**](cmdqueryname=interface) GigabitEthernet0/1/0.1 command to create a sub-interface and enter the sub-interface view.
4. You do not need to exit the current view. Run the [**interface**](cmdqueryname=interface) LoopBack 1 command to create a loopback interface and enter the loopback interface view.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If the intelligent rollback function is enabled, commands may be executed in unexpected views, and services may be interrupted. Before configuring a command, check whether the command to be configured exists in the view. If the command does not exist, run the command in the correct view.

To disable the intelligent rollback function, run the [**undo terminal command forward matched upper-view**](cmdqueryname=undo+terminal+command+forward+matched+upper-view) command.