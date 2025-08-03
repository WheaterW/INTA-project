Configuring an Authentication Mode for DLDPDUs
==============================================

You can configure the authentication mode of DLDPDUs to prevent network attacks and malicious probes.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface or interface group view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   [port-group](cmdqueryname=port-group) port-group-name
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)  
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure an authentication mode for DLDPDUs exchanged between interfaces on the local and neighbor devices.
   
   
   ```
   [dldp authentication-mode](cmdqueryname=dldp+authentication-mode) { md5 { md5-password1 | md5-password2 } | simple { simple-password1 | simple-password2 } | sha { sha-password1 | sha-password2 } | hmac-sha256 { hmac-password1 | hmac-password2 } }
   ```
   By default, no authentication is performed on DLDPDUs exchanged between interfaces on the local and neighbor devices.![](public_sys-resources/note_3.0-en-us.png) 
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display dldp**](cmdqueryname=display+dldp) [ **interface** *interface-type* *interface-number* ] command to check the DLDP configuration and neighbor entries.
* Run the [**display dldp statistics**](cmdqueryname=display+dldp+statistics) [ **interface** *interface-type* *interface-number* ] command to check statistics about DLDPDUs on all interfaces or a specific one.
* Run the [**display fwm dldp statistics**](cmdqueryname=display+fwm+dldp+statistics) [ **all** ] **slot** *slot-id* command in any view to check statistics about the DLDP module on a specified board.