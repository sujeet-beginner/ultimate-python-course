# 2. WAP to fill in a letter template given below with name and date

  

letter = ''' Dear <|Name |>
            you are selected
            <|Date|> '''

print(letter.replace("<|Name |>", "Sujeet,").replace("<|Date|>", "18 August 2026"))

     # these can also be called as chaning 