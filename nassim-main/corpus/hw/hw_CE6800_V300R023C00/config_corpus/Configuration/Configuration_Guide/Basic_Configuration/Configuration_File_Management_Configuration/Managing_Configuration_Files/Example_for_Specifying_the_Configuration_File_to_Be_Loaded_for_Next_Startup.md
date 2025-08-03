Example for Specifying the Configuration File to Be Loaded for Next Startup
===========================================================================

Example for Specifying the Configuration File to Be Loaded for Next Startup

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001563770617__fig74331217517), the current system software cannot meet user needs. The device must load new software version with more features. Then the device software needs to be upgraded remotely.

**Figure 1** Network diagram of specifying the configuration file to be loaded for next startup  
![](figure/en-us_image_0000001927089573.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Upload the new system software to the root directory of the device.
2. Save the current configuration so that it remains effective after upgrade.
3. Specify the system software to be loaded for next startup.
4. Specify the configuration file to be loaded for next startup.
5. Restart the device to complete upgrade.

#### Procedure

1. Upload the new system software to the root directory of the device.
   
   
   1. Before configuration, run the [**display startup**](cmdqueryname=display+startup) command to view the files for next startup. (The actual command output varies depending on the device. The following command output is only an example.)
      ```
      <HUAWEI> display startup
      MainBoard:   
        Configured startup system software:        flash:/basicsoft.cc   
        Startup system software:                   flash:/basicsoft.cc   
        Next startup system software:              flash:/basicsoft.cc   
        Startup saved-configuration file:          flash:/vrpcfg.zip   
        Next startup saved-configuration file:     flash:/vrpcfg.zip   
        Startup paf file:                          default   
        Next startup paf file:                     default   
        Startup patch package:                     NULL   
        Next startup patch package:                NULL
        Startup feature software:                  NULL
        Next startup feature software:             NULL
        Startup extended-system software:          NULL
        Next startup extended-system software:     NULL
      ```
   2. Configure the device as an SFTP server.
      
      Upload the new system software to the device. This example uses SFTP to transfer the system software. Configure the device as an SFTP server and upload the system software to the device from the SFTP client. Ensure that there is enough space in the storage medium before uploading files. If the space is insufficient, delete unnecessary files from the storage medium.
      
      # Configure an IP address for the SFTP server.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname SSH Server
      [*HUAWEI] commit
      [*SSH Server] interface 100ge 1/0/1
      [~SSH Server-100GE1/0/1] undo portswitch
      [*SSH Server-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
      [*SSH Server-100GE1/0/1] quit
      [*SSH Server] commit
      ```
      
      # Configure the public key algorithm, encryption algorithm, key exchange algorithm list, HMAC authentication algorithm, and minimum key length on the SSH server.
      
      ```
      [~SSH Server] ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
      [*SSH Server] ssh server hmac sha2_256 sha2_512
      [*SSH Server] ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
      [*SSH Server] ssh server publickey rsa_sha2_256 rsa_sha2_512
      [*SSH Server] ssh server dh-exchange min-len 3072
      [*SSH Server] commit
      ```
      
      # On the server, generate a local key pair and enable the SFTP server function.
      
      ```
      [~SSH Server] sftp server enable
      [*SSH Server] ssh server-source all-interface
      [*SSH Server] commit
      ```
      
      # Configure SSH user information including the authentication mode, service type, authorized directory, user name, and password.
      
      ```
      [~SSH Server] ssh user client authentication-type password
      Info: Succeeded in adding a new SSH user. 
      [*SSH Server] ssh user client service-type sftp
      [*SSH Server] ssh user client sftp-directory flash: 
      [*SSH Server] aaa
      [*SSH Server-aaa] local-user client password
      Please configure the login password (8-128)
      It is recommended that the password consist of of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
      Please enter password:                                      
      Please confirm password:                               
      Info: Add a new user.
      [*SSH Server-aaa] local-user client privilege level 3
      [*SSH Server-aaa] local-user client service-type ssh
      [*SSH Server-aaa] quit
      [*SSH Server] commit
      ```
      
      # Configure access permissions on the SSH server.
      
      ```
      [~SSH Server] acl 2000
      [*SSH Server-acl4-basic-2000] rule permit source 10.1.1.0 24
      [*SSH Server-acl4-basic-2000] quit
      [*SSH Server] ssh server acl 2000
      [*SSH Server] commit
      [~SSH Server] quit
      ```
   3. Run the **sftp 10.1.1.1** command in the CLI window of the PC to set up an SFTP connection with the device. Run the **put** command to upload new system software **newbasicsoft.cc**.After the system software is successfully uploaded, run the **dir** command on the SSH server to view the uploaded system software.
      ```
      <SSH Server> dir
      Directory of  flash:/
      
        Idx  Attr     Size(Byte)  Date        Time       FileName
          0  drw-              -  Apr 16 2012 13:19:58   logfile
          1  -rw-     85,925,409  Apr 16 2012 13:18:02   basicsoft.cc
          2  -rw-              4  Oct 27 2011 17:25:22   snmpnotilog.txt
          3  -rw-          6,033  Jul 16 2012 16:40:02   private-data.txt
          4  -rw-          3,275  Jul 14 2012 14:18:08   vrpcfg.zip
          5  drw-              -  Nov 14 2011 19:14:26   sysdrv 
          6  drw-     88,239,759  Jul 16 2012 19:14:26   newbasicsoft.cc
      ...
      
      670,092 KB total (569,904 KB free)
      ```
2. Save the current configuration.
   
   
   ```
   <SSH Server> save
   ```
   
   The system displays a message indicating that the current configuration will be saved and asks you whether to continue. Enter **y** and the configuration will be saved to the device.
3. Specify the system software to be loaded for next startup.
   
   
   ```
   <SSH Server> startup system-software newbasicsoft.cc
   ```
4. Specify the configuration file to be loaded for next startup.
   
   
   ```
   <SSH Server> startup saved-configuration vrpcfg.zip
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   In step 1, you can run the [**display startup**](cmdqueryname=display+startup) command to check the configuration file for next startup. The message "Next startup saved-configuration file: flash:/**vrpcfg.zip**" will be displayed. This means that the **vrpcfg.zip** configuration file has been specified for next startup, so skip this step. To specify another file for next startup, perform this step.
5. Verify the configuration.
   
   
   
   Run the following command to view the system software and configuration file for next startup. (The actual command output varies depending on the device. The following command output is only an example.)
   
   ```
   <HUAWEI> display startup
   MainBoard:   
     Configured startup system software:        flash:/basicsoft.cc   
     Startup system software:                   flash:/basicsoft.cc   
     Next startup system software:              flash:/newbasicsoft.cc   
     Startup saved-configuration file:          flash:/vrpcfg.zip   
     Next startup saved-configuration file:     flash:/vrpcfg.zip   
     Startup paf file:                          default   
     Next startup paf file:                     default   
     Startup patch package:                     NULL   
     Next startup patch package:                NULL
     Startup feature software:                  NULL
     Next startup feature software:             NULL
     Startup extended-system software:          NULL
     Next startup extended-system software:     NULL
   ```
6. Restart the device.
   
   
   
   # Because the configuration file has been saved, run the following command to restart the device quickly.
   
   ```
   <SSH Server> reboot fast
   ```
   
   When the system asks you whether to continue with a system restart, enter **y**.

#### Verifying the Configuration

# Wait for several minutes until the device restart is complete. Run the **display version** command to check the current system version. If the current system software is new, the upgrade has succeeded.


#### Configuration Scripts

```
#
sysname SSH Server
#
acl number 2000
 rule 5 permit source 10.1.1.0 0.0.0.255
#
aaa
 local-user client password irreversible-cipher $1d$+,JS+))\\2$KVNj(.3`_5x0FCKGv}H&.kUTI`Ff&H*eBqO.ua>)$
 local-user client service-type ssh
 local-user client privilege level 3
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.1 255.255.255.0
#
sftp server enable
ssh server-source all-interface
ssh server acl 2000
ssh user client
ssh user client authentication-type password
ssh user client service-type sftp
ssh user client sftp-directory flash:
#
ssh server cipher aes128_ctr aes256_ctr aes192_ctr aes128_gcm aes256_gcm
ssh server hmac sha2_256 sha2_512
ssh server key-exchange dh_group_exchange_sha256 dh_group16_sha512
ssh server publickey rsa_sha2_256 rsa_sha2_512
ssh server dh-exchange min-len 3072
#
return
```