Configuring the MACsec Encryption Mode
======================================

Configuring_the_MACsec_Encryption_Mode

#### Context

When data packets sent by an interface are encrypted using MACsec, you can configure an encryption mode for the interface.

* **normal**: implements both integrity check and data encryption.
* **integrity-only**: implements only integrity check but not data encryption.

Data encryption and integrity check are as follows:

* Data encryption: The sender encrypts the data and transmits the data in ciphertext on the LAN link. The receiver decrypts the received encrypted data and then performs other processing.
* Integrity check: The receiver checks the integrity of received data to determine whether the data is tampered with. The sender calculates the Integrity Check Value (ICV) based on the data packet and encryption algorithm and adds it to the tail of the packet. After receiving the packet, the receiver calculates the ICV based on the data packet excluding the ICV field and the same encryption algorithm, and compares the obtained ICV with the ICV in the packet. If they are the same, the packet is considered complete and passes the check. Otherwise, the packet is discarded.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**macsec mode**](cmdqueryname=macsec+mode) { **normal** | **integrity-only** }
   
   
   
   The MACsec encryption mode is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.