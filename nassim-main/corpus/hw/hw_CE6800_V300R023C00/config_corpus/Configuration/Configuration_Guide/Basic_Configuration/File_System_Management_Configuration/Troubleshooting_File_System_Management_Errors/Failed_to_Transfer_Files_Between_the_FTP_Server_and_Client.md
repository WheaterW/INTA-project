Failed to Transfer Files Between the FTP Server and Client
==========================================================

Failed to Transfer Files Between the FTP Server and Client

#### Possible Causes

* The FTP source or destination directory name contains characters not supported by the device, such as spaces.
* The root directory on the FTP server does not have sufficient storage space.

#### Procedure

1. Check whether the FTP source or destination directory name contains characters not supported by the device.
   
   
   
   The directory name cannot contain spaces or the following special characters: ~ \* / \ : ' "
   
   If the directory name contains any of these characters, change the directory name.
2. Check whether there is sufficient storage space in the root directory on the FTP server.
   
   
   
   Run the [**dir**](cmdqueryname=dir) command on the FTP server to check the available space of the root directory on the FTP server.
   
   If the storage space is insufficient, run the [**delete /unreserved**](cmdqueryname=delete+%2Funreserved) command in the user view to delete unnecessary files.