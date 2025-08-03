Maintaining Service Diagnosis
=============================

Maintaining Service Diagnosis

#### Context

After service diagnosis is enabled and a diagnosis object is created on a device, the device creates a diagnosis instance when a user matching the attributes of the diagnosis object goes online. If the device performs service diagnosis for multiple users, it creates a diagnosis instance for each user, which occupies a large number of system resources. To prevent waste, the device automatically deletes diagnosis instances when corresponding users go offline. The drawback here is that if some users are disconnected unexpectedly, the service diagnosis module cannot detect when users go offline, and retains the diagnosis instances created for these users, wasting system resources. To resolve this issue, the device provides an aging mechanism for diagnosis instances. That is, when the aging period of a diagnosis instance expires, the device automatically deletes the diagnosis instance to reclaim resources.

In addition, you can run the [**reset trace instance**](cmdqueryname=reset+trace+instance) command to clear all diagnosis instances on the device.

![](public_sys-resources/notice_3.0-en-us.png) 

After the [**reset trace instance**](cmdqueryname=reset+trace+instance) command is executed, running diagnosis instances are also deleted. Exercise caution when you use this command.



#### Procedure

1. Run the [**reset trace instance**](cmdqueryname=reset+trace+instance) command in the system view to clear all diagnosis instances on the device.