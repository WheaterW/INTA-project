(Optional) Configuring IS-IS to Add the POI TLV to Purge LSPs
=============================================================

(Optional) Configuring IS-IS to Add the POI TLV to Purge LSPs

#### Context

This function helps locate the source of error packets when a fault occurs on the network.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Enable IS-IS to add the POI TLV to purge LSPs.
   
   
   ```
   [purge-originator-identification enable](cmdqueryname=purge-originator-identification+enable) [ always ]
   ```
   
   If the dynamic hostname function is configured on the local device, the hostname TLV is also added to purge LSPs.
   
   * If the [**purge-originator-identification enable**](cmdqueryname=purge-originator-identification+enable) command is run and HMAC-MD5 authentication is configured, generated purge LSPs do not carry the POI TLV/hostname TLV. If the command is run and authentication of another type is configured or no authentication is configured, generated purge LSPs carry the POI TLV/hostname TLV.
   * If the [**purge-originator-identification enable always**](cmdqueryname=purge-originator-identification+enable+always) command is run, generated purge LSPs carry the POI TLV/hostname TLV, regardless of whether authentication is configured or whether the **send-only** parameter is specified when configuring authentication.![](public_sys-resources/note_3.0-en-us.png) 
     
     Simple or HMAC-MD5 authentication is not recommended if high security is required. To prevent routing information from being tampered with, you are advised to enable authentication and use the keychain or HMAC-SHA256 algorithm to improve security.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display isis purge packet**](cmdqueryname=display+isis+purge+packet) *process-id* [ *packet-number* ] command to check statistics about received IS-IS purge LSPs carrying the POI TLV.

Run the [**display isis statistics purge-lsp**](cmdqueryname=display+isis+statistics+purge-lsp) [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] [ **level-1** | **level-2** ] command to check statistics about purge LSPs on the network.