Managing Files
==============

You can log in to the file system to view, delete, or rename files on a device.

#### Context

* Managing files include displaying file content, copying files, moving files, renaming files, compressing files, deleting files, restoring deleted files, deleting files in the recycle bin, running batch files, and configuring notification modes.
* To operate a file, run the [**cd**](cmdqueryname=cd) *directory* command to switch the current directory to the file's directory.

#### Procedure

* Run [**more**](cmdqueryname=more) *file-name*
  
  
  
  The content of a specified file is displayed.
* Run [**copy**](cmdqueryname=copy) *source-filename* *destination-filename*
  
  
  
  A file is copied.
* Run [**move**](cmdqueryname=move) *source-filename* *destination-filename*
  
  
  
  A file is moved.
* Run [**rename**](cmdqueryname=rename) *source-filename* *destination-filename*
  
  
  
  A file is renamed.
* Run [**zip**](cmdqueryname=zip) *source-filename* *destination-filename*
  
  
  
  A file or directory is compressed.
* Run [**unzip**](cmdqueryname=unzip) *source-filename* *destination-filename*
  
  
  
  A file is decompressed.
  
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The [**zip**](cmdqueryname=zip) command can be used to compress files or directories, whereas the [**unzip**](cmdqueryname=unzip) command can only be used to decompress files.
* Run [**delete**](cmdqueryname=delete) [ **/unreserved** ] *filename* [ **all** ]
  
  
  
  A file is deleted.
  
  
  
  If you use the /**unreserved** parameter in the command, the file cannot be restored after being deleted.
  
  In VS mode, this command is supported only by the admin VS.
* Run [**undelete**](cmdqueryname=undelete) *filename*
  
  
  
  The deleted file is restored.
  
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  You can run the **[**dir /all**](cmdqueryname=dir+%2Fall)** command to view information about all files, including the files moved to the recycle bin, which are enclosed in square brackets ([]).
  
  The files that are deleted using the [**delete**](cmdqueryname=delete) command with **/unreserved** specified cannot be restored.
  
  In VS mode, this command is supported only by the admin VS.
* Run [**reset recycle-bin**](cmdqueryname=reset+recycle-bin) [ **/f** | *filename* ]
  
  
  
  A file in the recycle bin is deleted.
  
  
  
  You can permanently delete files in the recycle bin. The **/f** parameter indicates that all files in the recycle bin are deleted without prompting for your confirmation.
* Run [**tail**](cmdqueryname=tail) *file-name*
  
  
  
  The information in the last lines of a specified file is displayed.
* Run a batch file or VRP Shell Languages (VSL) script file.
  
  
  
  To perform multiple operations on a file at a time, create and run a batch file. The created batch file must be saved in a device's storage component in advance.
  
  To run a batch file, perform the following steps:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**execute**](cmdqueryname=execute) *filename* [ *parameter* &<1-8> ]
     
     
     
     A batch file or VSL script file is executed.
     
     
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     To prevent user information leakage, do not carry sensitive user data (such as ciphertext passwords and ciphertext keys) in the specified batch file or VSL script file.
* Configure a notification mode.
  
  
  
  The system displays a notification or warning message when you operate a device (especially operations leading to data loss). To change the notification mode for file operations, perform the following steps:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**file prompt**](cmdqueryname=file+prompt) { **alert** | **quiet** }
     
     
     
     A notification mode is configured.
     
     
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If the notification mode is set to **quiet**, the system does not display a warning message for data loss caused by misoperations.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.