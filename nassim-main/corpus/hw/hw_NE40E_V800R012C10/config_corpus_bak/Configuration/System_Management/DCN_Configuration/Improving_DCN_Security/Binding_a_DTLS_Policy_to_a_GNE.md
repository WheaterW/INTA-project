Binding a DTLS Policy to a GNE
==============================

After a DTLS policy is bound to a GNE in the DCN view, the NMS can communicate with the GNE only after the policy is authenticated.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**dtls policy**](cmdqueryname=dtls+policy)*policyName* command to enter the DTLS policy view.
3. Run the [**pki-domain**](cmdqueryname=pki-domain)*pki-domain* command to bind a PKI domain to the DTLS policy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After a PKI domain is bound to a DTLS policy, the policy uses the certificates and CRL in the PKI domain.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. Run the [**dcn**](cmdqueryname=dcn) command to enter the DCN view.
7. Run the **set compatible mode** command to configure the DCN compatible mode on the GNE.
8. Run the [**bind client dtls-policy**](cmdqueryname=bind+client+dtls-policy) *dtlsPolicyName* command to bind a DTLS policy to the domain.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the default configuration file for an unconfigured device contains the [**dcn security-mode enable**](cmdqueryname=dcn+security-mode+enable) command, the [**bind client dtls-policy qx\_dtls\_client**](cmdqueryname=bind+client+dtls-policy+qx_dtls_client) command is automatically configured in the DCN view when the device starts with no configuration. In this case, you do not need to run the [**bind client dtls-policy**](cmdqueryname=bind+client+dtls-policy) *dtlsPolicyName* command to unbind the DTLS policy.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.