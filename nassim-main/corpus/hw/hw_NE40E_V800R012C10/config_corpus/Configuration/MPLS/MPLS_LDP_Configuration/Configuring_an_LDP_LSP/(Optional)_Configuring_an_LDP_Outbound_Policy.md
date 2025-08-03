(Optional) Configuring an LDP Outbound Policy
=============================================

Configuring an LDP outbound policy helps prevent an LSR from establishing unwanted LSPs, saving memory resources.

#### Context

Generally, an LSR sends Label Mapping messages to all its LDP peers. This results in the establishment of numerous LSPs, wasting resources and leading to unstable device running status, especially on low-performance devices. To address these issues, an LDP outbound policy can be configured to limit Label Mapping messages to be sent, thereby reducing the number of LDP LSPs to be established and memory resource consumption.

The following parameters can be specified in an LDP outbound policy to limit Label Mapping messages to be sent:

* **none**: filters out all FECs. If this parameter is specified, the device does not send Label Mapping messages for IGP routes to specified peers.
* **host**: allows only the FECs on host routes to pass. If this parameter is specified, the device sends Label Mapping messages only for host routes to specified peers.
* **ip-prefix**: allows only the FECs on routes in a specified IP prefix list. If this parameter is specified, the device sends Label Mapping messages only for IGP routes in the specified IP prefix list to specified peers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The MPLS-LDP-IPv4 view is displayed.
4. Perform either of the following steps to apply the outbound policy that allows Label Mapping messages for specified IGP routes or BGP labeled routes to be sent to a specified LDP peer:
   
   
   * Run the [**outbound peer**](cmdqueryname=outbound+peer+peer-group+all+fec+none+host+ip-prefix) { *peer-id* | **peer-group** *peer-group-name* | **all** } **fec** { **none** | **host** | **ip-prefix** *prefix-name* } command to apply an outbound policy to specified IGP routes to specified peers.
   * Run the [**outbound peer**](cmdqueryname=outbound+peer+peer-group+all+bgp-label-route+none+ip-prefix) { *peer-id* | **peer-group** *peer-group-name* | **all** } **bgp-label-route** { **none** | **ip-prefix** *prefix-name* } command to apply an outbound policy to specified BGP labeled routes to specified peers.
   
   
   
   If FECs in the Label Mapping messages to be sent to an LDP peer group or all LDP peers are in the same range, specify either **peer-group** *peer-group-name* or **all** in the command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) If multiple outbound policies are configured for a specified LDP peer, the earliest configuration takes effect. For example, the following configurations are performed in sequence:
   ```
   outbound peer 2.2.2.2 fec host
   ```
   ```
   outbound peer peer-group group1 fec none
   ```
   As group1 also contains an LDP peer with *peer-id* of 2.2.2.2, the following outbound policy takes effect for the peer:
   ```
   outbound peer 2.2.2.2 fec host
   ```
   
   If two outbound policies are configured in sequence and the **peer** parameters in the two commands are the same, the latter configuration overwrites the former. For example, the following configurations are performed in sequence:
   ```
   outbound peer 2.2.2.2 fec host
   ```
   ```
   outbound peer 2.2.2.2 fec none
   ```
   The second configuration overwrites the first one. This means that the following outbound policy takes effect for the LDP peer with *peer-id* of 2.2.2.2:
   ```
   outbound peer 2.2.2.2 fec none
   ```
   
   MPLS and MPLS LDP must be enabled globally before an outbound policy is configured.
   
   To delete all outbound policies simultaneously, run the [**undo outbound peer all**](cmdqueryname=undo+outbound+peer+all) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.