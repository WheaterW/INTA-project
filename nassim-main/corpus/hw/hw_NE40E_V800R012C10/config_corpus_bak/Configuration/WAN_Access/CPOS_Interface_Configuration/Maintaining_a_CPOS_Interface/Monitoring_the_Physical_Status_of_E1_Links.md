Monitoring the Physical Status of E1 Links
==========================================

To ensure correct link connections, you must monitor the
physical status of E1 links.

#### Context

Monitoring the physical status of E1 links can help you
locate E1 link faults, ensuring correct link connections. You can
configure the system to monitor the physical status of multiple E1
links simultaneously while not affecting
existing services.

Perform the following steps on a device to
be checked:


#### Procedure

1. Run [**monitor**](cmdqueryname=monitor) **e1** { *interface-type* *interface-number* | *interface-name* } &<1-16> [ **interval** *interval* [ **times** *times* ] | **times** *times* [ **interval** *interval* ] ]
   
   
   
   The physical status of E1 links is monitored.