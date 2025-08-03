Configuring an ARP Resource Allocation Mode
===========================================

Configuring an ARP Resource Allocation Mode

#### Context

ARP information learned by a device is stored in EEDB entries of chips. According to the mode in which ARP information is stored in the EEDB entries, ARP resource allocation modes are classified as follows:

* Global mode
  
  In global mode, ARP information is identified based on a key composed of the IP address, logical interface index, and physical interface index. ARP information is stored on all chips based on the same resource index, meaning that ARP information stored on each chip is the same.
  
  In this mode, the maximum number of ARP resources supported by the device refers to that of the chip with minimum specifications among all chips.
* Extend mode
  
  In extend mode, ARP information is identified based on a key composed of 43 most significant bits of a MAC address. ARP information is stored on all chips based on the same resource index, meaning that ARP information stored on each chip is the same. The extend mode differs from the global mode in that ARP information corresponding to contiguous MAC addresses is aggregated in extend mode. This means that ARP information with the same 43 most significant bits of a MAC address corresponds to the same ARP resource.
  
  In this mode, the maximum number of ARP resources supported by the device depends on whether the MAC addresses corresponding to ARP information are contiguous.
  
  + If the MAC addresses corresponding to all ARP information are not contiguous, the maximum number of ARP resources supported by the device refers to that of the chip with minimum specifications among all chips.
  + If the MAC addresses corresponding to all ARP information are contiguous, the maximum number of ARP resources supported by the device refers to that of the chip with minimum specifications among all chips multiplied by 32.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an ARP resource allocation mode.
   
   
   ```
   [arp resource-mode](cmdqueryname=arp+resource-mode) { global | extend }
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```