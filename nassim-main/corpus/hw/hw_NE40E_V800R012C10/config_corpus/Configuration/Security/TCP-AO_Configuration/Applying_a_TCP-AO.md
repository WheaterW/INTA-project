Applying a TCP-AO
=================

Applying a TCP-AO

#### Prerequisites

A TCP-AO has been configured.


#### Context

TCP-AO implements two-way authentication during TCP connection setup.

When TCP is used as the transport layer protocol for an application, such as the BGP, MSDP, or LDP application, a TCP connection must be created before a session can be established between two ends.

TCP-AOs can be used in these applications to protect session security at the transport layer.

For details about how to apply a TCP-AO, see the reference configuration sections listed in [Table 1](#EN-US_TASK_0000001086078520__table565131515447).

**Table 1** Applying a TCP-AO in an application
| Application | Reference Section |
| --- | --- |
| BGP | IP Routing > BGP Configuration > Improving BGP Security > Configuring TCP-AO Authentication  IP Routing > BGP4+ Configuration > Improving BGP4+ Security > Configuring BGP4+ Authentication |
| LDP | MPLS > MPLS LDP Configuration > Configuring LDP Security Features > Configuring LDP TCP-AO Authentication |
| MSDP | IP Multicast > MSDP Configuration > Controlling MSDP Peer Connections > Configuring MSDP Peer Authentication |

The following uses BGP as an example to describe how to apply a TCP-AO.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
3. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* | *ipv6-address* } **tcp-ao** **policy** *tcp-ao-name* command to configure TCP-AO authentication.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The TCP-AO authentication configured in the BGP view also takes effect for the BGP extended address family view because they use the same TCP connection.
   * BGP MD5 authentication, BGP keychain authentication, and BGP TCP-AO authentication are mutually exclusive.
   * A TCP connection cannot be set up if the specified TCP-AO has not been configured or the TCP-AO does not have an active key.
   * After a TCP-AO is applied, the TCP connection does not support NAT traversal.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.