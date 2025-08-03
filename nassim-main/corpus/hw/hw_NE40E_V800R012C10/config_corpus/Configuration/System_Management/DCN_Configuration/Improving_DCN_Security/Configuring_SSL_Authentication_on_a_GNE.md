Configuring SSL Authentication on a GNE
=======================================

After Secure Sockets Layer (SSL) authentication is configured on a GNE, the GNE can communicate with its interworking NMSs only when the exchanged packets are authenticated.

#### Prerequisites

Before configuring DCN SSL functions, configure an SSL policy and load a digital certificate.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**bind ssl-policy**](cmdqueryname=bind+ssl-policy) *ssl-policy-name*
   
   
   
   An SSL policy is bound to DCN.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Load the certificate of the SSL policy to be bound to the NMSs and GNE, so DCN can use the certificate to implement SSL handshake authentication after the SSL policy is bound to DCN.
4. Run [**connect-mode**](cmdqueryname=connect-mode) { **normal** | **security** | **both** }
   
   
   
   A connection mode is specified for the GNE to set up connections with NMSs.
   
   
   
   * **normal**: indicates that SSL encryption is not applied to the TCP connection.
   * **security**: indicates that SSL encryption is applied to the TCP connection.
   * **both**: indicates that both **normal** and **security** are supported.
5. Run [**ssl verify-mode**](cmdqueryname=ssl+verify-mode) { **single** | **dual** }
   
   
   
   The SSL authentication mode is configured.
   
   
   
   * **single**: indicates that SSL authentication applies only to the GNE.
   * **dual**: indicates that SSL authentication applies both to the GNE and NMS.
6. (Optional) Run [**ssl-auth-fail threshold-alarm**](cmdqueryname=ssl-auth-fail+threshold-alarm) **report-times** *report-times*
   
   
   
   An alarm generation threshold is set for the number of SSL authentication failures within 60s.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.