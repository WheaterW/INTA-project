Controlling Certificate Access Based on Certificate Attributes
==============================================================

The access control policy based on certificate attributes is an extra measure for certificate-based authentication. Only the certificates meeting specific requirements can be authenticated. This achieves refined control on user access permissions.

#### Context

In the application scenario where the certificate verification mechanism is used to establish an IPsec tunnel, there is a possibility that only the certificates meeting specific requirements can be authenticated for the establishment of the IPsec tunnel. For example, only certificates issued by a specific CA can be authenticated. You can also configure the access control policy that allows only certificates of specific devices to be authenticated, and these specific devices can establish IPsec tunnels. This achieves refined control on user access permissions.

If information in a certificate does not match the rules in the access control policy, the default action **permit** in the access control policy is performed on the NE40E. As a result, the certificate can be authenticated.


#### Procedure

* Configure the access control policy based on certificate attributes.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + If multiple attribute rules are configured in a certificate attribute group, the relationship between the rules is "And". This means that the action defined in the certificate attribute group will be implemented only if the certificate to be authenticated matches all the rules.
  + If multiple control rules are configured in an access control policy based on certificate attributes, the relationship between the rules is "Or". This means that the action defined in the access control policy is implemented as long as the certificate to be authenticated matches one rule. The following rules will not be matched.
  + If multiple access control policies are configured in the system based on certificate attributes, the policies are matched one by one. If the certificate to be authenticated matches no control policy, the action in the default access control policy is implemented.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pki certificate attribute-group**](cmdqueryname=pki+certificate+attribute-group) *group-name*
     
     
     
     A certificate attribute group is created and the PKI attribute configuration view is displayed.
  3. Run the following commands to configure certificate attribute rules:
     
     
     + Run [**attribute**](cmdqueryname=attribute+alt-subject-name+fqdn+ctn+equ+nctn+nequ) *id* **alt-subject-name** **fqdn** { **ctn** | **equ** | **nctn** | **nequ** } *attribute-value*
       
       The attribute rule for matching a specific FQDN in an alternative subject name is configured.
     + Run [**attribute**](cmdqueryname=attribute+alt-subject-name+ip+ctn+equ+nctn+nequ) *id* **alt-subject-name** **ip** { **ctn** | **equ** | **nctn** | **nequ** } *ip-address*
       
       The attribute rule for matching a specific IP address in an alternative subject name is configured.
     + Run [**attribute**](cmdqueryname=attribute+issuer-name+dn+ctn+equ+nctn+nequ) *id* **issuer-name** **dn** { **ctn** | **equ** | **nctn** | **nequ** } *attribute-value*
       
       The attribute rule for matching a specific certificate issuer name is configured.
     + Run [**attribute**](cmdqueryname=attribute+subject-name+dn+ctn+equ+nctn+nequ) *id* **subject-name** **dn** { **ctn** | **equ** | **nctn** | **nequ** } *attribute-value*
       
       The attribute rule for matching a specific certificate subject name is configured.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**pki certificate access-control-policy**](cmdqueryname=pki+certificate+access-control-policy) *policy-name*
     
     
     
     The access control policy based on certificate attributes is created and the PKI access configuration view is displayed.
  6. Run [**rule**](cmdqueryname=rule+permit+deny) *id* { **permit** | **deny** } *group-name*
     
     
     
     The control rules for certificate attributes are configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the default access control policy based on certificate attributes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pki certificate access-control-policy**](cmdqueryname=pki+certificate+access-control-policy+default+deny+permit) **default** { **deny** | **permit** }
     
     
     
     The default access control policy based on certificate attributes is configured.
     
     If the certificate access control policy is not required during negotiation for establishing an IPsec tunnel, run the [**pki certificate access-control-policy**](cmdqueryname=pki+certificate+access-control-policy+default+permit) **default** **permit** command to permit the certificate to be authenticated.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.