Configuring a NAT Conversion Policy
===================================

Before converting private IP addresses of user traffic into public IP addresses from a NAT address pool, configure a NAT conversion policy to determine whether to filter the user traffic diverted to a NAT service board using ACL rules.

#### Context

There are two NAT conversion policies:

* ACL-based
  
  In this policy, an ACL and a NAT address pool are configured, and NAT can be performed only for user packets that match a **permit** ACL rule.
* Non-ACL-based
  
  In this policy, packets diverted to a NAT service board are not matched against ACL rules. By default, the IP addresses of these packets are converted into public IP addresses from a specified NAT address pool.


#### Procedure

* Configure an ACL-based NAT conversion policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
     
     
     
     The NAT instance view is displayed.
  3. Run [**nat outbound**](cmdqueryname=nat+outbound) *acl-number* **address-group** *address-group-name*
     
     
     
     A NAT conversion policy in which the ACL bound to the address pool is used to filter packets for translation.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When performing this step, ensure that the address range of the ACL rule used in the conversion policy covers the address range of the ACL rule used in the traffic diversion policy. Otherwise, service interruptions may occur. To prevent such interruptions, use either of the following measures:
     
     + Keep *acl-number* in this step consistent with that in the traffic diversion policy.
     + Configure a default address pool in this step for translating the addresses unmatched by the configured traffic conversion policy. For example:
       ```
       The ACL rule referenced by the traffic diversion policy is as follows:
       #
       acl number 3000
        rule 1 permit source 1.1.1.1 0.0.0.255
       #
       acl number 3999 //Default address pool configuration
        rule 1 permit ip //Default address pool configuration
       The conversion policy is as follows:
       nat instance nat1 id 1
        nat address-group group1 group-id 1 10.10.1.0 10.10.1.254
        nat address-group group2 group-id 2 10.10.1.255 10.10.1.255 //Default address pool configuration
        nat outbound 3000 address-group address-group1
        nat outbound 3999 address-group address-group2 //Default address pool configuration
       ```
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a non-ACL-based NAT conversion policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
     
     
     
     The NAT instance view is displayed.
  3. Run [**nat outbound**](cmdqueryname=nat+outbound) **any** **address-group** *address-group-name*
     
     
     
     A non-ACL-based NAT conversion policy is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.