A User Cannot Log In to the Device Through Telnet When AAA Local Authentication Is Used
=======================================================================================

A User Cannot Log In to the Device Through Telnet When AAA Local Authentication Is Used

#### Fault Symptom

When AAA local authentication is used, a user cannot log in to the device through Telnet.


#### Possible Causes

* The user does not have an account on the device.
* The user name or password entered by the user is incorrect.
* The service type of the user is not set to Telnet.
* No authentication mode is configured for the user interface.

#### Troubleshooting Procedure

1. Run the [**display this**](cmdqueryname=display+this) command in the AAA view to check whether the user exists on the device and whether the service type of the user is Telnet.
   
   ```
   <HUAWEI> system-view
   [HUAWEI] aaa
   [HUAWEI-aaa] display this
   #
   aaa                                                                             
    local-user user1-huawei password irreversible-cipher $1a$+:!j;\;$Z!$&%}p%ctzj"W`GM;APoC=XPLB=L-vJG3-'3Dhyci;$  //The user name is user1-huawei. The password entered during user authentication is in plain text and displayed in cipher text on the device.
    local-user user1-huawei service-type none //none: The service type of the user is not specified.
   # 
   ```
   * If the user does not have an account on the device, run the [**local-user**](cmdqueryname=local-user) *user-name* **password** **irreversible-cipher** *password* command in the AAA view to create a local user.
   * If the user has an account on the device, ensure that the user name and password entered by the user are the same as those configured on the device.
     
     The password is displayed in cipher text on the device. If you forget the password, run the [**local-user**](cmdqueryname=local-user) *user-name* **password** **irreversible-cipher** *password* command in the AAA view to reconfigure the password.
   * If the user exists on the device, ensure that the service type of the user is Telnet or includes Telnet.
     
     Run the [**local-user**](cmdqueryname=local-user) *user-name* **service-type telnet** command in the AAA view to set the service type of the user to Telnet.
2. Run the [**display this**](cmdqueryname=display+this) command in the user interface view to check whether the authentication mode is set to **aaa**.
   
   If not, run the [**authentication-mode**](cmdqueryname=authentication-mode) **aaa** command in the user interface view, for example, in the VTY user interface view.
   
   ```
   <HUAWEI> system-view
   [HUAWEI] user-interface maximum-vty 15
   [HUAWEI] user-interface vty 0 14
   [HUAWEI-ui-vty0-14] display this
   # 
   user-interface maximum-vty 15
   user-interface vty 0 14
    authentication-mode aaa
    protocol inbound telnet
   #
   ```