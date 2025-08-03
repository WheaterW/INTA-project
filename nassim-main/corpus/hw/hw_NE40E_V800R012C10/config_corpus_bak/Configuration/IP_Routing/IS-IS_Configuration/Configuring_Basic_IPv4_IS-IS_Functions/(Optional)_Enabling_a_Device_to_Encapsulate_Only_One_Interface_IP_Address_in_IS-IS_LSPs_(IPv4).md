(Optional) Enabling a Device to Encapsulate Only One Interface IP Address in IS-IS LSPs (IPv4)
==============================================================================================

To implement interworking between Huawei and non-Huawei devices, you need to enable the type-132 TLV in LSPs to carry the IP address of only one IS-IS interface on the Huawei device.

#### Context

By default, on Huawei devices, the type-132 TLV in LSPs carries the IP addresses of all IS-IS interfaces. However, on some non-Huawei devices, the type-132 TLV in LSPs carries the IP address of only one IS-IS interface. To implement interworking between Huawei devices and these non-Huawei devices, enable the type-132 TLV in LSPs to carry the IP address of only one IS-IS interface on the Huawei devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and its view is displayed.
3. Run [**advertise one-interface-address**](cmdqueryname=advertise+one-interface-address)
   
   
   
   The type-132 TLV in LSPs is enabled to carry the IP address of only one IS-IS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.