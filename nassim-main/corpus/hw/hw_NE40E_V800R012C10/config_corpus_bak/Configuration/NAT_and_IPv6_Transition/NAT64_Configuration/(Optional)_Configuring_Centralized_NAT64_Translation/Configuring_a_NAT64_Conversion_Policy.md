Configuring a NAT64 Conversion Policy
=====================================

You can configure NAT64 conversion policies to determine whether to implement ACL-based filtering of the traffic introduced to a service board and to redistribute the traffic to different NAT64 address pools for NAT64 treatment.

#### Context

A NAT64 conversion policy for user traffic distributed to a service board supports either of the following modes:

* Match ACL rules:
  
  An ACL and a NAT64 address pool must be specified. If packets match the ACL, and the action specified in the ACL rule is **permit**, NAT64 translates the packets using addresses in the NAT64 address pool.
* Not match ACL rules:
  
  User traffic distributed to a service board does not need to match any ACL rule. By default, NAT64 is performed for user traffic using addresses from a specified NAT64 address pool.


#### Procedure

* Configure a NAT64 conversion policy in which ACL rules are used to filter packets for translation.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
     
     
     
     The NAT64 instance view is displayed.
  3. Run [**nat64 outbound**](cmdqueryname=nat64+outbound) *acl-number* **address-group** *address-group-name*
     
     
     
     A NAT64 conversion policy in which the ACL is bound to the address pool is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When performing this step, ensure that the address range of the ACL rule used in the conversion policy covers the address range of the ACL rule used in the traffic diversion policy. Otherwise, service interruptions may occur. To prevent such interruptions, use either of the following measures:
     
     + Keep *acl-number* in this step consistent with that in the traffic diversion policy.
     + Configure a default address pool in this step for translating the addresses unmatched by the configured traffic conversion policy. For example:
       ```
       The ACL rule referenced by the traffic diversion policy is as follows:
       #
       acl ipv6 3000
        rule 1 permit ipv6 source 2001:db8::1 64
       #
       acl ipv6 3999 //Default address pool configuration
       rule 1 permit ipv6 //Default address pool configuration
       The conversion policy is as follows:
       nat64 instance nat1 id 1
        nat64 address-group group1 group-id 1 10.10.1.0 10.10.1.254
        nat64 address-group group2 group-id 2 10.10.1.255 10.10.1.255 //Default address pool configuration
        nat64 outbound 3000 address-group address-group1
        nat64 outbound 3999 address-group address-group2 //Default address pool configuration
       ```
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a NAT64 conversion policy in which ACL rules are not used to filter packets for translation.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
     
     
     
     The NAT64 instance view is displayed.
  3. Run [**nat64 outbound**](cmdqueryname=nat64+outbound) **any** **address-group** *address-group-name*
     
     
     
     A NAT64 conversion policy is configured to not allow packets to match against ACL rules.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.