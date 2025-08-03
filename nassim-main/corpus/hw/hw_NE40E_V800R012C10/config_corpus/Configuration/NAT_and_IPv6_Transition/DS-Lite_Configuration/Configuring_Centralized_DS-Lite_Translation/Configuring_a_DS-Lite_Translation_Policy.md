Configuring a DS-Lite Translation Policy
========================================

You can configure DS-Lite translation policies to determine whether to implement ACL-based filtering of the traffic introduced to a service board and to redistribute the traffic to different DS-Lite address pools for DS-Lite translation.

#### Context

A DS-Lite translation policy for user traffic distributed to a service board can be configured to:

* Match ACL rules:
  
  An ACL and a DS-Lite address pool must be specified. If packets match the ACL, and the action specified in the ACL rule is **permit**, DS-Lite translates the packets using addresses in the DS-Lite address pool.
* Not match ACL rules:
  
  User traffic distributed to a service board does not need to match any ACL rule. By default, the addresses of user traffic are translated using addresses from a specified DS-Lite address pool.


#### Procedure

* Configure a DS-Lite translation policy to match ACL rules.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
     
     
     
     The DS-Lite instance view is displayed.
  3. (Optional) Run the [**ds-lite filter**](cmdqueryname=ds-lite+filter) { *acl-number* | **acl-name** *acl-name* } **outbound** command to filter DS-Lite packets based on inner-layer IPv4 information before configuring DS-Lite translation.
     
     
     
     If you need to filter out invalid packets such as spam before DS-Lite translation, perform this step to configure filtering rules. If the action defined in the ACL rule is deny, the packet is discarded. If the action defined in the ACL rule is permit, DS-Lite translation is performed. DS-Lite translation can be performed for packets that do not match ACL rules.
  4. Run [**ds-lite outbound**](cmdqueryname=ds-lite+outbound) *acl-number* **address-group** *address-group-name*
     
     
     
     An ACL is bound to an address pool, and a DS-Lite translation policy is configured to match ACL rules.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When performing this step, ensure that the address segment of the ACL rule used in the translation policy covers the address segment of the ACL rule used in the traffic diversion policy. Otherwise, service interruptions may occur. To prevent such interruptions, use either of the following measures:
     
     + Keep *acl-number* in this step consistent with that in the traffic diversion policy.
     + Configure a default address pool in this step for translating the addresses unmatched by the configured traffic translation policy. For example:
       ```
       The ACL rule referenced by the traffic diversion policy is as follows:
       #
       acl ipv6 3000
        rule 1 permit ipv6 source 2001:db8::1 64
       #
       acl ipv6 3999 //Default address pool configuration
        rule 1 permit ipv6  //Default address pool configuration
       The translation policy is as follows:
       ds-lite instance ds-lite1 id 1
        ds-lite address-group group1 group-id 1 10.10.1.0 10.10.1.254
        ds-lite address-group group2 group-id 2 10.10.1.255 10.10.1.255 //Default address pool configuration
        ds-lite outbound 3000 address-group address-group1
        ds-lite outbound 3999 address-group address-group2 //Default address pool configuration
       ```
* Configure a DS-Lite translation policy not to match ACL rules.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
     
     
     
     The DS-Lite instance view is displayed.
  3. (Optional) Run the [**ds-lite filter**](cmdqueryname=ds-lite+filter) { *acl-number* | **acl-name** *acl-name* } **outbound** command to filter DS-Lite packets based on inner-layer IPv4 information before configuring DS-Lite translation.
     
     
     
     If you need to filter out invalid packets such as spam before DS-Lite translation, perform this step to configure filtering rules. If the action defined in the ACL rule is deny, the packet is discarded. If the action defined in the ACL rule is permit, DS-Lite translation is performed. DS-Lite translation can be performed for packets that do not match ACL rules.
  4. Run [**ds-lite outbound**](cmdqueryname=ds-lite+outbound) **any** **address-group** *address-group-name*
     
     
     
     A DS-Lite translation policy is configured not to allow packets to match against ACL rules.