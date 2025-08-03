After DHCP Snooping Is Enabled, a User Can Obtain an IP Address but Cannot Access the Internet
==============================================================================================

After DHCP Snooping Is Enabled, a User Can Obtain an IP Address but Cannot Access the Internet

#### Fault Symptom

After DHCP snooping is enabled, a user can obtain an IP address but cannot access the Internet.


#### Possible Causes

If the IP address is assigned by a bogus DHCP server, the DHCP client cannot access the Internet with the bogus IP address.


#### Procedure

If this problem occurs, you are advised to configure DHCP snooping on the Layer 2 access device or the first DHCP relay agent to ensure that the client can obtain a correct IP address.

* If you are configuring DHCP snooping on a Layer 2 access device, perform Steps 1 to 3 in sequence.
* If you are configuring DHCP snooping on a DHCP relay agent, only Steps 1 and 2 are required.

1. Perform the configuration in the system view.
   ```
   [system-view](cmdqueryname=system-view)
   [dhcp enable](cmdqueryname=dhcp+enable)
   [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
   ```
2. Perform the configuration on all interfaces connected to DHCP clients. The following uses the configuration on 100GE 1/0/1 as an example.
   ```
   [interface](cmdqueryname=interface) 100GE 1/0/1
   [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
   [quit](cmdqueryname=quit)
   ```
3. Perform the configuration on the interface connected to the DHCP server. The following uses 100GE 1/0/2 as an example.
   ```
   [interface](cmdqueryname=interface) 100GE 1/0/2
   [dhcp snooping trusted](cmdqueryname=dhcp+snooping+trusted)
   [quit](cmdqueryname=quit)
   ```