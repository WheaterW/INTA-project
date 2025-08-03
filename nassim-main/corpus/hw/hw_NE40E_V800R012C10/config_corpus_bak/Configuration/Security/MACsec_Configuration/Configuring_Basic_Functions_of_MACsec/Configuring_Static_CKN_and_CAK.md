Configuring Static CKN and CAK
==============================

Configuring_Static_CKN_and_CAK

#### Context

The key used by MACsec to encrypt and decrypt data packets is generated and distributed by the key server based on the encryption algorithm in the MKA protocol and the configured static CAK. Therefore, you need to configure the CKN and corresponding CAK on the interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**mka cak-mode static**](cmdqueryname=mka+cak-mode+static) **ckn** *ckn* **cak** { **simple** *cak-simple* | **cipher** *cak-cipher* }
   
   
   
   Static CKN and CAK are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.