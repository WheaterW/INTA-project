Specifying the System Software to Be Used at the Next Startup
=============================================================

Specifying the system software to be used at the next startup ensures that the device runs the new system software after being restarted.

#### Context

Before the version upgrade, you can run the [**upgrade rollback**](cmdqueryname=upgrade+rollback)  **enable rollback-timer** *time-value* command in the user view to enable the version rollback function and set a timeout period for version rollback during version upgrade. After the timeout period is set, the system will perform version rollback if no users log in to the device during the set timeout period.

The [**display upgrade rollback**](cmdqueryname=display+upgrade+rollback) command displays whether the version rollback function is enabled on a device.

Before the startup, run the [**check system-software**](cmdqueryname=check+system-software) command to verify the digital signature and check whether the target software is secure and available. The execution of this command lasts for about 3 to 10 minutes.


#### Procedure

1. In the user view, run [**startup system-software**](cmdqueryname=startup+system-software) *system-file*
   
   
   
   The system software to be used on the main control board at the next startup is specified.
   
   *system-file* indicates the file name of the system software, which is in the format of \*.cc.

#### Follow-up Procedure

If you want a PAF file to be loaded and run after the system restarts, you can run the [**startup paf**](cmdqueryname=startup+paf) { [**default**](cmdqueryname=default) | *file-name* } command to specify the PAF file to be used at the next startup.