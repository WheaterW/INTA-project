Managing Directories
====================

You can manage directories to logically store files in hierarchy.

#### Context

Through directory management, you can create, delete, change, or view directories and view files in directories and sub-directories.


#### Procedure

* Run [**cd**](cmdqueryname=cd) *directory*
  
  
  
  A directory is changed to a specified directory.
* Run [**pwd**](cmdqueryname=pwd)
  
  
  
  The current directory is displayed.
* Run [**dir**](cmdqueryname=dir) [ **/all** ] [ *filename* ]
  
  
  
  Information about all files or a specified file is displayed.
  
  Either an absolute or relative path can be specified in this command.
  
  The following table describes files displayed in the command output.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Files displayed depend on the system software version and service configurations. The following table lists only common files.
  
  The wildcard "\*" can be used in the command.
  
  
  **Table 1** Files displayed in the command output
  | File Name | File Description |
  | --- | --- |
  | $\_checkpoint | File in which configuration rollback point information is saved. |
  | \*\*.cc | Software version file. |
  | $\_install\_hpg | Directory where patches released with the software version are saved. |
  | $\_install\_mod | Directory where dynamic module packages are saved. |
  | $\_license | Directory where activated licenses are backed up. |
  | $\_security\_info | Directory where the historical AAA user data is saved. |
  | $\_system | Linux system-predefined directory where system scripts are saved. |
  | backup\_bkp\_elb.txt | Backup file of the backplane electronic label (E-label). |
  | backupelb.txt | Backup file of the E-Label of a specific board, which is generated after the board's E-Label is automatically read most recently. |
  | backupelable.txt | Backup file of the E-Label of a specific board, which is generated after the board's E-Label is read manually most recently. |
  | dbupgrade.log | Log file containing logs generated during each database upgrade. |
  | device.sys | System hardware configuration file. |
  | lcsbox | File that saves the names and content of activated GTL license files. |
  | lpustat | Directory where the statistics about discarded packets on interface board chips are saved. Interface boards periodically collect such statistics and report them to the main control board. The statistics are then saved in this directory. |
  | pmdata | Directory where the service performance data file is saved. |
  | security | Directory where SSL certificates are stored. |
  | logfile | Log file, occupying independent storage space. |
  | KPISTAT | Used to store collected KPI data. |
  | said | Used to store information generated during fault detection, diagnosis, and rectification on the SAID node. |
  | lost+found | File management module's file that is damaged and then restored during a device restart. |
  | \*\*.zip/\*\*.cfg/\*\*.dat | System configuration file. For details, see the [**save**](cmdqueryname=save) command.  After being compressed, log files are suffixed with .zip. Compressed log files are classified as follows:  + log\_slot ID\_time.log.zip: a common log file that is greater than or equal to a specified size. + diaglog\_slot ID\_time.log.zip: a diagnostic log file that is greater than or equal to a specified size. To set the size of a log file, run the [**info-center logfile size**](cmdqueryname=info-center+logfile+size) command. |
  | \*.pat | Patch file. |
  | lpustat.dat | Log file containing logs generated when packets are discarded due to a forwarding engine fault.  The device automatically records data about lost packets in this case and saves the data to the lpustat directory on the CF card of the main control board as a structured hexadecimal file named **lpustat.dat**. As the **lpustat.dat** file is stored in hexadecimal format, it cannot be directly opened for viewing. To view this file, ask Huawei engineers to convert it into an lpustat.csv file in which data is displayed by time, slot ID, module, chip, fault ID, and fault information.  When the remaining space of the CF card is less than or equal to 110 MB, the device no longer records packet loss logs. |
  | insegdroplog.log | Log file containing logs about packet loss during MPLS forwarding. The device automatically records packet loss data generated due to label table query failures that occur during label-based service forwarding. The device saves the data to the insegdroplog directory on the CF card of the main control board as a file named **insegdroplog.log**. When the insegdroplog.log file is greater than 8 MB, the device automatically compresses the file into an insegdroplog\_timestamp.rar package and deletes the insegdroplog.log file. If new packet loss occurs, the device creates another insegdroplog.log file to record the data. The insegdroplog directory provides a maximum of 10 MB for log files. When the size of all log files in the directory exceeds 10 MB, the device deletes earliest log files to store new ones. |
* Run [**mkdir**](cmdqueryname=mkdir) *directory*
  
  
  
  A directory is created.
* Run [**rename**](cmdqueryname=rename) *source-filename* *destination-filename*
  
  
  
  The directory is renamed.
* Run [**rmdir**](cmdqueryname=rmdir) *directory*
  
  
  
  A specified directory is deleted.