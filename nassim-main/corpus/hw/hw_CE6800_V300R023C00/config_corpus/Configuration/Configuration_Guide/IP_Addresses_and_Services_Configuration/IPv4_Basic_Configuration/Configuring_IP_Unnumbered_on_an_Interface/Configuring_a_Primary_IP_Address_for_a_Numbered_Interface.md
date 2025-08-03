Configuring a Primary IP Address for a Numbered Interface
=========================================================

Configuring a Primary IP Address for a Numbered Interface

#### Prerequisites

Before configuring a primary IP address for a numbered interface, configure a link layer protocol for unnumbered and numbered interfaces to ensure that their link layer protocol status is up.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the numbered interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Configure a primary IP address for the numbered interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }[ tag tag-value ]
   ```
   
   
   
   Each interface has only one primary IP address. If you configure multiple primary IP addresses for an interface, the last configured IP address becomes the primary IP address of the interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```