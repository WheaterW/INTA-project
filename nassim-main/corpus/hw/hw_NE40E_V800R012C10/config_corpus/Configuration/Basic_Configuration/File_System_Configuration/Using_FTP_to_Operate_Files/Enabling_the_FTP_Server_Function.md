Enabling the FTP Server Function
================================

Before using FTP to operate files, enable the FTP server function on a device.

#### Context

Perform the following steps on the device to be used as an FTP server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ftp**](cmdqueryname=ftp) [ **ipv6** ] **server** **enable**
   
   
   
   The FTP server function is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After files are successfully transferred between the client and server, run the [**undo ftp**](cmdqueryname=undo+ftp) [ **ipv6** ] [**server**](cmdqueryname=server) command to disable the FTP server function for security purposes.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.