Configuring Source Address-based MLD Message Filtering
======================================================

Source address-based MLD message filtering is a security policy used for filtering MLD message on the Router's interface connected to user hosts.

#### Context

By default, no source address-based MLD message filtering is configured on the Router's interface connected to user hosts.

After you configure source address-based MLD message filtering on the Router's interface connected to user hosts, the interface filters MLD messages based on the access control list (ACL) configuration.

Perform the following operations on the Router's interface connected to user hosts.


#### Procedure

* Configure source address-based MLD Report or Done message filtering.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL6 or a named ACL6 as needed.
     
     
     + Configure a basic numbered ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ] command to create a basic numbered ACL6 and enter the ACL6 view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the basic numbered ACL6.
     + Configure a named ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ] command to create a named ACL6 and enter its view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the named ACL6.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**mld ip-source-policy**](cmdqueryname=mld+ip-source-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
     
     
     
     Source address-based MLD Report or Done message filtering is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an MLD Report or Leave message matches an ACL rule and the action is **permit**, the interface permits this message.
     + If an MLD Report or Leave message matches an ACL rule and the action is **deny**, the interface denies this message.
     + If an MLD Report or Leave message does not match any ACL rule, the interface denies this message.
     + If a specified ACL does not exist or does not contain rules, the interface denies all MLD Report and Leave messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure source address-based MLD Query message filtering.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a basic numbered ACL6 or a named ACL6 as needed.
     
     
     + Configure a basic numbered ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ] command to create a basic numbered ACL6 and enter the ACL6 view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the basic numbered ACL6.
     + Configure a named ACL6.
       
       1. Run the [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ] command to create a named ACL6 and enter its view.
       2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \* command to configure a rule for the named ACL6.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**mld query ip-source-policy**](cmdqueryname=mld+query+ip-source-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
     
     
     
     Source address-based MLD Query message filtering is configured to control querier election.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If an MLD Query message matches an ACL rule and the action is **permit**, the interface permits this message.
     + If an MLD Query message matches an ACL rule and the action is **deny**, the interface denies this message.
     + If an MLD Query message does not match any ACL rule, the interface denies this message.
     + If a specified ACL does not exist or does not contain rules, the interface denies all MLD Query messages.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.