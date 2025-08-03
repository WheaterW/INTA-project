Enabling PKI Whitelist Check
============================

In LTE scenarios, a security gateway and base stations use certificates to negotiate IPsec tunnels. The PKI whitelist on the security gateway can be used to uniformly manage certificates of base stations.

#### Context

If PKI whitelist check is enabled on the security gateway using the [**pki whitelist enable**](cmdqueryname=pki+whitelist+enable) command, the common names in the certificate subjects of base stations must be imported to the security gateway's PKI whitelist using the [**pki import whitelist file-name**](cmdqueryname=pki+import+whitelist+file-name) *filename* command for certificate verification of the base stations.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Enable PKI whitelist check globally or for an IKE peer.
   
   
   * Enable global PKI whitelist check.
     
     Run [**pki whitelist enable**](cmdqueryname=pki+whitelist+enable)
     
     Global PKI whitelist check is enabled.
   * Enable PKI whitelist check for an IKE peer.
     
     1. Run [**ike peer**](cmdqueryname=ike+peer) *peer-name*
        
        The IKE peer view is displayed.
     2. Run [**pki whitelist enable**](cmdqueryname=pki+whitelist+enable)
        
        The PKI whitelist check function is enabled for an IKE peer.
        
        After PKI whitelist check is enabled for an IKE peer using the [**pki whitelist enable**](cmdqueryname=pki+whitelist+enable) command and the IKE peer receives certificate authentication packets from a remote device, the IKE peer checks whether the common names in the remote certificate subjects match the PKI whitelist. If not, the authentication fails.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**pki whitelist enable**](cmdqueryname=pki+whitelist+enable) or [**pki whitelist disable**](cmdqueryname=pki+whitelist+disable) command has been run in the IKE peer view, the configuration in the IKE peer view takes effect, regardless of whether global PKI whitelist check is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pki import whitelist file-name**](cmdqueryname=pki+import+whitelist+file-name) *filename*
   
   
   
   The PKI whitelist in an XML file is imported to a device.
5. (Optional) Run [**pki whitelist filter enable**](cmdqueryname=pki+whitelist+filter+enable)
   
   
   
   The suffix filtering function is enabled to filter suffixes of whitelists imported to the device and common name suffixes of the certificates received from the peer end during whitelist-based IPsec certificate negotiation.
   
   In whitelist based IPsec certificate authentication scenarios, when the names of whitelists imported into a device or common names of the certificates received from the peer end are redundant, run the [**pki whitelist filter enable**](cmdqueryname=pki+whitelist+filter+enable) command to simplify the imported whitelists. For example, after the common name of a base station certificate on the live network is imported into a whitelist, a record carrying different suffixes may be generated, causing one base station in the whitelist to consume multiple whitelist resources. To resolve this problem, run the [**pki whitelist filter enable**](cmdqueryname=pki+whitelist+filter+enable) command.
6. Run [**pki whitelist capacity warning-threshold**](cmdqueryname=pki+whitelist+capacity+warning-threshold) *threshold-value*
   
   
   
   An alarm threshold is configured for the number of imported whitelists.
7. Run [**pki whitelist**](cmdqueryname=pki+whitelist+add+delete+common-name+filename) { **add** | **delete** } **common-name** *common-name* **filename** *file-name*
   
   
   
   The IPsec PKI whitelist data is dynamically modified.
8. Run [**pki whitelist update**](cmdqueryname=pki+whitelist+update+filename+all) { **filename** *filename* | **all** }
   
   
   
   The modified IPsec PKI whitelist data is updated.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

To check the PKI whitelists on a device, run the [**display pki whitelist**](cmdqueryname=display+pki+whitelist) command. The command output helps fault locating and analyzing.

To check the whitelist data dynamically modified by users through the command, run the [**display pki whitelist update**](cmdqueryname=display+pki+whitelist+update+filename+all) { **filename** *file-name* | **all** } command.