; --- Copyright Jonathan Meyer 1996. All rights reserved. -----------------
; File:      jasmin/examples/HelloWorld.j
; Author:    Jonathan Meyer, 10 July 1996
; Purpose:   Prints out "Hello World!"
; Edited by: Joshua Hoshiko
; -------------------------------------------------------------------------


.class public NoJad.j
.super java/lang/Object

;
; standard initializer
.method public <init>()V
   aload_0
 
   invokenonvirtual java/lang/Object/<init>()V
   return
.end method

.method public static main([Ljava/lang/String;)V
   .limit stack 2
   .limit locals 2
   
   bipush 2
   astore_0
   bipush 3
   astore_1

   aload_0
   aload_1
   astore_0
   astore_1

   return
.end method
