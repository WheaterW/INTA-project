NTP
===

NTP

#### Security Policy

Rapid network development poses higher network security requirements. The Network Time Protocol (NTP) packets transmitted on the network may be modified. NTP packet attacks may cause network interruption, disturb synchronization, and cause network data loss. Therefore, packets need to be protected.

NTP supports the following security policies:

* NTP support authentication to prevent receiving of bad synchronization data, error packets, and replay attacks from the networks.
* NTP supports the whitelist function. NTP creates a whitelist security label for each known port to rapidly exchange packets. This function is necessary for quick convergence on the network. If ports that send packets are not in the whitelist, they will only be assigned a default low bandwidth to prevent DOS attacks.
* NTP allows you to run commands to change the default port number that receives NTP packets.
* You can set access authority to protect local NTP services. This is a simple measure to ensure security.


#### Attack Methods

If authentication is configured on the client and server, NTP will accept the packets only if packets are authenticated to prevent accepting packets from unauthenticated peers.

To protect against subnet attacks, you can choose trusted time servers and allow only these trusted time servers to be the synchronization source.


#### Configuration and Maintenance Methods

NTP can authenticate protocol packets and provide HMAC-SHA256 authentication to enhance security.

1. # Set the authentication key of the key to **Huawei-12345** and authentication algorithm to **HMAC-SHA256** on the client.
   
   ```
   [~HUAWEI] ntp-service authentication enable
   ```
   ```
   [*HUAWEI] ntp-service authentication-keyid 1 authentication-mode hmac-sha256 cipher Huawei-12345
   ```
   ```
   [*HUAWEI] ntp-service reliable authentication-keyid 1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI] display current-configuration | include ntp
   ```
   ```
   #
   ```
   ```
   ntp-service authentication-keyid 1 authentication-mode hmac-sha256 cipher %^%#5_TD+l')]GVp>0:^0zBMN{%V;<_rw:v7E3,1X}C/%^%#
   ```
   ```
   ntp-service reliable authentication-keyid 1
   ```
   ```
   ntp-service authentication enable
   ```
   ```
   #
   ```
2. # Set the authentication key of the key to **Huawei-12345** and authentication algorithm to **HMAC-SHA256** on the server.
   
   ```
   [~HUAWEI] ntp-service authentication enable
   ```
   ```
   [*HUAWEI] ntp-service authentication-keyid 1 authentication-mode hmac-sha256 cipher Huawei-12345
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI] display current-configuration | include ntp
   ```
   ```
   #
   ```
   ```
   ntp-service authentication-keyid 1 authentication-mode hmac-sha256 cipher %@%@rob%'[{S0IcI6$Y.xM]+,1e*%@%@
   ```
   ```
   ntp-service authentication enable
   ```
   ```
   #
   ```
3. # Allow the peers matching IPv4 ACL 2000 and IPv6 ACL 2002 to perform time request, query control, and time synchronization on the local device.
   
   ```
   [~HUAWEI] ntp-service access peer 2000 ipv6 2002
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI] display current-configuration | include ntp
   ```
   ```
   #
   ```
   ```
   ntp-service access peer 2000 ipv6 2002
   ```
   ```
   #
   ```

NTP allows you to run commands to change the default port number that receives NTP packets.

1. Set the number of the port that receives NTP packets to 1026.
   ```
   [~HUAWEI] ntp-service port 1026
   ```

#### Configuration and Maintenance Suggestions

As the HMAC-SHA256 algorithm is more secure, using the HMAC-SHA256 algorithm is recommended.

The last rule in the ACL needs to deny all IP addresses. If an ACL is used to filter VPN addresses, run the [**rule**](cmdqueryname=rule) [ *rule-id* ] **deny** **vpn-instance** *vpn-instance-name* command in the ACL.


#### Verifying the Security Hardening Result

* Run the **[**display ntp-service sessions**](cmdqueryname=display+ntp-service+sessions)** [ ****verbose**** ] command to check the status of sessions maintained by the NTP service.
* Run the [**display ntp-service statistics packet**](cmdqueryname=display+ntp-service+statistics+packet) command to check statistics about global NTP packets.