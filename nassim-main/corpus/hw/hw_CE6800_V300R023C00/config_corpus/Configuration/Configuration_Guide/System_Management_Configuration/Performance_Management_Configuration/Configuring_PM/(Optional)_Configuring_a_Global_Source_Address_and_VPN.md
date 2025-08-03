(Optional) Configuring a Global Source Address and VPN
======================================================

(Optional) Configuring a Global Source Address and VPN

#### Context

To use the same source interface address and VPN for uploading performance statistics files to multiple performance management server processes, configure a global source interface and VPN. This interface and VPN are used if no source interface address or VPN is specified for a specific performance management server process using the [**protocol**](cmdqueryname=protocol) command.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the performance management view.
   
   
   ```
   [pm](cmdqueryname=pm)
   ```
3. Configure a global source address and VPN for uploading performance statistics files.
   
   
   * Configure a global IPv4 source address.
     ```
     [client-source interface](cmdqueryname=client-source+interface) { interface-name | interface-type interface-number }
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The device uses the IPv4 address and VPN configured on the interface for uploading performance statistics files.
     
     If no IPv4 address is configured for the interface, files may fail to be uploaded.
   * Configure a global IPv6 source address and VPN.
     ```
     [client-source ipv6](cmdqueryname=client-source+ipv6) IPV6ADDR [ [vpn-instance](cmdqueryname=vpn-instance) vpnInstanceName ]
     ```
     
     The CE6885-LL supports this configuration only in standard forwarding mode.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```