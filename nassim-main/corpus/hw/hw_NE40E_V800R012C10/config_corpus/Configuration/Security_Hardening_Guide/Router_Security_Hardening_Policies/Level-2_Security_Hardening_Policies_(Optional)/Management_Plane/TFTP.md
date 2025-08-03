TFTP
====

TFTP

#### Security Policy

The Trivial File Transfer Protocol (TFTP) does not support authentication. It is an insecure file copy protocol. Huawei devices support the TFTP client functions, but not TFTP server functions.

Only users with management rights (level 3) can run TFTP client-related commands to operate files on a device.


#### Attack Methods

N/A


#### Configuration and Maintenance Methods

* Configure an ACL.
  
  ```
  [~HUAWEI] acl 2000
  ```
  ```
  [~HUAWEI-acl-basic-2000] display this
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
  [~HUAWEI] tftp-server acl 2000
  ```
  ```
  [*HUAWEI] commit
  ```
* Configure an IPv6 ACL.
  
  ```
  [~HUAWEI] acl ipv6 2001
  ```
  ```
  [~HUAWEI-acl6-basic-2001] display this
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
  [~HUAWEI-acl6-basic-2001] quit
  ```
  ```
  [~HUAWEI] tftp-server ipv6 acl 2001
  ```
  ```
  [*HUAWEI] commit
  ```
* Configure a source interface.
  
  ```
  [~HUAWEI] interface LoopBack 0
  ```
  ```
  [~HUAWEI-LoopBack0] display this
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
   ipv6 enable
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
  [~HUAWEI-LoopBack0] quit
  ```
  ```
  [~HUAWEI] tftp client-source -i LoopBack 1 
  ```
  ```
  Info: Succeeded in setting the source interface of the TFTP client to LoopBack1.
  ```
  ```
  [*HUAWEI] commit
  ```

#### Configuration and Maintenance Suggestions

Use SFTP because TFTP is not secure.


#### Verifying the Security Hardening Result

Run the **[**display tftp-client**](cmdqueryname=display+tftp-client)** command to check the configuration of the TFTP client.