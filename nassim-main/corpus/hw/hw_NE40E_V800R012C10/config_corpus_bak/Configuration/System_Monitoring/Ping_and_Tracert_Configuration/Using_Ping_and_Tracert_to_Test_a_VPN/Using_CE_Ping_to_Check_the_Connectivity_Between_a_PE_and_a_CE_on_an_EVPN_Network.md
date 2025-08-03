Using CE Ping to Check the Connectivity Between a PE and a CE on an EVPN Network
================================================================================

After configuring an EVPN, you can use CE ping to check the connectivity between a PE and a CE.

#### Prerequisites

The EVPN has been correctly configured.


#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

When you specify a source IP address, note the following:

* The source IP address must be on the same network segment as the CE's IP address. If they are on different network segments, the CE considers received CE ping packets invalid and discards them.
* The source IP address must be an unused IP address in the specified EVPN broadcast domain. Otherwise, CE ping packets cannot be properly forwarded. As a result, the user whose IP address is specified as the source IP address cannot access the Internet. If you specify the gateway IP address as the source IP address, all users cannot access the Internet.

To avoid this problem, after you run the [**ce-ping evpn**](cmdqueryname=ce-ping+evpn) command, the device prompts you to confirm whether the specified source IP address is unused. The command takes effect only after you enter **Y**.



#### Procedure

1. Run the [**ce-ping**](cmdqueryname=ce-ping) *ip-address* **evpn** *evpn-name* **source-ip** *source-ip-address* [ **mac** *mac-address* ] [ **count** *count* | **interval** *interval* ] \* command in any view to check the connectivity from the PE to the CE.
   
   
   ```
   <HUAWEI> ce-ping 10.1.1.1 evpn huawei123 source-ip 10.1.1.12 mac e024-7fa4-d2cb interval 2 count 5
   Info: If the designated source IP address is in use, it could cause the abnormal data transmission in EVPN network. Are you sure the source-ip is unused in this EVPN? [Y/N]:y
   Ce-ping is in process...
   10.1.1.1 is used by 00-e0-fc-12-34-56 
   ```