Checking the Validity of the Certificate for the SSL Connection Between a GNE and NMS
=====================================================================================

If the certificate for the SSL connection between a GNE and NMS expires, you need to bind a new SSL policy to DCN.

#### Context

DCN allows an SSL connection to be established between a GNE and the NMS. The SSL connection has a valid period, and its validity is controlled through a certificate in a security policy that is applied to this connection. If the certificate expires, the SSL connection becomes invalid, and the NMS fails to manage devices through the GNE. Therefore, you need to check whether the certificate expires.


#### Procedure

1. Run the [**display ssl policy**](cmdqueryname=display+ssl+policy) [ *policy-name* ] command in any view to check the configuration of the SSL policy configured in the system.
2. If the SSL policy has expired, check whether the certificate specified in the policy is still valid. For details, see Checking Security Risks.
3. If the certificate has expired, run the [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name* command in the DCN view to bind a new SSL policy to DCN.

#### Result

Run the [**display ssl policy**](cmdqueryname=display+ssl+policy) command to view the configuration of the SSL policy configured in the system.