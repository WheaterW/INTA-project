Overview of SSH
===============

Overview of SSH

#### Definition

Secure Shell (SSH) is a cryptographic network protocol for transmitting network services (such as access and file transfer) securely over an unsecured network.

SSH versions are classified as SSH1.X and SSH2.0. SSH2.0 has an extended structure and features both security and function improvements over SSH1.X, including support for SFTP and more authentication and key exchange methods.


#### Purpose

Telnet lacks a secure authentication mode and uses TCP to transmit data in clear text, which brings great security risks. As a result, the system is vulnerable to attacks such as denial of service (DoS), IP address spoofing, and route spoofing. Telnet alone is no longer viable with the increasing importance of network security. SSH addresses Telnet's shortcomings by providing secure login and other secure network services on an insecure network.

SSH provides a secure channel over TCP for data exchange using the well-known port 22 (this can be changed as required for security purposes).