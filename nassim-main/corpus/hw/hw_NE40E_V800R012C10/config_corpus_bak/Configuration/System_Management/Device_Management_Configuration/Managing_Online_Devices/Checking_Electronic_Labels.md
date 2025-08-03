Checking Electronic Labels
==========================

By checking the electronic label of a board, you can obtain the type, bar code, Bill of Material (BOM) code, description, production date, supplier name, issuing number, Common Language Equipment Identification (CLEI) code, and sales BOM code of the board.

#### Context

In VS mode, this section applies only to the admin VS.


#### Procedure

1. Run [**display elabel**](cmdqueryname=display+elabel) [ *slot-id* | **brief** ]
   
   
   
   The electronic label information is displayed.
   
   
   
   In practice, you can run this command in the user view to check the electronic label of each board on the device. You can specify the *slot-id* parameter to check the electronic label of the board in the specified slot.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For the slot ID range, see the *Hardware Description*.
   
   Information in the electronic label of a board includes the type, bar code, item code, description, production date, supplier name, issuing number, CLEI code, and sales BOM code of the board.
2. Run [**display elabel optical-module**](cmdqueryname=display+elabel+optical-module) { **brief** | **interface** *ifnum* }
   
   
   
   The electronic label of an optical module is displayed.
3. Run [**display fan manufacture-info slot**](cmdqueryname=display+fan+manufacture-info+slot) *slot-id*
   
   
   
   The electronic label of a fan is displayed.
4. Run [**display power manufacture-info**](cmdqueryname=display+power+manufacture-info) **slot** *slot-id*
   
   
   
   The electronic label of a power module is displayed.