Configuring SSH Bidirectional Certificate Authentication for NETCONF Connections
================================================================================

Configuring SSH Bidirectional Certificate Authentication for NETCONF Connections

#### Security Policy

1. Certificate authentication requests and certificate obtaining requests can be exchanged between the SSH and PKI components.
2. After receiving a connection request, if the negotiated host authentication method is certificate authentication, the SSH component sends a CERT Req message to the PKI component to obtain the certificate and the corresponding KEY file.
3. A timer is started to retransmit a certificate request message if no CERT RSP ACK message is received. The timer interval is 5s, and the certificate request message is retransmitted for a maximum of three times. This mechanism prevents DoS attacks.
4. After three timeouts, the SSH connection is torn down, and the cause of the SSH login failure is recorded as no response from the PKI component during host authentication.
5. When receiving a user certificate authentication request, the SSH component sends an authentication request message to the PKI component.
6. A timer is started to retransmit an authentication request message if no AUTH RSP ACK message is received. The timer interval is 5s, and the certificate request message is retransmitted for a maximum of three times. This mechanism prevents DoS attacks.
7. After three timeouts, the SSH connection is torn down, and the cause of the SSH login failure is recorded as no response from the PKI component during user authentication.

#### Configuration and Maintenance Methods

1. Run [**ssh server assign**](cmdqueryname=ssh+server+assign) **pki** *pki-keyname*
   
   A certificate source is bound for host certificate authentication. The user certificate in the PKI domain is required.
2. Run [**ssh server publickey**](cmdqueryname=ssh+server+publickey) **x509v3-ssh-rsa**
   
   The host authentication method is specified to certificate authentication in x509 format.
3. Run [**ssh user**](cmdqueryname=ssh+user) *user-name* **authentication-type** { **password-x509v3-rsa** | **x509v3-rsa** }
   
   The authentication mode of the SSH user is specified to certificate authentication in x509 format.
4. Run [**ssh user**](cmdqueryname=ssh+user) *user-name* **assign** **pki** *pki-name*
   
   A PKI domain is bound to the SSH user.
5. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Verifying the Security Hardening Result

* Run the **[**display ssh server status**](cmdqueryname=display+ssh+server+status)** command to check global configurations of the SSH server.
* Run the **[**display ssh server session**](cmdqueryname=display+ssh+server+session)** command to check session connection information of the SSH server.
* Run the **[**display ssh server-info**](cmdqueryname=display+ssh+server-info)** command to check the SSH server and public key binding information when the device functions as an SSH client.