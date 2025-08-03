(Optional) Configuring the Function to Generate and Send User Login, User Logout, and User Login Result Logs
============================================================================================================

User login, user logout, and user login result logs can be used to query user information, such as the user IP address and the time when a user went online or offline.

#### Context

After the function to generate user login, user logout, and user login result logs is enabled on the Router, the Router records the related information when users successfully go online or offline. Such information includes the username, user login/logout operation, user login/logout time, user access interface, user IP address, and user MAC address.

In addition, the Router supports the sending of user login, user logout, and user login result logs to a log server so that network maintenance personnel can query these logs on the log server.![](../../../../public_sys-resources/note_3.0-en-us.png) 

It is recommended that IPsec be deployed to protect transmission channels and ensure security.




#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip userlog**](cmdqueryname=ip+userlog) { **access** | **call-status** } **export host** *ip-address* *port* **transport** **tcp** command to configure the IP address and port number of the log server that receives user login, user logout, and user login result logs.
3. Run the [**ip userlog export host**](cmdqueryname=ip+userlog+export+host) *ip-address port* **bind ssl-policy** *ssl-policy-name* command to configure an SSL policy for the log server that receives user login, user logout, and user login result log packets.
   
   
   
   The IP address and port number of the log server configured in this command must be the same as those configured in [Step 2](#EN-US_TASK_0172373731__cmd1675786779214107). The **transport tcp** parameter must be set to TCP in [Step 2](#EN-US_TASK_0172373731__cmd1675786779214107).
4. Run the [**ip userlog access export version**](cmdqueryname=ip+userlog+access+export+version) **version** command to configure the version number of the user login and logout logs to be sent.
5. Run the [**ip userlog access send format syslog**](cmdqueryname=ip+userlog+access+send+format+syslog) command to configure the format of the user login and logout logs to be sent.
6. Run the [**ip userlog access**](cmdqueryname=ip+userlog+access) command to enable the function to generate and send user login and logout logs.
7. Run the [**ip userlog call-status**](cmdqueryname=ip+userlog+call-status) command to enable the function to generate and send user login result logs.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Result

* After the function to generate and send user login, user logout, and user login result logs is configured, run the [**display ip userlog access**](cmdqueryname=display+ip+userlog+access) **config** command to check the configurations.
* If a user has successfully gone online or offline, run the [**display ip userlog access**](cmdqueryname=display+ip+userlog+access) **statistic** command to check statistics.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  To re-collect information about user login, user logout, and user login result results, run the [**reset ip userlog statistics access**](cmdqueryname=reset+ip+userlog+statistics+access) command to clear the existing records on the device.
  
  Statistics about user login, logout, and online
  result logs cannot be restored after they are cleared. Therefore,
  exercise caution when running this command.
* After the function to generate and send user login, user logout, and user login result logs is configured, run the [**display ip userlog buffer access**](cmdqueryname=display+ip+userlog+buffer+access) command to check the control block information and user information in the buffer of user login, user logout, and user login result logs.