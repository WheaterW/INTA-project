SSH Key Exchange Failure
========================

SSH Key Exchange Failure

#### Fault Symptom

When the device is used as an SSH server, the third-party client software fails to exchange the key with the SSH server, causing SSH connection failure.


#### Possible Cause

Keys can be exchanged only after the client and server negotiate the key exchange algorithm, encryption algorithm, public key algorithm, and HMAC algorithm. If any algorithm fails to be negotiated, the key exchange will fail. The algorithm negotiation fails because the algorithm supported by the client is not configured on the SSH server.


#### Procedure

1. Use other methods to log in to the SSH server. For details, see "Logging In to the CLI" in Configuration Guide - Basic Configuration.
2. Enable the debugging for the SSH server.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   [info-center enable](cmdqueryname=info-center+enable)
   [quit](cmdqueryname=quit)
   terminal monitor
   terminal debugging
   [debugging ssh server](cmdqueryname=debugging+ssh+server) all
   ```
3. Connect the SSH server through third-party client software.
4. Check the algorithms supported by the client in the debug information displayed by the SSH server user terminal.
   
   
   
   Copy the debug information to a TXT file, and use the following regular expressions to search for the algorithms supported by the third-party client software. For details, see [Table 1](#EN-US_TASK_0000001563753669__table369912567165).
   
   **Table 1** Searching for the algorithms supported by the third-party client software
   | Algorithm | Regular Expression |
   | --- | --- |
   | Key exchange algorithm | SSH protocol packet received.\*key\_ex |
   | Encryption algorithm | SSH protocol packet received.\*ciph\_ctos |
   | Public key algorithm | SSH protocol packet received.\*ser\_host\_key |
   | HMAC algorithm | SSH protocol packet received.\*hmac\_ctos |
5. Configure the key exchange algorithm, encryption algorithm, public key algorithm, and HMAC algorithm supported by both the client and server on the SSH server. For details about the supported algorithms and configuration methods, see [Configuring the SSH Server Function and Related Parameters](galaxy_ssh_cfg_0009.html).