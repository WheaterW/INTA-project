Configuring Bit-Error-Triggered Protection Switching for a Specific IGP Neighbor Relationship
=============================================================================================

If multiple links are available between two IGP neighbors on an NG MVPN, configure IGP bit error detection and bit-error-triggered protection switching, allowing the remote mLDP tunnel end to select a new outbound downstream interface if the interface in use is suffering a high bit error rate.

#### Context

In an NG MVPN scenario, multicast data flows must be transmitted on a link that has no or few bit errors because even low bit error rates may cause black screen, erratic display, or frame interruption. If bit errors occur on a downstream inbound interface, mLDP can use bit-error-triggered section switching or bit-error-triggered IGP route switching to prevent a high bit-error-rate link from being selected. If an mLDP upstream node has multiple links to the same downstream node and no bit error occurs on any of the links, the mLDP LSP randomly selects an outbound interface for sending traffic to the downstream node. If bit errors occur on a link of the outbound interface, you can configure bit-error-triggered protection switching for this IGP neighbor relationship to minimize service loss. After detecting bit errors, a device notifies the IGP BFD module of the bit error status, and the module sends the bit error status to the IGP neighbor through BFD messages. If the neighbor is also configured with bit-error-triggered protection switching for this neighbor relationship, the BFD module of the neighbor receives the bit error rate. The mLDP LSP then selects an outbound interface based on bit error rates. An mLDP LSP selects a downstream link with a smaller cost or a link with no bit error rate.

The network shown in [Figure 1](#EN-US_TASK_0172362285__fig_dc_vrp_cfg_error-code_ngmvpn_000101) is an NG MVPN that uses P2MP mLDP LSPs to transmit services. If no bit error occurs on the links, multicast traffic is transmitted along the path Root-P1-Leaf. There are two links between P2 and the leaf node, one physical direct link and one logical direct link. The logical direct link passes through Leaf-P1-Root-P2. P2 and the leaf node establish an IGP neighbor relationship using the two links. If bit errors occur an interface that connects the leaf node to P1, traffic is switched to the backup link Root-P2-Leaf. Traffic switching is implemented through mLDP LSP outbound interface switching. The switching process is as follows:

* The leaf node notifies the local interface management module of the bit error fault, triggering IGP to increase the cost value of the link connected to this interface and switch the route to the backup link. The mLDP egress then switches services to the backup link Leaf-P2-Root of the newly selected unicast route.
* The leaf node uses BFD messages to transmit the bit error status to P2. P2 is an mLDP intermediate node and has two links connected to its downstream node. After receiving the bit error rate of the logical direct link, P2 selects the downstream outbound interface that connects to the physical direct link with no bit errors. mLDP outbound interface switching is then complete.

**Figure 1** Configuring bit-error-triggered protection switching for a specific IGP neighbor relationship  
![](images/fig_dc_vrp_cfg_error-code_ngmvpn_000101.png)

#### Pre-configuration Tasks

Before configuring bit-error-triggered protection switching for a specific IGP neighbor relationship, complete the following tasks:

* Configure IS-IS to generate routes and establish a neighbor relationship.
* Enable LDP and mLDP across the entire network.
* Enable BFD globally.

#### Procedure

* Run [**system-view**](cmdqueryname=system-view)
  
  
  
  The system view is displayed.
* Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
  
  
  
  The interface view is displayed.
* Run [**isis bfd bit-error enable**](cmdqueryname=isis+bfd+bit-error+enable)
  
  
  
  BFD-based bit error detection is enabled on the specified IS-IS interface.
* Run [**commit**](cmdqueryname=commit)
  
  
  
  The configuration is committed.

#### Verifying the Configuration

After configuring BFD-based bit error detection for a specified IS-IS neighbor relationship, run the following commands to check the configuration.

* Run the [**display isis bfd-bit-error interface**](cmdqueryname=display+isis+bfd-bit-error+interface) command to check the interfaces enabled with BFD-based bit error detection.
* Run the [**display isis bfd-bit-error session**](cmdqueryname=display+isis+bfd-bit-error+session) command to check BFD sessions used for bit error detection.