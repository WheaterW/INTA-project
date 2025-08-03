Configuring a Service Identification Policy
===========================================

Service identification enables the system to determine which authentication domain is used based on the information about some fields carried in user packets.

#### Context

The NE40E supports the following service identification modes. You can select a mode as required.

* Service identification based on VLAN IDs in inner or outer VLAN tags
* Service identification based on 802.1p values in inner or outer VLAN tags
* Service identification based on DSCP values
* Service identification based on DHCP Option 60 information

#### Procedure

* Configuring service identification based on VLAN IDs in inner or outer VLAN tags
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**service-identify-policy**](cmdqueryname=service-identify-policy) *policy-name*
     
     
     
     A service identification policy is created and its view is displayed.
  3. Run [**service-identify**](cmdqueryname=service-identify) { **inner-vlan** | **outer-vlan** }
     
     
     
     A service identification mode is configured.
  4. Run [**vlan**](cmdqueryname=vlan) *vlan-id1* [ **to** *vlan-id2* ] **domain** *domain-name*
     
     
     
     The packets with a specified VLAN ID are mapped a domain.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configuring service identification based on 802.1p values in inner or outer VLAN tags
  
  
  
  In VS mode, this configuration task is supported only by the admin VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**service-identify-policy**](cmdqueryname=service-identify-policy) *policy-name*
     
     
     
     A service identification policy is created and its view is displayed.
  3. Run [**service-identify**](cmdqueryname=service-identify) **8021p** { **inner-vlan** | **outer-vlan** }
     
     
     
     A service identification mode is configured.
  4. Run [**8021p**](cmdqueryname=8021p) *start-num* [ *end-num* ] **domain** *domain-name*
     
     
     
     The packets with a specified 802.1p value in the inner or outer VLAN tag are mapped to a domain.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configuring service identification based on DSCP values
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**service-identify-policy**](cmdqueryname=service-identify-policy) *policy-name*
     
     
     
     A service identification policy is created and its view is displayed.
  3. Run [**service-identify**](cmdqueryname=service-identify) **dscp**
     
     
     
     A service identification mode is configured.
  4. Run [**dscp**](cmdqueryname=dscp) *start-dscp-id* [ *end-dscp-id* ] **domain** *domain-name*
     
     
     
     The packets with a specified DSCP value are mapped to a domain.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configuring service identification based on DHCP Option 60 information
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**service-identify-policy**](cmdqueryname=service-identify-policy) *policy-name*
     
     
     
     A service identification policy is created and its view is displayed.
  3. Run [**service-identify**](cmdqueryname=service-identify) **dhcp-option60**
     
     
     
     A service identification mode is configured.
  4. (Optional) Run [**option60 partial-match**](cmdqueryname=option60+partial-match) { **domain-included** | **included-in-domain** } or [**vendor-class partial-match**](cmdqueryname=vendor-class+partial-match) { **domain-included** | **included-in-domain** }
     
     
     
     Partial matching of the VENDOR-CLASS (DHCPv4 OPTION60/DHCPv6 OPTION16) information is configured.
  5. (Optional) Run [**option60 partial-info**](cmdqueryname=option60+partial-info) { **cn** | [ **offset** *offset* ] { **length** *length* | **sub-option** *option* [ **sub-offset** *sub-offset* ] [ **sub-length** *sub-length* ] } } or [**vendor-class partial-info**](cmdqueryname=vendor-class+partial-info) { **cn** | [ **offset** *offset* ] { **length** *length* | **sub-option** *option* [ **sub-offset** *sub-offset* ] [ **sub-length** *sub-length* ] } }
     
     
     
     Partial information of the vendor-class (DHCPv4 option60/DHCPv6 option16) attribute is used to identify services.
  6. (Optional) Run [**option60 encrypt**](cmdqueryname=option60+encrypt) or [**vendor-class encrypt**](cmdqueryname=vendor-class+encrypt)
     
     
     
     The VENDOR-CLASS (DHCPv4 OPTION60/DHCPv6 OPTION16) field value is encrypted.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.