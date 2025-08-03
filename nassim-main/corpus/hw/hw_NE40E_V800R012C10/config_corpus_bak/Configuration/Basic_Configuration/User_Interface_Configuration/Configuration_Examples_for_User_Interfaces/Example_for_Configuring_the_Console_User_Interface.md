Example for Configuring the Console User Interface
==================================================

This section provides an example for configuring the user level, authentication mode, authentication password, physical attributes and terminal attributes for the console user interface so that you can log in to the device through the console port in password authentication mode.

#### Networking Requirements

To initialize the configurations of a new device or locally maintain the device, log in to the device through the console user interface. You can configure attributes for the console user interface based on use and security requirements.


#### Precautions


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure physical attributes for the console user interface.
2. Configure terminal attributes for the console user interface.
3. Set a user level.
4. Configure an authentication mode and password.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The user name and password do not have default values. Other parameters have default values, which are recommended.



#### Data Preparation

To complete the configuration, you need the following data:

* Transmission rate of a connection: 4800 bit/s
* Flow control mode: none
* Parity: even
* Stopbits: 2
* Databits: 6
* Timeout period of an idle connection: 30 minutes
* Number of rows displayed on a terminal screen: 30
* Buffer size for historical commands: 20
* User level: 15
* User authentication mode: AAA

#### Procedure

1. Configure physical attributes for the console user interface.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] user-interface console 0
   ```
   ```
   [~HUAWEI-ui-console0] speed 4800
   ```
   ```
   [*HUAWEI-ui-console0] flow-control none
   ```
   ```
   [*HUAWEI-ui-console0] parity even
   ```
   ```
   [*HUAWEI-ui-console0] stopbits 2
   ```
   ```
   [*HUAWEI-ui-console0] databits 6
   ```
   ```
   [*HUAWEI-ui-console0] commit
   ```
2. Configure terminal attributes for the console user interface.
   
   
   ```
   [~HUAWEI-ui-console0] shell
   ```
   ```
   [*HUAWEI-ui-console0] idle-timeout 30
   ```
   ```
   [*HUAWEI-ui-console0] screen-length 30
   ```
   ```
   [*HUAWEI-ui-console0] history-command max-size 20
   ```
   ```
   [*HUAWEI-ui-console0] commit
   ```
3. Set a user level for the console user interface.
   
   
   ```
   [~HUAWEI-ui-console0] user privilege level 3
   ```
   ```
   [*HUAWEI-ui-console0] commit
   ```
4. Set the user authentication mode to AAA for the console user interface.
   
   
   ```
   [~HUAWEI-ui-console0] authentication-mode aaa
   ```
   ```
   [~HUAWEI-ui-console0] quit
   ```
   ```
   [*HUAWEI]aaa
   ```
   ```
   [*HUAWEI-aaa] local-user admin1234 password irreversible-cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-aaa] local-user admin1234 level 3
   ```
   ```
   [*HUAWEI-aaa] local-user admin1234 service-type terminal
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   
   After the console user interface is configured, you can log in to the device through the console port in AAA mode. For details about how to log in to the device, see [Configuring Login Through a Console Port](dc_vrp_basic_cfg_0026.html).
5. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display user-interface**](cmdqueryname=display+user-interface) command to check the status of Console 0.
   
   ```
   <HUAWEI> display user-interface 0
   ```
   ```
     Idx  Type    Tx/Rx Modem Privi ActualPrivi Auth Int
     +0   CON  0  4800  -     3     3           A    16
     + : Current UI is active.
     F : Current UI is active and work in async mode.
     Idx : Absolute index of UIs.
     Type : Type and relative index of UIs.
     Privi : The privilege of UIs.
     ActualPrivi : The actual privilege of user-interface.
     Auth : The authentication mode of UIs.
        A : Authenticate use AAA.
        P : Authenticate use current UI's password.
     Int  : The physical location of UIs.
   ```

#### Configuration Files

```
#
 sysname HUAWEI
#
aaa  
 local-user admin1234 password irreversible-cipher $1d$g8wLJ`LjL!$CyE(V{3qg5DdU:PM[6=6O$UF-.fQ,Q}>^)OBzgoU$    
 local-user admin1234 service-type terminal  
 local-user admin1234 level 3
#
user-interface con 0
 authentication-mode aaa
 history-command max-size 20
 idle-timeout 30 0
 databits 6
 parity even
 stopbits 2
 speed 4800
 screen-length 30
#
return
```