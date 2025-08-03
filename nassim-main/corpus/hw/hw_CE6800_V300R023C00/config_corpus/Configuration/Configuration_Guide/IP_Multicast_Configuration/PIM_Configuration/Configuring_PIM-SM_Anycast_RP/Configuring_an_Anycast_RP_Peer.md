Configuring an Anycast RP Peer
==============================

Configuring an Anycast RP Peer

#### Context

When sending a Register message to an anycast RP peer, the local anycast RP needs to convert the destination address of the message into the local address of the anycast RP peer.

The devices functioning as anycast RPs can be identified by the same logical address so that the RP in the PIM-SM domain is unique. These devices, however, need to distinguish one another during communication. Therefore, the configured anycast RP address cannot be used. In this case, you need to configure a local address for an anycast RP and an anycast RP peer relationship.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a basic or an advanced ACL as needed.
   
   
   * Configure a basic ACL.
     
     1. Create a basic ACL and enter its view.
        ```
        [acl](cmdqueryname=acl) [ number ] basic-acl-number 
        ```
     2. Configure a rule for the basic ACL.
        ```
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } source { source-ip-address { source-wildcard | 0 } | any }
        ```
   * Configure an advanced ACL.
     
     1. Create an advanced ACL and enter its view.
        ```
        [acl](cmdqueryname=acl) { name advance-acl-name [ advance | [ advance ] number advance-acl-number ] | [ number ] advance-acl-number } [ match-order { config | auto } ]
        ```
     2. Configure a rule for the advanced ACL.
        ```
        [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } ip [ destination { destination-ip-address { destination-wildcard | 0 } | any } | source { source-ip-address { source-wildcard | 0 } | any } ]
        ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
5. Configure an anycast RP and enter its view.
   
   
   ```
   [anycast-rp](cmdqueryname=anycast-rp) rp-address
   ```
6. Configure an anycast RP peer.
   
   
   ```
   [peer](cmdqueryname=peer) peer-address [ fwd-msdp-sa [ acl-number | acl-name acl-name ] ]
   ```
   
   
   
   *peer-address* specifies the local address of an anycast RP peer.
   
   If **fwd-msdp-sa** is specified, the local RP extracts source and group information from received Multicast Source Discovery Protocol (MSDP) Source Active (SA) messages, encapsulates the information into Register messages, and sends the messages to anycast RP peers.
   
   In a PIM-SM domain, all the devices deployed with anycast RP must be fully connected logically. Anycast RP peer relationships need to be configured between every two devices deployed with anycast RP.
   
   If no ACL is configured, the device extracts source and group information from received MSDP SA messages, encapsulates the information into a Register message, and sends the message to anycast RP peers.
   
   If an ACL is configured, the device uses configured ACL rules to filter multicast group addresses in MSDP SA messages to be forwarded.
   * If an MSDP SA message matches an ACL rule and the action is **permit**, the device forwards this message.
   * If an MSDP SA message matches an ACL rule and the action is **deny**, the device does not forward this message.
   * If an MSDP SA message does not match any ACL rule, the device does not forward this message.
   * If a specified ACL does not exist or contain rules, the device does not forward any MSDP SA messages.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```