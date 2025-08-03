Using CE Ping to Check the Connectivity Between a PE and a CE on a VPLS Network
===============================================================================

After you configure a virtual private LAN service (VPLS) network, use customer edge (CE) ping to monitor the connectivity between a provider edge (PE) and a CE on the VPLS network.

#### Prerequisites

The VPLS network has been correctly configured, and the specified virtual service instance (VSI) is up.


#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

When you specify a source IP address, note the following:

* The source IP address must be on the same network segment as the destination IP address. If they are on different network segments, the destination node considers Address Resolution Protocol (ARP) request packets invalid and does not return ARP response packets.
* The specified source IP address must be unique on an L2VPN. If the specified source IP address is the same as an in-use IP address, packets cannot be properly forwarded. As a result, the user whose IP address is specified as the source IP address cannot access the Internet. If the gateway IP address is specified as the source IP address, no user can access the Internet.

To avoid this problem, after you run the [**ce-ping**](cmdqueryname=ce-ping) command, the device prompts you to confirm whether the specified source IP address is unused. The command takes effect only after you enter **Y**.



#### Procedure

1. Run the following command to monitor the connectivity between a PE and a CE:
   
   
   
   [**ce-ping**](cmdqueryname=ce-ping) *ip-address* **vsi** *vsi-name* **source-ip** *source-ip-address* [ **mac** *mac-address* ] [ **interval** *interval* | **count** *count* ] \*
   
   For example:
   
   ```
   <HUAWEI> ce-ping 10.1.1.1 vsi abc source-ip 10.1.1.2 mac e024-7fa4-d2cb interval 2 count 5
   Info: If the designated source IP address is in use, it could cause the abnormal data transmission in VPLS network. Are you sure the source-ip is unused in this VPLS? [Y/N]:y
   Ce-ping is in process...
   10.1.1.1 is used by 00e0-fc12-3456 
   ```