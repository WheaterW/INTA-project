Example for Configuring Data Center Network Management (RADIUS Authentication)
==============================================================================

Example for Configuring Data Center Network Management (RADIUS Authentication)

#### Networking Requirements

An enterprise operates a complex data center network and wants to monitor the network in real time and restrict login rights of the administrator in order to ensure network security and stability. A network management system can meet these requirements.

As shown in [Figure 1](#EN-US_TASK_0000001512671274__fig_dc_dc_cfgcase_netmgt_0003), IP addresses have been configured for the network devices and there is a reachable route between the RADIUS server and NMS. Users are allowed to log in to the devices only after passing the RADIUS authentication. The NMS monitors the entire network, and receives the traps and logs from each device.

**Figure 1** Example for configuring data center network management (RADIUS authentication)  
![](figure/en-us_image_0000001512830950.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the RADIUS protocol to implement RADIUS authentication. After the configuration is complete, you can use the username and password configured on the RADIUS server to log in to a device through STelnet, ensuring login security.
2. Configure STelnet. The STelnet protocol provides secure remote login on insecure networks to ensure secure data transmission as well as data integrity and reliability.
3. Configure SNMP. The authentication and encryption methods of SNMPv3 are used to ensure the security of the connection between the device and NMS. The NMS can centrally manage all network devices.
4. Configure the device to send logs and traps to the NMS through SNMP.

![](public_sys-resources/note_3.0-en-us.png) 

The following procedure uses DeviceA as an example. The configurations of other devices are similar to the configuration of DeviceA.

Ensure that the RADIUS server IP address, port number, and shared key in the RADIUS server template are configured correctly and are the same as those on the RADIUS server.

Ensure that users have been configured on the RADIUS server. In this example, a user with the username admin@admin123 and password YsHsjx\_202206 has been configured on the RADIUS server.

To simplify configuration if multiple users are configured on the RADIUS server, you are advised to run the [**ssh authentication-type default password**](cmdqueryname=ssh+authentication-type+default+password) command to use the preset password authentication mode for local users.



#### Procedure

1. Configure RADIUS.
   1. Configure a RADIUS server template.
      
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceA
      [*HUAWEI] commit
      [~DeviceA] radius-server template shiva
      [*DeviceA-radius-shiva] radius-server authentication 10.7.66.66 1812          //Configure an IP address and a port number for the RADIUS server.
      [*DeviceA-radius-shiva] radius-server shared-key cipher YsHsjx_202206                  //Configure a shared key for the RADIUS server.
      [*DeviceA-radius-shiva] radius-server retransmit 2                              //Set the number of retransmissions to 2.
      [*DeviceA-radius-shiva] quit
      ```
   2. Create AAA authentication scheme **auth** and set the authentication method to RADIUS.
      
      
      ```
      [*DeviceA] aaa
      [*DeviceA-aaa] authentication-scheme auth
      [*DeviceA-aaa-authen-auth] authentication-mode radius
      [*DeviceA-aaa-authen-auth] quit
      ```
   3. Create the domain **admin123** and bind the AAA authentication scheme **auth** and RADIUS server template **shiva** to the domain.
      
      
      ```
      [*DeviceA-aaa] domain admin123
      [*DeviceA-aaa-domain-admin123] authentication-scheme auth
      [*DeviceA-aaa-domain-admin123] radius-server shiva
      [*DeviceA-aaa-domain-admin123] quit
      [*DeviceA-aaa] quit
      [*DeviceA] commit
      ```
2. Configure STelnet.
   1. Configure the device to support STelnet.
      
      
      ```
      [~DeviceA] rsa local-key-pair create
      The key name will be: DeviceA_Host                                
      The range of public key size is (2048, 4096).  
      NOTE: Key pair generation will take a short while.  
      Please input the modulus [default = 3072]:3072 //After the command is run, you are prompted to enter the length of the generated RSA key pair. Currently, the modulus length can be 2048 bits, 3072 bits, or 4096 bits. If you press Enter without entering the key pair length, a 3072-bit RSA key pair is generated. If you do not perform any operation, the device does not generate an RSA key pair. You are advised to use an RSA key pair of 3072 bits or more, which is more secure.
      [*DeviceA] stelnet server enable
      ```
   2. Configure a user interface for SSH login.
      
      
      ```
      [*DeviceA] user-interface vty 0 4
      [*DeviceA-ui-vty0-4] authentication-mode aaa
      [*DeviceA-ui-vty0-4] protocol inbound ssh
      [*DeviceA-ui-vty0-4] user privilege level 3
      [*DeviceA-ui-vty0-4] quit
      ```
   3. Configure the SSH user admin@admin123.
      
      
      ```
      [*DeviceA] ssh user admin@admin123 authentication-type password
      [*DeviceA] ssh user admin@admin123 service-type stelnet
      [*DeviceA] commit
      ```
3. Configure SNMP.
   1. Connect the SNMP agent to the NMS.
      
      
      ```
      [~DeviceA] snmp-agent sys-info version v3
      [*DeviceA] snmp-agent mib-view included iso-view iso
      [*DeviceA] snmp-agent group v3 admingroup privacy write-view iso-view notify-view iso-view
      [*DeviceA] snmp-agent usm-user v3 adminuser admingroup authentication-mode sha2-256 YsHsjx_202206 privacy-mode aes128 Helloworld@6789   //Authentication methods include MD5 and SHA. SHA has higher security and MD5 has higher speed. In this example, sha2-256 is used. Encryption methods include 3DES168, AES128, AES192, AES256, and DES56. AES has higher security. In this example, AES128 is used.
      ```
   2. Configure a trap host.
      
      
      ```
      [*DeviceA] snmp-agent target-host host-name nms trap address udp-domain 10.7.60.66 params securityname adminuser v3 privacy  //The security level of the trap host must be higher than or equal to the user's security level. In this example, the security level is set to privacy (authentication and encryption).
      [*DeviceA] commit
      ```
4. Configure the device to send logs and traps to the NMS through SNMP.
   
   
   ```
   [~DeviceA] info-center source default channel 5 log state on
   [*DeviceA] commit
   ```

#### Verifying the Configuration

The configuration is successful if the following conditions are met:

* You can successfully log in to the device through STelnet by using the username and password configured on the RADIUS server.
* The NMS successfully manages the device. You can use the NMS to operate the device through SNMP, and the NMS can receive logs and traps from the device.


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA 
# 
info-center source default channel 5 log state on
#
radius-server template shiva
 radius-server shared-key cipher %^%#L@71VU/>5>n/c$GKI>J!i:Uz~:!<.W'jc0X@nE4$%^%#  //The ciphertext format provided here is for example only. The format may vary depending on the system software version.
 radius-server authentication 10.7.66.66 1812
 radius-server retransmit 2  
#
aaa
 authentication-scheme auth
  authentication-mode radius
 domain admin123
  authentication-scheme auth
  radius-server shiva
#
snmp-agent
snmp-agent local-engineid 800007DB03306B20792201
#
snmp-agent sys-info version v3
snmp-agent group v3 admingroup privacy write-view iso-view notify-view iso-view
snmp-agent target-host host-name nms trap address udp-domain 10.7.60.66 params securityname adminuser v3 privacy
#
snmp-agent mib-view included iso-view iso
snmp-agent usm-user v3 adminuser
snmp-agent usm-user v3 adminuser group admingroup
snmp-agent usm-user v3 adminuser authentication-mode sha2-256 cipher %^%#BQV1%E-zm5`pG^HCe.4-yi-EUx$iv=S(jiKO7tJN%^%#  //The ciphertext format provided here is for example only. The format may vary depending on the system software version.
snmp-agent usm-user v3 adminuser privacy-mode aes128 cipher %^%#4_o.,z8`_OmbfU4svg>8"[TxSo\9'R]d/[TXR3!&%^%#  //The ciphertext format provided here is for example only. The format may vary depending on the system software version.
#
stelnet server enable
ssh user admin@admin123
ssh user admin@admin123 authentication-type password
ssh user admin@admin123 service-type stelnet
ssh authorization-type default aaa 
#
user-interface vty 0 4
 authentication-mode aaa
 user privilege level 3
 protocol inbound ssh
#
return
```