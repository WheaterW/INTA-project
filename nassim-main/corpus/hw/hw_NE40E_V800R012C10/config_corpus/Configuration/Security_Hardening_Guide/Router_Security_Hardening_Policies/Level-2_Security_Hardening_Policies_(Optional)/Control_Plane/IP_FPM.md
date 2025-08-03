IP FPM
======

This section describes the security policies, attack methods, and configuration and maintenance methods and suggestions applied to IP FPM.

#### Security Policy

IP FPM helps improve system security through configurable packet authentication. After the same authentication mode and password are configured on an MCP and its associated DCPs, the MCP processes packets only from authenticated DCPs. This improves not only network security, but also the reliability of network performance measurement. To configure the authentication mode and password for an IP FPM instance, run the [**authentication-mode**](cmdqueryname=authentication-mode) **hmac-sha256** **key-id** *key-id* [ **cipher** ] *password* command. Note the following:

* The same authentication password must be configured on the sender and receiver.
  + The value of *key-id* is an integer ranging from 1 to 64.
  + The authentication password is a string of 1 to 255 characters in cleartext or a string of 24 or 32 to 432 characters in ciphertext.
* After packet authentication is configured, an authentication data segment is added to each packet sent by a DCP.
* After receiving a packet from a DCP, an MCP decapsulates the packet and parses the authentication password in ciphertext. If the password differs from that on the MCP, the MCP discards the packet; otherwise, the MCP continues to parse the packet loss and delay data.
* An authentication password can be configured in cleartext or ciphertext. In either mode, the password is displayed in ciphertext in the configuration file.

#### Attack Methods

An attacker forges IP FPM packets and sends them to a victim, which forwards the packets or sends them to the CPU.


#### Configuration and Maintenance Methods

* Configure authentication in the IP FPM DCP view.
  
  Run the [**authentication-mode**](cmdqueryname=authentication-mode) **hmac-sha256** **key-id** *key-id* [ **cipher** ] *password* command. If an authentication password is configured in the IP FPM DCP view but not in the IP FPM DCP instance view, the authentication password configured in the IP FPM DCP view is used. The MCP can parse packets correctly only when authentication information is consistent on the DCP and MCP.
* Configure authentication in the IP FPM DCP instance view.
  
  Run the [**authentication-mode**](cmdqueryname=authentication-mode) **hmac-sha256** **key-id** *key-id* [ **cipher** ] *password* command. If an authentication password is configured in both the IP FPM DCP instance view and IP FPM DCP view, the authentication password configured in the IP FPM DCP instance view is used. The MCP can parse packets correctly only when authentication information is consistent on the DCP and MCP.
* Configure authentication in the IP FPM MCP view.
  
  Run the [**authentication-mode**](cmdqueryname=authentication-mode) **hmac-sha256** **key-id** *key-id* [ **cipher** ] *password* command. The MCP can parse packets correctly only when authentication information is consistent on the DCP and MCP.

#### Verifying the Security Hardening Result

Run the [**display ipfpm dcp**](cmdqueryname=display+ipfpm+dcp) and [**display ipfpm mcp**](cmdqueryname=display+ipfpm+mcp) commands to check the IP FPM authentication configuration.


#### Configuration and Maintenance Suggestions

Enable IP FPM packet authentication on a network requiring high security.