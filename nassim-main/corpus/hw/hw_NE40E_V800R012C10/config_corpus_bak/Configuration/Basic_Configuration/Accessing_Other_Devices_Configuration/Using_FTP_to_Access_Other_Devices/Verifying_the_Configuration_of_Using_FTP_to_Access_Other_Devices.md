Verifying the Configuration of Using FTP to Access Other Devices
================================================================

After completing the configuration of accessing other devices by using FTP, you can view the parameters configured on the FTP client.

#### Prerequisites

The configurations of accessing other devices by using FTP are complete.


#### Procedure

* Run the [**display ftp-client**](cmdqueryname=display+ftp-client) command to check the source address of the FTP client.
* Run the [**display ftp server ip auth-fail information**](cmdqueryname=display+ftp+server+ip+auth-fail+information) command to check information about the IP addresses of all the clients that fail to pass authentication.
* Run the [**display ftp server ip-block list**](cmdqueryname=display+ftp+server+ip-block+list) command to check information about the locked IP addresses of all the clients that fail to pass authentication.