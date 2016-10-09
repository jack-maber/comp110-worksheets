START

password = RANDOMLY PICKED FROM BANK/MATRIX
guess_attempts = 0                             //SETS NUMBER OF PLAYER GUESSES AT LOWEST VALUE

WHILE guess_attempts<3                         //ALLOWS LOOP TO RUN WHILE THE PLAYER STILL HAS GUESSES REMAINING
    guessedinput=randomchar                    //MATCHES PLAYER INPUT TO RANDOM WORD CHARACTER
    i=0                                        //SETS CHARACTER READ NUMBER I.E. FIRST LETTER = 0
    similarity=0                               //SIMILARITY VALUE OF THE TWO WORDS
    
     WHILE(I<4)                                   
        IF (guessedinput=randomchar)
            similarity = similarity + 1 
            i = i + 1
        ELSE IF
            i = i + 1
        END IF
     END WHILE

     PRINT "Similarity to word is" + similarity
      
     IF (similarity = 4)
        GRANT PLAYER ACCESS TO TERMINAL
        guess_attempts = 3
     IFELSE
        guess_attempts = guess_attempts + 1

END WHILE
      
          
            
    
    
