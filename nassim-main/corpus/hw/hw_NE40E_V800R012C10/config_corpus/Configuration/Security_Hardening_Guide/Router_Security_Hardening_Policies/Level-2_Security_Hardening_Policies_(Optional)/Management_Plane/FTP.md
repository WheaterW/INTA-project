FTP
===

FTP

#### Security Policy

* Authentication
  
  The File Transfer Protocol (FTP) server supports AAA authentication. Only users who pass authentication can access devices and the command line window.
* Service disabling
  
  When the FTP server is enabled, the socket listening is enabled for devices. In this case, the devices are easily scanned by attackers. When the FTP server is not used, the FTP server and the relative port number can be disabled.
  
  The FTP server is disabled by default.
* Port number changes
  
  Port 21 of the FTP server is a well-known port number. Therefore, the port number is easily scanned and attacked. The port number of the FTP server can be changed to a private port number to reduce the probability of being scanned and attacked.
* ACLs
  
  ACLs can be configured for the FTP server in the system view. ACLs are used to limit the client IP addresses that can access a device.
* Source interface allowed to access a device
  
  Source interfaces supported by the FTP server can be configured. Users must access a device using the IP addresses of the configured source interfaces. In this way, the access range is controlled, and device security is enhanced.
* CPCAR-based flood attack defense
  
  In the scenario where Internet public addresses are deployed, a device may be attacked by traffic flooding on the management and control plane. You can configure a CPU defense policy to protect the device against traffic attacks.

#### Attack Methods

* Password cracking
  
  After an attacker obtains an FTP port number of a device, the attacker attempts to access the device. When the device requests authentication information, the attacker may crack the password. The device considers the attacker authenticated and allows the attacker to access.
* DoS
  
  The FTP server supports a limited number of users. When the number of allowed users reaches the upper limit, other users cannot access the device. This situation may occur as a result of normal FTP server usage, or when an FTP server is attacked.

#### Configuration and Maintenance Methods

* Disable the FTP service.
  
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] undo ftp server
  ```
  ```
  Warning: The operation will stop the FTP server. Do you want to continue? [Y/N]:y
  ```
  ```
  Info: Succeeded in closing the FTP server.
  ```
  ```
  [*HUAWEI] commit
  ```
* Change the port number of an FTP server.
  
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] ftp server port 5553
  ```
  ```
  Info: Port change successful. Please start the FTP service.
  ```
  ```
  [*HUAWEI] commit
  ```
* Configure an ACL.
  
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] acl 2000
  ```
  ```
  [*HUAWEI-acl-basic-2000] display this
  ```
  ```
  #
  ```
  ```
  acl number 2000
  ```
  ```
   rule 15 permit source 10.1.1.1 0
  ```
  ```
   rule 20 deny
  ```
  ```
  #
  ```
  ```
  return
  ```
  ```
  [*HUAWEI-acl-basic-2000] quit
  ```
  ```
  [*HUAWEI] ftp acl 2000
  ```
  ```
  [*HUAWEI] commit
  ```
* Configure an IPv6 ACL.
  
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] acl ipv6 2001
  ```
  ```
  [*HUAWEI-acl6-basic-2001] display this
  ```
  ```
  #
  ```
  ```
  acl ipv6 number 2001
  ```
  ```
   rule 5 permit source 2001:db8:1::1/64
  ```
  ```
   rule 10 deny
  ```
  ```
  #
  ```
  ```
  return
  ```
  ```
  [*HUAWEI-acl6-basic-2001] quit
  ```
  ```
  [*HUAWEI] ftp ipv6 acl 2001
  ```
  ```
  [*HUAWEI] commit
  ```
* Configure a source interface.
  
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] interface LoopBack 0
  ```
  ```
  [*HUAWEI-LoopBack0] display this
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip binding vpn-instance vpn1
  ```
  ```
   ip address 10.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```
  ```
  [*HUAWEI-LoopBack0] quit
  ```
  ```
  [*HUAWEI] ftp server-source -i loopback 0
  ```
  ```
  Warning: To make the server source configuration take effect, the FTP server will be restarted. Continue? [Y/N]:Y
  ```
  ```
  Info: Succeeded in setting the source interface of the FTP server to LoopBack0.
  ```
  ```
  Info: Succeeded in starting the FTP secure server.
  ```
  ```
  [*HUAWEI] commit
  ```
* Configure a source IPv6 IP address.
  
  ```
  <HUAWEI> system-view
  ```
  ```
  [~HUAWEI] ftp ipv6 server-source -a 2001:db8:1::1
  ```
  ```
  Warning: To make the server source configuration take effect, the FTP server will be restarted. Continue? [Y/N]:y
  ```
  ```
  [*HUAWEI] commit
  ```
* Configure CPCAR-based flood attack defense.
  
  1. Configure a CPU defense policy.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] cpu-defend policy 10
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] commit
     ```
  2. Configure TCP/IP attack defense.
     
     ```
     [~HUAWEI-cpu-defend-policy-10] tcpsyn-flood enable
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] fragment-flood enable
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] udp-packet-defend enable
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] abnormal-packet-defend enable
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] quit
     ```
     ```
     [*HUAWEI] commit
     ```
  3. Create an ACL.
     
     Create an advanced ACL 3341 and configure an FTP rule to allow the device to send FTP packets with the specified source interface address and deny other FTP packets.
     
     ```
     [~HUAWEI] acl number 3341
     ```
     ```
     [*HUAWEI-acl-adv-3341] rule permit udp source 192.168.1.0 0.0.0.255 source-port eq ftp
     ```
     ```
     [*HUAWEI-acl-adv-3341] rule permit udp source 192.168.1.0 0.0.0.255 destination-port eq ftp
     ```
     ```
     [*HUAWEI-acl-adv-3341] rule deny udp destination-port eq ftp
     ```
     ```
     [*HUAWEI-acl-adv-3341] commit
     ```
  4. Create a user-defined flow.
     
     After the ACL is used to classify protocol packets, you can apply the ACL to create user-defined flows so that different protocol packets are transmitted through different channels.
     
     Telnet is an access protocol, requires less processing bandwidth, and has low real-time requirements. Therefore, it is recommended that you set the bandwidth limit to 512 kbit/s and set the priority to low.
     
     ```
     [~HUAWEI] cpu-defend policy 10
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] user-defined-flow 11 acl 3341
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] car user-defined-flow 11 cir 512 cbs 5120
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] priority user-defined-flow 11 low
     ```
     ```
     [*HUAWEI-cpu-defend-policy-10] quit
     ```
     ```
     [*HUAWEI] commit
     ```
  5. Apply the attack defense policy.
     
     ```
     [~HUAWEI] slot 1
     ```
     ```
     [~HUAWEI-slot-1] cpu-defend-policy 10
     ```
     ```
     [*HUAWEI-slot-1] quit
     ```
     ```
     [*HUAWEI] commit
     ```

#### Configuration and Maintenance Suggestions

* Disable the FTP service when it is not in use.
* Change the port number of an FTP server.
* Configure ACLs.
* Use SFTP because FTP is not secure.

#### Verifying the Security Hardening Result

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration ftp** command to check the FTP configuration.
* Run the **[**display ftp-**](cmdqueryname=display+ftp-)[**server**](cmdqueryname=server)** command to check the status and configuration of the FTP server.
* Run the **[**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy)** *policy-number* command to check the attack defense policy.