Configuring Source Address-based IGMP Message Filtering
=======================================================

Source address-based IGMP message filtering is a security policy used for filtering IGMP message on the Router's interface connected to user hosts.

#### Context

By default, no source address-based IGMP message filtering is configured on the Router's interface connected to user hosts.

After you configure source address-based IGMP message filtering on the Router's interface connected to user hosts, the interface filters IGMP messages based on the access control list (ACL) configuration.

Perform the following operations on the Router's interface connected to user hosts.


#### Procedure

* Configure source address-based IGMP Report or Leave message filtering
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL or a naming ACL as needed.
     
     
     + Configure a basic numbered ACL.
       
       1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
          
          A basic numbered ACL is created, and the basic numbered ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the basic numbered ACL.
     + Configure a naming ACL.
       
       1. Run [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ]
          
          A naming ACL is created, and the naming ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the naming ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**igmp ip-source-policy**](cmdqueryname=igmp+ip-source-policy) [ *basic-acl-number* | **acl-name** *acl-name* ]
     
     
     
     Source address-based IGMP Report or Leave message filtering is configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an ACL is not configured in this command, the device permits an IGMP Report or Leave message if the message's source address is 0.0.0.0 or if the message's source address is on the same network segment as the address of the interface that receives the message, but discards the message if the message's source address is on a different network segment from the address of the interface that receives the message.
     + If an ACL is configured on an interface, the interface uses configured ACL rules to filter source addresses in IGMP Report or Leave messages.
       - If an IGMP Report or Leave message matches an ACL rule and the action is **permit**, the interface permits this message.
       - If an IGMP Report or Leave message matches an ACL rule and the action is **deny**, the interface denies this message.
       - If an IGMP Report or Leave message does not match any ACL rule, the interface denies this message.
       - If a specified ACL does not exist or does not contain rules, the interface denies all IGMP Report and Leave messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure source address-based IGMP Query message filtering
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL or a naming ACL as needed.
     
     
     + Configure a basic numbered ACL.
       
       1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
          
          A basic numbered ACL is created, and the basic numbered ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the basic numbered ACL.
     + Configure a naming ACL.
       
       1. Run [**acl**](cmdqueryname=acl) **name** *acl-name* **basic** [ **match-order** { **auto** | **config** } ]
          
          A naming ACL is created, and the naming ACL view is displayed.
       2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
          
          Rules are configured for the naming ACL.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**igmp query ip-source-policy**](cmdqueryname=igmp+query+ip-source-policy) { *basic-acl-number* | **acl-name** *acl-name* }
     
     
     
     Source address-based IGMP Query message filtering is configured to control querier election.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an IGMP Query message matches an ACL rule and the action is **permit**, the interface permits this message.
     + If an IGMP Query message matches an ACL rule and the action is **deny**, the interface denies this message.
     + If an IGMP Query message does not match any ACL rule, the interface denies this message.
     + If a specified ACL does not exist or does not contain rules, the interface denies all IGMP Query messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.