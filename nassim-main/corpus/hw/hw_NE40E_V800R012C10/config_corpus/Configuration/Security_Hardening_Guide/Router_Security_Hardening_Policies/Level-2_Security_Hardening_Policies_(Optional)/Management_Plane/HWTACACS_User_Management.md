HWTACACS User Management
========================

The Huawei Terminal Access Controller Access Control System (HWTACACS) protocol is an enhancement of the Terminal Access Controller Access Control System Plus (TACACS+) protocol. Similar to RADIUS, HWTACACS uses the client/server model to implement multiple AAA functions and can be used for authentication, authorization, and accounting of Point-to-Point Protocol (PPP) and login users.

#### Security Policy

HWTACACS transmits traffic over TCP connections. A shared key, which is not transmitted over a network, is used for authentication between clients and the HWTACACS server. In addition, the packet body is encrypted based on the shared key so that packets can be securely transmitted.

A shared key configured on a device is stored using an enhanced encrypted algorithm by default.


#### Attack Methods

There are few TACACS-exploiting attacks:

* An attacker can change the content of packets in transit. Currently, complete packet information cannot be provided.
* An attacker can sniff the TACACS packets transmitted in plaintext. It is recommended to encrypt packets.

#### Configuration and Maintenance Methods

Run the [**hwtacacs-server shared-key**](cmdqueryname=hwtacacs-server+shared-key) **cipher** *key-string* command to configure a shared key for each HWTACACS group. The shared key is used to encrypt packets transmitted over HWTACACS by using MD5, increasing the transmission security. The **cipher** keyword is used when the shared key is configured. When the shared key is viewed, the encrypted key is displayed, increasing the key security.![](../../../../public_sys-resources/note_3.0-en-us.png) 

The MD5 algorithm is insecure and poses security risks.




#### Configuration and Maintenance Suggestions

Run the [**hwtacacs-server shared-key**](cmdqueryname=hwtacacs-server+shared-key) **cipher** *key-string* command to configure a key for encrypting packet bodies.


#### Verifying the Security Hardening Result

Run the [**display hwtacacs-server template**](cmdqueryname=display+hwtacacs-server+template) command to check the HWTACACS server configuration.