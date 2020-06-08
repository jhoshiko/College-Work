.class public OPTest.j
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
   
	iconst_1
	iconst_2
	iadd
	;result=3
	
	iconst_5
	iconst_3
	isub
	;result=2
	
	iconst_4
	iconst_2
	idiv
	;result=2
	
	iconst_3
	iconst_5
	imul
	;result=15
	
	iconst_5
	iconst_2
	irem
	;result=1
	
	iconst_m1
	ineg
	;result=1
	
	iconst_2
	iconst_0
	ior
	;result=2
	
	iconst_5
	iconst_3
	iand
	;result=1
	
	iconst_2
	iconst_3
	ixor
	;result=1
	
	iconst_2
	iconst_1
	ishl
	;result=
	
	iconst_4
	iconst_1
	ishr
	;result=
	
	iconst_4
	iconst_2
	iushr
	;result=
	
	iconst_5
	istore_0
	
	iconst_2
	istore_1
	
	iconst_3
	istore_2
	
	iconst_2
	istore_3
	
	iconst_4
	istore 4
	
	iconst_3
	istore 5
	
	iload_0
	i2b
	
	iload_1
	i2c
	
	iload_2
	i2d
	
	iload_3
	i2f
	
	iload 4
	i2l
	
	iload 5
	i2s

   return
.end method