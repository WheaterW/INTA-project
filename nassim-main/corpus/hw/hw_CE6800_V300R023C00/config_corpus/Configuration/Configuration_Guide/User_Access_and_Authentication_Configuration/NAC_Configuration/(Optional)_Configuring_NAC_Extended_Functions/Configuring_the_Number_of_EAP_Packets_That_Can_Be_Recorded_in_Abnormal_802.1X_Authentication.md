Configuring the Number of EAP Packets That Can Be Recorded in Abnormal 802.1X Authentication
============================================================================================

Configuring the Number of EAP Packets That Can Be Recorded in Abnormal 802.1X Authentication

#### Context

If 802.1X authentication fails, you need to check EAP packet exchange information for fault locating. To facilitate fault locating, you can configure the number of EAP packets to be recorded when 802.1X authentication is abnormal.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the number of EAP packets that can be recorded in abnormal 802.1X authentication.
   
   
   ```
   [dot1x abnormal-track cache-record-num](cmdqueryname=dot1x+abnormal-track+cache-record-num) cache-record-num
   ```
   
   By default, the device can record 20 EAP packets in abnormal 802.1X authentication.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```