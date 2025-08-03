Understanding BGP Authentication
================================

BGP peer relationships must be established for BGP to work properly, and these BGP peers can be authenticated for improved BGP security.

#### MD5 Authentication

BGP uses TCP as the transport layer protocol. When TCP connections are established, message-digest algorithm 5 (MD5) authentication can be used to improve BGP security. You can set an MD5 authentication password for a TCP connection so that TCP implements MD5 authentication of BGP. If authentication fails, no TCP connection can be established.

![](public_sys-resources/notice_3.0-en-us.png) 

MD5 authentication provides low security. To ensure high security, you are advised to use keychain authentication and a high-security algorithm, such as HMAC-SHA-256.

For security purposes, MD5 is not recommended. If MD5 is required, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.



#### Keychain Authentication

Keychain authentication is performed at the application layer. It ensures smooth service transmission and improves security by periodically changing the password and encryption algorithms. When keychain authentication is configured for BGP peer relationships over TCP connections, BGP messages as well as the establishment process of a TCP connection can be authenticated. For keychain configuration details, see "Keychain Configuration" in  Configuration Guide -> Security Configuration.


#### SSL/TLS Authentication

Secure Sockets Layer (SSL) is a security protocol that protects data privacy on the Internet. Transport Layer Security (TLS), the successor of SSL, also protects data integrity and privacy by preventing attackers from eavesdropping on the data exchanged between a client and server. SSL/TLS authentication can be configured to encrypt BGP messages, ensuring data transmission security.