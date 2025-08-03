PPP
===

PPP

#### Security Policy

Protocol security policy : Provides optional authentication parameters. PPP provides two authentication modes: Password Authentication Protocol (PAP) and Challenge Hand Authentication Protocol (CHAP), and supports passwords in simple text and ciphertext.


#### Attack Methods

An attacker sends a large number of PPP packets to a device.


#### Configuration and Maintenance Methods

* Configure an authentication mode: no authentication, PAP authentication, or CHAP authentication.
* Configure the packet validation function. This function is configured by default.

#### Configuration and Maintenance Suggestions

Configure CHAP authentication to enhance PPP security.


#### Verifying the Security Hardening Result

Run the **display interface** [ *interface-type* [ **interface-number** ]] command to check the configuration and running status of the interface.