Configuring a PKI Entity
========================

Configuring a PKI Entity

#### Context

Local certificates are signed and issued by the CA. A local certificate is a bundle of a public key and a PKI entity. PKI entity information contains the identity information of a PKI entity, based on which the CA identifies a certificate applicant. As such, when applying for a local certificate, the PKI entity must send PKI entity information to the CA.

The entity information includes the common name, FQDN, IP address, and email address. The common name is mandatory, while others are optional. The preceding information is contained in the certificate.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PKI entity view. If no PKI entity exists, create one first.
   
   
   ```
   [pki entity](cmdqueryname=pki+entity) entity-name
   ```
3. Configure a common name for the PKI entity.
   
   
   ```
   [common-name](cmdqueryname=common-name) common-name
   ```
4. **Optional:** Set other parameters for the PKI entity.
   
   
   
   To uniquely identify an applicant, you can run the following optional commands to configure the alias name for the PKI entity. If you do not configure alias names for the PKI entities that have the same common name, these PKI entities will fail to apply for a certificate.
   
   
   
   | To... | Run... |
   | --- | --- |
   | Configure an IP address for the PKI entity | [**ip-address**](cmdqueryname=ip-address) { *ipv4-address* | *ipv6-address* | *interface-type interface-number* [ **ipv6** ] } |
   | Configure an FQDN for the PKI entity | [**fqdn**](cmdqueryname=fqdn) *fqdn-name* |
   | Configure an email address for the PKI entity | [**email**](cmdqueryname=email) *email-address* |
   | Configure a country code for the PKI entity | [**country**](cmdqueryname=country) *country-code* |
   | Configure a locality name for the PKI entity | [**locality**](cmdqueryname=locality) *locality-name* |
   | Configure a state name for the PKI entity | [**state**](cmdqueryname=state) *state-name* |
   | Configure an organization name for the PKI entity | [**organization**](cmdqueryname=organization) *organization-name* |
   | Configure an organizational unit name for the PKI entity | [**organization-unit**](cmdqueryname=organization-unit) *organization-unit-name* |
5. Exit the PKI entity view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display pki entity**](cmdqueryname=display+pki+entity) [ *entity-name* ] command to check the PKI entity information.