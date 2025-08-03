Log Information Security
========================

Log_Information_Security

#### Function Description

Logs record device information such as user operations and device running status, and are stored on devices as log files. Logs help network administrators monitor the running status of Routers and diagnose network faults.


#### Security Policy

Log security is assured by the access mode authentication and socket security. Only administrators have permissions to view logs. You can view logs in any of the following ways:

* Log in to a device and view logs through the CLI.
* Download log files to the local device through SFTP.
* Connect a device to a log server and configure the device to send log files to the log server.

The preceding methods require that a user pass password authentication, SSL certificate authentication, AAA authentication, or public key authentication and log in to the device to view logs online or obtain log files.

To ensure log transmission security, using the TCP-based SSL encryption mode is recommended.


#### Configuration and Maintenance Methods

For details, see the configuration and maintenance methods in console/Telnet/SSH/FTP/TFTP/socket.

Using the TCP-based SSL encryption mode for log transmission on a VPN is recommended.

1. Configure a VPN instance.
   ```
   [~HUAWEI] ip vpn-instance vrf2
   ```
   ```
   [*HUAWEI-vpn-instance-vrf2] route-distinguisher 2:2
   ```
   ```
   [*HUAWEI-vpn-instance-vrf2-af-ipv4] commit
   ```
   ```
   [~HUAWEI-vpn-instance-vrf2-af-ipv4] quit
   ```
   ```
   [~HUAWEI-vpn-instance-vrf2] vpn-target 2:2
   ```
   ```
   IVT Assignment result:
   Info: VPN-Target assignment is successful.
   EVT Assignment result:
   Info: VPN-Target assignment is successful.
   ```
   ```
   [*HUAWEI-vpn-instance-vrf2] commit
   ```
   ```
   [~HUAWEI-vpn-instance-vrf2] quit
   ```
   ```
   [~HUAWEI] interface gigabitethernet0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] ip binding vpn-instance vrf2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] ip address 10.137.130.245 255.255.254.0
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] commit
   ```
2. Configure an SSL policy and load certificates.
   ```
   [~HUAWEI] ssl policy huawei2014
   ```
   ```
   [*HUAWEI-ssl-policy-huawei2014] certificate load pem-cert servercert.pem key-pair dsa key-file serverkey.pem auth-code cipher huawei-123456
   ```
   ```
   [*HUAWEI-ssl-policy-huawei2014] crl load pem-crl server.pem
   ```
   ```
   [*HUAWEI-ssl-policy-huawei2014] trusted-ca load asn1-ca servercert.der
   ```
   ```
   [*HUAWEI-ssl-policy-huawei2014] commit
   ```
   ```
   [~HUAWEI-ssl-policy-huawei2014] quit
   ```
3. Configure a log host with a VPN attribute, with the TCP-based SSL encryption mode for log transmission.
   ```
   [~HUAWEI] info-center loghost 10.137.130.245 vpn-instance vrf2 transport tcp ssl-policy huawei2014
   ```
   ```
   [*HUAWEI] commit
   ```


#### Configuration and Maintenance Suggestions

For details, see the configuration and maintenance suggestions in console/Telnet/SSH/FTP/TFTP/socket. Using TCP-based SSL encryption for log transmission helps prevent unauthorized users from obtaining packets.


#### Verifying the Security Hardening Result

* Run the [**display info-center**](cmdqueryname=display+info-center) [ **statistics** ] command to check IM statistics.
* Run the [**display channel**](cmdqueryname=display+channel) [ *channel-number* | *channel-name* ] command to check the information channel.