Adding a PKI Realm to a Specified VPN
=====================================

Adding a PKI Realm to a Specified VPN

#### Context

A device needs to communicate with a server (for example, a CA server) to obtain and verify certificates. When the server is in a VPN, add a PKI realm to the VPN.


#### Procedure

* PKI realm view
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the PKI realm view. If no PKI realm exists, create one first.
     
     
     ```
     [pki realm](cmdqueryname=pki+realm) realm-name
     ```
  3. Adds a PKI realm to a specified VPN.
     
     
     ```
     [vpn-instance](cmdqueryname=vpn-instance) { vpn-instance-name }
     ```
     
     
     
     By default, a PKI realm does not belong to any VPN.
     
     The *vpn-instance-name* parameter is set using the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) command.
  4. Exit the PKI entity view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* CMP session view
  
  
  
  In the CMP session view, add a PKI realm to a specified VPN. This operation is used only when CMPv2 is used to apply for and update a certificate in online mode.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the CMP session view. If no CMP session exists, create one first.
     
     
     ```
     [pki cmp session](cmdqueryname=pki+cmp+session) session-name
     ```
     
     
     
     By default, no CMP session is created.
     
     A CMP session is locally available. It is not available to the CA and other devices.
  3. Adds a PKI realm to a specified VPN.
     
     
     ```
     [vpn-instance](cmdqueryname=vpn-instance) vpn-name { vpn-instance-name }
     [quit](cmdqueryname=quit)
     ```
     
     
     
     By default, a PKI realm does not belong to any VPN.
     
     The *vpn-instance-name* parameter is set using the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) command.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```