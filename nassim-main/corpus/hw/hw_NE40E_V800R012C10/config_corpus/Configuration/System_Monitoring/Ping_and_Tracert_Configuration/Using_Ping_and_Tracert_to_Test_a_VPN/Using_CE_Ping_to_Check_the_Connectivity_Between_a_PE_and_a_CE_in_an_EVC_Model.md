Using CE Ping to Check the Connectivity Between a PE and a CE in an EVC Model
=============================================================================

After configuring a Bridge Domain (BD), you can use CE ping to check the connectivity between a PE and a CE in an Ethernet Virtual Connection (EVC) model.

#### Prerequisites

The network has been correctly configured, and the specified BD is Up.


#### Context

An EVC model unifies the Layer 2 bearer service model and configuration model. In an EVC model, you can use CE ping to check the link reachability between a PE and a CE in a specified BD. For details about EVCs, see *HUAWEI NE40E-M2 series Feature Description > Local Area Network*. For configuration details, see [EVC Configuration](dc_vrp_evc_cfg_0000.html).

When using CE ping to check the link reachability between a PE and a CE, you must specify a source IP address that meets the following conditions:

* The source IP address must be on the same network segment as the CE's IP address. If they are on different network segments, the CE considers received CE Ping packets invalid and discards them.
* The source IP address must be an unused IP address in the specified BD. If you specify a used IP address for the source IP address, CE Ping packets cannot be properly forwarded. As a result, the user using the source IP address cannot access the Internet. If you specify a gateway IP address for the source IP address, all users cannot access the Internet.

To avoid this problem, after you run the [**ce-ping bd**](cmdqueryname=ce-ping+bd) command, the device displays a message, prompting you to confirm that you have specified an unused IP address as the source IP address. The command takes effect only after you enter **Y**.


#### Procedure

1. Run the [**ce-ping**](cmdqueryname=ce-ping) *ip-address* **bd** *bd-id* **source-ip** *source-ip-address* [ **mac** *mac-address* ] [ **interval** *interval* | **count** *count* ] \* command in any view to check the link reachability between a PE and a CE.
   
   
   ```
   <HUAWEI> ce-ping 10.1.1.1 bd 123 source-ip 10.1.1.2 mac e024-7fa4-d2cb interval 2 count 5
   Info: If the designated source IP address is in use, it could cause the abnormal data transmission in EVC network. Are you sure the source-ip is unused in this EVC? [Y/N]:y
   Ce-ping is in process...
   10.1.1.1 is used by 00e0-fc12-3456 
   ```