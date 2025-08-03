Example for Configuring a Device to Communicate with ncclient Using NETCONF
===========================================================================

Example for Configuring a Device to Communicate with ncclient Using NETCONF

#### Networking Requirements

When the NMS is used to centrally manage devices on a network that requires high security and scalability, you can use NETCONF to ensure communication between the NMS and the devices.

On the network shown in [Figure 1](#EN-US_TASK_0000001512842470__fig_dc_vrp_netconf_cfg_000901), the NMS is deployed on client001 that functions as the SSH client. The server functions as the SSH server, which receives connection requests and establishes a connection with the SSH client, implementing configuration file management using NETCONF. SSH is a secure application-layer protocol, thereby enhancing the reliability of NETCONF.

**Figure 1** Network diagram of configuration file management using NETCONF![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001615334489.png)

#### Precautions

An SSH user named **client001** is used as an example. If password authentication is used to authenticate the SSH user, the server needs to generate an Elliptic Curves Cryptography (ECC) key.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for the server interface1 connecting to the client so that the Layer 3 route between the client and server is reachable.
2. Configure virtual type terminal (VTY) user interfaces on the server to support SSH so that SSH users can be managed and monitored with better connection security.
3. Deploy SSH on the server to improve NETCONF security.
   
   1. Create an SSH user with administrative rights.
   2. Create an ECC key pair.
   3. Configure an authentication mode for the SSH user.
   4. Configure a service type for the SSH user.
4. Enable NETCONF so that the client can log in to the server.
5. Deploy the NMS on the client to implement NMS-based network management on the client.
6. Log in to the server using the NMS to manage configuration files remotely.

#### Procedure

1. Configure an IP address for 100GE1/0/1.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname netconf-agent
   [*HUAWEI] commit
   [~netconf-agent] interface 100ge 1/0/1
   [*netconf-agent-100GE1/0/1] undo portswitch
   [*netconf-agent-100GE1/0/1] ip address 10.1.1.1 24
   [*netconf-agent-100GE1/0/1] quit
   [*netconf-agent] commit
   ```
2. Configure VTY user interfaces on the server to support SSH.
   
   
   ```
   [~netconf-agent] user-interface vty 0 4
   [*netconf-agent-ui-vty0-4] authentication-mode aaa
   [*netconf-agent-ui-vty0-4] protocol inbound ssh
   [~netconf-agent-ui-vty0-4] quit
   [*netconf-agent] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After SSH is configured, the device automatically disables the Telnet function.
3. Deploy SSH on the server.
   
   
   1. Create an SSH user.
      
      # Create the SSH user **client001**.
      
      ```
      [~netconf-agent] ssh user client001
      [*netconf-agent] aaa
      [*netconf-agent-aaa] local-user client001 password irreversible-cipher YsHsjx_202206
      [*netconf-agent-aaa] local-user client001 service-type ssh
      [*netconf-agent-aaa] local-user client001 privilege level 3
      [~netconf-agent-aaa] quit
      [*netconf-agent] commit
      ```
   2. Create an ECC key pair.
      
      ```
      [~netconf-agent] ecc local-key-pair create
      Info: The key name will be: Host_ECC
      Info: The key modulus can be any one of the following: 256, 384, 521.
      Info: Key pair generation will take a short while.
      Please input the modulus [default=521]: 
      Info: Generating keys...
      Info: Succeeded in creating the ECC host keys.
      [*netconf-agent] commit
      ```
      
      After the ECC key pair is created, run the [**display ecc local-key-pair public**](cmdqueryname=display+ecc+local-key-pair+public) command to check information about the public key in the ECC key pair.
   3. Configure an authentication mode for the SSH user.
      
      ```
      [~netconf-agent] ssh user client001 authentication-type password
      [*netconf-agent] commit
      ```
   4. Configure a service type for the SSH user.
      
      ```
      [~netconf-agent] ssh user client001 service-type all
      [*netconf-agent] commit
      ```
   5. Configure a source interface for the SSH server.
      ```
      [~netconf-agent] ssh server-source all-interface
      [*netconf-agent] commit
      ```
4. Enable NETCONF on the server.
   
   
   ```
   [~netconf-agent] snetconf server enable
   [*netconf-agent] commit
   ```
5. Set the NETCONF timeout interval.
   
   
   ```
   [~netconf-agent] netconf
   [~netconf-agent-netconf] idle-timeout 0 0
   [~netconf-agent-netconf] quit
   [*netconf-agent] commit
   ```
6. Deploy the NMS on the client and log in to the server through the NMS.
   
   
   
   The following uses ncclient as an example to describe how to establish a NETCONF session. Before establishing a NETCONF session, ensure Layer 3 communication between ncclient and the management network interface on the server.
   
   Create an SSH connection from the ncclient to the server whose IP address is 10.1.1.1. The connection uses password authentication, with a username of **client001** and a password of **YsHsjx\_202206**. When the connect function is invoked, the client connects to the device and automatically establishes a NETCONF session. The following two examples can be used as references. Run the following script on the ncclient. If a message like "No module named XXX" is displayed during script running, run the **pip install** *XXX* command to install the required module.
   
   * Example 1: In this example, connection-related parameters are provided during script execution.
     1. Create a file named **huawei-connect-1.py** and copy the following content to it.
        ```
        # -*- coding: utf-8 -*- 
        import sys 
        from ncclient import manager 
        from ncclient import operations 
         
        def huawei_connect(host, port, user, password): 
            return manager.connect(host=host, 
                                   port=port, 
                                   username=user, 
                                   password=password, 
                                   hostkey_verify = False, 
                                   device_params={'name': "huaweiyang"}, 
                                   allow_agent = False, 
                                   look_for_keys = False) 
         
        def test_connect(host, port, user, password): 
            with huawei_connect(host, port=port, user=user, password=password) as m: 
         
                n = m._session.id         
                print("The session id is %s." % (n)) 
         
        if __name__ == '__main__':
            test_connect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        ```
        
        Relevant parameters are as follows:
        
        + **host**: IP address of the device functioning as a NETCONF server or the device that is accessed through SSH.
        + **port**: number of the port used to establish an SSH connection. The default port number is 22 if you run the **snetconf server enable** command to enable NETCONF,
          
          or 830 if you run the **protocol inbound ssh port 830** command to establish a NETCONF connection.
        + **username**: name of the configured SSH user.
        + **password**: password of the SSH user.
     2. Navigate to the path where the Python file resides and execute the file:
        ```
        >python huawei-connect-1.py 10.1.1.1 22 client001 YsHsjx_202206
        ```
   * Example 2: In this example, connection-related parameters are provided in a script file.
     1. Create a file named **huawei-connect-2.py** and copy the following content to it.
        ```
        # -*- coding: utf-8 -*- 
        import sys 
        from ncclient import manager 
        from ncclient import operations 
         
        def huawei_connect(): 
            return manager.connect(host="10.1.1.1", 
                                   port=22, 
                                   username="client001", 
                                   password="YsHsjx_202206", 
                                   hostkey_verify = False, 
                                   device_params={'name': "huaweiyang"}, 
                                   allow_agent = False, 
                                   look_for_keys = False) 
         
        def test_connect(): 
            with huawei_connect() as m: 
         
                n = m._session.id         
                print("The session id is %s." % (n)) 
         
        if __name__ == '__main__':
            test_connect()
        ```
     2. Navigate to the path where the Python file resides and execute the file:
        ```
        >python huawei-connect-2.py
        ```
   
   **----End**

#### Verifying the Configuration

After the preceding configuration is complete, you can log in to the remote device using NETCONF to manage its configuration files remotely.

Run the following commands on the server (SSH server) to check configuration information:

# Run the **display users** command to check information about users who have logged in to the server.

```
[~netconf-agent] display users
```
```
NOTE:
User-Intf: The absolute number and the relative number of user interface
Authen: Whether the authentication passes
Author: Command line authorization flag
--------------------------------------------------------------------------------
  User-Intf   Delay     Type   Network Address   Authen    Author   Username
--------------------------------------------------------------------------------
  100 NCA 0   00:02:50  SSH    10.2.2.2          pass      yes      client001
```

# Run the **display ssh user-information** command to check SSH user information.

```
[~netconf-agent] display ssh user-information
```
```
--------------------------------------------------------------------------------
User Name             : client001
Authentication-Type   : password
User-public-key-name  : -
User-public-key-type  : -
Sftp-directory        : -
Service-type          : snetconf
--------------------------------------------------------------------------------
Total 1, 1 printed
```

# Run the **display ssh server status** command to check global configurations of the SSH server.

```
[~netconf-agent] display ssh server status
```
```
SSH Version                                : 2.0
SSH authentication timeout (Seconds)       : 60
SSH authentication retries (Times)         : 3
SSH server key generating interval (Hours) : 0
SSH version 1.x compatibility              : Enable
SSH server keepalive                       : Disable
SFTP IPv4 server                           : Disable
SFTP IPv6 server                           : Disable
STELNET IPv4 server                        : Disable
STELNET IPv6 server                        : Disable
SNETCONF IPv4 server                       : Enable
SNETCONF IPv6 server                       : Enable
SNETCONF IPv4 server port(830)             : Disable
SNETCONF IPv6 server port(830)             : Disable
SSH port forwarding                        : Disable
SSH IPv4 server port                       : 22
SSH IPv6 server port                       : 22
ACL name                                   :
ACL number                                 :
ACL6 name                                  :
ACL6 number                                :
SSH server ip-block                        : Enable
```

# Run the **display netconf capability** command to check the capabilities that the server supports.

```
[~netconf-agent] display netconf capability
```
```
--------------------------------------------------
Capability                                        
--------------------------------------------------
urn:ietf:params:netconf:base:1.0                  
urn:ietf:params:netconf:base:1.1                  
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:candidate:1.0  
urn:ietf:params:netconf:capability:confirmed-commit:1.0
urn:ietf:params:netconf:capability:confirmed-commit:1.1
urn:ietf:params:netconf:capability:rollback-on-error:1.0
urn:ietf:params:netconf:capability:validate:1.0   
urn:ietf:params:netconf:capability:validate:1.1   
urn:ietf:params:netconf:capability:startup:1.0    
urn:ietf:params:netconf:capability:url:1.0?scheme=file,ftp,sftp
urn:ietf:params:netconf:capability:xpath:1.0      
urn:ietf:params:netconf:capability:notification:1.0
urn:ietf:params:netconf:capability:interleave:1.0 
urn:ietf:params:netconf:capability:with-defaults:1.0?basic-mode=report-all&also-supported=report-all-tagged,trim
urn:ietf:params:netconf:capability:yang-library:1.0?revision=2016-06-21&module-set-id=1903662584
http://www.huawei.com/netconf/capability/sync/1.0 
http://www.huawei.com/netconf/capability/sync/1.1 
http://www.huawei.com/netconf/capability/sync/1.2 
http://www.huawei.com/netconf/capability/sync/1.3 
http://www.huawei.com/netconf/capability/exchange/1.0
http://www.huawei.com/netconf/capability/exchange/1.2
http://www.huawei.com/netconf/capability/active/1.0
http://www.huawei.com/netconf/capability/action/1.0
http://www.huawei.com/netconf/capability/discard-commit/1.0
http://www.huawei.com/netconf/capability/execute-cli/1.0
http://www.huawei.com/netconf/capability/update/1.0
http://www.huawei.com/netconf/capability/commit-description/1.0
http://www.huawei.com/netconf/capability/sync-config/1.0
http://www.huawei.com/netconf/capability/sync-config/1.1
http://www.huawei.com/netconf/capability/schema/1.0
--------------------------------------------------
```

#### Configuration Scripts

Server

```
#
sysname netconf-agent
#
aaa
 local-user client001 password irreversible-cipher $1d$v!=.5/:(q-$xL=\K+if"'S}>k7vGP5$_ox0B@ys7.'DBHL~3*aN$
 local-user client001 service-type ssh
 local-user client001 privilege level 3
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.1.1.1 255.255.255.0
#
snetconf server enable
ssh server-source all-interface
ssh user client001
ssh user client001 authentication-type password
ssh user client001 service-type all
#
user-interface vty 0 4
 authentication-mode aaa
 user privilege level 3
 protocol inbound ssh
#
netconf
 idle-timeout 0 0
#
return
```