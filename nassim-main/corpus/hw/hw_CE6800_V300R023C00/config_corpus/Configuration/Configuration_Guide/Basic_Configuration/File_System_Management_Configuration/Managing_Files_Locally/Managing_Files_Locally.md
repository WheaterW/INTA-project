Managing Files Locally
======================

Managing Files Locally

#### Prerequisites

Before managing files locally, complete the following tasks:

* Ensure that there are reachable routes between the terminal and the device.
* Log in to the device from the terminal.

#### Procedure

* **Perform operations on directories.**
  
  
  
  **Table 1** Operations on directories
  | Operation | Command | Description |
  | --- | --- | --- |
  | Display the current directory. | [**pwd**](cmdqueryname=pwd) | - |
  | Change the current directory. | [**cd**](cmdqueryname=cd) [ *directory* ] | - |
  | Display files and subdirectories in a specified directory. | [**dir**](cmdqueryname=dir) [ **/all** ] [ *filename* | **/all-filesystems** ] | - |
  | Display all files in the backup partition. | [**display backup-file**](cmdqueryname=display+backup-file) | - |
  | Create a directory. | [**mkdir**](cmdqueryname=mkdir) *directory* | - |
  | Delete a directory. | [**rmdir**](cmdqueryname=rmdir) *directory* | + The directory to be deleted must be empty. + A deleted directory and its files cannot be restored from the recycle bin. |
* **Perform operations on files.**
  
  
  
  **Table 2** Operations on files
  | Operation | Command | Description |
  | --- | --- | --- |
  | Display the file content. | [**more**](cmdqueryname=more) *file-name* [ *offset* ] | You can also run the [**tail**](cmdqueryname=tail) *file-name* [ *line* ] command to view the last specified lines in the specified file. |
  | Copy a file. | [**copy**](cmdqueryname=copy) *source-filename* *destination-filename* [ **all** ] | + Before copying a file, ensure that the storage space is sufficient for the file. + If the destination file has the same name as an existing file, the system prompts you whether to overwrite the existing file. |
  | Copy the files in the backup partition to the specified path. | [**copy backup-file**](cmdqueryname=copy+backup-file) **file-name** *scrFile* **path** *desFile*  [**copy backup-file**](cmdqueryname=copy+backup-file) **all path** *desFile* | - |
  | Move a file. | [**move**](cmdqueryname=move) *source-filename* *destination-filename* | If the destination file has the same name as an existing file, the system prompts you whether to overwrite the existing file. |
  | Rename a file. | [**rename**](cmdqueryname=rename) *old-name* *new-name* | - |
  | Compressed file or directory | [**zip**](cmdqueryname=zip) *source-filename* *destination-filename* [ **password** *password* ] | - |
  | Decompress a file. | [**unzip**](cmdqueryname=unzip) *source-filename* *destination-filename* [ **password** *password* ] | - |
  | Delete a file. | [**delete**](cmdqueryname=delete) [ **/unreserved** ] [ **/quiet** ] *filename* [ **all** ] | This command cannot be used to delete a directory.  NOTICE:  If the command contains the **/unreserved** parameter, the deleted file cannot be restored. |
  | Restore a deleted file. | [**undelete**](cmdqueryname=undelete) *filename* | After you run the [**delete**](cmdqueryname=delete) command without the **/unreserved** parameter, the file is moved to the recycle bin. You can run the **undelete** command to restore the file. |
  | Delete a file from the recycle bin. | [**reset recycle-bin**](cmdqueryname=reset+recycle-bin) [ **/f** | *filename* ] | To permanently delete a file from the recycle bin, run this command. |
  | Run a batch file or VRP Shell Languages (VSL) script file. | [**execute**](cmdqueryname=execute) *filename* [ *parameter* &<1-8> ] | To perform multiple file operations at a time, run the **execute** *filename* command in the system view. The created batch file must be saved in the storage medium in advance. NOTICE:  To prevent user information leakage, do not carry sensitive user data (such as ciphertext passwords and ciphertext keys) in specified batch processing files or VSL script files. |