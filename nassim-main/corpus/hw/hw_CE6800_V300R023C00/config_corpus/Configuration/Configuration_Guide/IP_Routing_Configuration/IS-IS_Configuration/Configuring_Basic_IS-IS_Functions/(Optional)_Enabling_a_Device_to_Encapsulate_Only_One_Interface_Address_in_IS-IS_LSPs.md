(Optional) Enabling a Device to Encapsulate Only One Interface Address in IS-IS LSPs
====================================================================================

(Optional) Enabling a Device to Encapsulate Only One Interface Address in IS-IS LSPs

#### Context

By default, the Type-132 TLV in LSPs sent by Huawei devices carries the IP addresses of all IS-IS interfaces, whereas the Type-132 TLV in LSPs sent by some non-Huawei devices carries the IP address of only one IS-IS interface. To implement interworking between Huawei devices and these non-Huawei devices, enable the Huawei devices to encapsulate the IP address of only one IS-IS interface in the Type-132 TLV in LSPs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an IS-IS process and enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ] [ vpn-instance vpn-instance-name ]
   ```
3. Enable the device to encapsulate the IP address of only one IS-IS interface in the Type-132 TLV in LSPs.
   
   
   ```
   [advertise one-interface-address](cmdqueryname=advertise+one-interface-address)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```