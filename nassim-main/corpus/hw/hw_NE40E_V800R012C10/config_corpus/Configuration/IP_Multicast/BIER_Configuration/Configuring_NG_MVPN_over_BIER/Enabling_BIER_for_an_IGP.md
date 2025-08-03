Enabling BIER for an IGP
========================

Information such as the BFR-IDs and IP addresses of BIER nodes in each BIER sub-domain needs to be flooded through an IGP, and then BIER forwarding information is generated on each node on the network.

#### Context

Each edge node (PE) in a BIER sub-domain must be configured with a BFR-ID that is unique to the sub-domain. BFR-IDs in the BIER sub-domain, together with other information (for example, nodes' IP addresses), are flooded through the IGP. Each node on the network generates its BIER forwarding information. After receiving a BIER packet carrying a BitString, each node performs packet replication and forwarding according to the BitString in the packet.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is configured, and the IS-IS view is displayed.
3. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** | **compatible** }
   
   
   
   The cost style of the routes received and sent by the IS-IS device is set to **wide**, **wide-compatible**, or **compatible**.
4. Run the [**bier enable**](cmdqueryname=bier+enable) command to enable BIER in the IS-IS process.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The cost style of the routes received and sent by the IS-IS device must be set to **wide**, **wide-compatible**, or **compatible** before you enable BIER in the IS-IS process.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.