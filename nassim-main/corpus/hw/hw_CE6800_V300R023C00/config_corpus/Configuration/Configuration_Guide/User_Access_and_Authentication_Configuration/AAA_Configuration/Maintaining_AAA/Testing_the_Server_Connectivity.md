Testing the Server Connectivity
===============================

Testing the Server Connectivity

#### Context

When configuring remote server authentication, you can run the [**test-aaa**](cmdqueryname=test-aaa) command to manually test the connectivity between a single user and the authentication or accounting server. This facilitates fault location.


#### Procedure

* Run the [**test-aaa**](cmdqueryname=test-aaa) command in any view to test the connectivity between the device and server.
  
  
  
  **Table 1** Testing the server connectivity
  | Operation | Command |
  | --- | --- |
  | Test the connectivity between the device and the RADIUS authentication or accounting server. | [**test-aaa**](cmdqueryname=test-aaa) *user-name* *user-password* **radius-template** *template-name* [ **chap** | **pap** | **accounting** ] [ **chap** | **pap** | **accounting** [ **start** | **realtime** | **stop** ] ] [ **called-station-id** ] |
  | Test the connectivity between the device and the HWTACACS authentication or accounting server. | [**test-aaa**](cmdqueryname=test-aaa) *user-name* *user-password* **hwtacacs-template** *template-name* [ **accounting** [ **start** | **realtime** | **stop** ] ] |
  | Test the connectivity between the device and the LDAP authentication server. | [**test-aaa**](cmdqueryname=test-aaa) *user-name* *user-password* **ldap-template** *template-name* |

#### Follow-up Procedure

The Info messages of the [**test-aaa**](cmdqueryname=test-aaa) do not distinguish between the server types. [Table 2](#EN-US_TASK_0000001513035670__table1663784615338) describes the Info messages.

**Table 2** Info messages of the [**test-aaa**](cmdqueryname=test-aaa) command
| Info Message | Description | Troubleshooting Method |
| --- | --- | --- |
| Info: Account test succeeded. | The device can communicate with the server. | See·[Info: Account test succeeded.](#EN-US_TASK_0000001513035670__li72026307467) |
| Info: Authentication may fail due to incorrect name or password. | The device can communicate with the server. However, the user name and password used in the test are different from those configured on the server. | Run the **test-aaa** command to check whether the user name and password are correct. If this Info message is displayed, the user name and password are incorrect. Ensure that the user name and password are correct during user authentication. |
| Info: Authentication may fail due to incorrect shared key. | The shared key of the server configured on the device is different from that configured on the server. | Reconfigure the shared key on the device and server. |
| Info: The server template does not exist. | The server template used for the test is not configured on the device. | Configure a server template for the test on the device. |
| Info: One more user doing this operation is not permitted. Please wait for a while to do this operation again. | Multiple users are running the **test-aaa** command at the same time. | Ensure that the **test-aaa** command is run by only one user at a time. |
| Info: Account test failed. | Test failed. | See [Info: Account test failed.](#EN-US_TASK_0000001513035670__li10201193020467) |
| Info: Account test time out. | The test timed out. | See·[Info: Account test time out.](#EN-US_TASK_0000001513035670__li162011130134617) |

* **Info: Account test time out.**The following describes possible causes:
  + There are no reachable routes between the device and the server.
  + The NAS IP address configured in the RADIUS server template is different from that on the RADIUS server.
  + The RADIUS server address in the RADIUS server template is incorrect.
  + The authentication port number configured in the RADIUS server template is incorrect.
  + The authentication port number on the RADIUS server is used by another program.
  + The IP address of the access control device is incorrect or the RADIUS server is not started.
  Procedure
  + Run the [**ping**](cmdqueryname=ping) command to check whether there are reachable routes between the device and the server.
  + Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **template** *template-name* ] command in any view to check whether the port number configured in the RADIUS server template is the same as that on the RADIUS server and whether the NAS IP address is the same as that on the RADIUS server.
  + When the controller functions as the RADIUS server, run the [**netstat -nao**](cmdqueryname=netstat+-nao) | [**findstr 1812**](cmdqueryname=findstr+1812) and [**netstat -nao**](cmdqueryname=netstat+-nao) | [**findstr 1813**](cmdqueryname=findstr+1813) commands on the server to check whether the authentication port number is used by another program. If another program uses this port number, close the program.
  + Check whether the IP address of the access control device is correct.
* **Info: Account test failed.**
  
  The following describes possible causes:
  
  The RADIUS server IP address is not configured.
  
  Procedure
  
  Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **template** *template-name* ] command in any view to check whether the RADIUS server IP address is configured in the RADIUS server template.
* **Info: Account test succeeded.** The device is connected to the server, but the user cannot pass the authentication during login.
  
  The following describes possible causes:
  
  Check whether the domain used for user authentication is the same as the domain configured for RADIUS authentication on the device.
  
  Procedure
  + Run the [**display this**](cmdqueryname=display+this) command in the AAA view to check whether the domain used for user authentication is the same as the domain configured for RADIUS authentication on the device.
    
    - If the user name entered by the user contains a domain name, check whether RADIUS authentication is configured in the domain with the domain name.
    - If the user name entered by the user does not contain a domain name, check whether RADIUS authentication is configured in the global default domain.
  + Run the [**display this**](cmdqueryname=display+this) command in the AAA view to check whether the AAA authentication scheme and RADIUS server template are applied to the domain.