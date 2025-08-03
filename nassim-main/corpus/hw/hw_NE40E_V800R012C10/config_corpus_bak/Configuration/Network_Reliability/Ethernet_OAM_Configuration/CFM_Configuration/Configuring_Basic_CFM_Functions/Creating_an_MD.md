Creating an MD
==============

This section describes how to create a maintenance domain (MD).

#### Context

You can create different MDs for different network ranges to isolate faults. IEEE Standard 802.1ag-2007 defines the following MD formats to indicate special MDs:

* no-md-name: The MAID field in a sent continuity check message (CCM) does not carry an MD name.
* dns-md-format-name: The MD information in the MAID field in a sent CCM is a character string obtained from a domain name service (DNS) text.
* mac-md-format-name: The MD information in the MAID field in a sent CCM consists of a 6-byte Media Access Control (MAC) address and a 2-byte integer ranging from 0 to 65535.
* string: The MD information in the MAID field in a sent CCM is a character string.

Perform the following steps on each NE40E on which CFM needs to be deployed:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name* [ **format** { **no-md-name** | **dns** *dns-md-format-name* | **mac-address** *mac-md-format-name* | **string** *string-md-format-name* } ] [ **level** *level* ]
   
   
   
   An MD is created, and the MD view is displayed.
   
   
   
   To create multiple MDs, repeat this step.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   CFM packets in low-level MDs cannot pass through identical- or high-level MDs, whereas CFM packets in high-level MDs can pass through low-level MDs.
3. (Optional) Run [**senderid-tlv-type**](cmdqueryname=senderid-tlv-type) { { **chassis** | **chassis-manage** } [ **chassis-subtype** { **mac-address** | **locally-assigned** } ] | **defer** | **manage** | **none** }
   
   
   
   The type of the sender ID TLV in a CFM packet is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.