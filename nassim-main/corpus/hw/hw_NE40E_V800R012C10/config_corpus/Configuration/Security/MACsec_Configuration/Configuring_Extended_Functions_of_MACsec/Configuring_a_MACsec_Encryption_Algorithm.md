Configuring a MACsec Encryption Algorithm
=========================================

Configuring a MACsec Encryption Algorithm

#### Context

When data packets sent by an interface are encrypted using MACsec, you can configure an encryption algorithm for the interface. To reduce the MACsec renegotiation frequency and protocol processing pressure on the device, you are advised to use an extended encryption algorithm when the interface rate reaches 100 Gbit/s or higher.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**macsec cipher-suite**](cmdqueryname=macsec+cipher-suite) { **gcm-aes-128** | **gcm-aes-xpn-128** | **gcm-aes-256** | **gcm-aes-xpn-256** | **gcm-aes-xpn-128-compatible** }
   
   
   
   A MACsec encryption algorithm is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.