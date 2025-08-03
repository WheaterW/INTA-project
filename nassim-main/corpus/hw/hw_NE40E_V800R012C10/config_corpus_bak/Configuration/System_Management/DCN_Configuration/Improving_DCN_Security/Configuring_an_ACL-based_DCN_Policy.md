Configuring an ACL-based DCN Policy
===================================

An ACL-based DCN policy can be used to filter DCN packets. The DCN packets that fail to match the ACL rule are discarded, improving DCN network security.

#### Prerequisites

Before configuring an ACL-based DCN policy, complete either of the following tasks:

* Create a basic ACL using the [**acl (basic ACL)**](cmdqueryname=acl+%28basic+ACL%29) command and configure a rule for the ACL using the [**rule (basic ACL view)**](cmdqueryname=rule+%28basic+ACL+view%29) command in the basic ACL view.
* Create an advanced ACL using the [**acl (advanced ACL)**](cmdqueryname=acl+%28advanced+ACL%29) command and configure a rule for the ACL using the [**rule (advanced ACL view)**](cmdqueryname=rule+%28advanced+ACL+view%29) command in the advanced ACL view.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**packet-policy**](cmdqueryname=packet-policy) { **acl-name** *acl-name* | *basic-number* | *adv-number* }
   
   
   
   An ACL-based DCN policy is configured.
   
   A basic or an advanced ACL can be specified in the command. ACLs numbered 2000 to 2999 are basic ACLs; ACLs numbered 3000 to 3999 are advanced ACLs.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.