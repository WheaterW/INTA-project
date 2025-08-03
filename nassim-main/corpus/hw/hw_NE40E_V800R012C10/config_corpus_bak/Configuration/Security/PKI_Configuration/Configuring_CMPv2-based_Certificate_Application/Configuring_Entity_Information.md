Configuring Entity Information
==============================

When applying for certificates, an entity must add entity information to a certificate request file and send the file to a CA. The CA uses a piece of important information to describe an entity, and identifies the entity using a unique distinguished name (DN).

#### Context

A local certificate associates user identity information with the user public key, while the identity information must be associated with a specific PKI entity. The CA identifies the certificate applicant based on the identity information provided by the entity. Entity information includes:

* Common name of the entity
* Country code of the entity
* Email address of the entity
* Fully qualified domain name (FQDN) of the entity
* IP address of the entity
* Name of the region where the entity resides
* Organization name of the entity
* Department name of the entity
* State or province of the entity![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In the entity information, the common name of the entity is mandatory. Whether to configure other attributes depends on the certificate issuing policy on the CA server. If the attributes used to filter certificates do not map the certificate issuing policy, certificate application will fail.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pki entity**](cmdqueryname=pki+entity) *entity-name*
   
   
   
   An entity is created, and the entity view is displayed.
3. Configure entity attributes.
   
   
   * Run the [**common-name**](cmdqueryname=common-name) *cn-name* command to configure a common name for the entity.
   * (Optional) Run the [**country**](cmdqueryname=country) *country-code* command to configure a country code for the entity.
   * (Optional) Run the [**email**](cmdqueryname=email) *email-address* command to configure an email address for the entity.
   * (Optional) Run the [**fqdn**](cmdqueryname=fqdn) *fqdn-name* command to configure an FQDN for the entity.
   * (Optional) Run the [**ip-address**](cmdqueryname=ip-address) *ip-address* command to configure an IP address for the entity.
   * (Optional) Run the [**locality**](cmdqueryname=locality) *locality-name* command to configure a region name for the entity.
   * (Optional) Run the [**organization**](cmdqueryname=organization) *organization-name* command to configure an organization name for the entity.
   * (Optional) Run the [**organization-unit**](cmdqueryname=organization-unit) *org-unit* command to configure a department name for the entity.
   * (Optional) Run the [**state**](cmdqueryname=state) *state-province-name* command to configure a state or province name for the entity.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.