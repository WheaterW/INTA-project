Configuring the CRL Function
============================

Configuring the CRL function includes enabling CRL check and updating the CRL. After the CRL function is configured, a device checks the validity of the peer device's certificate. If the serial number of the peer device's certificate is listed in the CRL, the peer device's certificate has been revoked and is considered invalid.

#### Prerequisites

Before setting automatic CRL update, verify functions to ensure that the network and server are normal.


#### Context

Before configuring the CRL function, be aware of the following information:

* Enable CRL check.
  
  Before configuring CRL, enable CRL check.
  
  When a certificate is being verified after CRL check is enabled, the CRL is queried for checking whether it contains the serial number of the certificate. If the CRL contains the serial number of the certificate, the certificate has been revoked and considered invalid. For details about how to verify the certificate validity, see [Verifying Certificates](dc_vrp_cfg_cmp_0010.html).
* Update the CRL.
  
  To ensure that the latest CRL is used, check the CRL status periodically and download the latest CRL from the CRL server using HTTP or LDAP.
  
  Updating the CRL consists of automatically updating the CRL and manually updating the CRL. Automatically updating the CRL can be implemented using HTTP or LDAP. After the specified interval elapses, the system automatically downloads the CRL using HTTP or LDAP. When the latest CRL is urgently required, manually update the CRL by downloading the CRL from the CRL server.

If the device does not have any homogeneous CRL certificate, the new CRL certificate is imported to the non-domain.

If the device has only one homogeneous CRL certificate, the new CRL certificate replaces this certificate.

If the device has multiple homogeneous CRL certificates, the new CRL certificate preferentially replaces the homogeneous CRL certificate in the local domain. If this condition is not met, the new CRL certificate replaces the homogeneous CRL certificate in the non-domain. If both of the preceding conditions are not met, the new CRL certificate is imported into the non-domain.

Homogeneous certificates refer to certificates with the same issuer and subject. Local domain refers to the PKI domain where configurations need to be automatically updated. Non-domain refers to an isolated domain that does not belong to any PKI domain.


#### Procedure

1. Enable CRL check.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**pki crl check enable**](cmdqueryname=pki+crl+check+enable) command to enable CRL check.
2. Update the CRL.
   
   Perform the following operations as needed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the CRL is automatically updated or downloaded through HTTP or LDAP, ensure that the CF card has sufficient space for the CRL file to prevent update failures.
   
   HTTP is insecure. Therefore, you are advised to use other methods to update the CRL.
   
   * Enable the function of automatically updating the CRL using HTTP.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**pki domain**](cmdqueryname=pki+domain) *domain-name* command to enter the PKI domain name configuration view.
     3. Run the [**crl auto-update enable**](cmdqueryname=crl+auto-update+enable) command to enable automatic CRL update.
     4. Run the [**crl update-period**](cmdqueryname=crl+update-period) *interval* command to set an interval between two consecutive automatic CRL updates.
     5. Run the [**crl http**](cmdqueryname=crl+http) command to enable the function of automatically updating the CRL using HTTP.
     6. Run the [**crl url**](cmdqueryname=crl+url+source+vpn-instance) *url-addr* [ **source** *source-ip-address* ] [ **vpn-instance** *vpn-instance-name* ] command to configure the URL of the CRL distribution point (CDP).
        
        This command can be executed only after the [**crl http**](cmdqueryname=crl+http) command is run.
     7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Enable the function of automatically updating the CRL using LDAP.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. (Optional) Run the **ssl policy** *policy-name* command to create an SSL policy and enter the SSL policy view.
        
        After creating the SSL policy, import a CA certificate to it. For details, see **Basic Configuration** > **Accessing Other Devices Configuration** > **Configuring and Binding an SSL Policy**.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. (Optional) Run the **pki ldap bind ssl-policy** *policy-name* command to bind the SSL policy to the device functioning as an LDAP client.
     5. Run the [**pki domain**](cmdqueryname=pki+domain) *domain-name* command to enter the PKI domain name configuration view.
     6. Run the [**crl auto-update enable**](cmdqueryname=crl+auto-update+enable) command to enable automatic CRL update.
     7. Run the [**crl update-period**](cmdqueryname=crl+update-period) *interval* command to set an interval between two consecutive automatic CRL updates.
     8. Run the [**crl ldap**](cmdqueryname=crl+ldap) command to enable the function of automatically updating the CRL using LDAP.
     9. Run the [**ldap-server**](cmdqueryname=ldap-server+authentication+ip+vpn-instance+source+port+version) { **authentication** *ldap-dn* *ldap-password* | **ip** *ldap-ip-address* [ **vpn-instance** *vpn-instance-name* ] [ **source** *source-ip-address* ] { [ **port** *port* ] | [ **version** *version* ] } \* [ **ssl** ] } command to configure the LDAP server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If the **ssl** parameter is specified, you need to bind the SSL policy to the LDAP client. For details, see optional steps b and d.
        
        
        This command can be executed only after the [**crl ldap**](cmdqueryname=crl+ldap) command is run.
     10. Run the [**crl ldap**](cmdqueryname=crl+ldap+attribute+dn) [ **attribute** *attr-value* ] **dn** *dn-value* command to configure the attributes and identifier used to obtain the CRL from the LDAP server.
         
         This command can be executed only after the [**crl ldap**](cmdqueryname=crl+ldap) command is run.
     11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Manually update the CRL.
     1. Download a CRL. Select a CRL download mode as needed.
        + Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
        + Run the [**pki http**](cmdqueryname=pki+http+vpn-instance+source) *url-addr* [ **vpn-instance** *vpn-instance-name* ] *save-name* [ **source** *source-ip-address* ] command to download a CRL through HTTP.
        + Run the [**pki ldap**](cmdqueryname=pki+ldap+ip+vpn-instance+source+port+version+attribute) **ip** *ldap-ip-address* [ **vpn-instance** *vpn-instance-name* ] [ **source** *source-ip-address* ] **port** *port* **version** *version* [ **attribute** *attr-value* ] [ **authentication** *ldap-dn* *ldap-password* ] [ **ssl** ] *save-name* **dn** *dn-value* command to download a CRL through LDAP.
     2. Run the [**pki import-certificate**](cmdqueryname=pki+import-certificate+crl+domain+filename) **crl** [ **domain** *domainName* ] **filename** *file-name* command to import the CRL.