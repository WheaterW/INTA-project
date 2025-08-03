(Optional) Configuring an LDP Inbound Policy
============================================

An LDP inbound policy can be configured to prevent the establishment of unwanted LSPs, reducing memory consumption.

#### Context

Generally, an LSR receives Label Mapping messages from all LDP peers. This results in the establishment of numerous LSPs, wasting resources and leading to unstable device running status, especially on low-performance devices. To address these issues, an LDP inbound policy can be configured to limit Label Mapping messages to be received, thereby reducing the number of LDP LSPs to be established and memory resource consumption.

An LDP inbound policy restricts the receiving of LDP Label Mapping messages based on the selected parameter:

* **none**: filters out all FECs. If this parameter is set, the specified peer does not receive Label Mapping messages on any IGP route.
* **host**: allows only the FECs on host routes to pass. If this parameter is set, the specified peer receives Label Mapping messages on host routes.
* **ip-prefix**: allows only the FECs on routes in a specified IP prefix list. If this parameter is set, the specified peer receives Label Mapping messages on IGP routes in the specified IP prefix list.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The MPLS-LDP-IPv4 view is displayed.
4. Run [**inbound peer**](cmdqueryname=inbound+peer+peer-group+all+fec+none+host+ip-prefix) { *peer-id* | **peer-group** *peer-group-name* | **all** } **fec** { **none** | **host** | **ip-prefix** *prefix-name* }
   
   
   
   An inbound policy is applied to specified IGP routes to specified peers.
   
   
   
   To apply a policy associated with the same FEC range to an LDP peer group or all LDP peers receiving Label Mapping messages, specify either **peer-group** *peer-group-name* or **all** in the command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) If multiple inbound policies are configured for a specified peer, the earliest configuration takes effect. For example, the following configurations are performed in this sequence:
   ```
   inbound peer 2.2.2.2 fec host
   ```
   ```
   inbound peer peer-group group1 fec none
   ```
   As **group1** also contains an LDP peer with *peer-id* of 2.2.2.2, the following inbound policy takes effect:
   ```
   inbound peer 2.2.2.2 fec host
   ```
   
   If two inbound policies are configured one after the other and the **peer** parameter settings in the two commands are the same, the latter configuration overwrites the former. For example, the following configurations are performed in this sequence:
   ```
   inbound peer 2.2.2.2 fec host
   ```
   ```
   inbound peer 2.2.2.2 fec none
   ```
   The second configuration overwrites the first one. This means that the following inbound policy takes effect for the LDP peer with *peer-id* of 2.2.2.2:
   ```
   inbound peer 2.2.2.2 fec none
   ```
   
   If an inbound policy for all peers is configured and another inbound policy for a specified peer or peer group is configured, the former policy has a higher priority, and the latter policy does not take effect. For example:
   ```
   inbound peer all fec none
   ```
   ```
   inbound peer 2.2.2.2 fec host
   ```
   The following inbound policy takes effect:
   ```
   inbound peer all fec none
   ```
   
   MPLS and MPLS LDP must be enabled globally before an inbound policy is configured.
   
   To delete all inbound policies simultaneously, run the [**undo inbound peer all**](cmdqueryname=undo+inbound+peer+all) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.