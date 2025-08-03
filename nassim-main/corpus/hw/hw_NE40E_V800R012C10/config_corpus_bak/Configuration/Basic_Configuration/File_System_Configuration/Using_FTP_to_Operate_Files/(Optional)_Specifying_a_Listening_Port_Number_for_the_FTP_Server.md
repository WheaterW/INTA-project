(Optional) Specifying a Listening Port Number for the FTP Server
================================================================

After a listening port number is specified for the FTP server, only users who know the new port number can access the server, ensuring security.

#### Context

Users can directly log in to a device functioning as an FTP server by using the default listening port number. Attackers may access the default listening port, consuming bandwidth, deteriorating server performance, and causing authorized users unable to access the server. After a listening port number is specified for the FTP server, attackers do not know the new listening port number. This effectively prevents attackers from accessing the listening port.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Ensure that the FTP server function is disabled before specifying a listening port number.

Perform the following steps on the device that functions as an FTP server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ftp**](cmdqueryname=ftp) [ **ipv6** ] **server port** *port-number*
   
   
   
   A listening port number is specified for the FTP server.
   
   If a new listening port number is set, the FTP server terminates all established FTP connections and uses the new port number to listen to new FTP connection attempts.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.