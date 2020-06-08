;Joshua Hoshiko
;CS2400
;March 28, 2018

	AREA zeroCounter, CODE, READONLY
	
	EXPORT main
	IMPORT randomnumber
	
main
	MOV R0, #0				;Clear R0
	MOV R1, #0				;Clear R1
	MOV R2, #0				;Clear R2
	MOV R3, #0				;Clear R3
	MOV R4, #0				;Clear R4
	MOV R5, #0				;Clear R5
	MOV R6, #0				;Clear R6
	MOV R7, #0				;Clear R7
	MOV R8, #0				;Clear R8
	LDR R8, =array			;Load array starting address into R1
	LDR R6, =allOnes
loadLoop	
	BL randomnumber			;randomnumber stored in R0
	STR R0, [R8], #4		;Store random number into the array, spot by spot
	ADD R7, R7, #1			;Increment word counter
	TEQ R7, #11				;Check if 11 words have been loaded
	BNE loadLoop			;Repeat loads till we reach 11
	LDR R8, =array			;reset address pointer
	
	MOV R2, #0				;Clear the bubble sort counter
bubbleSort	
	BL swap					;branch to bubbleSort subroutine
	ADD R2,R2, #1			;Increment bubble sort counter
	TEQ R2, #11				;Test if we've looped enough
	
	BNE bubbleSort			;If we haven't lopped enough go and loop again
	LDR R8, =array			;Reset address pointer
	MOV R2, #0				;Clear the bubble sort counter
	TEQ R7, #0				;Test if we swapped at all
	MOV R7, #0				;Clear the swap counter
	BNE bubbleSort			;Branch back to bubble sort if the preivious sort had a swap
	
	BL countZero
	
swap
	LDR R0, [R8]			;load first word into R0
	LDR R1, [R8, #4]		;load second word into R1
	ADD R8, R8, #4			;Increment address
	CMP R0, R1				;Compare the two values
	STRGT R0, [R8]			;Swap if R0 to R1's position if R0 is greater than 
	STRGT R1, [R8, #-4]		;Swap if R1 to R0's position 
	MOVGT R7, #1
	BX LR
	
countZero
	TEQ R4, #11			;(cleared outside subroutine), counter for number of words checked
	BXEQ LR				;exit to main if done with all words
	ADD R4, R4, #1		;increment word counter
	LDR R5, [R8], #4	;load number from address, shift to next word after 
countLoop
	TEQ R5, R6			;does this have any 0's left?
	BEQ countZero		;end the count for this word
	ADD R2, R5, #1		;remove a zero by adding and performing ORR
	ORR R5, R5, R2
	ADD R3, R3, #1		;increment counter of number of 0's
	B	countLoop		;Go through loop again to check for 0's again
	
	AREA arrayArea, DATA, READWRITE
array % 11*4
allOnes DCD 0xFFFFFFFF
	ALIGN
	END