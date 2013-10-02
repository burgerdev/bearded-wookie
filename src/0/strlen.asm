;----------------------------------------------------------------------
; Nach: http://en.wikipedia.org/wiki/Assembly_language#Example_listing_of_assembly_language_source_code

; zstr_count:
; Speichere die Länge eines Strings, der sich an Adresse 'eax'
; befindet, in Register ecx. Der String muss mit einem Nullbyte
; abschließen.
;
; Wir haben vier Multi-Purpose-Register:
;	[Stringadresse|egal|Rückgabewert|egal]
;	      eax      ebx      ecx      edx
;
; Memory-Layout an der Stringadresse:
; 
; [	'H'	'A'	'L'	'L'	'O'	0	]
;	eax	eax+1	eax+2	eax+3	eax+4	eax+5

zstr_count:
	
	mov ecx, -1				; initialisiere den Zähler auf -1
	
	
	.loop:					;				<---------------
						;						|
		inc ecx				; erhöhe den Zähler um 1 (increment)		|
						;						|
		cmp byte [eax + ecx], 0		; prüfe, ob wir am Ende des Strings 		|
						; (Nullbyte) sind (die eckige Klammer		|
						; inspiziert eine Adresse)			|
						;						|
		jne .loop			; wiederhole Schleifendurchlauf, wenn wir	|
						; noch nicht beim Nullbyte sind			|
						;				----------------

	.done:

		ret				; Die Länge des Strings liegt in ecx, 
						; wir geben zurück ans Hauptprogramm

