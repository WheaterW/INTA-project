Configuring Flexible Interoperation of RADIUS Attributes
========================================================

Configuring_Flexible_Interoperation_of_RADIUS_Attributes

#### Context

The usage scenarios of different vendors' RADIUS attributes may differ. If the device interconnects with different vendors' RADIUS servers, you can configure flexible interoperation of RADIUS attributes. This enables the device to flexibly connect to the RADIUS server by invoking Python scripts.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access enable python extend script-package**](cmdqueryname=access+enable+python+extend+script-package) *script-package-name*
   
   
   
   The Python script extension function is enabled.
3. Run [**access python-policy**](cmdqueryname=access+python-policy) *policy-name*
   
   
   
   A python policy template is configured, and its view is displayed.
4. Run [**protocol**](cmdqueryname=protocol) *protocol-type* { **packet** *packet-type* [ **direction** { **ingress** | **egress** } ] } **python-script** *script-name*
   
   
   
   The specified Python script is configured to process packets based on the specified protocol type, packet type, and packet direction (inbound or outbound).
5. (Optional) Run [**protocol**](cmdqueryname=protocol) *protocol-type* **packet process-fail passthrough**
   
   
   
   A policy is configured for handling the failure to modify packet information using a Python script.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
8. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
9. Run [**python-policy**](cmdqueryname=python-policy) *policy-name*
   
   
   
   The Python policy template is bound.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.