(Optional) Configuring an Interface Splitting Mode
==================================================

By configuring an interface splitting mode, you can switch the bandwidth mode of the split interface.

#### Context

To switch an interface bandwidth mode, configure an interface splitting mode, which increases the networking flexibility and saves interface costs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **port split dimension interface** { { *interface-name1* | *interface-type* *interface-number1* } [ **to** { *interface-name2* | *interface-type* *interface-number2* } ] } &<1â32> **split-type** *split-type*
   
   
   
   A split mode is configured for specified interfaces.
   
   
   
   The names of the breakout interfaces are displayed in the format of current interface bandwidth + original interface number. If the interface is split into multiple interfaces, ":0", ":1", or the like is added after the interface number.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.