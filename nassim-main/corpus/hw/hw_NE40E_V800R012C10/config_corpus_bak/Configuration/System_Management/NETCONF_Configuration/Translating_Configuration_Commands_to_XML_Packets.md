Translating Configuration Commands to XML Packets
=================================================

This section describes how to translate configuration commands into XML packets in the NETCONF YANG model. The obtained packets help you manage devices through the NETCONF model.

#### Context

CLI and NETCONF are two device management models, which have a mapping relationship. To quickly obtain NETCONF YANG packets corresponding to configuration commands, perform the following steps.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**xml-translate begin**](cmdqueryname=xml-translate+begin)
   
   
   
   The CLI-to-XML translation mode is accessed.
3. Run the configuration commands to be translated.
4. Run either of the following commands as needed:
   
   
   * To translate the configuration commands to XML packets, run the [**xml-translate end**](cmdqueryname=xml-translate+end) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When the command to be converted corresponds to both the new and deprecated nodes, the YANG packet converted using the [**xml-translate end**](cmdqueryname=xml-translate+end) command contains the data of the two nodes. When the converted packet is sent, a message is displayed, indicating that the configuration already exists. You are advised to delete the data of a node based on the actual situation before the packet is sent.
   * To stop the CLI-to-XML translation and exit the translation mode, run the [**xml-translate abort**](cmdqueryname=xml-translate+abort) command.