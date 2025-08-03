Configuring Static BFD for IPv6 IS-IS
=====================================

Configuring Static BFD for IPv6 IS-IS

#### Prerequisites

Before configuring static BFD for IPv6 IS-IS, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

Static BFD sessions cannot detect route switching. This means that if a change in the bound peer IP address causes a route to switch to another link, the BFD session is renegotiated only when the original link fails.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Create a binding between a BFD for IPv6 IS-IS session and a peer IPv6 address, and then enter the BFD session view.
   
   
   ```
   [bfd](cmdqueryname=bfd) sessname-value bind peer-ipv6 peerip6-value [ vpn-instance vpnname-value ] [ interface { interface-value | ifType ifNum } ] source-ipv6 sourceip6-value [ select-board slot-id [ slot-id2 ] ] auto
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The source address must be specified.
   * The peer IPv6 address must be specified and cannot be a multicast IPv6 address.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
7. Change the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
8. Enable static BFD for IPv6 IS-IS on the interface.
   
   
   ```
   [isis ipv6 bfd static](cmdqueryname=isis+ipv6+bfd+static) 
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis ipv6 bfd**](cmdqueryname=display+isis+ipv6+bfd) [ *process-id* | **vpn-instance** *vpn-instance-name* ] **session** { **peer**  *peer-addr* | **all** } command to check information about static BFD for IPv6 IS-IS sessions.
* Run the [**display isis interface**](cmdqueryname=display+isis+interface) **verbose** command to check the configurations of static BFD for IPv6 IS-IS on interfaces.