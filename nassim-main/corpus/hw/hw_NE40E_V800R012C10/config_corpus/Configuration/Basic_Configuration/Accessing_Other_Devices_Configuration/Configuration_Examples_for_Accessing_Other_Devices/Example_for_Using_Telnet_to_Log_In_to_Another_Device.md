Example for Using Telnet to Log In to Another Device
====================================================

This section provides an example for using Telnet to log in to another device. In this example, the user authentication mode and password are configured to implement Telnet login.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

As Telnet poses security risks, using STelnet V2 is recommended.

Large numbers of devices need to be managed and maintained on a network. It is impossible to connect each device to a terminal. If no reachable route exists between a remote device and a terminal, you can use Telnet to log in to the remote device for management and maintenance.

On the network shown in [Figure 1](#EN-US_TASK_0172360126__fig_dc_vrp_basic_cfg_010901), you can directly use Telnet to log in to P1 instead of P2. P1 and P2 are routable to each other. To remotely manage and configure P2, use Telnet on P1 to log in to P2.

**Figure 1** Using Telnet to log in to another device![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 stands for GE 0/1/1.


  
![](images/fig_dc_vrp_basic_cfg_010901.png)  


#### Precautions

* P1 and P2 must be routable to each other.
* To log in to P2 from P1 through Telnet, ensure that you can successfully log in to P1.
* In insecure network environments, you are advised to use a secure protocol. [Example for Using STelnet to Log In to Another Device (ECC Authentication Mode)](dc_vrp_basic_cfg_0120.html) provides examples for secure protocols.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the Telnet authentication mode and password on P2.
2. Use Telnet on P1 to log in to P2.

#### Data Preparation

To complete the configuration, you need the following data:

* Host address of P2: 2.1.1.1
* User authentication mode AAA, username **huawei**, and password **YsHsjx\_202206**

#### Procedure

1. Configure the Telnet authentication mode and password on P2.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P2] user-interface vty 0 4
   ```
   ```
   [~P2-ui-vty0-4] authentication-mode aaa
   ```
   ```
   [*P2-ui-vty0-4] commit
   ```
   ```
   [~P2-ui-vty0-4] quit
   ```
   ```
   [~P2] aaa
   ```
   ```
   [*P2-aaa] local-user huawei password
   ```
   ```
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The password must meet the following requirements:
   
   * The password is entered in man-machine interaction mode. The system does not display the entered password.
   * A password is a string of 8 to 16 case-sensitive characters and must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
   * Special characters exclude question marks (?) and spaces. However, spaces are allowed in the password if the password is enclosed in quotation marks.
     + Double quotation marks cannot contain double quotation marks if spaces are used in a password.
     + Double quotation marks can contain double quotation marks if no space is used in a password.
     
     For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
   
   The configured password is displayed in ciphertext in the configuration file.
   
   ```
   [*P2-aaa] local-user huawei service-type telnet
   ```
   ```
   [*P2-aaa] local-user huawei level 3
   ```
   ```
   [*P2-aaa] commit
   ```
   ```
   [~P2-aaa] quit
   ```
   
   If an ACL is configured to access other devices by using Telnet, perform the following configurations on P2:
   
   ```
   [~P2] acl 2000
   ```
   ```
   [*P2-acl4-basic-2000] rule permit source 1.1.1.1 0
   ```
   ```
   [*P2-acl4-basic-2000] quit
   ```
   ```
   [*P2] user-interface vty 0 4
   ```
   ```
   [*P2-ui-vty0-4] acl 2000 inbound
   ```
   ```
   [*P2-ui-vty0-4] commit
   ```
   ```
   [~P2-ui-vty0-4] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The ACL configurations are optional.
2. Verify the configuration.
   
   
   
   After the configurations are complete, use Telnet on P1 to log in to P2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P1] quit
   ```
   ```
   <P1> telnet 2.1.1.1
   ```
   ```
   Trying 2.1.1.1
   Press CTRL+K to abort
   Connected to 2.1.1.1 ...
   Warning: Telnet is not a secure protocol, and it is recommended to use Stelnet.
   Username: huawei
   Password:
   ```
   ```
   <P2>
   ```

#### Configuration Files

* P1 configuration file
  
  ```
  #
  sysname P1
  #
  interface gigabitethernet0/1/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
  #
  admin
  return
  ```
* P2 configuration file
  
  ```
  #
  sysname P2
  #
  acl number 2000
   rule 5 permit source 1.1.1.1 0
  #
  aaa
   local-user huawei password irreversible-cipher $1c$]zV2B\j!z:$hRujV[%/IE|0MwBQ}5sAX(RdE[oj#5otqG6=@>KK$
   local-user huawei service-type telnet
   local-user huawei level 3
  #
  interface gigabitethernet0/1/1
   undo shutdown
   ip address 2.1.1.1 255.255.255.0
  #
  user-interface vty 0 4
   authentication-mode aaa
   acl 2000 inbound
  #
  return
  ```